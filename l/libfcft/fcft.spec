Name: libfcft
Version: 2.5.1
Release: alt1

Summary: A small font loading and glyph rasterization library
License: MIT
Group: Graphical desktop/Other
Url: https://codeberg.org/dnkl/fcft

Source: %name-%version-%release.tar

BuildRequires: meson scdoc
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(tllist)

%package devel
Summary: Development part of fcft
Group: Development/C

%description
%summary

%description devel
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README* LICENSE
%_libdir/libfcft.so.*

%files devel
%_includedir/fcft
%_libdir/libfcft.so
%_man3dir/fcft*
%_pkgconfigdir/fcft.pc

%changelog
* Tue Feb 01 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.1-alt1
- 2.5.1 released

* Tue Nov 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.0-alt1
- 2.5.0 released

* Mon Aug 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.4-alt1
- 2.4.4 released
