%define _unpackaged_files_terminate_build 1
%define oname paramiko

%def_with check

Name: python3-module-%oname
Version: 2.8.1
Release: alt1

Summary: SSH2 protocol for python
License: LGPL-2.1
Group: Development/Python3
# Source-git: https://github.com/paramiko/paramiko.git
Url: http://www.paramiko.org/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(bcrypt)
BuildRequires: python3(cryptography)
BuildRequires: python3(gssapi)
BuildRequires: python3(invoke)
BuildRequires: python3(pyasn1)
BuildRequires: python3(k5test)
BuildRequires: python3(mock)
BuildRequires: python3(nacl)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines. It is written
entirely in python (no C or platform-dependent code).

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vv -r -- -v -ra

%files
%doc README.rst LICENSE
%python3_sitelibdir/paramiko/
%python3_sitelibdir/paramiko-%version-py%_python3_version.egg-info/

%changelog
* Thu Dec 02 2021 Stanislav Levin <slev@altlinux.org> 2.8.1-alt1
- 2.7.2 -> 2.8.1.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 2.7.2-alt2
- Fixed FTBFS(Pytest 6).

* Thu Sep 10 2020 Stanislav Levin <slev@altlinux.org> 2.7.2-alt1
- 2.7.1 -> 2.7.2.

* Mon Jul 06 2020 Stanislav Levin <slev@altlinux.org> 2.7.1-alt1
- 2.6.0 -> 2.7.1.

* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1
- 2.4.2 -> 2.6.0.

* Mon Oct 29 2018 Stanislav Levin <slev@altlinux.org> 2.4.2-alt1
- 2.4.1 -> 2.4.2.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1
- 2.4.0 -> 2.4.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.0-alt1
- Updated to upstream version 2.4.0.

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.1-alt1
- Updated to upstream version 2.2.1.

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.16.0-alt2.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.16.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.16.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Jan 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt2
- 1.16.0 Release

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.0-alt1.git20150429
- Version 1.16.0

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.2-alt1
- Version 1.15.2

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.1-alt1
- Version 1.15.1

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.0-alt1
- Version 1.14.0
- Added module for Python 3

* Fri Aug 09 2013 Anatoly Kitaykin <cetus@altlinux.org> 1.11.0-alt1
- Version 1.11.0 (ALT #29340)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.6-alt1.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.6-alt1
- Version 1.7.6 (ALT #23843)

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1.1.1
- Rebuilt with python 2.6

* Fri Feb 08 2008 Grigory Batalov <bga@altlinux.ru> 1.7.2-alt1.1
- Rebuilt with python-2.5.

* Mon Feb 04 2008 Andriy Stepanov <stanv@altlinux.ru> 1.7.2-alt1
- Up to new version

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.5.3-alt2.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Fri Mar 31 2006 Andriy Stepanov <stanv@altlinux.ru> 1.5.3-alt2
- Modifications in spec file for doc package

* Fri Mar 31 2006 Stepanov Andriy <stanv@altlinux.ru> 1.5.3-alt1
- Initial build

