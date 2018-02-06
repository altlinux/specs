%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname twunnel3

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt2.1
Summary: A HTTPS/SOCKS4/SOCKS5 tunnel for AsyncIO
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/twunnel3/

# https://github.com/jvansteirteghem/twunnel3.git
Source: %{oname}-%{version}.zip
Patch1: %oname-%version-alt-python3-build.patch

%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(asyncio)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(asyncio)
%endif

%py_provides %oname
%py_requires asyncio

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
pushd ../python3
%patch1 -p2
popd
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt2
- Updated build dependencies.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20140701.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.git20140701.1
- NMU: Use buildreq for BR.

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20140701
- Initial build for Sisyphus

