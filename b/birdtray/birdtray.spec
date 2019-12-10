%define _unpackaged_files_terminate_build 1

Name: birdtray
Version: 1.5
Release: alt1
Summary: Birdtray is a free system tray notification for new mail for Thunderbird
License: GPLv3 
Group: Networking/Mail
Url: https://github.com/gyunaev/birdtray
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-macros-qt5 
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: libsqlite3-devel
BuildRequires: qt5-x11extras-devel

%description
System tray notifications for Thunderbird
Birdtray provides systray notifications for Thunderbird.  It displays the
count of unread mail, hides the Thunderbird window when not in use, and
restores it on clicking the tray icon.  It also provides a context menu
with commands such as starting composing a new mail.

It is a nasty hack -- an external process looking at Thunderbird's
insides, it suffers from problems like noticing new mails only after a
delay, having to restart Thunderbird just to hide its window, etc --
you'd want to use an extension like firetray instead -- but, it is
likely that support for Thunderbird XUL extensions will be dropped soon,
possibly by the time you read these words.

%prep
%setup

%build
%qmake_qt5 src/birdtray.pro
%make_build

%install
install -D %_builddir/%name-%version/%name  %buildroot%_bindir/%name
mkdir -p %buildroot%_pixmapsdir
cp %_builddir/%name-%version/src/res/*.png %buildroot%_pixmapsdir/

mkdir -p %buildroot%_desktopdir
cat <<EOF >%buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Birdtray
Comment=Birdtray is a free system tray notification for new mail for Thunderbird
Comment[ru]=Birdtray - это бесплатная система уведомлений в системном трее для новой почты для Thunderbird
TryExec=%name
Exec=%_bindir/%name
Icon=thunderbird.png
Terminal=false
Type=Application
Categories=Application;Network
EOF

%files
%doc LICENSE README.md
%_bindir/%name
%_pixmapsdir/*.png
%_desktopdir/%name.desktop

%changelog
* Wed May 15 2019 Mikhail Chernonog <snowmix@altlinux.org> 1.5-alt1
- Initial build for Sisyphus
