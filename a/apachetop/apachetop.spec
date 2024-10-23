Name: apachetop
Version: 0.23.2
Release: alt1

Epoch: 20060605

Summary: ApacheTop is top-like utility for Apache 
License: BSD-3-Clause
Group: Monitoring

Url: https://github.com/tessus/apachetop
Source: %name-%version.tar.gz
Summary(ru_RU.KOI8-R): ApacheTop -- top'��������� ������� ��� Apache
Summary(uk_UA.KOI8-U): ApacheTop -- top'�������� ���̦�� ��� Apache

# Automatically added by buildreq on Mon Jun 05 2006
BuildRequires: gcc-c++ libadns-devel libreadline-devel
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(libpcre2-posix)

%description
A curses-based top-like display for Apache information, including requests per
second, bytes per second, most popular URLs, etc.

%description -l ru_RU.KOI8-R
���������� ������� ��� ����������� web-������� Apache, ������������ ����������
��������/���� � �������, �������� ���������� ������ � �.�.

%description -l uk_UA.KOI8-U
��������� ���̦�� ��� ��Φ������� web-������� Apache, �� �����դ ˦��˦���
����Ԧ�/���� � �������, ���¦��� �������Φ ������ �� ��.

%prep
%setup -q

%build
%autoreconf
%configure --with-logfile=%_logdir/httpd2/access_log --without-fam
%make_build

%install
%makeinstall

%files
%_bindir/%name
%doc AUTHORS ChangeLog LICENSE NEWS README
%doc %_man1dir/%name.1.*

# TODO:
# - some wrapper to point at /var/log/httpd/access_log ?
#   (until proper multi-host infrastructure is in place)

%changelog
* Tue Oct 22 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 20060605:0.23.2-alt1
- new version

* Tue Feb 05 2019 Michael Shigorin <mike@altlinux.org> 20060605:0.12.6-alt2
- rebuilt against readline7

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 20060605:0.12.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Jun 05 2006 Michael Shigorin <mike@altlinux.org> 20060605:0.12.6-alt1
- 0.12.6
- applied gcc41 patch from Gentoo
- removed separate CAN-2005-2660 patch (fixed upstream)
- noticed --with-fam; after some consideration left disabled by default

* Wed Oct 05 2005 Michael Shigorin <mike@altlinux.org> 20051005:0.12.5-alt2
- applied Debian patch to fix CAN-2005-2660:
  Eric Romang discovered an insecurely created temporary file in
  apachetop, a realtime monitoring tool for the Apache webserver that
  could be exploited with a symlink attack to overwrite arbitrary files
  with the user id that runs apachetop.

* Wed Jan 19 2005 Alex Murygin <murygin@altlinux.ru> 20050119:0.12.5-alt1
- new version
- moved apachetop from sbin to bin (due to upstream)

* Thu Nov 11 2004 Alex Murygin <murygin@altlinux.ru> 20041111:0.12-alt1
- new version
- fixed for pcre
- configured with adns and pcre support
- configured without fam support
- removed README.ALT, because it looks for correct log
- added NEWS to docs

* Tue Oct 14 2003 Michael Shigorin <mike@altlinux.ru> 20031014:0.7-alt1
- 0.7 (code cleanup)

* Mon Oct 06 2003 Michael Shigorin <mike@altlinux.ru> 20031006:0.6-alt1
- should fix "cpu-hungry bug" as reported against 0.4
- spec cleanup due to upstream switch to autotools
- binary location changed from %_bindir to %_sbindir (upstream install)
- added README.ALT with sample command
- updated %%files

* Mon Sep 29 2003 Michael Shigorin <mike@altlinux.ru> 20030929:0.4-alt1
- built for ALT Linux

