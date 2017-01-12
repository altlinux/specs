%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname haversine

%def_with python3

Name: python-module-%oname
Version: 0.4.5
#Release: alt1.git20150615.1.1
Summary: Calculate the distance bewteen 2 points on Earth
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/haversine/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mapado/haversine.git
Source0: https://pypi.python.org/packages/57/b4/3b1f5ca78876ad00cbb2a2bf7bcebfe4751c00ddabc47005b59f33835646/%{oname}-%{version}.tar.gz

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python3-devel rpm-build-python3

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
%setup -q -n %{oname}-%{version}

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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150615.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150615.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20150615.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150615
- Version 0.4.2

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20130720
- Initial build for Sisyphus

