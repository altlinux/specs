%define _unpackaged_files_terminate_build 1
%define oname pytest-mock

%def_with check

Name: python-module-%oname
Version: 1.10.4
Release: alt2

Summary: Thin-wrapper around the mock package for easier use with py.test
License: MIT
Group: Development/Python
# https://github.com/pytest-dev/pytest-mock.git
Url: https://pypi.python.org/pypi/pytest-mock

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python2.7(setuptools_scm)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python2.7(coverage)
BuildRequires: python2.7(mock)
BuildRequires: python2.7(pytest)
BuildRequires: python3(coverage)
BuildRequires: python3(tox)
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
%patch -p1
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
sed -i '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/coverage \{envbindir\}\/coverage\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/coverage' tox.ini
export PIP_NO_INDEX=YES
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc LICENSE *.rst
%python_sitelibdir/_pytest_mock_version.py*
%python_sitelibdir/pytest_mock.py*
%python_sitelibdir/pytest_mock-*.egg-info/

%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/_pytest_mock_version.py
%python3_sitelibdir/pytest_mock.py
%python3_sitelibdir/pytest_mock-*.egg-info/
%python3_sitelibdir/__pycache__/_pytest_mock_version.*
%python3_sitelibdir/__pycache__/pytest_mock.*

%changelog
* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.10.4-alt2
- Added missing dep on Pytest.

* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 1.10.4-alt1
- 1.10.1 -> 1.10.4.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 1.10.1-alt1
- 1.10.0 -> 1.10.1.

* Sun Oct 21 2018 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1
- 1.9.0 -> 1.10.0.

* Thu Apr 12 2018 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.6.2 -> 1.9.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.2-alt1
- Updated to upstream version 1.6.2.

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux Sisyphus.
