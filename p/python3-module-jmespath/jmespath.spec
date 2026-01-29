%define pypi_name jmespath

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1.1

Summary: JSON Matching Expressions
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/jmespath/
Vcs: https://github.com/jmespath/jmespath.py

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(hypothesis)
%endif

%description
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%_bindir/jp.py
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jan 29 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1.1
- packaged lost dist-info

* Fri Jan 23 2026 Anton Vyatkin <toni@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Tue Apr 04 2023 Anton Vyatkin <toni@altlinux.org> 1.0.1-alt1
- (NMU) New version 1.0.1.

* Tue Mar 24 2020 Alexey Shabalin <shaba@altlinux.org> 0.9.5-alt1
- new version 0.9.5
- build python3 only
- disable build doc

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.3-alt1
- Updated to upstream version 0.9.3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1.git20150712.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1.git20150712.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20150712
- Version 0.7.1

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20150420
- Version 0.7.0

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150203
- Version 0.6.1

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141105
- Initial build for Sisyphus

