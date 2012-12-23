Name: livecd-ru
Version: 0.2
Release: alt1

Summary: hardwire Russian keyboard layout availability for a LiveCD
License: Public domain
Group: System/Configuration/Other

Url: http://www.opennet.ru/openforum/vsluhforumID3/83728.html#136
BuildArch: noarch
Requires: xinitrc

AutoReqProv: no

%description
%summary

%prep

%post
mkdir -p /etc/sysconfig &&
cat >> /etc/sysconfig/i18n << _EOF_
# %name
SYSFONT=UniCyr_8x16
LANG=ru_RU.utf8
_EOF_

install -d %_sysconfdir/X11/xinit &&
echo "-option grp:ctrl_shift_toggle,grp_led:scroll \
-variant ,winkeys -layout us,ru" > %_sysconfdir/X11/xinit/Xkbmap ||:

%files

%changelog
* Sun Dec 23 2012 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- added /etc/sysconfig/i18n setup

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- crafted initial release for live-webkiosk.iso

