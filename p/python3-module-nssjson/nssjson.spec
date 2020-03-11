%define oname nssjson

Name: python3-module-%oname
Version: 0.7
Release: alt2

Summary: Not So Simple JSON encoder/decoder
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/nssjson

# https://github.com/lelit/nssjson.git
# branch: nssjson
Source: %name-%version.tar
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname


%description
nssjson is a (not so) simple, fast, complete, correct and extensible
JSON encoder and decoder for Python 2.5+ and Python 3.3+. It is pure
Python code with no dependencies, but includes an optional C extension
for a serious speed boost.

nssjson is a fork of simplejson that fulfills my need of having a good
performance JSON encoder/decoder able to handle also Python's datetime
and UUID, even if with an admittedly non-standard and faulty heuristic
that was not considered within the scope of the original product.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
nssjson is a (not so) simple, fast, complete, correct and extensible
JSON encoder and decoder for Python 2.5+ and Python 3.3+. It is pure
Python code with no dependencies, but includes an optional C extension
for a serious speed boost.

nssjson is a fork of simplejson that fulfills my need of having a good
performance JSON encoder/decoder able to handle also Python's datetime
and UUID, even if with an admittedly non-standard and faulty heuristic
that was not considered within the scope of the original product.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Wed Mar 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7-alt1.git20150807.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.git20150807.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt1.git20150807.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20150807
- Initial build for Sisyphus

