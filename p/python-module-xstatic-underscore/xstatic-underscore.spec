# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1.1.1
%define mname xstatic
%define oname %mname-underscore

%def_with python3

Name: python-module-%oname
Version: 1.7.0.1
#Release: alt1.1.1
Summary: underscore 1.7.0 (XStatic packaging standard)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/XStatic-underscore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-%mname
%endif

%py_provides %mname.pkg.underscore
%py_requires %mname.pkg

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools python-module-xstatic python3-module-setuptools python3-module-xstatic rpm-build-python3

%description
underscore javascript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by any project that needs these
files.

%package -n python3-module-%oname
Summary: underscore 1.7.0 (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.underscore
%py3_requires %mname.pkg

%description -n python3-module-%oname
underscore javascript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by any project that needs these
files.

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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.0.1-alt1.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.0.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.0.1-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0.1-alt1
- Initial build for Sisyphus

