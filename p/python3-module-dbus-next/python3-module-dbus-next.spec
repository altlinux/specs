%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-dbus-next
Version: 0.2.3
Release: alt1

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
/bin/dbus-run-session -- %__python3 -m pytest test

%files
%doc LICENSE README.md
%python3_sitelibdir_noarch/dbus_next
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 0.2.3-alt1
- First build for ALT
