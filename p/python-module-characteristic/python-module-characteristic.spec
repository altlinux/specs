%define oname characteristic
%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1

Summary: Python library that eases the chores of implementing attributes

License: MIT
Group: Development/Python
Url: https://github.com/hynek/characteristic

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/c/characteristic/characteristic-0.1.0.tar.gz
Source: %oname-%version.tar
BuildArch: noarch

BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%setup_python_module %oname

%description
characteristic is an MIT-licensed Python package with class decorators that ease the chores of
implementing the most common attribute-related object protocols.

%if_with python3
%package -n python3-module-%oname
Summary: Python library that eases the chores of implementing attributes (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
characteristic is an MIT-licensed Python package with class decorators that ease the chores of
implementing the most common attribute-related object protocols.
%endif


%prep
%setup -n %oname-%version

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc AUTHORS.rst CONTRIBUTING.rst README.rst
%python_sitelibdir/%oname.py
%python_sitelibdir/test_%oname.py
%exclude %python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*.pyc
%exclude %python_sitelibdir/*.pyo

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname.py
%python3_sitelibdir/test_%oname.py
%exclude %python3_sitelibdir/*.egg-*
%exclude %python3_sitelibdir/__pycache__/
%endif

%changelog
* Thu Jul 31 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.0-alt1
- initial build for Sisyphus
