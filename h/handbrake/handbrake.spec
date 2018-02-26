Name: handbrake
Version: 0.9.5
Release: alt1.3
Summary: Multithreaded Video Transcoder
Packager: Motsyo Gennadi <drool@altlinux.ru>
Source: http://prdownloads.sourceforge.net/handbrake/HandBrake-%version.tar.bz2
Source101: http://download.handbrake.fr/handbrake/contrib/a52dec-0.7.4.tar.gz
Source102: http://download.handbrake.fr/handbrake/contrib/faac-1.28.tar.gz
Source103: http://download.handbrake.fr/handbrake/contrib/faad2-2.7.tar.gz
Source104: http://download.m0k.org/handbrake/contrib/ffmpeg-r25689.tar.bz2
Source105: http://download.handbrake.fr/handbrake/contrib/lame-3.98.tar.gz
Source106: http://download.handbrake.fr/handbrake/contrib/libdca-r81-strapped.tar.gz
Source107: http://download.handbrake.fr/handbrake/contrib/libdvdnav-svn1168.tar.gz
Source108: http://download.handbrake.fr/handbrake/contrib/libdvdread-svn1168.tar.gz
Source109: http://download.m0k.org/handbrake/contrib/libmkv-0.6.4.1-0-ga80e593.tar.bz2
Source110: http://download.handbrake.fr/handbrake/contrib/libogg-1.1.3.tar.gz
Source111: http://download.handbrake.fr/handbrake/contrib/libsamplerate-0.1.4.tar.gz
Source112: http://download.handbrake.fr/handbrake/contrib/libtheora-1.1.0.tar.bz2
Source113: http://download.handbrake.fr/handbrake/contrib/libvorbis-aotuv_b5.tar.gz
Source114: http://download.handbrake.fr/handbrake/contrib/mp4v2-trunk-r355.tar.bz2
Source115: http://download.handbrake.fr/handbrake/contrib/mpeg2dec-0.5.1.tar.gz
Source116: http://download.handbrake.fr/handbrake/contrib/x264-r1834-a51816a.tar.gz
Source117: http://download.m0k.org/handbrake/contrib/fontconfig-2.8.0.tar.gz
Source118: http://download.m0k.org/handbrake/contrib/freetype-2.3.9.tar.gz
Source119: http://download.m0k.org/handbrake/contrib/libass-0.9.9.tar.bz2
Source120: http://download.m0k.org/handbrake/contrib/libbluray-0.0.1-pre-16-g1aab213.tar.gz
Source121: http://download.m0k.org/handbrake/contrib/libxml2-2.7.7.tar.gz
Source151: handbrake-ffmpeg_fix_missing_return_in_nonvoid_function.patch
Url: http://handbrake.fr/
Group: Video
License: GPLv2
Patch0: %name-0.9.5-fix-for-newer-libnotify-versions.patch

# Automatically added by buildreq on Fri Jun 01 2012 (-bi)
# optimized out: elfutils fontconfig glib2-devel gstreamer-devel gtk-update-icon-cache libX11-devel libatk-devel libcairo-devel libdbus-devel libdbus-glib libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgst-plugins libgtk+2-devel libpango-devel libsoup-devel libstdc++-devel libtinfo-devel libxml2-devel perl-XML-Parser pkg-config python-base python-modules shared-mime-info xml-utils xorg-xproto-devel
BuildRequires: bzlib-devel gcc-c++ gst-plugins-devel intltool libalsa-devel libdbus-glib-devel libgudev-devel libncurses-devel libnotify-devel libwebkitgtk2-devel nasm python-modules-compiler python-modules-encodings wget yasm zlib-devel

%description
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

%package cli
Summary: Multithreaded Video Transcoder
Group: Video

%description cli
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

This package contains a command-line interface for Handbrake.

%package gtk
Summary: Multithreaded Video Transcoder
Group: Video
Requires: %name-cli = %version-%release

%description gtk
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

This package contains a GTK+ graphical user interface for Handbrake.

%prep
%setup -n HandBrake-%version
%patch0 -p1

# Copy 3rd party dependencies into expected locations:
%__mkdir download
for f in \
%{S:101} %{S:102} %{S:103} %{S:104} %{S:105} %{S:106} \
%{S:107} %{S:108} %{S:109} %{S:110} %{S:111} %{S:112} \
%{S:113} %{S:114} %{S:115} %{S:116} %{S:117} %{S:118} \
%{S:119} %{S:120} %{S:121} \
; do
     %__ln_s "$f" download/
done

# check beforehand that the versions match what the
# build system expects:
missing=$PWD/.missing
%__grep -hE '\.FETCH\.url *=' contrib/*/module.defs \
| %__awk -F' =' '{print $2}' \
| while read url; do
     f=$(echo "$url" | %__sed 's|^.*/||')
     case $f in
    	  bzip2*|libiconv*|pthreads*|zlib*) continue ;;
     esac
     [ -e "$RPM_SOURCE_DIR/$f" ] || echo "$url">>"$missing"
done

if test -e "$missing"; then
     echo "ERROR: missing contrib source archives:" >&2
     cat "$missing" >&2
     exit 1
fi

%build
# will be removed when the makefiles are fixed, currently
# fails on openSUSE factory because of --as-needed
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"

%__cp "%{S:151}" contrib/ffmpeg/A99-fix-missing-return-in-nonvoid-function.patch

%__mkdir build
./configure \
     --force \
     --build="$PWD/build" \
     --prefix="%buildroot%prefix" \
     --strip="/bin/true" \
     --optimize=speed \
     --debug=max

GHB_PKGS="dbus-glib-1 glib-2.0 gdk-pixbuf-2.0 gudev-1.0 webkit-1.0 libnotify"
GHB_PKGS="$GHB_PKGS gstreamer-interfaces-0.10 gstreamer-0.10 gstreamer-pbutils-0.10 gstreamer-video-0.10"
pushd build
%__make libhb/project.h
%__make %{?_smp_mflags} \
    GHB_CFLAGS="$(pkg-config --cflags $GHB_PKGS) -I../../libhb" \
    GHB_LIBS="$(pkg-config --libs $GHB_PKGS)"
popd #build

%install
pushd build
%__make install
popd #build

%__ln_s ghb "%buildroot%_bindir/HandBrakeGUI"

%__rm "%buildroot%_datadir/icons"/*/*.cache

%files cli
%doc AUTHORS COPYING CREDITS NEWS THANKS
%_bindir/HandBrakeCLI

%files gtk
%doc AUTHORS COPYING CREDITS NEWS THANKS
%_bindir/HandBrakeGUI
%_bindir/ghb
%_desktopdir/ghb.desktop
%_datadir/icons/*/*/apps/hb-icon.png

%changelog
* Tue Jun 05 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.3
- fir build for Sisyphus (thank azol@ for help)

* Sun Jun 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.2
- test fix for sisyphus

* Sun Jun 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.1
- test fix for sisyphus

* Fri Jun 01 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1
- initial build for ALT Linux from OpenSUSE package
