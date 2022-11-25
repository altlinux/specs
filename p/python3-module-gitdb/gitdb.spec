%define _unpackaged_files_terminate_build 1
%define pypi_name gitdb

%def_with check

Name: python3-module-%pypi_name
Version: 4.0.10
Release: alt1

Summary: IO of git-style object databases

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/gitdb/
VCS: https://github.com/gitpython-developers/gitdb.git

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires=
BuildRequires: python3(smmap)

BuildRequires: python3(pytest)
BuildRequires: /usr/bin/git
%endif

%description
IO of git-style object databases.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description tests
IO of git-style object databases.

This package contains tests for %pypi_name.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# unbundle
rm -vr gitdb/ext/*

%check
# need git repo and objects, see gitdb/test/lib.py
git init
git config user.email "someone@somewhere.com"
git config user.name "someone"
git add -A
git commit -m "%version"

%tox_create_default_config
%tox_check_pyproject

%files
%doc AUTHORS *.rst
%python3_sitelibdir/gitdb/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/gitdb/test/

%files tests
%python3_sitelibdir/gitdb/test/

%changelog
* Fri Nov 25 2022 Stanislav Levin <slev@altlinux.org> 4.0.10-alt1
- 4.0.9 -> 4.0.10.

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

