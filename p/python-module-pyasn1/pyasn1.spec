%define _unpackaged_files_terminate_build 1
%define mname pyasn1

%def_with check

Name: python-module-%mname
Version: 0.4.8
Release: alt1

Summary: Abstract Syntax Notation One (ASN.1), Python implementation
License: BSD
Group: Development/Python
# Source-git: https://github.com/etingof/pyasn1.git
Url: https://pypi.python.org/pypi/pyasn1

Source0: %name-%version.tar
Source1: pyasn1.watch
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(pytest)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
This is an implementation of ASN.1 types and codecs in Python programming
language. It has been first written to support particular protocol (SNMP)
but then generalized to be suitable for a wide range of protocols
based on ASN.1 specification.

%package -n python3-module-%mname
Summary: Abstract Syntax Notation One (ASN.1), Python 3 implementation
Group: Development/Python3

%description -n python3-module-%mname
This is an implementation of ASN.1 types and codecs in Python3 programming
language. It has been first written to support particular protocol (SNMP)
but then generalized to be suitable for a wide range of protocols
based on ASN.1 specification.

%prep
%setup
%patch -p1

rm -rf ../python3
cp -a . ../python3

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
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc LICENSE.rst README.md CHANGES.rst
%python_sitelibdir/pyasn1/
%python_sitelibdir/pyasn1-%version-*.egg-info/

%files -n python3-module-%mname
%doc LICENSE.rst README.md CHANGES.rst
%python3_sitelibdir/pyasn1/
%python3_sitelibdir/pyasn1-%version-*.egg-info/

%changelog
* Sat Nov 23 2019 Stanislav Levin <slev@altlinux.org> 0.4.8-alt1
- 0.4.5 -> 0.4.8.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 0.4.5-alt1
- 0.4.4 -> 0.4.5.

* Sun Oct 07 2018 Stanislav Levin <slev@altlinux.org> 0.4.4-alt1
- 0.4.3 -> 0.4.4.

* Thu May 31 2018 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1
- 0.4.2 -> 0.4.3

* Thu Mar 29 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt2
- Marked docstrings with backslashes as raw strings.

* Tue Mar 13 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1
- 0.3.7 -> 0.4.2

* Wed Nov 08 2017 Stanislav Levin <slev@altlinux.org> 0.3.7-alt1
- 0.1.8 -> 0.3.7

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt2.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.8-alt2.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt2
- Version 0.1.8

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.rc1
- Version 0.1.8rc1

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7-alt1.rc2
- Version 0.1.7rc2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.1.4-alt1.rc4.1
- Rebuild with Python-3.3

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.rc4
- Version 0.1.4rc4

* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Version 0.1.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.11a-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.11a-alt1
- Version 0.0.11a
- Added docs and tests

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7a-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.0.7a-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 16 2007 Peter V. Saveliev <peet@altlinux.org> 0.0.7a-alt1
- initial build

