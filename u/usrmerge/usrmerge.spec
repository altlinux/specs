%define _unpackaged_files_terminate_build 1

Name: usrmerge
Version: 0.2
Release: alt1

Summary: transition to merged usr

URL: https://altlinux.org/Usrmerge
License: MIT
Group: Other

Source: usrmerge-%version.tar

BuildRequires: make
BuildRequires: gcc

# Pull in all subpackages.
Requires: %name-hier-convert = %EVR

%description
A toolset to merge /bin, /sbin, /lib, /%_lib with their counterparts
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

# Unfortunately, we cannot make the base package noarch and put arch-specific
# tools in a subpackage; we have to do quite the opposite.
%package hier-convert
Summary: Hierarchy conversion script
Group: System/Base
BuildArch: noarch
AutoReq: no
Requires: bash
Requires: coreutils
Requires: findutils
Requires: usrmerge = %EVR

%description hier-convert
A script which merges /bin, /sbin, /lib, /lib%_lib with their counterparts
under /usr, as safely as possible.

This package contains the script which converts the hierarchy layout.
It is intended to be called from a filetrigger or in rpm pretrans stage, but
can be invoked directly by an administrator who knows what they are doing.

%files hier-convert
%_prefix/libexec/usrmerge/hier-convert

%changelog
* Fri Jul 28 2023 Arseny Maslennikov <arseny@altlinux.org> 0.2-alt1
- 0.1 -> 0.2; see commit history for details.
  Notably:
  + Added support for /lib32.
  + Made sure emergency cleanup is non-destructive.
  + Added various conflict resolution heuristics to hier-convert.

* Mon Jul 24 2023 Arseny Maslennikov <arseny@altlinux.org> 0.1-alt1
- Initial build.
