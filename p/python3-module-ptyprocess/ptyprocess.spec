%define _unpackaged_files_terminate_build 1
%define oname ptyprocess

%def_with check

Name: python3-module-%oname
Version: 0.7.0
Release: alt1

Summary: Run a subprocess in a pseudo terminal

License: ISCL
Group: Development/Python3
Url: https://pypi.python.org/pypi/ptyprocess

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /dev/pts
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

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	tests/test_invalid_binary.py \
	tests/test_preexec_fn.py

%build
%python3_build

%install
%python3_install

%check
py.test3 -v

%files
%doc README.rst docs/*.rst
%python3_sitelibdir/ptyprocess/
%python3_sitelibdir/ptyprocess-*.egg-info

%changelog
* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt2
- Drop python2 support.

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

