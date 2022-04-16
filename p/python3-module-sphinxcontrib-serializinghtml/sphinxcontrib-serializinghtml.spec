%define oname sphinxcontrib-serializinghtml

%def_with check

Name:    python3-module-%oname
Version: 1.1.5
Release: alt2

Summary: Sphinx extension for serialized HTML

Group:   Development/Python3
License: BSD-2-Clause
URL:     https://pypi.org/project/sphinxcontrib-serializinghtml

Source0: %oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires:      gettext

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinx-tests
%endif

%description
sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized"
HTML files (json and pickle).

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%check
python3 -m pytest

%files
%doc README.rst
%python3_sitelibdir/sphinxcontrib
%python3_sitelibdir/*.pth
%python3_sitelibdir/*.egg-info/

%changelog
* Sat Apr 16 2022 Fr. Br. George <george@altlinux.ru> 1.1.5-alt2
- Fix old version

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.5-alt1
- Automatically updated to 1.1.5.

* Mon Mar 02 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.4-alt1
- Build new version.
- Build with check.
- Fix license.

* Thu Apr 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus.
