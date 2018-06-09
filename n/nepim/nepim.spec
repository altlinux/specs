Name: nepim
Version: 0.54
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Network pipemeter is a network benchmark utility

License: GPLv2+
Group: Networking/Other
Url: http://www.nongnu.org/nepim/

# Source-url: https://github.com/udhos/nepim/archive/v%version.tar.gz
Source: %name-%version.tar
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

%build
%make_build CC="gcc %optflags" -C src

%install
install -pD -m755 src/nepim %buildroot%_bindir/nepim

%files
%doc README.md
%_bindir/*

%changelog
* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.54-alt1
- new version (0.54) with rpmgs script

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.53-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 24 2008 Victor Forsyuk <force@altlinux.org> 0.53-alt1
- 0.53

* Fri Sep 19 2008 Victor Forsyuk <force@altlinux.org> 0.52-alt1
- 0.52

* Mon Sep 01 2008 Victor Forsyuk <force@altlinux.org> 0.51-alt1
- Initial build.
