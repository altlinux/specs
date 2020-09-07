%define _unpackaged_files_terminate_build 1
%define oname pytest-virtualenv

%def_with check

Name: python3-module-%oname
Version: 1.7.0
Release: alt2

Summary: Virtualenv fixture for py.test
License: MIT
Group: Development/Python
# Source-git: https://github.com/manahl/pytest-plugins.git
Url: https://pypi.python.org/pypi/pytest-virtualenv

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(mock)
BuildRequires: python3(pytest_fixture_config)
BuildRequires: python3(pytest_shutil)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
Create a Python virtual environment in your test that cleans up on teardown.
The fixture has utility methods to install packages and list what's installed.

%prep
%setup -n %oname-%version

# fix dependency
sed -i -e 's:setuptools-git:setuptools:g' \
	common_setup.py

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
export TOXENV=py%{python_version_nodots python3}
export TOX_TESTENV_PASSENV='PIP_NO_INDEX'
tox.py3 --sitepackages -vvr

%files
%doc LICENSE *.md
%python3_sitelibdir/pytest_virtualenv.py
%python3_sitelibdir/__pycache__/pytest_virtualenv.cpython-*
%python3_sitelibdir/pytest_virtualenv-%version-py%_python3_version.egg-info/

%changelog
* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 1.7.0-alt2
- Stopped build Python2 package.

* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.6.0 -> 1.7.0.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 1.6.0-alt2
- Fixed minor typo in tox.ini.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.3.0 -> 1.6.0.

* Sun Mar 25 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.11 -> 1.3.0
- Change Python3 DEFAULT_VIRTUALENV_FIXTURE_EXECUTABLE to ALT specific

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.11-alt1
- Initial build for ALT.
