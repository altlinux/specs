Name:		focuswriter
Version:	1.8.4
Release:	alt1
Summary:	FocusWriter is a fullscreen, distraction-free word processor
License:	GPLv3
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Group:		Text tools
Url:		http://gottcode.org/focuswriter/
Source0:	http://gottcode.org/focuswriter/%name-%version.tar.bz2

BuildRequires:	libhunspell-devel gcc-c++ zlib-devel 
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake rpm-macros-qt6 qt6-base-devel qt6-tools-devel qt6-multimedia-devel qt6-declarative-devel qt6-5compat-devel libicu-devel

%description
FocusWriter is a fullscreen, distraction-free word processor
designed to immerse you as much as possible in your work.
The program autosaves your progress, and reloads the last files
you had open to make it easy to jump back in during your next
writing session, and has many other features that make it such
that only one thing matters: your writing.

%prep
%setup
%ifarch %e2k
# lcc 1.23.12 doesn't grok u'’' by default
%add_optflags -finput-charset=utf8
%endif

%build
%cmake \
    -DENABLE_LTO=OFF 
%cmake_build

%install

%cmakeinstall_std
# http://altlinux.org/Icon_Paths_Policy
rm -f %buildroot%_pixmapsdir/*.xpm

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_datadir/metainfo/%name.*
%_man1dir/%name.*
%_iconsdir/hicolor/*/apps/*

%changelog
* Thu Jan 12 2023 Ilya Mashkin <oddity@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Tue Sep 27 2022 Ilya Mashkin <oddity@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Sat Sep 03 2022 Ilya Mashkin <oddity@altlinux.ru> 1.8.2-alt2
- fix source path

* Sat Sep 03 2022 Ilya Mashkin <oddity@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Jul 05 2022 Ilya Mashkin <oddity@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Wed Jun 22 2022 Ilya Mashkin <oddity@altlinux.ru> 1.8.0-alt1
- 1.8.0
- Build with Qt6/cmake

* Fri May 01 2020 Motsyo Gennadi <drool@altlinux.ru> 1.7.6-alt1
- 1.7.6

* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 1.6.16-alt3
- E2K: better fix (see also mcst#3940)

* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 1.6.16-alt2
- E2K: ftbfs workaround

* Wed Oct 03 2018 Michael Shigorin <mike@altlinux.org> 1.6.16-alt1
- 1.6.16
- minor spec cleanup

* Fri Jan 26 2018 Motsyo Gennadi <drool@altlinux.ru> 1.6.8-alt1
- 1.6.8

* Mon Mar 13 2017 Motsyo Gennadi <drool@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Wed Oct 05 2016 Motsyo Gennadi <drool@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Sat Aug 27 2016 Motsyo Gennadi <drool@altlinux.ru> 1.6.0-alt2
- fix BuildRequires for Qt5

* Sat Aug 27 2016 Motsyo Gennadi <drool@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Sat Jun 25 2016 Motsyo Gennadi <drool@altlinux.ru> 1.5.6-alt1
- 1.5.6

* Sun Sep 06 2015 Motsyo Gennadi <drool@altlinux.ru> 1.5.5-alt1
- 1.5.5

* Sun Jun 14 2015 Motsyo Gennadi <drool@altlinux.ru> 1.5.4-alt1
- 1.5.4

* Sun Jun 29 2014 Motsyo Gennadi <drool@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Sun Apr 13 2014 Motsyo Gennadi <drool@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Fri Mar 28 2014 Motsyo Gennadi <drool@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Fri May 31 2013 Motsyo Gennadi <drool@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Mon Apr 08 2013 Motsyo Gennadi <drool@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Thu Mar 28 2013 Motsyo Gennadi <drool@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Thu Nov 29 2012 Motsyo Gennadi <drool@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sun Sep 23 2012 Motsyo Gennadi <drool@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Sun Jun 17 2012 Motsyo Gennadi <drool@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Fri Dec 09 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.5.1-alt1
- 1.3.5.1

* Sat Nov 05 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.4.1-alt1
- 1.3.4.1

* Tue Mar 22 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.2.1-alt1
- initial build for ALT Linux
