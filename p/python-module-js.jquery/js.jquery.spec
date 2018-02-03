# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1.1.1
%define oname js.jquery

%def_with python3

Name: python-module-%oname
Version: 1.9.1
#Release: alt1.1.1
Summary: fanstatic jQuery
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.jquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-fanstatic python-module-shutilwhich
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-fanstatic python3-module-shutilwhich
%endif

%py_provides %oname
%py_requires js fanstatic shutilwhich

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-module-shutilwhich python-module-webob python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-pytest python3-module-setuptools python3-module-webob
BuildRequires: python-module-fanstatic python-module-setuptools python3-module-fanstatic python3-module-setuptools rpm-build-python3

%description
This library packages jQuery for fanstatic. It is aware of jQuery's
structure and different modes (normal, minified).

%package -n python3-module-%oname
Summary: fanstatic jQuery
Group: Development/Python3
%py3_provides %oname
%py3_requires js fanstatic shutilwhich

%description -n python3-module-%oname
This library packages jQuery for fanstatic. It is aware of jQuery's
structure and different modes (normal, minified).

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
python -c "from js.jquery import jquery; jquery.need()"
%if_with python3
pushd ../python3
python3 setup.py test
python3 -c "from js.jquery import jquery; jquery.need()"
popd
%endif

%files
%doc *.txt
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9.1-alt1.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt1
- Initial build for Sisyphus

