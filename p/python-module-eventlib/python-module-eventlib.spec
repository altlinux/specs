%define  modulename eventlib

Name:    python-module-%modulename
Version: 0.2.3
Release: alt2

Summary: Networking library for SIP SIMPLE Client SDK
License: MIT
Group:   Development/Python
URL:     https://github.com/AGProjects/python-eventlib

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  %modulename-%version.tar
Patch1:  alt-remove-obsoleted-hubs.patch

%add_python_req_skip stackless
%py_requires greenlet

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

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Sat Mar 10 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt2
- Add requirements of greenlet python module.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus
