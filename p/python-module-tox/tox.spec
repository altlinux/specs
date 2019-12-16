%define _unpackaged_files_terminate_build 1
%define oname tox

%def_with check

Name: python-module-%oname
Version: 3.14.2
Release: alt1

Summary: virtualenv-based automation of test activities
License: MIT
Group: Development/Python
# Source-git: https://github.com/tox-dev/tox.git
Url: https://pypi.python.org/pypi/tox/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: /proc
BuildRequires: python3(flaky)
BuildRequires: python3(freezegun)
BuildRequires: python3(pathlib2)
BuildRequires: python3(pip)
BuildRequires: python3(psutil)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(pytest_randomly)
BuildRequires: python3(pytest-xdist)
BuildRequires: python3(virtualenv)
BuildRequires: python3(six)
BuildRequires: python3(toml)
BuildRequires: python3(filelock)
%endif

BuildArch: noarch
%py_requires virtualenv

%description
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%package -n python3-module-%oname
Summary: virtualenv-based automation of test activities
Group: Development/Python3
%py3_requires virtualenv

%description -n python3-module-%oname
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%prep
%setup
%patch -p1

# unpin deps
grep -qsF 'psutil >= 5.6.1' setup.cfg || exit 1
sed -i 's/psutil >= 5.6.1, < 6;/psutil;/g' setup.cfg

cp -a . ../python3

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build

pushd ../python3
%python3_build
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
        mv $i $i.py3
done
popd

%python_install

%check
pushd ../python3
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export PIP_FIND_LINKS=%python3_sitelibdir_noarch/virtualenv_support
export TOX_TESTENV_PASSENV='SETUPTOOLS_SCM_PRETEND_VERSION PIP_NO_INDEX \
PIP_FIND_LINKS TOX_LIMITED_SHEBANG'
export TOX_LIMITED_SHEBANG=1
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
export TOXENV=py%{python_version_nodots python3}

sed -i '/\[testenv\][[:space:]]*$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini

%buildroot%_bindir/tox.py3 --sitepackages -p auto -o -rv -- -m "not internet"
popd

%files
%_bindir/tox
%_bindir/tox-quickstart
%python_sitelibdir/tox/
%python_sitelibdir/tox-*.egg-info/

%files -n python3-module-%oname
%_bindir/tox.py3
%_bindir/tox-quickstart.py3
%python3_sitelibdir/tox/
%python3_sitelibdir/tox-*.egg-info/

%changelog
* Thu Dec 12 2019 Stanislav Levin <slev@altlinux.org> 3.14.2-alt1
- 3.14.1 -> 3.14.2.

* Fri Nov 15 2019 Stanislav Levin <slev@altlinux.org> 3.14.1-alt1
- 3.14.0 -> 3.14.1.

* Fri Oct 11 2019 Stanislav Levin <slev@altlinux.org> 3.14.0-alt1
- 3.13.2 -> 3.14.0.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 3.13.2-alt2
- Fixed testing against Pytest 5.

* Fri Aug 02 2019 Stanislav Levin <slev@altlinux.org> 3.13.2-alt1
- 3.12.1 -> 3.13.2.

* Fri May 24 2019 Stanislav Levin <slev@altlinux.org> 3.12.1-alt1
- 3.11.1 -> 3.12.1.

* Thu May 16 2019 Stanislav Levin <slev@altlinux.org> 3.11.1-alt1
- 3.11.0 -> 3.11.1.

* Thu May 16 2019 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.10.0 -> 3.11.0.

* Mon May 13 2019 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1
- 3.9.0 -> 3.10.0.

* Wed May 01 2019 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.7.0 -> 3.9.0.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.6.1 -> 3.7.0.

* Mon Dec 31 2018 Stanislav Levin <slev@altlinux.org> 3.6.1-alt1
- 3.5.3 -> 3.6.1.

* Mon Oct 29 2018 Stanislav Levin <slev@altlinux.org> 3.5.3-alt1
- 3.5.2 -> 3.5.3.

* Thu Oct 04 2018 Stanislav Levin <slev@altlinux.org> 3.5.2-alt1
- 3.2.1 -> 3.5.2.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1
- 3.0.0 -> 3.2.1.

* Wed Apr 11 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.9.1 -> 3.0.0

* Thu Oct 19 2017 Stanislav Levin <slev@altlinux.org> 2.9.1-alt1
- Version 2.9.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Version 1.9.0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Version 1.8.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

