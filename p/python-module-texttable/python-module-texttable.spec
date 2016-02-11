%define oname texttable
%def_with python3

Name: python-module-%oname
Version: 0.8.4
Release: alt1

Summary: Module for creating simple ASCII tables

License: %lgpl3only
Group: Development/Python
Url: https://github.com/foutaise/texttable

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%setup_python_module %oname

%description
texttable is a module to generate a formatted text table, using ASCII characters.

%if_with python3
%package -n python3-module-%oname
Summary: Module for creating simple ASCII tables (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
texttable is a module to generate a formatted text table, using ASCII characters.
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
%doc LICENSE
%python_sitelibdir/%oname.*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname.*
%python3_sitelibdir/*.egg-*
%python3_sitelibdir/__pycache__/*
%endif

%changelog
* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.ru> 0.8.3-alt1
- 0.8.3
