%define oname colour

%def_with python3

Name: python-module-%oname
Version: 0.0.6
Release: alt1.git20141118
Summary: converts and manipulates various color representation (HSL, RVB, web, X11, ...)
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/colour/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vaab/colour.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests git
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Converts and manipulates common color representation (RGB, HSV, web, ...)

Feature:

* Damn simple and pythonic way to manipulate color representation (see
  examples below)
* Full conversion between RGB, HSV, 6-digit hex, 3-digit hex, human
  color
* One object (Color) or bunch of single purpose function (rgb2hex,
  hsl2rgb ...)
* web format that use the smallest representation between 6-digit,
  3-digit, fully spelled color, that is following W3C color naming for
  CSS or HTML color specifications.
* smooth intuitive color scale generation choosing N color gradients.
* can pick colors for you to identify objects of your application.

%package -n python3-module-%oname
Summary: converts and manipulates various color representation (HSL, RVB, web, X11, ...)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Converts and manipulates common color representation (RGB, HSV, web, ...)

Feature:

* Damn simple and pythonic way to manipulate color representation (see
  examples below)
* Full conversion between RGB, HSV, 6-digit hex, 3-digit hex, human
  color
* One object (Color) or bunch of single purpose function (rgb2hex,
  hsl2rgb ...)
* web format that use the smallest representation between 6-digit,
  3-digit, fully spelled color, that is following W3C color naming for
  CSS or HTML color specifications.
* smooth intuitive color scale generation choosing N color gradients.
* can pick colors for you to identify objects of your application.

%prep
%setup
git init-db
git add . -A
git config user.email "real at altlinux.org"
git config user.name "REAL"
git commit -a -m "commit"
git tag %version

%if_with python3
cp -fR . ../python3
%endif

%build
./autogen.sh
%python_build_debug

%if_with python3
pushd ../python3
./autogen.sh
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
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
* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141118
- Version 0.0.6

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20140614
- Initial build for Sisyphus

