%define oname snowballstemmer

%def_with python3

Name: python-module-%oname
Version: 1.2.0
Release: alt2.1
Summary: 16 stemmer algorithms (15 + Poerter English stemmer) generated from Snowball algorithms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/snowballstemmer
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

Requires: python-module-PyStemmer

#BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python-tools-2to3
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

%description
This package provides 16 stemmer algorithms (15 + Poerter English
stemmer) generated from Snowball algorithms.

It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkish

%package -n python3-module-%oname
Summary: 16 stemmer algorithms (15 + Poerter English stemmer) generated from Snowball algorithms
Group: Development/Python

%description -n python3-module-%oname
This package provides 16 stemmer algorithms (15 + Poerter English
stemmer) generated from Snowball algorithms.

It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkish

%prep
%setup

%if_with python3
rm -rf ../python3
cp -R ../%name-%version ../python3
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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Mar  2 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt2

- (.spec) Safer build: cleanup ../python3/ before use.
  (Nevertheless, beware: using ../python3/ for the build is very dirty
  because it is not cleaned up automatically afterwards and can cause
  side-effects in other unsafe specs, similar to this one. This dirty
  use of ../python3/ is very wide-spread in Sisyphus packages.)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Mon Jun 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

