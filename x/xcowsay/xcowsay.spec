Name: xcowsay
Version: 1.3
Release: alt1
Summary: displays a cute cow and message on your desktop
Group: Games/Other
License: GPL
Url: http://www.doof.me.uk/xcowsay/
Source: %name-%version.tar.gz
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sun Jun 15 2008
BuildRequires: libdbus-glib-devel libgtk+2-devel

%description
xcowsay displays a cute cow and message on your desktop. Inspired by the original cowsay
%prep
%setup -q

%build
%configure --disable-rpath --enable-dbus
%make

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc README ABOUT-NLS INSTALL AUTHORS ChangeLog NEWS
%_bindir/xcow*
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/locale/*/*/%name.*
%_man6dir/xcow*

%changelog
* Sun Nov 14 2010 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Autobuild version bump to 1.3

* Mon Sep 20 2010 Fr. Br. George <george@altlinux.ru> 1.2-alt2
- Closes: #23403

* Wed Apr 28 2010 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Version up
- Use find_lang for .po files

* Thu Sep 25 2008 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Version up

* Sun Jun 15 2008 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build

