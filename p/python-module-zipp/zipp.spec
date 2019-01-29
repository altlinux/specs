%define _unpackaged_files_terminate_build 1
%define oname zipp

%def_with check

Name: python-module-%oname
Version: 0.3.3
Release: alt1
Summary: A pathlib-compatible Zipfile object wrapper
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/zipp/

# Source-git: https://github.com/jaraco/zipp.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python-module-pytest
BuildRequires: python-module-pytest-flake8
BuildRequires: python3-module-pytest-flake8
BuildRequires: python3-module-tox
%endif

%description
%summary

%package -n python3-module-%oname
Summary: %summary
Group: Development/Python3

%description -n python3-module-%oname
%summary

%prep
%setup
# currently disable PEP517/518
rm -f pyproject.toml

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
    cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini

# no used requires
sed -i -e '/pytest-checkdocs/d' \
-e 's/pathlib2$/pathlib2; python_version < \x273\x27/' setup.cfg
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
%_bindir/tox.py3 --sitepackages -p auto -o -v

%files
%doc LICENSE README.rst
%python_sitelibdir/zipp.py*
%python_sitelibdir/zipp-*.egg-info/

%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/zipp.py
%python3_sitelibdir/__pycache__/zipp.cpython-*.py*
%python3_sitelibdir/zipp-*.egg-info/

%changelog
* Mon Jan 28 2019 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- Initial build.
