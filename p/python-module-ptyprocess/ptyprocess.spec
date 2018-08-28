%define _unpackaged_files_terminate_build 1
%define oname ptyprocess

%def_with check

Name: python-module-%oname
Version: 0.6.0
Release: alt1

Summary: Run a subprocess in a pseudo terminal
License: ISCL
Group: Development/Python
# Source-git: https://github.com/pexpect/ptyprocess.git
Url: https://pypi.python.org/pypi/ptyprocess

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /dev/pts
BuildRequires: python-module-pytest
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

Sometimes, piping stdin and stdout is not enough. There might be a
password prompt that doesn't read from stdin, output that changes when
it's going to a pipe rather than a terminal, or curses-style interfaces
that rely on a terminal. If you need to automate these things, running
the process in a pseudo terminal (pty) is the answer.

%package -n python3-module-%oname
Summary: Run a subprocess in a pseudo terminal
Group: Development/Python3

%description -n python3-module-%oname
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

Sometimes, piping stdin and stdout is not enough. There might be a
password prompt that doesn't read from stdin, output that changes when
it's going to a pipe rather than a terminal, or curses-style interfaces
that rely on a terminal. If you need to automate these things, running
the process in a pseudo terminal (pty) is the answer.

%prep
%setup

cp -a . ../python3

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	../python3/tests/test_invalid_binary.py \
	../python3/tests/test_preexec_fn.py

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
py.test -v

pushd ../python3
py.test3 -v
popd

%files
%doc README.rst docs/*.rst
%python_sitelibdir/ptyprocess/
%python_sitelibdir/ptyprocess-*.egg-info

%files -n python3-module-%oname
%doc README.rst docs/*.rst
%python3_sitelibdir/ptyprocess/
%python3_sitelibdir/ptyprocess-*.egg-info

%changelog
* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.2 -> 0.6.0.

* Wed Mar 21 2018 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1
- 0.5 -> 0.5.2

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

