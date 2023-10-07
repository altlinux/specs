Name: cool-retro-term
Version: 1.2.0
Release: alt2

Summary: Cool Retro Terminal
License: GPLv3+
Group: Terminals

Url: https://github.com/Swordfish90/cool-retro-term
Source0: %name-%version.tar.gz
#Source1: qmltermwidget.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: qt5-declarative-devel qt5-qmltermwidget 
BuildRequires: desktop-file-utils qt5-quickcontrols2-devel

Requires: qt5-graphicaleffects qt5-qmltermwidget 
Requires: qt5-quickcontrols qt5-quickcontrols2

%description
cool-retro-term is a terminal emulator which tries to mimic the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.

%prep
#setup -a 1
%setup -q

rm -rf ./qmltermwidget
sed -e "s/SUBDIRS += qmltermwidget//" -i %{name}.pro

%build
qmake-qt5
%make_build

%install
# Work around weird qmake behaviour:
# http://davmac.wordpress.com/2007/02/21/qts-qmake/
make INSTALL_ROOT=%buildroot install

desktop-file-install \
	--dir=%buildroot%_datadir/applications \
	%name.desktop

%files
%doc gpl-2.0.txt gpl-3.0.txt README.md
%_bindir/%name
#_libdir/qt5/qml/
%_datadir/applications/%name.desktop
%_iconsdir/*/*/*/*.png

%changelog
* Sat Oct 07 2023 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt2
- Build with system qt5-qmltermwidget  (Closes: #44546)

* Sun Jan 30 2022 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt1
- 1.2.0
- Update url (Closes: #41687)
- Add BR: qt5-quickcontrols2

* Wed Jun 16 2021 Ilya Mashkin <oddity@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Tue Apr 03 2018 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1 (thx zerg@)

* Tue Apr 03 2018 Michael Shigorin <mike@altlinux.org> 1.0.0-alt2
- updated BR:

* Sun Jan 25 2015 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- v1.0.0
- added qmltermwidget (upstream pulls it in as submodule)

* Mon Oct 13 2014 Michael Shigorin <mike@altlinux.org> 0.9-alt4
- ge4f89f0 (incl. --fullscreen)

* Mon Oct 06 2014 Michael Shigorin <mike@altlinux.org> 0.9-alt3
- actually fixed upstream #143

* Mon Oct 06 2014 Michael Shigorin <mike@altlinux.org> 0.9-alt2
- relax unresolved ELF symbol check (upstream #143)

* Sun Oct 05 2014 Michael Shigorin <mike@altlinux.org> 0.9-alt1
- built for ALT Linux (based on original spec by Markus S. <kamikazow@web.de>)
- upstream commit g9deeb5e

