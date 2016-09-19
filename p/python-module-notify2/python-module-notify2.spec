%def_with python3
%define oname notify2

Name: python-module-notify2
Version: 0.3
Release: alt1
Summary: Python interface to DBus notifications

License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/notify2
Packager: Python Development Team <python at packages.altlinux.org>

Source: %oname-%version.tar
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-dbus
%endif
BuildPreReq: python-devel python-module-setuptools python-module-dbus
%py_provides %oname

%description
This is a pure-python replacement for notify-python, using python-dbus to
communicate with the notifications server directly. It's compatible with Python
2 and 3, and its callbacks can work with Gtk 3 or Qt 4 applications.

%package -n python3-module-%oname
Summary: Python interface to DBus notifications
Group: Development/Python
%py3_provides %oname
BuildArch: noarch

%description -n python3-module-%oname
This is a pure-python replacement for notify-python, using python-dbus to
communicate with the notifications server directly. It's compatible with Python
2 and 3, and its callbacks can work with Gtk 3 or Qt 4 applications.
Python 3 version.

%prep
%setup -n %oname-%version

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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 19 2016 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- Initial build for Alt Linux Sisiphus.
