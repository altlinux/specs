Name: cool-retro-term
Version: 0.9
Release: alt4

Summary: Cool Retro Terminal
License: GPLv3
Group: Terminals

Url: https://github.com/Swordifish90/cool-retro-term
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Declarative)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: desktop-file-utils

Requires: qt5-graphicaleffects
Requires: qt5-quickcontrols

%description
cool-retro-term is a terminal emulator which tries to mimic the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.

%prep
%setup

%build
qmake-qt5
%make_build

%install
# Work around weird qmake behaviour:
# http://davmac.wordpress.com/2007/02/21/qts-qmake/
make INSTALL_ROOT=%buildroot install

desktop-file-install \
	--dir=$RPM_BUILD_ROOT%_datadir/applications \
	%name.desktop

%files
%doc gpl-2.0.txt gpl-3.0.txt README.md
%_bindir/%name
%_libdir/qt5/qml/
%_datadir/applications/%name.desktop

%changelog
* Mon Oct 13 2014 Michael Shigorin <mike@altlinux.org> 0.9-alt4
- ge4f89f0 (incl. --fullscreen)

* Mon Oct 06 2014 Michael Shigorin <mike@altlinux.org> 0.9-alt3
- actually fixed upstream #143

* Mon Oct 06 2014 Michael Shigorin <mike@altlinux.org> 0.9-alt2
- relax unresolved ELF symbol check (upstream #143)

* Sun Oct 05 2014 Michael Shigorin <mike@altlinux.org> 0.9-alt1
- built for ALT Linux (based on original spec by Markus S. <kamikazow@web.de>)
- upstream commit g9deeb5e

