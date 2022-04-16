%define oname sphinxcontrib-htmlhelp

Name:           python3-module-%oname
Version:        2.0.0
Release:        alt2

Summary:        A sphinx extension which renders HTML help files

Group:          Development/Python3
License:        BSD
URL:            https://pypi.org/project/sphinxcontrib-htmlhelp

Source0:        %oname-%version.tar.gz

BuildArch:      noarch

BuildRequires:  gettext

%description
%summary

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/sphinxcontrib/
%python3_sitelibdir/*.pth
%python3_sitelibdir/*.egg-info/

%changelog
* Sat Apr 16 2022 Fr. Br. George <george@altlinux.ru> 2.0.0-alt2
- Fix old version in version.py

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Mon Apr 29 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- new version 1.0.2

* Thu Apr 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
