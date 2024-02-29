%define _unpackaged_files_terminate_build 1
%define oname shortuuid

%def_with check

Name: python3-module-%oname
Version: 1.0.12
Release: alt1

Summary: A generator library for concise, unambiguous and URL-safe UUIDs

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/shortuuid/

BuildArch: noarch

# Source-url: https://github.com/skorokithakis/shortuuid.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
A library that generates short, pretty, unambiguous unique IDs by using
an extensive, case-sensitive alphabet and omitting similar-looking
letters and numbers.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# strip tests
rm %buildroot%python3_sitelibdir/%oname/test_shortuuid.py
# remove strange COPYING file
rm %buildroot%python3_sitelibdir/COPYING

%check
%pyproject_run_pytest -v

%files
%doc README.md
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu Feb 29 2024 Anton Vyatkin <toni@altlinux.org> 1.0.12-alt1
- new version 1.0.12

* Wed Jan 24 2024 Anton Vyatkin <toni@altlinux.org> 1.0.11-alt1
- new version 1.0.11

* Wed Mar 30 2022 Stanislav Levin <slev@altlinux.org> 1.0.8-alt1
- 1.0.0 -> 1.0.8.

* Fri Aug 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version (1.0.0) with rpmgs script
- cleanup spec, disable packing tests

* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt2.git20140426.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2.git20140426
- Disabled test_pep8 (broken with new pep8)

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20140426
- Initial build for Sisyphus

