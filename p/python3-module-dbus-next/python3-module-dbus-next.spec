%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-dbus-next
Version: 0.2.3
Release: alt2

Summary: The next great DBus library for Python with asyncio support
License: MIT
Group: Development/Python3
BuildArch: noarch

# VCS: https://github.com/altdesktop/python-dbus-next
Url: https://python-dbus-next.readthedocs.io
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-macros-python3
BuildRequires: rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-timeout
BuildRequires: dbus
%endif

%description
The next great DBus library for Python.

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install

%check
#See: https://lists.altlinux.org/pipermail/devel/2022-December/217237.html
sed -e 's|unix:tmpdir=/run/dbus/users|unix:abstract=/usr/src/tmp|' \
    /usr/share/dbus-1/session.conf > /usr/src/rpmb-dbus-1-session.conf

/bin/dbus-run-session --config-file=/usr/src/rpmb-dbus-1-session.conf \
                      -- %__python3 -m pytest test

%files
%doc LICENSE README.md
%python3_sitelibdir_noarch/dbus_next
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Sun Mar 26 2023 Egor Ignatov <egori@altlinux.org> 0.2.3-alt2
- Fix FTBFS: change dbus session daemon socket path for tests

* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 0.2.3-alt1
- First build for ALT
