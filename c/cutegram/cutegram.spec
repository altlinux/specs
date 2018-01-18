%global origname Cutegram

Name: cutegram
Version: 2.99
Release: alt1.git_2_e489812
Summary: Cutegram is a telegram client by Aseman Land

# Bundled JS stuff:
# js-linkify: MIT
# js-twemoji: MIT and CC-BY-4.0
# awesome-fonts: MIT and OFL-1.0
License: GPLv3+ and MIT and CC-BY-4.0 and OFL
Group: Networking/Instant messaging
Url: https://github.com/Aseman-Land/%origname
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar

Patch: cutegram-2.99-dialog_fix.patch

# https://github.com/Aseman-Land/Cutegram/pull/233
#  Patch1: 0001-Install-cutegram-binary-when-BinaryMode-is-enabled.patch
#  Patch2: 0002-desktop-Exec-cutegram-when-binaryMode-is-enabled.patch
#  Patch3: 0003-don-t-install-qmlFiles-when-binaryMode-is-enabled.patch



BuildRequires(pre): rpm-macros-qt5

# Automatically added by buildreq on Sat Apr 22 2017
# optimized out: gcc-c++ libGL-devel libqt5-core libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-widgets libstdc++-devel python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-script-devel qt5-webchannel-devel qt5-xmlpatterns-devel
BuildRequires: python3-module-zope qt5-3d-devel qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-quickcontrols2-devel qt5-sensors-devel 
BuildRequires:qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel


Requires: aseman-qt-tools
Requires: telegramqml
Requires: qt5-graphicaleffects

%description
A different telegram client from Aseman team. Cutegram forked from Sigram
by Sialan Labs. Cutegram project are released under the terms of the GPLv3
license.

%prep
%setup -n %name-%version 
%patch -p1

#patch1 -p1
#patch2 -p1
#patch3 -p1


%build
%qmake_qt5 PREFIX=%prefix CONFIG+=binaryMode

%make_build 

%install
INSTALL_ROOT=%buildroot %makeinstall_std


%files
%doc README.md
%_bindir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_pixmapsdir/%name.png
%_desktopdir/%origname.desktop

%changelog
* Wed Jan 17 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2.99-alt1.git_2_e489812
- Add requires qt5-graphicaleffects
- Closes: #34432

* Sat Apr 22 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2.99-alt1.git_1_e489812
- New version from git e489812

* Fri Apr 21 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2.99-alt1.git_0_bfdceb
- initial build for ALT Linux Sisyphus

* Sat Aug 06 2016 Igor Gnatenko <ignatenko@redhat.com> - 3.0-0.6gitbfdceb3
- Update to latest snapshot
- Add runtime req: qt5-qtimageformats to display stickers

* Mon Jul 25 2016 Igor Gnatenko <ignatenko@redhat.com> - 3.0-0.5gitc67ce70
- Add Provides and License for awesome-fonts
- Run update-desktop-database due to MimeType in %%post and %%postun

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 3.0-0.4git7294861
- Add missing Requires: qt5-qtgraphicaleffects

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 3.0-0.3git7294861
- Apply patch to not install uncompressed qml files (we use one-binary mode)

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 3.0-0.2git7294861
- Fix BuildRequires and Requires

* Sat Jul 23 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0-0.1git7294861
- Initial commit.
