%define oname sphinxtesters

%def_with check

Name: python3-module-%oname
Version: 0.2.3
Release: alt4

Summary: Utilities for testing Sphinx extensions

License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinxtesters

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-docutils
BuildRequires: python3-module-sphinx
%endif

%description
Sphinxtesters - utilities for testing Sphinx extensions.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install
%python3_prune

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv -k 'not test_bad_pagebuilder'

%files
%doc LICENSE README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info


%changelog
* Fri Apr 07 2023 Anton Vyatkin <toni@altlinux.org> 0.2.3-alt4
- Fix BuildRequires

* Sat Apr 09 2022 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt3
- disable tests (due test_pagebuilder.py:88)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt2
- NMU: build python3 module separately

* Wed Aug 28 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.3-alt1
- Build new version.

* Mon Dec 24 2018 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt1
- Build new version.

* Thu Feb 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2
- Updated build dependencies.

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt1
- Initial build for ALT.
