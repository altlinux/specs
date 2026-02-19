%def_disable static
%define soname 1
%define oname libmb

Name: libmatchbox
Version: 1.14
Release: alt1

Summary: Libraries for the Matchbox Desktop
License: LGPLv2+
Group: System/Libraries

Url: https://git.yoctoproject.org/libmatchbox
Vcs: https://git.yoctoproject.org/libmatchbox

Source: %name-%version.tar

BuildRequires: pkg-config
BuildRequires: libXft-devel
BuildRequires: libXext-devel
BuildRequires: libpango-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libxsettings-client-devel
BuildRequires: /usr/bin/doxygen
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libcheck-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xft)

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package devel
Summary: Header files for %name
Group: Development/C
%description devel
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
%description devel-static
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.
%endif

%package -n %name%soname
Group: System/Libraries
Summary: %name library
Obsoletes: %name <= 1.9-alt5

%description -n %name%soname
%name library.

%prep
%setup

%build
autoreconf -fisv
%configure \
	--enable-pango \
	--enable-jpeg \
	--enable-png \
	--enable-xsettings \
	%{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n %name%soname
%_libdir/%oname.so.%soname
%_libdir/%oname.so.%{soname}.*

%files devel
%doc AUTHORS ChangeLog README COPYING
%_includedir/%oname
%_libdir/%oname.so
%_pkgconfigdir/%oname.pc

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Thu Feb 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.14-alt1
- 1.9 -> 1.14
- chenged url tag
- added vcs tag
- droped old patchs
- builded in accordance with Shared Libs Policy

* Wed Dec 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.9-alt5
- Fix FTBFS.

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt4.1
- updated watch file

* Fri Nov 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt4
- build with libxsettings-client-devel

* Fri Nov 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3
- added patches 10 and 11 from fedora

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt2.2
- Fixed build

* Tue Dec 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt2.1
- Rebuilt for soname set-versions

* Sat Dec 13 2008 Aleksey Lim <alsroot@altlinux.org> 1.9-alt2
- move .so to devel package

* Sun Nov 16 2008 Aleksey Lim <alsroot@altlinux.org> 1.9-alt1
- first build for ALT Linux Sisyphus
