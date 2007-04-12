%define	name	libwcat
%define	version	1.0
%define	release	%mkrel 3

%define	major 1
%define libname	%mklibname wcat %{major}

Summary:	Library for the watchcat software watchdog
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Libraries
URL:		http://oss.digirati.com.br/watchcatd/
Source0:	http://oss.digirati.com.br/watchcatd/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
libwcat is an API to watchcatd, a software watchdog that uses an
approach not as drastic as the usual watchdog solutions. It tries
to kill the locked process only.

%package -n	%{libname}
Summary:	Library for the watchcat software watchdog
Group:		System/Libraries

%description -n	%{libname}
libwcat is an API to watchcatd, a software watchdog that uses an
approach not as drastic as the usual watchdog solutions. It tries
to kill the locked process only.

%package -n	%{libname}-devel
Summary:	Static library and header files for the watchcat library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
libwcat is an API to watchcatd, a software watchdog that uses an
approach not as drastic as the usual watchdog solutions. It tries
to kill the locked process only.

This package contains the static libwcat library and its header files
needed to compile applications that use libwcat.

%prep

%setup -q -n %{name}-%{version}

%build
export CFLAGS="%{optflags} -fPIC"

%make 

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}

install -m755 %{name}.so.%{major}.%{version} %{buildroot}%{_libdir}/
install -m644 %{name}.a %{buildroot}%{_libdir}/
install -m644 watchcat.h %{buildroot}%{_includedir}/

ln -s %{name}.so.%{major}.%{version} %{buildroot}%{_libdir}/%{name}.so
ln -s %{name}.so.%{major}.%{version} %{buildroot}%{_libdir}/%{name}.so.%{major}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a


