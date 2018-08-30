%define _unpackaged_files_terminate_build 1
%define oname pathlib

Name: python-module-%oname
Version: 1.0.1
Release: alt3
Summary: Object-oriented filesystem paths
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pathlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-test
BuildRequires: python-module-pytest

%description
pathlib offers a set of classes to handle filesystem paths. It offers
the following advantages over using string objects:

* No more cumbersome use of os and os.path functions. Everything can be
  done easily through operators, attribute accesses, and method calls.
* Embodies the semantics of different path types. For example, comparing
  Windows paths ignores casing.
* Well-defined semantics, eliminating any warts or ambiguities (forward
  vs. backward slashes, etc.).

%prep
%setup

%build
%python_build

%install
%python_install

%check
py.test -v

%files
%doc *.txt docs/*.rst
%python_sitelibdir/pathlib.py*
%python_sitelibdir/pathlib-*.egg-info/

%changelog
* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt3
- Drop python3 package.

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.1
- NMU: Use buildreq for BR.

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

