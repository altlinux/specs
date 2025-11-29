%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: noblenote
Version: 1.3.0
Release: alt1

Summary: Qt program for taking notes
License: MIT
Group: Office
Url: https://github.com/hakaishi/nobleNote

Source: %name-%version.tar

BuildRequires: qt5-base-devel
BuildRequires: /usr/bin/lrelease-qt5

%description
nobleNote is a program to organize and create notes. It has an icon
in the system tray and supports drag and drop. The note-editor supports
different fonts, font sizes and colors as well as background colors.
You can also import notes from other programs like gnote and tomboy.
The notes are saved in the html format.

%prep
%setup
sed -i 's|^Categories=.*|Categories=Utility;TextTools;|' noblenote.desktop
sed -i 's|Icon=noblenote|Icon=/usr/share/pixmaps/noblenote-icons/noblenote.png|' noblenote.desktop

%build
lrelease-qt5 nobleNote.pro
qmake-qt5 \
          PREFIX=%_prefix \
          CONFIG+=nostrip \
          QMAKE_CXXFLAGS="%optflags" \
          nobleNote.pro

%install
%makeinstall_std INSTALL_ROOT=%buildroot
install -Dm644 noblenote.desktop %buildroot%_desktopdir/noblenote.desktop

%find_lang %name --with-qt

%files -f %{name}.lang
%doc COPYING NEWS README.md screenshot
%_bindir/noblenote
%_desktopdir/noblenote.desktop
%dir %_pixmapsdir/noblenote-icons/
%_pixmapsdir/noblenote-icons/*

%changelog
* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
