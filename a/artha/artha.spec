Name: artha
Version: 1.0.2
Release: alt2

Summary: Handy off-line thesaurus based on WordNet database
License: GPLv2+
Group: Text tools
Url: http://%name.sourceforge.net/
# http://download.sourceforge.net/%name/%name-%version.tar.bz2
Source: %name-%version.tar

Requires: wordnet-dict
BuildRequires: libgtk+2-devel libwordnet-devel

%description
Artha is a free open-source thesaurus with WordNet as its database.

The main focus of Artha is high usuability, with much simplicity.  It
has distinct features like hot key combo lookup, notifications, regex
search, spelling suggestions, etc.  Once the application is launched,
it sits on the system tray.  The user can select text on any window, and
call Artha by pressing the set hot key combination, which pops up Artha
with the word looked-up.  If the user wants notifications, rather than
the app.  popping up, it can be done by enabling notifications, which
results in a (balloon tip) notification of the selected word's prime
definition from WordNet, from the system tray, when the hot hey is
pressed.

%prep
%setup
# suppress dbus dependencies
sed -i 's/ -ldbus-1 -ldbus-glib-1 / /' src/Makefile.*

%build
# suppress dbus dependencies
export libdbus_CFLAGS=' ' libdbus_LIBS=' '
%configure
# suppress dbus dependencies
sed -i /DBUS_AVAILABLE/d config.h
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%_desktopdir/*
%_pixmapsdir/*
%_datadir/%name
%doc AUTHORS NEWS

%changelog
* Fri Jun 03 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt2
- Updated desktop categories.

* Thu Oct 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Wed Oct 28 2009 Dmitry V. Levin <ldv@altlinux.org> 0.9.1-alt1
- Initial revision.

