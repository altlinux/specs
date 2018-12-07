%define  modulename termcolor
%def_with python3

Name:    python-module-%modulename
Version: 1.1.0
Release: alt1

Summary: ANSII Color formatting for output in terminal
License: MIT
Group:   Development/Python
URL:     http://pypi.python.org/pypi/termcolor

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildArch: noarch
Source:  %modulename-%version.tar.gz

%description
%summary

%package -n python3-module-%modulename
Summary: ANSII Color formatting for output in terminal
Group: Development/Python3

%description -n python3-module-%modulename
%summary

%prep
%setup -n %modulename-%version
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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%endif

%changelog
* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt1
Initial build
