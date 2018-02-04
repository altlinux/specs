%define oname pexif

%def_without python3

Name: python-module-%oname
Version: 0.15
Release: alt1.git20150205.1
Summary: A module for editing JPEG EXIF data
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pexif/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bennoleslie/pexif.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Conflicts: python-module-thumbor-%oname

%description
This module allows you to parse and edit the EXIF data tags in a JPEG
image.

%if_with python3
%package -n python3-module-%oname
Summary: A module for editing JPEG EXIF data
Group: Development/Python3
%py3_provides %oname
Conflicts: python3-module-thumbor-%oname

%description -n python3-module-%oname
This module allows you to parse and edit the EXIF data tags in a JPEG
image.
%endif

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
export PYTHONPATH=$PWD
python test/test.py -v
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 test/test.py -v
popd
%endif

%files
%doc *.md examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.15-alt1.git20150205.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt1.git20150205
- Initial build for Sisyphus

