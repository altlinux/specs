%define oname notify2

Name: python3-module-notify2
Version: 0.3.1
Release: alt1

Summary: Python interface to DBus notifications

License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/notify2

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-dbus

%py3_provides %oname

%description
This is a pure-python replacement for notify-python, using python-dbus to
communicate with the notifications server directly. It's compatible with Python
2 and 3, and its callbacks can work with Gtk 3 or Qt 4 applications.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt1
- Build new version.

* Thu May 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.3-alt3
- Drop python2 support.

* Sun Jan 22 2017 Anton Midyukov <antohami@altlinux.org> 0.3-alt2
- srpm build

* Mon Sep 19 2016 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- Initial build for Alt Linux Sisiphus.
