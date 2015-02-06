%define	major 1
%define libname %mklibname wcat %{major}
%define develname %mklibname wcat -d

Summary:	Library for the watchcat software watchdog
Name:		libwcat
Version:	1.1
Release:	4
License:	LGPL
Group:		System/Libraries
URL:		http://oss.digirati.com.br/watchcatd/
Source0:	http://oss.digirati.com.br/watchcatd/%{name}-%{version}.tar.gz
Patch0:		libwcat-ldflags.diff
Patch1:		libwcat-socket_location_fix.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{develname}
Summary:	Static library and header files for the watchcat library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname wcat 1 -d}

%description -n	%{develname}
libwcat is an API to watchcatd, a software watchdog that uses an
approach not as drastic as the usual watchdog solutions. It tries
to kill the locked process only.

This package contains the static libwcat library and its header files
needed to compile applications that use libwcat.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
export CFLAGS="%{optflags} -fPIC"

%make 

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}

install -m755 %{name}.so.%{major}.%{version} %{buildroot}%{_libdir}/
install -m644 %{name}.a %{buildroot}%{_libdir}/
install -m644 watchcat.h %{buildroot}%{_includedir}/

ln -s %{name}.so.%{major}.%{version} %{buildroot}%{_libdir}/%{name}.so
ln -s %{name}.so.%{major}.%{version} %{buildroot}%{_libdir}/%{name}.so.%{major}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-3mdv2011.0
+ Revision: 620235
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2010.0
+ Revision: 429847
- rebuild

* Sat Sep 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdv2009.0
+ Revision: 281985
- 1.1

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2009.0
+ Revision: 233756
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 11 2007 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2008.1
+ Revision: 117276
- rebuild (missing devl package  on ia32)

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2008.0
+ Revision: 83616
- new devel naming


* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdv2007.0
+ Revision: 93772
- Import libwcat

* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-3mdv2007.0
- rebuild

* Tue Jan 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-2mdk
- ahh, this one was allready packaged, use my spec file anyway

* Fri Aug 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0-1mdk
- from Michel Machado <michel@digirati.com.br> : 
	- Minor fixes.

* Thu Feb 05 2004 Andre Nathan <andre@digirati.com.br> 0.1-2mdk
- Export CFLAGS before building;

* Fri Jan 23 2004 Andre Nathan <andre@digirati.com.br> 0.1-1mdk
- First version of the .spec.

