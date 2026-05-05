Name: libraqm
Version: 0.10.5
Release: alt1

Summary: Complex Textlayout Library

License: MIT
Group: Publishing
Url: https://github.com/HOST-Oman/libraqm

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/HOST-Oman/libraqm/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: libfreetype-devel
BuildRequires: libharfbuzz-devel
BuildRequires: fribidi-devel
BuildRequires: gtk-doc

%description
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%package docs
Summary: Libraqm Documentation
BuildArch: noarch
Group: Publishing

%description docs
This package contains documentation files for raqm.

%package devel
Summary: Complex Textlayout Library
Requires: libraqm = %EVR
Group: Development/Other

%description devel
Library that encapsulates the logic for complex
text layout and provides a convenient API.

This package contains documentation files for raqm.

%prep
%setup

%build
%meson -Ddocs=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc COPYING
%_libdir/libraqm.so.*

%files devel
%doc COPYING
%_includedir/raqm.h
%_includedir/raqm-version.h
%_libdir/libraqm.so
%_pkgconfigdir/raqm.pc

%files docs
%doc COPYING
%doc AUTHORS NEWS README.md
%_datadir/gtk-doc/html/raqm

%changelog
* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10.5-alt1
- new version 0.10.5

* Mon Mar 09 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10.4-alt1
- new version 0.10.4

* Tue Mar 18 2025 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt1
- new version 0.10.2
- switched to meson build

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)

* Mon Jul 29 2019 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Fri May 17 2019 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Wed Apr 26 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- new version (0.2.0) with rpmgs script

* Wed Apr 26 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt1
- initial build for ALT Linux Sisyphus

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 1 2016 Mosaab Alzoubi <moceap@hotmail.com> - 0.1.1-1
- Updated to 0.1.1

* Mon Apr 25 2016 Mosaab Alzoubi <moceap@hotmail.com> - 0.1.0-3
- Use lib prefix in %%name
- Depends on same version -devel

* Sun Apr 24 2016 Mosaab Alzoubi <moceap@hotmail.com> - 0.1.0-2
- General revision

* Sat Apr 23 2016 Mosaab Alzoubi <moceap@hotmail.com> - 0.1.0-1
- Initial build
