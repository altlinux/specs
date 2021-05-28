%define  modulename eventlib

Name:    python3-module-%modulename
Version: 0.3.0
Release: alt1

Summary: Networking library for SIP SIMPLE Client SDK
License: MIT
Group:   Development/Python3
URL:     https://github.com/AGProjects/python3-eventlib

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-distribute

BuildArch: noarch

Source: %modulename-%version.tar
Patch1: alt-remove-obsoleted-hubs.patch
Patch2: eventlib-replace-popen2-by-subprocess.patch

%add_python3_req_skip stackless py.magic
%py3_requires greenlet

%description
Eventlib is a networking library written in Python. It achieves high
scalability by using non-blocking I/O while at the same time retaining
high programmer usability by using coroutines to make the non-blocking
io operations appear blocking at the source code level.

%prep
%setup -n %modulename-%version
# Remove stackless, ev and libevent support to prevent unmet
rm -f eventlib/support/stackles{ss,pypys}.py
rm -f eventlib/hubs/{libev,libevent}.py
%patch1 -p1
%patch2 -p1

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Wed May 26 2021 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- New version.

* Wed May 26 2021 Andrey Cherepanov <cas@altlinux.org> 0.2.5-alt1
- New version.
- Build as Python3 module.

* Sat Mar 10 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt2
- Add requirements of greenlet python module.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus
