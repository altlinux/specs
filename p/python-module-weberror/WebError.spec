%define oname weberror

%def_with python3

Name: python-module-%oname
Version: 0.10.3
Release: alt2.1.1
Summary: Web Error handling and exception catching
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/WebError
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

Source: WebError-%version.tar.gz

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

%description
Web Error handling and exception catching.

%package -n python3-module-%oname
Summary: Web Error handling and exception catching
Group: Development/Python3

%description -n python3-module-%oname
Web Error handling and exception catching.

%prep
%setup

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
%doc CHANGELOG LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.3-alt2.1
- NMU: Use buildreq for BR.

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.3-alt1.1
- Rebuild with Python-2.7

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1
- Version 0.10.3

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1
- Version 0.10.2

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt2
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus

