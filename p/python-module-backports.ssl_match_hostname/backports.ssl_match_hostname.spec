%define ocore backports
%define oname %ocore.ssl_match_hostname

%def_with python3

Name: python-module-%oname
Version: 3.4.0.2
Release: alt2.1
Summary: The ssl.match_hostname() function from Python 3.4
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/backports.ssl_match_hostname/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%py_requires %ocore

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-pytest rpm-build-python3

%description
The Secure Sockets layer is only actually secure if you check the
hostname in the certificate returned by the server to which you are
connecting, and verify that it matches to hostname that you are trying
to reach.

But the matching logic, defined in RFC2818, can be a bit tricky to
implement on your own. So the ssl package in the Standard Library of
Python 3.2 and greater now includes a match_hostname() function for
performing this check instead of requiring every application to
implement the check separately.

%package -n python3-module-%oname
Summary: The ssl.match_hostname() function from Python 3.4
Group: Development/Python3
%py3_provides %oname
%py3_requires %ocore

%description -n python3-module-%oname
The Secure Sockets layer is only actually secure if you check the
hostname in the certificate returned by the server to which you are
connecting, and verify that it matches to hostname that you are trying
to reach.

But the matching logic, defined in RFC2818, can be a bit tricky to
implement on your own. So the ssl package in the Standard Library of
Python 3.2 and greater now includes a match_hostname() function for
performing this check instead of requiring every application to
implement the check separately.

%package -n python-module-%ocore
Summary: Core package of %ocore
Group: Development/Python
%py_provides %ocore

%description -n python-module-%ocore
Core package of %ocore.

%package -n python3-module-%ocore
Summary: Core package of %ocore
Group: Development/Python3
%py3_provides %ocore

%description -n python3-module-%ocore
Core package of %ocore.

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

%files
%doc PKG-INFO
%python_sitelibdir/%ocore/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%ocore/__init__.py*

%files -n python-module-%ocore
%dir %python_sitelibdir/%ocore
%python_sitelibdir/%ocore/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/%ocore/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%ocore/__init__.py
#exclude %python3_sitelibdir/%ocore/__pycache__/__init__.*

%files -n python3-module-%ocore
%dir %python3_sitelibdir/%ocore
%dir %python3_sitelibdir/%ocore/__pycache__
%python3_sitelibdir/%ocore/__init__.py*
#python3_sitelibdir/%ocore/__pycache__/__init__.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.4.0.2-alt2.1
- NMU: Use buildreq for BR.

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.2-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.2-alt1
- Initial build for Sisyphus

