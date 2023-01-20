%define _unpackaged_files_terminate_build 1
%define pypi_name GitPython

%def_with check

Name: python3-module-%pypi_name
Version: 3.1.30
Release: alt1

Summary: GitPython is a python library used to interact with Git repositories

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/GitPython/
VCS: https://github.com/gitpython-developers/GitPython

Source: %name-%version.tar
Source1: git-history-tests.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires=
BuildRequires: python3(gitdb)
BuildRequires: python3(gitdb.test)
BuildRequires: /usr/bin/git
BuildRequires: /usr/sbin/git-daemon

BuildRequires: /proc
BuildRequires: python3(ddt)
BuildRequires: python3(pytest)
%endif

Requires: /usr/bin/git

# PyPI names
Provides: python3-module-gitpython = %EVR
%py3_provides GitPython
%py3_provides gitpython

%description
%pypi_name is a python library used to interact with git repositories,
high-level like git-porcelain, or low-level like git-plumbing.

It provides abstractions of git objects for easy access of repository data, and
additionally allows you to access the git repository more directly using either
a pure python implementation, or the faster, but more resource intensive git
command implementation.

The object database implementation is optimized for handling large quantities of
objects and large datasets, which is achieved by using low-level structures and
data streaming.

%prep
%setup -a 1
%autopatch -p1

# unbundle
rm -vr git/ext/*

%build
%pyproject_build

%install
%pyproject_install

%check
# Tests expect project's own git repo + submodules
export GIT_CONFIG_GLOBAL=~/.gitconfig
cat test/fixtures/.gitconfig > "$GIT_CONFIG_GLOBAL"
git config --global user.email "someone@somewhere.com"
git config --global user.name "someone"

# prepare test git repo
TEST_REPO="$(pwd)/test_repo"
rm -rf "$TEST_REPO"
mkdir "$TEST_REPO"
cp -a .git "$TEST_REPO"/
pushd "$TEST_REPO"
# see .github/workflows/pythonpackage.yml
TRAVIS=yes ../init-tests-after-clone.sh
popd
export GIT_PYTHON_TEST_GIT_REPO_BASE="$TEST_REPO"

# /usr/sbin/git-daemon
export PATH=$PATH:%_sbindir
export NO_SUBMODULES=YES
%pyproject_run_pytest \
    -vra \
    --ignore test/test_installation.py \
    --ignore test/test_submodule.py

%files
%python3_sitelibdir/git/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Fri Jan 20 2023 Stanislav Levin <slev@altlinux.org> 3.1.30-alt1
- 3.1.29 -> 3.1.30.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 3.1.29-alt1
- 3.1.28 -> 3.1.29.

* Fri Oct 07 2022 Stanislav Levin <slev@altlinux.org> 3.1.28-alt1
- 3.1.27 -> 3.1.28.

* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 3.1.27-alt1
- 3.1.14 -> 3.1.27.

* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.14-alt1
- new version
- build python3 module standalone

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.10-alt1
- Updated to upstream version 2.1.10.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- Updated to upstream version 2.1.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1
- Version 0.3.6
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1rc1.2
- Fixed build

* Mon Jul 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt1rc1.1
- merge upstream/master

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt0rc1.1
- 0.3.2-rc1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt1.1
- Rebuild with Python-2.7

* Fri Oct 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4.1-alt1.1
- Rebuilt with python 2.6

* Fri Nov 28 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 0.1.4.1-alt1
- Initial build for ALTLinux Sisyphus

