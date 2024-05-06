%define rname desktop-wallpapers

Name: alt-desktop-wallpapers
Version: 11.0.0
Release: alt1
%K5init no_altplace

Group: Graphical desktop/Other
Summary: ALT Desktop Wallpapers
Url: http://www.basealt.ru
License: Proprietary

BuildArch: noarch

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++ qt5-base-devel
BuildRequires: /usr/bin/convert

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

# generate previews
for d in %buildroot/%_datadir/wallpapers/* ; do
    [ -f ${d}/metadata.desktop ] || continue
    ! [ -f ${d}/contents/screenshot.png -o -f ${d}/contents/screenshot.jpg ] || continue
    BG=`find ${d}/contents/images/ -type f -name \*.png -o -type f -name \*.jpg | head -n 1`
    [ -n "$BG" ] || continue
    EXT=`echo "$BG" | sed  's|.*\.||'`
    convert $BG -resize 400x250 ${d}/contents/screenshot.${EXT}
done

# install GNOME wallpapers
PREFIX=%buildroot
WALLDIR=%buildroot/%_datadir/wallpapers
GNOMEWALLDIR=%buildroot/%_pixmapsdir
mkdir -p $GNOMEWALLDIR
pushd $WALLDIR 1>/dev/null
ls -1d * | \
while read W_NAME; do
    F_PATH=`find $W_NAME/contents/images -type f | head -n 1`
    [ -n "$F_PATH" ] || continue
    F_PATH=`realpath $F_PATH`
    W_EXT=`echo "$F_PATH"| sed 's|^.*\.||'`
    ln -sr $F_PATH $GNOMEWALLDIR/${W_NAME}.${W_EXT}
done
popd 1>/dev/null

%files
#%doc COPYING*
%_datadir/wallpapers/*
%_pixmapsdir/*

%changelog
* Mon May 06 2024 Sergey V Turchin <zerg at altlinux dot org> 11.0.0-alt1
- new version

* Fri Apr 29 2022 Sergey V Turchin <zerg at altlinux dot org> 0.3.0-alt1
- add more wallpapers

* Mon Nov 29 2021 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- fix morning_mist name

* Wed Nov 24 2021 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1
- new version

* Tue Oct 12 2021 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt2
- initial build
