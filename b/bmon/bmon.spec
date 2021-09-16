Name: bmon
Version: 4.0
Release: alt2

Summary: A portable bandwidth monitor
License: %bsd %mit
Group: Monitoring

Url: https://github.com/tgraf/bmon
Source: https://github.com/tgraf/bmon/releases/download/v4.0/%name-%version.tar.gz

Patch1: bmon-2.1.0-gcc4.diff
Patch2: bmon-2.1.0-nostrip.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildRequires: libconfuse-devel libnl-devel libncurses-devel

%description
%name is a portable bandwidth monitor and rate estimator
running on various operating systems.

It supports various input methods for different architectures.
Various output modes exist including an interactive curses
interface, lightweight HTML output but also formatable ASCII
output.  Statistics may be distributed over a network using
multicast or unicast and collected at some point to generate
a summary of statistics for a set of nodes. 

%prep
%setup 
#patch1 -p1
#patch2 -p0

%build
%configure --disable-asound
%make_build

%install
%makeinstall

# packaged by %doc examples/
rm -rf $RPM_BUILD_ROOT/usr/share/doc/bmon/examples

%files
%_bindir/*
%_mandir/man?/*
%doc NEWS examples/ LICENSE.BSD LICENSE.MIT

%changelog
* Thu Sep 16 2021 Ilya Mashkin <oddity@altlinux.ru> 4.0-alt2
- Rebuild with libconfuse-3.3

* Wed Nov 01 2017 Sergey Y. Afonin <asy@altlinux.ru> 4.0-alt1
- New version
- changed URL
- fixed "License"
- removed old patches

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1.0-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Sat Apr 17 2010 Sergey Y. Afonin <asy@altlinux.ru> 2.1.0-alt1.1
- rebuilt with new librrd

* Sun Feb 11 2007 Michael Shigorin <mike@altlinux.org> 2.1.0-alt1
- adopted an orphan
- fixed build with gcc4.1 (applied Gentoo patches)
- updated buildrequires

* Sun Nov 13 2005 Sasha Martsinuk <scampler@altlinux.ru> 2.1.0-alt1
- Initial build for ALTLinux Sisyphus 


