Name: iftop
Version: 0.17
Release: alt4

Summary: Display bandwidth usage on an interface
License: GPL
Group: Monitoring

Url: http://www.ex-parrot.com/~pdw/iftop/
Packager: Michael Shigorin <mike@altlinux.org>

# %url/download/iftop-%version.tar.gz
Source: iftop-%version.tar
Patch: iftop-%version-%release.patch

Summary(ru_RU.KOI8-R): Отображает использование полосы пропускания сети
Summary(uk_UA.KOI8-U): В╕дбива╓ використання мереж╕

Requires(pre): shadow-utils
Requires: /var/resolv

# Automatically added by buildreq on Wed Jan 20 2010
BuildRequires: libncurses-devel libpcap-devel

%description
iftop does for network usage what top(1) does for CPU usage.
It listens to network traffic on a named interface and displays
a table of current bandwidth usage by pairs of hosts.  Handy for
answering the question "why is our ADSL link so slow?".

%description -l ru_RU.KOI8-R
iftop - аналог top(1) по части использования сети: слушает
трафик на указанном интерфейсе и отображает таблицу текущего
использования по парам хостов.  Удобно для ответа на вопрос
"почему наш ADSL так тормозит?".

%description -l uk_UA.KOI8-U
iftop - аналог top(1) щодо використання мереж╕: слуха╓ траф╕к
на вказаному ╕нтерфейс╕ й зображу╓ таблицю поточного використання
за парами хост╕в.  Зручно для в╕дпов╕д╕ на запитання "чому наш
ADSL так гальму╓?".

%prep
%setup
%patch -p1

%build
%add_optflags -fno-strict-aliasing -DNO_SYSTEM
%autoreconf
%configure --with-user=_iftop --with-chroot=/var/resolv
%make_build

%install
%makeinstall
mkdir -p %buildroot%_bindir
chmod 700 %buildroot%_sbindir/iftop
mv %buildroot%_sbindir/iftop %buildroot%_bindir/
ln -s `relative %_bindir/iftop %_sbindir/` %buildroot%_sbindir/
install -pD -m755 iftop.control %buildroot%_controldir/iftop

%pre
%_sbindir/groupadd -r -f netadmin
%pre_control iftop

%post
%_sbindir/groupadd -r -f _iftop
%_sbindir/useradd -r -g _iftop -d /dev/null -s /dev/null -n _iftop >/dev/null 2>&1 ||:
%post_control -s netadmin iftop

%files
%_bindir/*
%_sbindir/*
%_controldir/iftop
%_man8dir/*
%doc ChangeLog README TODO

%changelog
* Wed Jan 20 2010 Michael Shigorin <mike@altlinux.org> 0.17-alt4
- disabled subshell execution, thanks Ali Jawad for heads-up
- spec cleanup
- buildreq

* Sun Mar 04 2007 Dmitry V. Levin <ldv@altlinux.org> 0.17-alt3
- Fixed crash on exit (#10888).
- Fixed compilation warnings.

* Fri Jun 23 2006 Michael Shigorin <mike@altlinux.org> 0.17-alt2
- added Gentoo patch fixing #3910 (instead of picking up from CVS)
- noticed that #6120 is also fixed with 0.17

* Tue Jun 20 2006 Michael Shigorin <mike@altlinux.org> 0.17-alt1
- 0.17

* Tue Mar 30 2004 Dmitry V. Levin <ldv@altlinux.org> 0.16-alt2
- Relocated binary from %_sbindir/ to %_bindir/.
- Implemented lowering privileges support:
  run as unprivileged user in chroot jail by default.

* Wed Mar 24 2004 Michael Shigorin <mike@altlinux.ru> 0.16-alt1
- 0.16
- moved to control macros
- changed default control mode to 'netadmin'

* Sun Feb 01 2004 Michael Shigorin <mike@altlinux.ru> 0.15-alt2
- rebuilt with libpcap-0.8.x

* Tue Nov 11 2003 Michael Shigorin <mike@altlinux.ru> 0.15-alt1
- 0.15

* Thu Jul 03 2003 Michael Shigorin <mike@altlinux.ru> 0.13-alt1
- 0.13

* Thu Jun 05 2003 Michael Shigorin <mike@altlinux.ru> 0.12-alt1
- built for ALT Linux
- added control support
