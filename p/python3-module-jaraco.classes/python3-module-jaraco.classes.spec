%define _unpackaged_files_terminate_build 1
%define  modulename jaraco.classes

%def_enable check

Name:    python3-module-%modulename
Version: 3.1.0
Release: alt1

Summary: Utility functions for Python class constructs
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.classes

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools_scm
BuildRequires: python3-module-setuptools

%if_enabled check
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

%description
%summary

%prep
%setup
%patch0 -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export PIP_NO_BUILD_ISOLATION=no
export TOXENV=py%{python_version_nodots python3}
# replace pytest executable name
sed -i 's|pytest |py.test3 |g' tox.ini

sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    _PYTEST_BIN = %_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/py.test3\
skip_install = True' tox.ini
# removing development stage testing options
sed -i 's|addopts=.*|addopts=|' pytest.ini
# no tests applied now in upstream. added dumb one now
cat > test_dumb.py <<EOF
def test_nothing():
    pass
EOF

tox.py3 --sitepackages -vvr

%files
%python3_sitelibdir/jaraco/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/jaraco/__init__*
%exclude %python3_sitelibdir/jaraco/__pycache__/__init__*

%changelog
* Wed Nov 18 2020 Danil Shein <dshein@altlinux.org> 3.1.0-alt1
- update version to 3.1.0
- build with check enabled

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 2.0-alt1
- first build for ALT

