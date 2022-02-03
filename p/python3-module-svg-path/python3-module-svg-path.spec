%define modname svg.path
%define srcname svg-path

Name: python3-module-svg-path
Version: 4.1
Release: alt1
Summary: SVG path objects and parser

Group: Development/Python3
License: CC0
Url: http://pypi.python.org/pypi/svg.path

Source: %srcname-%version.tar
# Source-url: https://github.com/regebro/svg.path/archive/%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-devel

%description
svg.path is a collection of objects that implement the different path
commands in SVG, and a parser for SVG path definitions.

%prep
%setup -n %srcname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README.rst CHANGES.txt CONTRIBUTORS.txt
%python3_sitelibdir/svg/path
%python3_sitelibdir/%modname-%version-*
%exclude %python3_sitelibdir/svg/path/tests

%changelog
* Thu Feb 03 2022 Anton Midyukov <antohami@altlinux.org> 4.1-alt1
- new version (4.1) with rpmgs script

* Tue May 25 2021 Anton Midyukov <antohami@altlinux.org> 2.2-alt3
- rename srpm to python3-module-svg-path
- drop python2 subpackage
- drop tests subpackage
- cleanup spec

* Fri Jul 28 2017 Anton Midyukov <antohami@altlinux.org> 2.2-alt2
- New subpackages tests

* Wed Jul 26 2017 Anton Midyukov <antohami@altlinux.org> 2.2-alt1
- Initial build for ALT Sisyphus
