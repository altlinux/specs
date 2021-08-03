%define _unpackaged_files_terminate_build 1
%define oname future

%def_with check

Name: python3-module-%oname
Version: 0.18.2
Release: alt2
Summary: Clean single-source support for Python 3 and 2
License: MIT
Group: Development/Python3
Url: https://python-future.org/

# https://github.com/PythonCharmers/python-future.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox)
%endif

# filter requires of self
%filter_from_requires /python3\(\.[[:digit:]]\)\?(future\..*)/d

%description
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/*/*/test
rm -r %buildroot%python3_sitelibdir/*/tests

rm -r %buildroot%_bindir/*

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
export NO_INTERNET=YES
export TOX_TESTENV_PASSENV='NO_INTERNET'
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc *.txt *.rst
%python3_sitelibdir/*

%changelog
* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 0.18.2-alt2
- Drop python2 support.

* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 0.18.2-alt1
- 0.16.0 -> 0.18.2.
- Reenabled testing for Python3.

* Tue Jul 25 2017 Terechkov Evgenii <evg@altlinux.org> 0.16.0-alt2
- Skip findreq on some carried modules

* Wed Jun 21 2017 Terechkov Evgenii <evg@altlinux.org> 0.16.0-alt1
- 0.16.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15.0-alt1.git20150725.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.15.0-alt1.git20150725.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1.git20150725
- Version 0.15.0

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.3-alt1.git20150203
- Version 0.14.3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.3-alt1
- Initial build for Sisyphus

