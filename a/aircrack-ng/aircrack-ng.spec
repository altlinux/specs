Name: aircrack-ng
Version: 1.1
Release: alt2

Summary: 802.11 WEP and WPA-PSK key recovery program
License: GPLv2+
Group: Networking/Other

Url: http://aircrack-ng.org

Packager: Timur Aitov <timonbl4@altlinux.org>

BuildRequires: libssl-devel libsqlite3-devel
Requires: iw

Source: %name-%version.tar

%description
Aircrack is an 802.11 WEP and WPA-PSK keys cracking program that can
recover keys once enough data packets have been captured.
It implements the standard FMS attack along with some optimizations
like KoreK attacks, thus making the attack much faster compared to
other WEP cracking tools. In fact aircrack is a set of tools for
auditing wireless networks.

%prep
%setup
sed -i 's,^\(CFLAGS\s\+?= \).*,\1%optflags,' common.mak

%build
%make_build sqlite=true prefix=%prefix mandir=%_man1dir

%install
%makeinstall_std sqlite=true prefix=%prefix mandir=%_man1dir
%make_build doc prefix=%prefix DESTDIR=%buildroot

%files
%_bindir/*
%_sbindir/*
%_man1dir/*
%doc %_docdir/*

%changelog
* Tue Dec 21 2010 Timur Aitov <timonbl4@altlinux.org> 1.1-alt2
- Add iw in dependence

* Tue Oct 12 2010 Timur Aitov <timonbl4@altlinux.org> 1.1-alt1
- new version

* Sun Oct 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt3
- fix installing of airolib-ng

* Tue Sep 08 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt2
- 1.0

* Sat Aug 15 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt1.rc4
- 1.0-rc4

* Thu May 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt1.rc3
- 1.0-rc3

* Sun Mar 01 2009 Maxim Ivaniv <redbaron at altlinux.org> 1.0-alt1.rc2
- Version bump to 1.0-rc2

* Mon Jul 30 2007 Alex V. Myltsev <avm@altlinux.ru> 0.9.1-alt1
- new version: critical security fix (remote execution), please upgrade
- more attacks, better SMP handling, bug fixes

* Thu Apr 12 2007 Alex V. Myltsev <avm@altlinux.ru> 0.7-alt1
- 0.7: many new features/attacks, bug fixes.

* Wed Nov 22 2006 Alex V. Myltsev <avm@altlinux.ru> 0.6.2-alt1
- 0.6.2: bug fixes. arpforge-ng is replaced by packetforge-ng.

* Fri Sep 22 2006 Alex V. Myltsev <avm@altlinux.ru> 0.6.1-alt1
- Initial build for Sisyphus.

