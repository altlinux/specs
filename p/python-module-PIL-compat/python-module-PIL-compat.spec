%define modulename PIL-compat

Name: python-module-PIL-compat
Version: 1.0.0
Release: alt2

Summary: Compatibility modules, bridging PIL -> Pillow

Url: https://pypi.org/project/pil-compat/
License: MIT
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Source-git: https://github.com/prophile/pil-compat.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools python-module-wheel

%description
Compatibility modules, bridging PIL -> Pillow.

%prep
%setup

%build
# generate Image*
mkdir -p .git/info
python2 materialise.py

%python_build_debug

%install
%python_install

%files
%doc README
%python_sitelibdir/*


%changelog
* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- Fixed FTBFS.

* Mon Jul 02 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

