%define oname thumbor-pexif

%def_without python3

Name: python-module-%oname
Version: 0.14.1
Release: alt1.git20141001
Summary: A module for editing JPEG EXIF data
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/thumbor-pexif/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/thumbor/pexif.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides pexif

%description
This module allows you to parse and edit the EXIF data tags in a JPEG
image.

%package -n python3-module-%oname
Summary: A module for editing JPEG EXIF data
Group: Development/Python3
%py3_provides pexif

%description -n python3-module-%oname
This module allows you to parse and edit the EXIF data tags in a JPEG
image.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

%check
nosetests
%if_with python3
pushd ../python3
nosetests3
popd
%endif

%files
%doc README examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt1.git20141001
- Initial build for Sisyphus

