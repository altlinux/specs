%def_with python3
%define oname raven

Name: python-module-raven
Version: 5.24.1
Release: alt1
Summary: Python client for Sentry

License: BSD
Group: Development/Python
Url: https://github.com/getsentry/raven-python
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif
BuildPreReq: python-devel python-module-setuptools-tests
%py_provides %oname
%add_findreq_skiplist %python_sitelibdir/%oname/contrib/zope/*

%description
Raven is a Python client for Sentry <http://getsentry.com>. It provides full
out-of-the-box support for many of the popular frameworks, including Django, and
Flask. Raven also includes drop-in support for any WSGI-compatible web
application.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 client for Sentry
Group: Development/Python
%py3_provides %oname
%add_findreq_skiplist %python3_sitelibdir/%oname/contrib/zope/*

%description -n python3-module-%oname
Raven is a Python client for Sentry <http://getsentry.com>. It provides full
out-of-the-box support for many of the popular frameworks, including Django, and
Flask. Raven also includes drop-in support for any WSGI-compatible web
application.
Python 3 version.
%endif

%package -n %oname
Summary: Python client for Sentry
Group: Development/Python
%if_with python3
Requires: python3-module-%oname = %version-%release
%else
Requires: python-module-%oname = %version-%release
%endif

%description -n %oname
Raven is a Python 3 client for Sentry <http://getsentry.com>. It provides full
out-of-the-box support for many of the popular frameworks, including Django, and
Flask. Raven also includes drop-in support for any WSGI-compatible web
application.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc LICENSE
%doc README.*
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc LICENSE
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%endif

%files -n %oname
%_bindir/%oname

%changelog
* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 5.24.1-alt1
- Initial build for ALT Linux Sisyphus.
