%define oname xapp
%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1

Summary: Python Xapp Library

License: LGPLv2
Group: Development/Python
Url: https://github.com/linuxmint/python-xapp

Source: python-%oname-%version.tar
BuildArch: noarch

BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%if_with python3
BuildRequires(pre): rpm-build-python3
%endif

%setup_python_module %oname

%description
Python Xapp Library

%if_with python3
%package -n python3-module-%oname
Summary: Python Xapp Library
Group: Development/Python3

%description -n python3-module-%oname
Python Xapp Library
%endif


%prep
%setup -n python-%oname-%version

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
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
