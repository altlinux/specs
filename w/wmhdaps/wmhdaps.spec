# vim: set ft=spec: -*- rpm-spec -*-

Name: wmhdaps
Version: 0.04
Release: alt3

Summary: Harddisk Active Protection System visualization DockApp
License: GPL
Group: Graphical desktop/Window Maker

Url: http://dockapps.org/file.php/id/297
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Sir Raorn <raorn@altlinux.org>

# Automatically added by buildreq on Tue Jan 23 2007
BuildRequires: libXext-devel libXpm-devel

%description
The goal of wmhdaps is to provide a tool for configuration of the
Harddisk Active Protection System (HDAPS) found in some R/G/T/X
thinkpad models.  HDAPS is realized as an acceleration sensor mounted
on systemboard and a userspace tool which detects based on
acceleration values from sensor shocks and freezes the harddrive(s)
until the "shock" is over.

%prep
%setup
%patch -p1

%build
pushd wmhdaps
%add_optflags "-std=gnu89"
%make_build CFLAGS="%optflags"

%install
install -pDm755 wmhdaps/wmhdaps %buildroot%_bindir/%name

%files
%doc README Changelog
%_bindir/%name

%changelog
* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 0.04-alt3
- gcc5 FTBFS workaround (-std=gnu89)
- minor spec cleanup

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.04-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Jan 23 2007 Sir Raorn <raorn@altlinux.ru> 0.04-alt2
- Fix model rotaton

* Tue Jan 23 2007 Sir Raorn <raorn@altlinux.ru> 0.04-alt1
- Built for Sisyphus

