%define _unpackaged_files_terminate_build 1
%define oname pytest-mock

%def_with check

Name: python-module-%oname
Version: 1.9.0
Release: alt1%ubt

Summary: Thin-wrapper around the mock package for easier use with py.test
License: MIT
Group: Development/Python
# https://github.com/pytest-dev/pytest-mock.git
Url: https://pypi.python.org/pypi/pytest-mock

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python-module-mock
BuildRequires: python-module-tox
BuildRequires: python-module-virtualenv
BuildRequires: python-module-coverage
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-coverage
%endif

BuildArch: noarch
# python2.7 requires mock
%py_requires mock
%py_provides %oname

%description
Thin-wrapper around the mock package for easier use with py.test

This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test

%package -n python3-module-%oname
Summary: Thin-wrapper around the mock package for easier use with py.test
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Thin-wrapper around the mock package for easier use with py.test

This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test

%prep
%setup
rm -rf ../python3
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

%python_install

pushd ../python3
%python3_install
popd

%check
%define python_version_nodots() %(%1 -Esc "import sys; sys.stdout.write('{0.major}{0.minor}'.format(sys.version_info))")

export PIP_INDEX_URL=http://host.invalid./
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

export PYTHONPATH=$(pwd)

# copy nessecary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages -e py%{python_version_nodots python} --notest
cp -f %_bindir/coverage .tox/py%{python_version_nodots python}/bin/

TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages -e py%{python_version_nodots python} -v

pushd ../python3
export PYTHONPATH=$(pwd)

# copy nessecary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/coverage3 .tox/py%{python_version_nodots python3}/bin/coverage

TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages -e py%{python_version_nodots python3} -v
popd

%files
%doc LICENSE *.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*

%changelog
* Thu Apr 12 2018 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1%ubt
- 1.6.2 -> 1.9.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.2-alt1
- Updated to upstream version 1.6.2.

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux Sisyphus.
