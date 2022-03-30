%define _unpackaged_files_terminate_build 1
%define oname testtools

%def_with check

Name: python3-module-%oname
Version: 2.5.0
Release: alt2

Summary: Extensions to the Python standard library's unit testing framework

Group: Development/Python3
License: MIT
Url: https://pypi.org/project/testtools/

# Source-url: https://github.com/testing-cabal/testtools
Source: %name-%version.tar

Patch0: testtools-2.5.0-Add-support-for-Python-3.10.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

%if_with check
# install_requires=
BuildRequires: python3(extras)
BuildRequires: python3(fixtures)

BuildRequires: python3(testscenarios)
BuildRequires: python3(testresources)
BuildRequires: python3(twisted.trial)

BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
%endif

%add_python3_req_skip twisted

%description
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.

%prep
%setup
%autopatch -p1

%build
export PBR_VERSION=%version
%python3_build

%install
export PBR_VERSION=%version
%python3_install

%check
export PBR_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps -vvr -s false --develop

%files
%doc LICENSE NEWS README*
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Mar 30 2022 Stanislav Levin <slev@altlinux.org> 2.5.0-alt2
- Fixed FTBFS (Python 3.10).

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0 (with rpmrb script)

* Wed Mar 31 2021 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- new version 2.4.0 (with rpmrb script)

* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt3
- build python3 package separately
- drop BR: html5lib

* Mon Apr 22 2019 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt2
- Fixed build for python3.7.

* Mon Aug 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0.

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.8.0-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt2
- Fixed requirements

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Version 1.8.0

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Fixed requirements

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0
- Added docs

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.9.8-alt1.2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.2
- Added module for Python 3 (bootstrap)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt1.1
- Rebuild with Python-2.7

* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.9.8-alt1
- New version 0.9.8

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.7-alt1
- New version 0.9.7

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.6-alt1
- initial build

