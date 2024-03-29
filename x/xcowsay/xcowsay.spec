Name: xcowsay
Version: 1.6
Release: alt1
Summary: displays a cute cow and message on your desktop
Group: Games/Other
License: GPLv3
Url: http://www.doof.me.uk/xcowsay/
Source: %name-%version.tar.gz
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sun Jun 15 2008
BuildRequires: libdbus-glib-devel libgtk+3-devel

%description
xcowsay displays a cute cow and message on your desktop. Inspired by the original cowsay
%prep
%setup

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
* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 1.6-alt1
- Autobuild version bump to 1.6

* Thu Jan 28 2021 Fr. Br. George <george@altlinux.ru> 1.5.1-alt1
- Autobuild version bump to 1.5.1

* Thu Aug 27 2020 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Autobuild version bump to 1.5
- Switch to gtk3

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Autobuild version bump to 1.4

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3-alt1.qa1
- NMU: rebuilt for debuginfo.

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

