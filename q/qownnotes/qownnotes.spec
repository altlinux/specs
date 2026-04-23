Name: qownnotes
Version: 26.4.19
Release: alt1
License: GPLv2
Group: Office
Summary: Note-taking app and todo list manager with ownCloud/Nextcloud integration
Url: http://www.qownnotes.org/

BuildRequires: gcc gcc-c++ fdupes libbotan-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-websockets-devel
BuildRequires: desktop-file-utils
Requires: libqt6-svg
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %name-%version.tar.xz

%description
QOwnNotes is the open source notepad and todo list manager, that works together
with the default notes application of ownCloud.
So you are able to write down your thoughts with QOwnNotes and edit or
search for them later from your mobile device (like with CloudNotes or
the ownCloud/Nextcloud web-service.
The notes are stored as plain text files and are synced with
ownCloud's/Nextcloud's file sync functionality. Of course other software,
like Dropbox can be used too.
I like the concept of having notes accessible in plain text files,
like it is done in the ownCloud notes app, to gain a maximum of freedom,
but I was not able to find a decent desktop note taking tool or a text editor,
that handles them well. Out of this need QOwnNotes was born.

%prep
%setup

%build
lrelease-qt6 src/QOwnNotes.pro

pushd src/
%qmake_qt6 \
    PREFIX=%_prefix \
    USE_SYSTEM_BOTAN=ON \
    QON_QT6_BUILD=ON
popd
%make_build -C src/

%install
pushd src/
install -D -m 0755 QOwnNotes %buildroot%_bindir/QOwnNotes

# install visuals
install -D -m 0644 PBE.QOwnNotes.desktop %buildroot%_desktopdir/QOwnNotes.desktop
install -D -m644 "images/icons/128x128/apps/QOwnNotes.png" "%buildroot%_pixmapsdir/QOwnNotes.png"
for format in {16x16,24x24,32x32,48x48,64x64,96x96,128x128,256x256,512x512}; do
    install -D -m644 "images/icons/$format/apps/QOwnNotes.png" "%buildroot%_iconsdir/hicolor/$format/apps/QOwnNotes.png"
    done

install -D -m644 "images/icons/scalable/apps/QOwnNotes.svg" "%buildroot%_iconsdir/hicolor/scalable/apps/QOwnNotes.svg"

install -d "%buildroot/%_qt6_translationdir/"
install -D -m644 languages/*.qm "%buildroot/%_qt6_translationdir/"
popd

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/QOwnNotes
%_qt6_translationdir/QOwnNotes_*.qm
%_desktopdir/QOwnNotes.desktop
%_iconsdir/hicolor/*/apps/QOwnNotes.png
%_iconsdir/hicolor/scalable/apps/QOwnNotes.svg
%_pixmapsdir/QOwnNotes.png

%changelog
* Thu Apr 23 2026 Daniil-Viktor Ratkin <krf10@altlinux.org> 26.4.19-alt1
- new version

* Wed Aug 30 2023 Ivan A. Melnikov <iv@altlinux.org> 23.8.2-alt1
- new version (by samael@).

* Mon Jul 13 2020 Grigory Ustinov <grenka@altlinux.org> 20.7.3-alt1
- new version
- build with system libbotan (Closes: #38379)

* Wed Jan 16 2019 Konstantin Artyushkin <akv@altlinux.org> 19.1.3-alt1
- new version

* Tue Jun 27 2017 Konstantin Artyushkin <akv@altlinux.org> 17.06.6-alt1
- initial build for ALT Sisyphus
