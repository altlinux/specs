%define _unpackaged_files_terminate_build 1
%define pypi_name pyasn1

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.1
Release: alt1
Summary: Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/pyasn1/
Vcs: https://github.com/pyasn1/pyasn1
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%endif

%description
This is an implementation of ASN.1 types and codecs in Python programming
language. It has been first written to support particular protocol (SNMP)
but then generalized to be suitable for a wide range of protocols
based on ASN.1 specification.

%prep
%setup
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -s tests

%files
%doc README.md CHANGES.rst
%python3_sitelibdir/pyasn1/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Dec 08 2023 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- 0.5.0 -> 0.5.1.

* Thu Apr 20 2023 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.8 -> 0.5.0.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 0.4.8-alt2
- Built Python3 package from its ows src.

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

