%define _unpackaged_files_terminate_build 1
%define oname pytest-flake8

%def_with check

Name: python-module-%oname
Version: 1.0.4
Release: alt1
Summary: pytest plugin for efficiently checking PEP8 compliance
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/pytest-flake8

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-flake8
BuildRequires: python-module-pytest
BuildRequires: python3-module-flake8
BuildRequires: python3-module-tox
%endif

%description
pytest plugin for efficiently checking PEP8 compliance

%package -n python3-module-%oname
Summary: pytest plugin for efficiently checking PEP8 compliance
Group: Development/Python3

%description -n python3-module-%oname
pytest plugin for efficiently checking PEP8 compliance

%prep
%setup

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
sed -i '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc LICENSE CHANGELOG README.rst
%python_sitelibdir/pytest_flake8-*.egg-info/
%python_sitelibdir/pytest_flake8.py*

%files -n python3-module-%oname
%doc LICENSE CHANGELOG README.rst
%python3_sitelibdir/pytest_flake8-*.egg-info/
%python3_sitelibdir/pytest_flake8.py
%python3_sitelibdir/__pycache__/

%changelog
* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1
- 1.0.3 -> 1.0.4.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1
- 1.0.2 -> 1.0.3.

* Mon Oct 15 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- 0.9.1 -> 1.0.2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.1-alt1
- Initial build for ALT.
