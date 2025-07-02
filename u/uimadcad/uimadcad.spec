%define oname uimadcad

Name: uimadcad
Version: 0.8.1
Release: alt1

Summary: User-friendly graphical environment for madcad

Url: https://github.com/jimy-byerley/uimadcad
License: GPL-3.0
Group: Development/Python3

# Source-url: https://github.com/jimy-byerley/uimadcad/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(poetry)
BuildRequires: python3(poetry.core)
BuildRequires: python3(flit_core)

BuildArch: noarch

Requires: python3(madcad)

%description
While pymadcad is a powerful and intuitive python module, any code generating a 3d
model still is a script full of coordinates and computational instructions, that
one needs to reexecute and wait for its result to show and every time you change a
value. uimadcad allows you to view every variable, every expression in your code
just by clicking on it, and interact with the display to edit it. With uimadcad,
you still work on the script, but you can combine the best of both world (text &
graphic) together to model faster.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
pushd %_builddir/%name-%version/

install -Dm755 madcad %buildroot%_bindir/madcad
install -Dm644 madcad.desktop %buildroot%_desktopdir/madcad.desktop
install -Dm644 uimadcad/icons/madcad-*.svg -t %buildroot%_iconsdir/hicolor/scalable/apps/
install -Dm644 uimadcad/icons/madcad.svg -t %buildroot%_iconsdir/hicolor/scalable/apps/
install -Dm644 uimadcad/icons/madcad.png -t %buildroot%_iconsdir/hicolor/256x256/apps/
install -Dm644 mimetypes/*.svg -t %buildroot%_iconsdir/hicolor/scalable/mimetypes/
install -Dm644 mimetypes/*.xml -t %buildroot%_datadir/mime/packages/

popd

%files
%_bindir/madcad
%_desktopdir/madcad.desktop
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}
%_iconsdir/hicolor/scalable/apps/madcad*.svg
%_iconsdir/hicolor/256x256/apps/madcad.png
%_iconsdir/hicolor/scalable/mimetypes/*.svg
%_datadir/mime/packages/*.xml

%changelog
* Mon Jun 30 2025 Ivan Mazhukin <vanomj@altlinux.org> 0.8.1-alt1
- Initial build for ALT Sisphys

