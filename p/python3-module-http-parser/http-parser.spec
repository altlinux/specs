%define _unpackaged_files_terminate_build 1
%define oname http-parser

%def_with check

Name: python3-module-%oname
Version: 0.9.0
Release: alt3
Summary: http request/response parser
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/http-parser/

# https://github.com/benoitc/http-parser.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(Cython)
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%py3_provides %oname

%description
HTTP request/response parser for Python compatible with Python 2.x
(>=2.6), Python 3 and Pypy. If possible a C parser based on http-parser
from Ryan Dahl will be used.

%prep
%setup

# regenerate with cython later
rm -f http_parser/parser.c

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc NOTICE *.rst *.md THANKS examples
%python3_sitelibdir/*

%changelog
* Tue Dec 19 2023 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt3
- Moved on pyproject macros.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 0.9.0-alt2
- Stopped build for Python2.

* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.3 -> 0.9.0.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt1.git20150514.1.3.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt1.git20150514.1.3
- Updated build dependencies.

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt1.git20150514.1.2
- Updated build spec

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt1.git20150514.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1.git20150514.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150514
- New snapshot

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20140925
- Initial build for Sisyphus

