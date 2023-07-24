%define _unpackaged_files_terminate_build 1

Name: usrmerge
Version: 0.1
Release: alt1

Summary: transition to merged usr

URL: https://altlinux.org/Usrmerge
License: MIT
Group: Other

Source: usrmerge-%version.tar

%description
A toolset to merge /bin, /sbin, /lib, /lib%_lib with their counterparts
under /usr, as safely as possible.

%prep
%setup

%build
CFLAGS="${CFLAGS:-%optflags}"; export CFLAGS;
./configure
%make_build -C out

%install
%make_install install -C out DESTDIR=%buildroot

%files
%dir %_prefix/libexec/usrmerge
%_prefix/libexec/usrmerge/mv-xchg

%package hier-convert
Summary: Hierarchy conversion script
Group: System/Base
BuildArch: noarch
AutoReq: no
Requires: bash
Requires: coreutils
Requires: findutils
Requires: usrmerge

%description hier-convert
A script which merges /bin, /sbin, /lib, /lib%_lib with their counterparts
under /usr, as safely as possible.

This package contains the script which converts the hierarchy layout.
It is intended to be called from a filetrigger or in rpm posttrans stage, but
can be invoked directly by an administrator who knows what they are doing.

%files hier-convert
%_prefix/libexec/usrmerge/hier-convert

%changelog
* Mon Jul 24 2023 Arseny Maslennikov <arseny@altlinux.org> 0.1-alt1
- Initial build.
