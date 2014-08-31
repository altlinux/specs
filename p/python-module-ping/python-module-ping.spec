%define module_name ping

%def_with python3

Name: python-module-ping
Version: 0.2
Release: alt2
Group: Development/Python
License: GPLv2
Summary: implementation of the standard ICMP ping in pure Python
URL: http://pypi.python.org/pypi/ping
Source: http://bitbucket.org/delroth/python-ping/downloads/python-%module_name-%version.tar.gz

BuildArch: noarch

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
This library is a fork of George Notaras' python-ping library, which is
an implementation of the standard ICMP ping in pure Python

%package -n python3-module-%module_name
Summary: implementation of the standard ICMP ping in pure Python
Group: Development/Python3

%description -n python3-module-%module_name
This library is a fork of George Notaras' python-ping library, which is
an implementation of the standard ICMP ping in pure Python

%prep
%setup -n python-%module_name-%version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc AUTHORS README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS README
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added module for Python 3

* Thu Jan 03 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1
- build for ALT
