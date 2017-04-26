Name: libraqm
Version: 0.2.0
Release: alt1

Summary: Complex Textlayout Library

License: MIT
Group: Publishing
Url: https://github.com/HOST-Oman/libraqm

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/HOST-Oman/libraqm/releases/download/v%version/raqm-%version.tar.gz
Source: %name-%version.tar

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
Requires: libraqm = %version-%release
Group: Development/Other

%description devel
Library that encapsulates the logic for complex
text layout and provides a convenient API.

This package contains documentation files for raqm.

%prep
%setup
%configure --enable-gtk-doc

%build
%make_build

%check
export LC_ALL=en_US.UTF-8
# TODO: check test
make check || true

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.{la,a}

%files
%doc COPYING
%_libdir/libraqm.so.*

%files devel
%doc COPYING
%_includedir/raqm.h
%_libdir/libraqm.so
%_pkgconfigdir/raqm.pc

%files docs
%doc COPYING
%doc AUTHORS NEWS README
%_datadir/gtk-doc/html/raqm

%changelog
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
