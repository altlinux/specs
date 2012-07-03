%define pkgname requests
%def_with python3

Summary: HTTP library, written in Python, for human beings
Name: python-module-requests
Version: 0.12.1
Release: alt1
License: ISC and MIT
Group: Development/Python
Url: https://github.com/kennethreitz/requests

Source: %name-%version.tar
BuildRequires: python-devel python-modules-json
BuildArch: noarch

%description
Most existing Python modules for sending HTTP requests are extremely verbose and 
cumbersome. Python's built-in urllib2 module provides most of the HTTP 
capabilities you should need, but the API is thoroughly broken. This library is 
designed to make HTTP requests easy for developers.

%if_with python3
%package -n python3-module-%pkgname
Summary: HTTP library, written in Python, for human beings
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%description -n python3-module-%pkgname
Most existing Python modules for sending HTTP requests are extremely verbose and 
cumbersome. Python's built-in urllib2 module provides most of the HTTP 
capabilities you should need, but the API is thoroughly broken. This library is 
designed to make HTTP requests easy for developers.
%endif

%prep
%setup
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
%doc README.rst
%python_sitelibdir/%pkgname
%python_sitelibdir/*.egg-info

%files -n python3-module-%pkgname
%python3_sitelibdir/%pkgname
%python3_sitelibdir/*.egg-info

%changelog
* Fri May 18 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1-alt1
- initial
