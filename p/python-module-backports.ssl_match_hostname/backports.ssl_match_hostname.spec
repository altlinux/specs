%define ocore backports
%define oname %ocore.ssl_match_hostname
Name: python-module-%oname
Version: 3.4.0.2
Release: alt1
Summary: The ssl.match_hostname() function from Python 3.4
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/backports.ssl_match_hostname/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools

%py_requires %ocore

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

%package -n python-module-%ocore
Summary: Core package of %ocore
Group: Development/Python

%description -n python-module-%ocore
Core package of %ocore.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc PKG-INFO
%python_sitelibdir/%ocore/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%ocore/__init__.py*

%files -n python-module-%ocore
%dir %python_sitelibdir/%ocore
%python_sitelibdir/%ocore/__init__.py*

%changelog
* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.2-alt1
- Initial build for Sisyphus

