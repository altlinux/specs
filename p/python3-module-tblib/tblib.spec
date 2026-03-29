%define _unpackaged_files_terminate_build 1
%define pypi_name tblib
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.1.0
Release: alt1.1
Summary: Traceback serialization library
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/tblib/
Vcs: https://github.com/ionelmc/python-tblib
BuildArch: noarch
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-benchmark
BuildRequires: python3-module-pytest-cov
%endif

%description
%pypi_name allows you to:
- pickle tracebacks and raise exceptions with pickled tracebacks in different
  processes. This allows better error handling when running code over multiple
  processes (imagine multiprocessing, billiard, futures, celery etc).

- create traceback objects from strings (the from_string method). No pickling is
  used.

- serialize tracebacks to/from plain dicts (the from_dict and to_dict methods).
  No pickling is used.

- raise the tracebacks created from the aforementioned sources.

- pickle an Exception together with its traceback and exception chain (raise ...
  from ...) (Python 3 only)

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1.1
- Demodernized packaging.

* Sun Oct 19 2025 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.

* Thu Oct 17 2024 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 1.3.0 -> 3.0.0.

* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.git20150727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.git20150727.1
- NMU: Use buildreq for BR.

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20150727
- Version 1.1.0

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150112
- Initial build for Sisyphus

