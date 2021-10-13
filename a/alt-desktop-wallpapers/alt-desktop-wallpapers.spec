%define rname desktop-wallpapers

Name: alt-desktop-wallpapers
Version: 0.1.0
Release: alt2
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
PREFIX=/home/zerg/RPM/TMP/alt-desktop-wallpapers-buildroot
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
* Tue Oct 12 2021 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt2
- initial build
