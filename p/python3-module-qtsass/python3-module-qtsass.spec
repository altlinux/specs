Name: python3-module-qtsass
Version: 0.0.1
Release: alt1.git132651a

License: MIT
Group: Development/Python
Url: https://github.com/spyder-ide/qtsass

Summary: QtSASS: Compile SCSS files to Qt stylesheets

# Source-url: https://github.com/spyder-ide/qtsass/archive/master.zip
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

# for test
BuildRequires: python3-module-libsass python3-module-pytest python3-module-PyQt5

%description
SASS brings countless amazing features to CSS.
Besides being used in web development,
CSS is also the way to stylize Qt-based desktop applications.
However, Qt's CSS has a few variations that prevent the direct use of SASS compiler.

The purpose of this tool is to fill the gap between SASS and Qt-CSS by handling those variations.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%python3_test

%files
%_bindir/qtsass
%python3_sitelibdir/*

%changelog
* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1.git132651a
- initial build for ALT Sisyphus
