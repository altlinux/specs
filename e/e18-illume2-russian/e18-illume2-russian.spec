Name: e18-illume2-russian
Version: 0
Release: alt1

Summary: Russian keyboard layout for Illume2
License: BSD
Group: Graphical desktop/Enlightenment

Url: http://docs.openmoko.org/trac/ticket/2101
Source: http://docs.openmoko.org/trac/raw-attachment/ticket/2101/Default_RU.kbd
Packager: Michael Shigorin <mike@altlinux.org>

%define kbddir %_libdir/enlightenment/modules/illume-keyboard/keyboards

%description
This package adds Cyrillic layout to Illume2 on-screen keyboard
for Enlightenment desktop environment.

NB: it's not locale specific, install as needed.

%prep

%install
install -pDm644 %SOURCE0 %buildroot/%kbddir/Default_RU.kbd

%files
%kbddir/Default_RU.kbd

%changelog
* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 0-alt1
- initial release

