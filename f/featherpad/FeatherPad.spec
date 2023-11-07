Name: featherpad
Version: 1.4.1
Release: alt1.2

Summary: A lightweight Qt5 plain-text editor for Linux
License: GPLv3+
Group: Editors

Url: https://github.com/tsujan/FeatherPad
Source: V%version.tar.gz

BuildPreReq: cmake rpm-build-ninja
BuildRequires: ImageMagick-tools qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-x11extras-devel libhunspell-devel


%description
FeatherPad is a lightweight Qt5 plain-text editor for Linux.

* Drag-and-drop support, including tab detachment and attachment;
* X11 virtual desktop awareness
* An optionally permanent search-bar with a different search entry for each tab;
* Instant highlighting of found matches when searching;
* A docked window for text replacement;
* Support for showing line numbers and jumping to a specific line;
* Automatic detection of text encoding as far as possible and optional saving with encoding;
* Syntax highlighting for common programming languages;
* Session management;
* Side-pane mode;
* Printing;
* Text zooming;
* Appropriate but non-interrupting prompts;

%prep
%setup -n FeatherPad-%version

%define _PX 128 16 192 24 256 32 48 64 72 96

%build
%cmake -GNinja
cmake --build "%_cmake__builddir" -j%__nprocs

for n in %_PX; do
	convert featherpad/data/icons/featherpad.svg $n.png
done

%install
%cmake_install

for n in %_PX; do
	install -D $n.png %buildroot%_iconsdir/hicolor/${n}x$n/apps/%name.png
done

%files
%_bindir/*
%_desktopdir/*
%_datadir/%name/*
%_iconsdir/*/*/*/*
%_datadir/metainfo/featherpad.metainfo.xml

%changelog
* Tue Nov 07 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.4.1-alt1.2
- NMU: trimmed build dependencies according to CMakeLists.txt
  (cross-check: dependencies of binary package did not change).
  As a result the package can be build for LoongArch.

* Tue Sep 19 2023 Leontiy Volodin <lvol@altlinux.org> 1.4.1-alt1.1
- fixed build with ImageMagick 7

* Thu Jun 15 2023 Leontiy Volodin <lvol@altlinux.org> 1.4.1-alt1
- new version 1.4.1

* Wed Apr 19 2023 Leontiy Volodin <lvol@altlinux.org> 1.4.0-alt1
- new version 1.4.0

* Tue Jan 10 2023 Leontiy Volodin <lvol@altlinux.org> 1.3.5-alt1
- new version 1.3.5

* Wed Nov 30 2022 Leontiy Volodin <lvol@altlinux.org> 1.3.4-alt1
- new version 1.3.4

* Mon Oct 10 2022 Leontiy Volodin <lvol@altlinux.org> 1.3.3-alt1
- new version 1.3.3

* Sat Sep 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.3.2-alt1
- new version 1.3.2

* Thu Aug 04 2022 Leontiy Volodin <lvol@altlinux.org> 1.3.1-alt1
- new version 1.3.1
- removed qmake support by upstream

* Thu Jun 16 2022 Leontiy Volodin <lvol@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Tue Apr 26 2022 Leontiy Volodin <lvol@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Wed Jan 12 2022 Leontiy Volodin <lvol@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Tue Oct 19 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.1-alt1
- new version 1.0.1

* Thu Sep 02 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt1
- new version 1.0.0
- built with cmake and ninja instead qmake and make

* Wed Mar 10 2021 Leontiy Volodin <lvol@altlinux.org> 0.18.0-alt1
- new version 0.18.0

* Wed Jan 13 2021 Leontiy Volodin <lvol@altlinux.org> 0.17.2-alt1
- new version 0.17.2

* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 0.17.1-alt1
- new version 0.17.1

* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Wed Aug 26 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Sun Jun 14 2020 Leontiy Volodin <lvol@altlinux.org> 0.14.2-alt1
- new version 0.14.2

* Thu May 07 2020 Leontiy Volodin <lvol@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Apr 27 2020 Leontiy Volodin <lvol@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Fri Mar 13 2020 Leontiy Volodin <lvol@altlinux.org> 0.13.1-alt1
- new version 0.13.1

* Thu Jan 16 2020 Leontiy Volodin <lvol@altlinux.org> 0.12.1-alt1
- new version 0.12.1

* Thu Jan 09 2020 Leontiy Volodin <lvol@altlinux.org> 0.12.0-alt1
- new version 0.12.0

* Thu Nov 07 2019 Leontiy Volodin <lvol@altlinux.org> 0.11.1-alt1
- new version 0.11.1

* Tue Jul 23 2019 Michael Shigorin <mike@altlinux.org> 0.10.0-alt2
- fixed icons installation
- E2K: avoid webview/webkit/webengine for now
  (looks totally unneeded btw!)

* Wed May 15 2019 Leontiy Volodin <lvol@altlinux.org> 0.10.0-alt1
- new version 0.10.0

* Tue Apr 16 2019 Leontiy Volodin <lvol@altlinux.org> 0.9.4-alt1
- new version 0.9.4

* Fri Feb 01 2019 Anton Midyukov <antohami@altlinux.org> 0.9.2-alt1
- new version 0.9.2

* Thu May 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1.1
- NMU: added Url

* Mon May 07 2018 Fr. Br. George <george@altlinux.ru> 0.8-alt1
- Autobuild version bump to 0.8

* Mon May 07 2018 Fr. Br. George <george@altlinux.ru> 0.7-alt1
- Initial build for ALT

