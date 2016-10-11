%define modulename wget
%def_with python3

Name: python-module-%modulename
Version: 3.2
Release: alt1

%setup_python_module %modulename

Summary: pure python download utility
License: GPL
Group: Development/Python

Url: https://pypi.python.org/pypi/wget
Packager: Konstantin Artyushkin <akv@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: %py_dependencies setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
%summary

#--------------------------------------------------------------------------------
%if_with python3
%package -n python3-module-%modulename
Summary: pure python download utility
Group: Development/Python3

%description -n python3-module-%modulename
%summary
%endif
#--------------------------------------------------------------------------------

%prep
%setup
%if_with python3
rm -fr ../python3
cp -a ./ ../python3
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
%python_sitelibdir/%modulename.*
%python_sitelibdir/%modulename-*.egg-info

#--------------------------------------------------------------------------------
%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/%modulename.*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%modulename-*.egg-info
%endif
#--------------------------------------------------------------------------------

%changelog
* Tue Oct 11 2016 Konstantin Artyushkin <akv@altlinux.org> 3.2-alt1
- new version

