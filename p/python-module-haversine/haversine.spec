%define oname haversine

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20130720
Summary: Calculate the distance bewteen 2 points on Earth
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/haversine/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mapado/haversine.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Calculate the distance (in km or in miles) bewteen two points on Earth,
located by their latitude and longitude.

%package -n python3-module-%oname
Summary: Calculate the distance bewteen 2 points on Earth
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Calculate the distance (in km or in miles) bewteen two points on Earth,
located by their latitude and longitude.

%prep
%setup

%if_with python3
cp -fR . ../python3
SUFF=$(echo %_python3_version%_python3_abiflags |sed 's|\.||')
sed -i "s|libhsine.so|libhsine.cpython-$SUFF.so|" \
	../python3/%oname/__init__.py
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
python setup.py build_ext -i
python -c "from %oname import %oname"
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
python3 -c "from %oname import %oname"
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20130720
- Initial build for Sisyphus

