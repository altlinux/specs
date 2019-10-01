%define oname raven

Name: python-module-raven
Version: 6.10.0
Release: alt1
Summary: Python client for Sentry

License: BSD
Group: Development/Python
Url: https://github.com/getsentry/raven-python
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
Raven is a Python client for Sentry <http://getsentry.com>. It provides full
out-of-the-box support for many of the popular frameworks, including Django, and
Flask. Raven also includes drop-in support for any WSGI-compatible web
application.

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

%package -n %oname
Summary: Python client for Sentry
Group: Development/Python
Requires: python3-module-%oname = %version-%release

%description -n %oname
Raven is a Python 3 client for Sentry <http://getsentry.com>. It provides full
out-of-the-box support for many of the popular frameworks, including Django, and
Flask. Raven also includes drop-in support for any WSGI-compatible web
application.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files -n python3-module-%oname
%doc LICENSE
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info

%files -n %oname
%_bindir/%oname

%changelog
* Tue Oct 01 2019 Anton Farygin <rider@altlinux.ru> 6.10.0-alt1
- 6.10.0
- built without python-2.7 support

* Sun Apr 21 2019 Anton Midyukov <antohami@altlinux.org> 6.9.0-alt1
- New version 6.9.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.32.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

 * Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 5.32.0-alt1
 - New version 5.32.0

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 5.24.1-alt1
- Initial build for ALT Linux Sisyphus.
