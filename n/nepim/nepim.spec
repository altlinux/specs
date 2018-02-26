Name: nepim
Version: 0.53
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Network pipemeter is a network benchmark utility
License: GPLv2+
Group: Networking/Other

Url: http://www.nongnu.org/nepim/
Source: http://download.savannah.gnu.org/releases/nepim/nepim-%{version}.tar.gz
Patch: nepim-0.51-asneeded.patch

# Automatically added by buildreq on Mon Sep 01 2008
BuildRequires: liboop-devel

%description
nepim stands for network pipemeter, a tool for measuring available bandwidth
between hosts. nepim is also useful to generate network traffic for testing
purposes.

nepim operates in client/server mode, is able to handle multiple parallel
traffic streams, reports periodic partial statistics along the testing, and
supports IPv6.

%prep
%setup
%patch -p1

%build
%make_build CC="gcc %optflags" -C src

%install
install -pD -m755 src/nepim %buildroot%_bindir/nepim

%files
%doc README
%_bindir/*

%changelog
* Wed Dec 24 2008 Victor Forsyuk <force@altlinux.org> 0.53-alt1
- 0.53

* Fri Sep 19 2008 Victor Forsyuk <force@altlinux.org> 0.52-alt1
- 0.52

* Mon Sep 01 2008 Victor Forsyuk <force@altlinux.org> 0.51-alt1
- Initial build.
