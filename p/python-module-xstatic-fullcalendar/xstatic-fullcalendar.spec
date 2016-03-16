%define mname xstatic
%define oname %mname-fullcalendar

%def_with python3

Name: python-module-%oname
Version: 2.2.2.1
Release: alt1.1.1
Summary: fullcalendar 2.2.2 (XStatic packaging standard)
License: MIT & GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/XStatic-fullcalendar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-%mname-jquery-ui python-module-%mname-moment
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-%mname-jquery-ui python3-module-%mname-moment
%endif

%py_provides %mname.pkg.fullcalendar
%py_requires %mname.pkg.jquery_ui %mname.pkg.moment

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-module-xstatic python-module-xstatic-jquery python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools python3-module-xstatic python3-module-xstatic-jquery
BuildRequires: python-module-setuptools-tests python-module-xstatic-jquery-ui python-module-xstatic-moment python3-module-setuptools-tests python3-module-xstatic-jquery-ui python3-module-xstatic-moment rpm-build-python3

%description
fullcalendar javascript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by any project that needs these
files.

%package -n python3-module-%oname
Summary: fullcalendar 2.2.2 (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.fullcalendar
%py3_requires %mname.pkg.jquery_ui

%description -n python3-module-%oname
fullcalendar javascript library packaged for setuptools (easy_install) /
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

%ifarch x86_64
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.2.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.2.2.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2.1-alt1
- Version 2.2.2.1

* Mon Nov 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3.1-alt1
- Initial build for Sisyphus

