%define oname dockerpty
%def_with python3

Name: python-module-%oname
Version: 0.3.4
Release: alt1

Summary: Use the pseudo-tty of a docker container.

License: %asl
Group: Development/Python
Url: https://github.com/d11wtq/dockerpty

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
Python library to use the pseudo-tty of a docker container.

%if_with python3
%package -n python3-module-%oname
Summary: Use the pseudo-tty of a docker container (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Python library to use the pseudo-tty of a docker container. 
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
%doc LICENSE.txt README.md
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.ru> 0.3.4-alt1
- 0.3.4
