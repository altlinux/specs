%define oname ptyprocess

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.git20150617.2.1
Summary: Run a subprocess in a pseudo terminal
License: ISCL
Group: Development/Python
Url: https://pypi.python.org/pypi/ptyprocess/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pexpect/ptyprocess.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools /dev/pts
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

Sometimes, piping stdin and stdout is not enough. There might be a
password prompt that doesn't read from stdin, output that changes when
it's going to a pipe rather than a terminal, or curses-style interfaces
that rely on a terminal. If you need to automate these things, running
the process in a pseudo terminal (pty) is the answer.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

Sometimes, piping stdin and stdout is not enough. There might be a
password prompt that doesn't read from stdin, output that changes when
it's going to a pipe rather than a terminal, or curses-style interfaces
that rely on a terminal. If you need to automate these things, running
the process in a pseudo terminal (pty) is the answer.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Run a subprocess in a pseudo terminal
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

Sometimes, piping stdin and stdout is not enough. There might be a
password prompt that doesn't read from stdin, output that changes when
it's going to a pipe rather than a terminal, or curses-style interfaces
that rely on a terminal. If you need to automate these things, running
the process in a pseudo terminal (pty) is the answer.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

Sometimes, piping stdin and stdout is not enough. There might be a
password prompt that doesn't read from stdin, output that changes when
it's going to a pipe rather than a terminal, or curses-style interfaces
that rely on a terminal. If you need to automate these things, running
the process in a pseudo terminal (pty) is the answer.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	../python3/tests/test_invalid_binary.py \
	../python3/tests/test_preexec_fn.py
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
cp -fR tests %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
cp -fR tests %buildroot%python3_sitelibdir/%oname/
popd
%endif

%check
py.test
%if_with python3
pushd ../python3
py.test3
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt1.git20150617.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt1.git20150617.2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150617.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150617
- Version 0.5

* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150222
- Version 0.4

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2.git20141013
- Enabled testing

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20141013
- Initial build for Sisyphus

