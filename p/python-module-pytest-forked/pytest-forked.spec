%define _unpackaged_files_terminate_build 1
%define oname pytest-forked

%def_with check

Name: python-module-%oname
Version: 0.2
Release: alt1%ubt

Summary: pytest plugin for running tests in isolated forked subprocesses
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pytest-forked.git
Url: https://pypi.python.org/pypi/pytest-forked

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python-module-tox
BuildRequires: python-module-pycmd
BuildRequires: python-module-virtualenv
BuildRequires: python3-module-tox
BuildRequires: python3-module-pycmd
BuildRequires: python3-module-virtualenv
%endif

BuildArch: noarch
%py_provides %oname

%description
%summary.

%package -n python3-module-%oname
Summary: pytest plugin for running tests in isolated forked subprocesses
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
%summary.

%prep
%setup
cp -fR . ../python3

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

%python_install

pushd ../python3
%python3_install
popd

%check
%define python_version_nodots() %(%1 -Esc "import sys; sys.stdout.write('{0.major}{0.minor}'.format(sys.version_info))")

export PIP_INDEX_URL=http://host.invalid./
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

export PYTHONPATH=%buildroot%python_sitelibdir_noarch

# copy nessecary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages -e py%{python_version_nodots python} --notest
cp -f %_bindir/py.test .tox/py%{python_version_nodots python}/bin/

TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch

# copy nessecary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/py.test3 .tox/py%{python_version_nodots python3}/bin/py.test

TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages -e py%{python_version_nodots python3} -v -- -v
popd

%files
%doc LICENSE CHANGELOG README.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc LICENSE CHANGELOG README.rst
%python3_sitelibdir/*

%changelog
* Fri Apr 13 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1%ubt
- Initial build for ALT.
