%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname twunnel3

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1
Summary: A HTTPS/SOCKS4/SOCKS5 tunnel for AsyncIO
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/twunnel3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jvansteirteghem/twunnel3.git
Source0: https://pypi.python.org/packages/dc/6d/bca8052d672700ef9c0c1d9ca6a7994b222435ec5cd00e8b9b3786be99b7/%{oname}-%{version}.zip
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python3-module-setuptools-tests rpm-build-python3

%description
A HTTPS/SOCKS4/SOCKS5 tunnel for AsyncIO.

Supports:

* TCP
* TCP over SSL

%package -n python3-module-%oname
Summary: A HTTPS/SOCKS4/SOCKS5 tunnel for AsyncIO
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
A HTTPS/SOCKS4/SOCKS5 tunnel for AsyncIO.

Supports:

* TCP
* TCP over SSL

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst PKG-INFO
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20140701.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.git20140701.1
- NMU: Use buildreq for BR.

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20140701
- Initial build for Sisyphus

