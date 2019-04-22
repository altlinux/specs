%define _unpackaged_files_terminate_build 1
%define oname unittest_mixins

%def_with check

Name: python-module-%oname
Version: 1.6
Release: alt1

Summary: A set of mixin classes and other helpers for unittest test case classes
License: LGPLv3
Group: Development/Python
# https://github.com/nedbat/unittest-mixins.git
Url: https://pypi.org/project/unittest-mixins/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(coverage)
BuildRequires: python2.7(pytest)
BuildRequires: python3(coverage)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
A set of mixin classes and other helpers for unittest test case classes.

%package -n python3-module-%oname
Summary: Declare constraints on function parameters and return values
Group: Development/Python3

%description -n python3-module-%oname
A set of mixin classes and other helpers for unittest test case classes.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd

%python_install

%check
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/coverage \{envbindir\}\/coverage\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/coverage' tox.ini

export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -vr

%files
%doc *.rst
%python_sitelibdir/%oname-%version-py%_python_version.egg-info/
%python_sitelibdir/%oname/

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/%oname/

%changelog
* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 1.6-alt1
- Initial build for Sisyphus.

