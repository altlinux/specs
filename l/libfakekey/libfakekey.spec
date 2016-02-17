# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen gcc-c++ libICE-devel libSM-devel pkgconfig(x11) pkgconfig(xtst)
# END SourceDeps(oneline)
%define major     0
%define oname     fakekey
%define libname   lib%{oname}%{major}
%define develname lib%{oname}-devel

Name:           libfakekey
Version:        0.1
Release:        alt6_9
Summary:        Converting characters to X key-presses

Group:          System/Libraries
License:        LGPLv2+
URL:            http://projects.o-hand.com/matchbox/
Source0:        http://matchbox-project.org/sources/libfakekey/0.1/%{name}-%{version}.tar.bz2
BuildRequires:  libXtst-devel
BuildRequires:  libX11-devel
Source44: import.info
Patch33: libfakekey-0.1-alt-link-fix.patch

%description
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package -n %{libname}
Summary:        Converting characters to X key-presses
Group:          System/Libraries

%description -n %{libname}
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package -n %{develname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides: fakekey-devel = %version-%release

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch33 -p1

%build
%configure --disable-static
%make LIBS+=-lX11

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%{_libdir}/libfakekey.so.%{major}*

%files -n %{develname}
%{_includedir}/fakekey/ 
%{_libdir}/libfakekey.so
%{_libdir}/pkgconfig/libfakekey.pc


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt6_9
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt6_8
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt6_7
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt6_6
- update by mgaimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt6_5
- fixed devel name

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt5_5
- update by mgaimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt5_3.5.2
- applied repocop patches

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_3.5.2
- added fakekey-devel provides

* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_3.5.2
- resurrected as mageia import

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.1
- Rebuilt for soname set-versions

* Sun Apr 11 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2
- Repair build with new xorg

* Wed Feb 17 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- Initial (from Fedora)
