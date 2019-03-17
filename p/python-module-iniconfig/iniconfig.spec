%define _unpackaged_files_terminate_build 1
%define oname iniconfig

%def_with check

Name: python-module-%oname
Version: 1.0.0
Release: alt1

Summary: A small and simple INI-file parser
License: MIT
Group: Development/Tools
# Source-git: https://github.com/RonnyPfannschmidt/iniconfig.git
Url: https://pypi.org/project/iniconfig/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python2.7(setuptools_scm)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python2.7(pytest)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
%summary

%package -n python3-module-%oname
Summary: %summary
Group: Development/Python3

%description -n python3-module-%oname
%summary

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
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
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOX_TESTENV_PASSENV='SETUPTOOLS_SCM_PRETEND_VERSION'
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}

sed -i '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
tox.py3 --sitepackages -p auto -o -v -r

%files
%doc CHANGELOG LICENSE README.txt
%python_sitelibdir/iniconfig.py*
%python_sitelibdir/iniconfig-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc CHANGELOG LICENSE README.txt
%python3_sitelibdir/iniconfig.py
%python3_sitelibdir/__pycache__/iniconfig.cpython-*
%python3_sitelibdir/iniconfig-%version-py%_python3_version.egg-info/

%changelog
* Sat Mar 16 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build.

