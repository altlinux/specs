%define module_name redis
%define oname redis-py
%def_with python3

Name: python-module-%oname
Version: 2.10.3
Release: alt2.1.1
Group: Development/Python
License: MIT License
Summary: The Python interface to the Redis key-value store
URL: http://github.com/andymccurdy/redis-py
Packager: Vladimir Didenko <cow@altlinux.org>
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: rpm-build-python
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
%endif

%setup_python_module %oname

%description
The Python interface to the Redis key-value store

%if_with python3
%package -n python3-module-%oname
Summary: The Python interface to the Redis key-value store
Group: Development/Python3

%description -n python3-module-%oname
The Python interface to the Redis key-value store
%endif

%prep
%setup -n %name-%version

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
%doc CHANGES LICENSE README.rst
%python_sitelibdir/%module_name/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%module_name/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.10.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.10.3-alt2.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10.3-alt2
- Don't exclude .egg-info

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10.3-alt1
- Version 2.10.3

* Mon Jun 23 2014 Vladimir Didenko <cow@altlinux.org> 2.10.1-alt1
- new version
- python 3 support

* Tue Aug 14 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.6.0-alt1
- new version

* Sat May 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.13-alt1
- build for ALT
