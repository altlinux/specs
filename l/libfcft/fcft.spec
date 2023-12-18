Name: libfcft
Version: 3.1.7
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
BuildRequires: pkgconfig(libutf8proc)

%package -n libfcft4
Summary: A small font loading and glyph rasterization library
Group: System/Libraries

%package devel
Summary: Development part of fcft
Group: Development/C

%define desc \
A small font loading and glyph rasterization library.

%description %desc

%description -n libfcft4 %desc
This package contains shared libfcft.

%description devel %desc
This package contains development part of libfcft.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files -n libfcft4
%_libdir/libfcft.so.*

%files devel
%_includedir/fcft
%_libdir/libfcft.so
%_man3dir/fcft*
%_pkgconfigdir/fcft.pc
%doc %_defaultdocdir/fcft

%changelog
* Mon Dec 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.7-alt1
- 3.1.7 released

* Mon Jul 17 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.6-alt1
- 3.1.6 released

* Thu Sep 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.5-alt1
- 3.1.5 released

* Tue Sep 13 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.4-alt1
- 3.1.4 released

* Thu Aug 25 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.3-alt1
- 3.1.3 released

* Tue May 31 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.2-alt1
- 3.1.2 relesed

* Wed May 11 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.1-alt1
- 3.1.1 released

* Sat Feb 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.0-alt1
- 3.0.0 released

* Tue Feb 01 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.1-alt1
- 2.5.1 released

* Tue Nov 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.0-alt1
- 2.5.0 released

* Mon Aug 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.4-alt1
- 2.4.4 released
