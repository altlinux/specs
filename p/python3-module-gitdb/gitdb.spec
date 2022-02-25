%define _unpackaged_files_terminate_build 1
%define oname gitdb

%def_with check

Name: python3-module-%oname
Version: 4.0.9
Release: alt1

Summary: IO of git-style object databases

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/gitdb/

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(smmap)

BuildRequires: python3(nose)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: /usr/bin/git
%endif

%description
IO of git-style object databases.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
IO of git-style object databases.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

# unbundle
rm -vr gitdb/ext/*

%check
# need git repo and objects, see gitdb/test/lib.py
git init
git config user.email "someone@somewhere.com"
git config user.name "someone"
git add -A
git commit -m "%version"

cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
# see gitdb/test/lib.py::skip_on_travis_ci
export TRAVIS=YES
export TOX_TESTENV_PASSENV='TRAVIS'
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc AUTHORS *.rst
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/%oname/test/

%files tests
%python3_sitelibdir/%oname/test/

%changelog
* Fri Jan 28 2022 Stanislav Levin <slev@altlinux.org> 4.0.9-alt1
- 4.0.7 -> 4.0.9.

* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.7-alt1
- new version (4.0.7) with rpmgs script
- build python3 module separately
- switch to build from tarball

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt3.qa1
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt2.qa1
- NMU: remove %%ubt from release

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1.qa1
- NMU: applied repocop patch

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.3-alt1
- Updated to upstream version 2.0.3.

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.4-alt1.git20150112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.6.4-alt1.git20150112.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.git20150112
- Version 0.6.4

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141114
- Version 0.6.0
- Added module for Python 3

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Fri Oct 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for ALTLinux Sisyphus

