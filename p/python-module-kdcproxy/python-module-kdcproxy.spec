%define _unpackaged_files_terminate_build 1

%define mname kdcproxy
%def_without python3

Name: python-module-%mname
Version: 0.3.2
Release: alt1
Summary: A kerberos KDC HTTP proxy WSGI module

Group: Development/Python
License: %mit
Url: https://github.com/latchset/kdcproxy

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildArch: noarch

BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-setuptools
#BuildRequires: libkrb5-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%setup_python_module %mname

%description
This package contains a Python 2.x WSGI module for proxying KDC requests
over HTTP by following the MS-KKDCP protocol. It aims to be simple
to deploy, with minimal configuration.

%if_with python3
%package -n python3-module-%mname
Summary: A kerberos KDC HTTP proxy WSGI module
Group: Development/Python3

%description -n python3-module-%mname
This package contains a Python 3.x WSGI module for proxying KDC requests
over HTTP by following the MS-KKDCP protocol. It aims to be simple
to deploy, with minimal configuration.
%endif

%prep
%setup
#patch -p1
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
%doc COPYING README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%mname
%doc COPYING README
%python3_sitelibdir/*

%endif

%changelog
* Wed Sep 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Initial build.

