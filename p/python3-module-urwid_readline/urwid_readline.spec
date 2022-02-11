Name: python3-module-urwid_readline
Version: 0.13
Release: alt1
Source: urwid_readline-%version.tar.gz
License: MIT
Group: Development/Python3
Summary: Text input widget for urwid that supports readline shortcuts
Url: https://github.com/rr-/urwid_readline
BuildArch: noarch

%description
%summary

%prep
%setup -n urwid_readline-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/*

%changelog
* Fri Feb 11 2022 Fr. Br. George <george@altlinux.org> 0.13-alt1
- Autobuild version bump to 0.13

* Fri Feb 11 2022 Fr. Br. George <george@altlinux.org> 0.12-alt1
- Initial relase for ALT
