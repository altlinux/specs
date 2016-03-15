%define module_name ping

%def_with python3

Name: python-module-ping
Version: 0.2
Release: alt2.1.1
Group: Development/Python
License: GPLv2
Summary: implementation of the standard ICMP ping in pure Python
URL: http://pypi.python.org/pypi/ping
Source: http://bitbucket.org/delroth/python-ping/downloads/python-%module_name-%version.tar.gz

BuildArch: noarch

#BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt2.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added module for Python 3

* Thu Jan 03 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1
- build for ALT
