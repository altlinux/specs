
Name: alsamixer-qt4
Version: 0.6.0
Release: alt1

Summary: GUI mixer application for ALSA
License: GPLv3
Group: Sound
Url: http://xwmw.org/alsamixer-qt4/

BuildRequires: gcc-c++ libqt4-devel libalsa-devel
BuildRequires: cmake rpm-macros-cmake
Requires: common-licenses

Packager: Ivan A. Melnikov <iv@altlinux.org>
Source: %name-%version.tar

%description
Alsamixer-Qt4 is a graphical (GUI) mixer application for the linux sound
system ALSA.

It provides sliders and switches to manipulate volume levels and other
aspects of sound playback and recording on the hardware level.

%prep
%setup

%build
%cmake
%make_build -CBUILD VERBOSE=1

%install
%makeinstall_std -CBUILD

pushd %buildroot%_docdir/%{name}*/
rm -f COPYING
ln -s "/usr/share/license/GPL-3" COPYING
popd

# TODO: make russian locale and package locales
rm -f %buildroot%_datadir/%name/l10n/app_*

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Alsamixer-Qt4
Comment=GUI mixer application for ALSA
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Audio;Mixer;Qt;
EOF

%files
%_bindir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/%{name}*
%_man1dir/*
%doc %_docdir/*

%changelog
* Wed Jan 12 2011 Ivan A. Melnikov <iv@altlinux.org> 0.6.0-alt1
- Initial build for ALTLinux.

