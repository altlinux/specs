%define oname piexif

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.c.git20150128.1
Summary: Exif manipulation with pure python script
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/piexif/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hMatoba/Piexif.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Pillow
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Pillow
%endif

%py_provides %oname

%description
This is a renamed project from Pyxif.
To simplify exif manipulations with python. Writing, reading, and more...
Piexif isn't a wrapper. To everywhere with Python.

%package -n python3-module-%oname
Summary: Exif manipulation with pure python script
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is a renamed project from Pyxif.
To simplify exif manipulations with python. Writing, reading, and more...
Piexif isn't a wrapper. To everywhere with Python.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
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
%doc *.rst *sample*.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *sample*.py
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.c.git20150128.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.c.git20150128
- Initial build for Sisyphus

