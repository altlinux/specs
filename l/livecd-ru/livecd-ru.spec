Name: livecd-ru
Version: 0.1
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
install -d %_sysconfdir/X11/xinit &&
echo "-option grp:ctrl_shift_toggle,grp_led:scroll \
-variant ,winkeys -layout us,ru" > %_sysconfdir/X11/xinit/Xkbmap ||:

%files

%changelog
* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- crafted initial release for live-webkiosk.iso

