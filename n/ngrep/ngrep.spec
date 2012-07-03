Name: ngrep
Version: 1.46
Release: alt0.1

Summary: ngrep - network grep
License: BSD-style
Group: Monitoring
Url: http://ngrep.sourceforge.net
# http://git.altlinux.org/gears/n/ngrep.git
Source: %name-%version-%release.tar

Requires: /var/resolv

BuildRequires: libpcap-devel libpcre-devel

Summary(ru_RU.UTF-8): ngrep - поиск строковых масок в сетевом трафике

%description
ngrep strives to provide most of GNU grep's common features, applying them
to the network layer.  ngrep is a pcap-aware tool that will allow you to
specify extended regular expressions to match against data payloads of
packets.  It currently recognizes TCP and UDP across ethernet, ppp and
slip interfaces, and understands bpf filter logic in the same fashion
as more common packet sniffing tools, like tcpdump and snoop.

%description -l ru_RU.UTF-8
ngrep реализует большинство возможностей, предоставляемых утилитой GNU grep
для поиска по образцам, но обрабатывает не файлы, а пакеты сетевого трафика.
Для задания правил поиска можно использовать расширенные регулярные выражения.
Для просмотра сетевого трафика ngrep (так же, как и другие популярные средства
перехвата пакетов наподобие tcpdump и snoop) использует библиотеку pcap.
В настоящий момент поддерживается просмотр пакетов TCP и UDP в Ethernet-,
PPP- и SLIP-соединениях.

%prep
%setup -n %name-%version-%release

%build
%autoreconf
%configure \
	--with-dropprivs-user=%name \
	--with-pcap-includes=%_includedir/pcap \
	--with-regex-impl=sys \
	--enable-ipv6 \
	--enable-pcre \
	--disable-pcap-restart
%make_build STRIPFLAG=

%install
install -pD -m755 %name %buildroot%_sbindir/%name
install -pD -m644 %name.8 %buildroot%_man8dir/%name.8

%pre
%_sbindir/groupadd -r -f %name
%_sbindir/useradd -r -g %name -d /dev/null -s /dev/null -n %name >/dev/null 2>&1 ||:

%files
%_sbindir/%name
%_mandir/man?/*
%doc doc/*.txt usage.html

%changelog
* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 1.46-alt0.1
- Updated to 1.45-35-g16ba99a.
- Switched to PCRE.

* Tue Dec 02 2008 Dmitry V. Levin <ldv@altlinux.org> 1.45-alt3
- Fixed regex support.
- Added basic i18n.

* Thu Jan  4 2007 Ilya Evseev <evseev@altlinux.ru> 1.45-alt2
- fixup PCRE usage, merge with 1.44-alt2 by ldv

* Thu Jan  4 2007 Ilya Evseev <evseev@altlinux.ru> 1.45-alt1
- update to new version 1.45; patchset revisited

* Thu Nov 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1.44-alt2
- Cleaned up chroot patch.
- Disabled use of pcap_restart.

* Fri Jul  1 2005 Ilya Evseev <evseev@altlinux.ru> 1.44-alt1
- update to new version 1.44; patchset revisited
- bugfix chrooting patch: was completely unusable

* Sat Mar 19 2005 Ilya Evseev <evseev@altlinux.ru> 1.43-alt2
- specfile bugfix: invalid email in changelog

* Wed Mar 16 2005 Ilya Evseev < evseev@altlinux.ru> 1.43-alt1
- 1.43, patchset revisited
- specfile: added russian summary and description
- added optional building of PCRE-based package

* Tue May 25 2004 Dmitry V. Levin <ldv@altlinux.org> 1.42-alt1
- Updated to 1.42, updated droppriv patch.

* Mon Jan 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1.41-alt1
- Updated to 1.41, updated droppriv patch.

* Wed Oct 30 2002 Dmitry V. Levin <ldv@altlinux.org> 1.40.1-alt3
- Explicitly use autoconf-2.13 for build.

* Wed Apr 10 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.40.1-alt2
- Relocated %_bindir/%name to %_sbindir/

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.40.1-alt1
- 1.40.1
- Fixed build.
- Rebuilt with libpcap-0.7.1.
- Drop privs and chroot to /var/resolv.

* Sun Mar 04 2001 Dmitry V. Levin <ldv@fandra.org> 1.39-ipl1
- 1.39

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 1.38-ipl2
- Rebuilt with libpcap-0.6.1.

* Sat Jul 01 2000 Dmitry V. Levin <ldv@fandra.org> 1.38-ipl1
- updated to 1.38
- FHSification.

* Sun Feb 20 2000 Dmitry V. Levin <ldv@fandra.org>
- updated to 1.37

* Tue Oct 26 1999 Dmitry V. Levin <ldv@fandra.org>
- updated to 1.35

* Tue Sep 09 1999 Dmitry V. Levin <ldv@fandra.org>
- initial revision
