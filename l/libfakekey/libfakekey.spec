# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen gcc-c++ libICE-devel libSM-devel
# END SourceDeps(oneline)
%define major     0
%define raw_name  fakekey
%define libname   lib%{raw_name}0
%define develname %{raw_name}-devel

Name:           libfakekey
Version:        0.1
Release:        alt3_3.5.2
Summary:        Converting characters to X key-presses

Group:          System/Libraries
License:        LGPLv2+
URL:            http://projects.o-hand.com/matchbox/
Source0:        http://matchbox-project.org/sources/libfakekey/0.1/%{name}-%{version}.tar.bz2
BuildRequires:  libXtst-devel
BuildRequires:  libX11-devel
Source44: import.info
Patch: libfakekey-0.1-alt-link-fix.patch

%description
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package        -n %libname
Summary:        Converting characters to X key-presses
Group:          System/Libraries

%description    -n %libname
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package        -n %develname
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %libname

%description    -n %develname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch -p1

%build
%configure --disable-static
%make

%install
%makeinstall_std
rm -f $RPM_BUILD_ROOT%{_libdir}/libfakekey.la

%files -n %libname
%doc COPYING
%{_libdir}/libfakekey.so.%{major}*


%files -n %develname
%{_includedir}/fakekey/
%{_libdir}/libfakekey.so
%{_libdir}/pkgconfig/libfakekey.pc





%changelog
* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_3.5.2
- resurrected as mageia import

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.1
- Rebuilt for soname set-versions

* Sun Apr 11 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2
- Repair build with new xorg

* Wed Feb 17 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- Initial (from Fedora)
