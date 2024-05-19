%define oname toolz

Name: python3-module-%oname
Version: 0.12.1
Release: alt1

Summary: List processing tools and functional utilities
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/toolz
VCS: https://github.com/pytoolz/toolz
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
A set of utility functions for iterators, functions, and dictionaries.

%prep
%setup

sed -i 's|"version": "0+unknown"|"version": "%version"|' versioneer.py

%build
%pyproject_build

%install
%pyproject_install

%check
# https://github.com/pytoolz/toolz/issues/564
%tox_check_pyproject -- -k'not test_shakespeare'

%files
%doc LICENSE.txt *.rst *.md
%python3_sitelibdir/tlz
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 0.12.1-alt1
- Built new version.
- Built with check.

* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt2
- python2 disabled

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version 0.9.0 (with rpmrb script)

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

