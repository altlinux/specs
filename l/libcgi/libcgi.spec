Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#
# Rebuild option:
#
#   --with static            creates the -static subpckage
#

%global static  0

%{?_with_static:%global static 1}

%global libcgi_somajor 1
%global libcgi_sominor 0

Name:           libcgi
Version:        1.0
Release:        alt3_35
Summary:        CGI easy as C
License:        LGPLv2+
URL:            http://libcgi.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/libcgi/libcgi-%{version}.tar.gz
Patch0:         libcgi-1.0-Makefile.in.patch
Patch1:         libcgi-1.0-cgi.c-hextable.patch
Patch2:         libcgi-1.0-string.c-make_string.patch
Patch3:         libcgi-configure-c99.patch
BuildRequires:  gcc
Source44: import.info

%description
LibCGI is a library written from scratch to easily make CGI applications in C.


%package devel
Group: Development/Other
Summary:        Header files and libraries for LibCGI development
Requires:       %{name} = %{version}-%{release}

%description devel
The libcgi-devel package contains the header files and libraries needed
to develop programs that use the LibCGI library.


%if %{static}
%package static
Group: Development/Other
Summary:        LibCGI static library

%description static
The libcgi-static package contains the static library needed
to develop programs that use the LibCGI library.
%endif


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
find examples/ -name "Makefile.am" -delete


%build
%configure
make SOMAJOR=%{libcgi_somajor} \
     SOMINOR=%{libcgi_sominor} \
     %{?_smp_mflags}


%install
make SOMAJOR=%{libcgi_somajor} \
     SOMINOR=%{libcgi_sominor} \
     DESTDIR=$RPM_BUILD_ROOT \
     LIBDIR=%{_libdir} \
     INCDIR=%{_includedir}/%{name} \
     install
make DESTDIR=$RPM_BUILD_ROOT install_man

%if ! %{static}
rm -f $RPM_BUILD_ROOT%{_libdir}/libcgi.a
%endif
# see https://bugzilla.altlinux.org/show_bug.cgi?id=11162
if [ -d %buildroot%_pkgconfigdir ]; then
    echo "fedoraimport: this hook is obsolete"
    exit 1
else
    mkdir -p %buildroot%_pkgconfigdir
    cat <<E_O_F> %buildroot%_pkgconfigdir/cgilib.pc
# sdl pkg-config source file
prefix=/usr
exec_prefix=/usr
libdir=%_libdir
includedir=%_includedir

Name: cgilib
Description:  Simple CGI library
Version: %version
Requires:
Conflicts:
Libs: -lcgi -lpthread
Cflags: -I${includedir}/libcgi -D_GNU_SOURCE=1 -D_REENTRANT
E_O_F
fi






%files
%doc AUTHORS BUGS ChangeLog README THANKS TODO
%{_libdir}/*.so.*


%files devel
%doc doc/html/ examples/
%{_libdir}/*.so
%{_includedir}/%{name}/
%{_mandir}/man3/*.3*
%_pkgconfigdir/cgilib.pc


%if %{static}
%files static
%{_libdir}/*.a
%endif


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.0-alt3_35
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_26
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_23
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_21
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_20
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_18
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_15
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_14
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_13
- update to new release by fcimport

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_12
- added compat cgilib.pc (#11162)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_11
- initial import by fcimport

* Sun Mar 19 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.5-alt2
- fix build with latest Sisyphus

* Tue Jun 28 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 0.5-alt1
- initial package for ALT Linux
