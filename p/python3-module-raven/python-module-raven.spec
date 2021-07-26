%define oname raven

Name: python3-module-raven
Version: 6.10.0
Release: alt2
Summary: Python client for Sentry

License: BSD
Group: Development/Python3
Url: https://github.com/getsentry/raven-python
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%py3_provides %oname
%add_findreq_skiplist %python3_sitelibdir/%oname/contrib/zope/*

%description
Raven is a Python client for Sentry <http://getsentry.com>. It provides full
out-of-the-box support for many of the popular frameworks, including Django, and
Flask. Raven also includes drop-in support for any WSGI-compatible web
application.

%package -n %oname
Summary: Python client for Sentry
Group: Development/Python3
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

%files
%doc LICENSE
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info

%files -n %oname
%_bindir/%oname

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 6.10.0-alt2
- Rename package, spec cleanup.

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
