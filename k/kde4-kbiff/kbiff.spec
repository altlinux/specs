Name: kde4-kbiff
Version: 4.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Kbiff is a new mail notification utility
Url: http://kbiff.org
License: GPL

Source0: kbiff-%version.tar.bz2

Conflicts: kbiff
BuildRequires(pre): kde4base-runtime-devel
BuildRequires: gcc-c++

Packager: Damir Shayhutdinov <damir@altlinux.ru>

%description
KBiff is a "biff", or new mail notification utility. It is highly configurable
but very easy to use and set up. It tries to combine the best of the features of
most of the "other" biff programs out there. KBiff supports all major mailbox
formats: mbox (Berkely style), maildir, mh, POP3, IMAP4 and NNTP.
This version is built for KDE4

%prep
%setup -n kbiff-%version

%build
%K4build

%install
%K4install

%K4find_lang --with-kde kbiff

%files -f kbiff.lang
%_K4bindir/kbiff
%_K4libdir/libkdeinit4_kbiff.so
%_K4xdg_apps/kbiff.desktop
%_K4iconsdir/hicolor/*/*/kbiff.*
%_K4apps/kbiff
%exclude %_K4iconsdir/locolor
%_man1dir/*

%changelog
* Fri Apr 29 2011 Damir Shayhutdinov <damir@altlinux.ru> 4.0-alt1
- Initial build with KDE4

