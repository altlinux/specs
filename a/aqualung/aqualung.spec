Name: aqualung
Summary: Music Player for GNU/Linux
Version: 2.0
Release: alt1
License: GPL-2.0
Group: Sound
Url: https://aqualung.jeremyevans.net
Vcs: https://github.com/jeremyevans/aqualung.git

Source: %name-%version.tar
Source1: %name.desktop

BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: libatk-devel
BuildRequires: libcairo-devel
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: glib2-devel
BuildRequires: libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
BuildRequires: libpango-devel
BuildRequires: libpixman-devel
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(oggz)
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(mad)
BuildRequires: pkgconfig(libmodplug)
BuildRequires: libmpcdec-devel
BuildRequires: libmac-devel
BuildRequires: ffmpeg
BuildRequires: liblame-devel
BuildRequires: pkgconfig(wavpack)
BuildRequires: pkgconfig(lrdf)
BuildRequires: pkgconfig(libcdio)
BuildRequires: libcdio-paranoia-devel
BuildRequires: pkgconfig(libcddb)
BuildRequires: pkgconfig(libusb)
BuildRequires: pkgconfig(lua)
BuildRequires: libavcodec-devel libavformat-devel libavutil-devel
# TODO:
BuildRequires: libjack-devel
BuildRequires: pkgconfig(jack)
#BuildRequires: libifp-devel

Requires: hicolor-icon-theme

%description
Aqualung is an advanced music player primarily targeted at the
GNU/Linux operating system, but also usable on FreeBSD, OpenBSD,
Cygwin and also runs natively on Microsoft Windows.

%prep
%setup
sed -i 's!/usr/lib/!%{_libdir}/!g' src/plugin.c

%build
./autogen.sh
# export CFLAGS="%optflags -Wno-error=format-truncation -Wno-error=stringop-truncation -Wno-error=format-overflow -Wno-error=stringop-overflow"
# TODO: ifp, jack
%configure \
    --without-sndio \
    --with-oss \
    --with-alsa \
    --without-jack \
    --with-pulse \
    --with-src \
    --with-sndfile \
    --with-flac \
    --with-vorbisenc \
    --with-speex \
    --with-mpeg \
    --with-mod \
    --with-mpc \
    --with-mac \
    --with-lavc \
    --with-lame \
    --with-wavpack \
    --with-ladspa \
    --with-cdda \
    --with-cddb \
    --without-ifp \
    --with-lua

%make_build

%install
%makeinstall_std
desktop-file-install --dir %buildroot%_datadir/applications %SOURCE1

for i in 16 24 32 48 64; do
  install -Dpm0644 src/img/icon_${i}.png \
    %buildroot%_datadir/icons/hicolor/${i}x${i}/apps/%name.png
done

cat <<EOF > %name.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>net.jeremyevans.aqualung</id>
    <name>Aqualung</name>
    <summary>Advanced music player</summary>
    <metadata_license>FSFAP</metadata_license>
    <project_license>GPL-2.0-or-later</project_license>
    <description>
        <p>
            Aqualung is an advanced music player originally targeted at the GNU/Linux
            operating system. It plays audio CDs, internet radio streams and pod casts as
            well as sound files in just about any audio format and has the feature of
            inserting no gaps between adjacent tracks.
        </p>
    </description>
    <launchable type="desktop-id">%name.desktop</launchable>
    <provides>
        <binary>aqualung</binary>
    </provides>
    <content_rating type="oars-1.1"/>
    <developer_name>Jeremy Evans</developer_name>
    <releases>
        <release version="%version" date="%(date +%F -r %SOURCE0)" />
    </releases>
    <screenshots>
      <screenshot type="default">
        <caption>Default skin (Music Store builder)</caption>
        <image>https://aqualung.jeremyevans.net/images/default.png</image>
      </screenshot>
      <screenshot>
        <caption>Woody skin (File Info and volume calculation)</caption>
        <image>https://aqualung.jeremyevans.net/images/woody.png</image>
      </screenshot>
      <screenshot>
        <caption>Metal skin (Playlist featuring Album mode)</caption>
        <image>https://aqualung.jeremyevans.net/images/metal.png</image>
      </screenshot>
      <screenshot>
        <caption>Dark skin (LADSPA plugin support)</caption>
        <image>https://aqualung.jeremyevans.net/images/dark.png</image>
      </screenshot>
      <screenshot>
        <caption>Plain skin (Settings dialog and album cover)</caption>
        <image>https://aqualung.jeremyevans.net/images/plain.png</image>
      </screenshot>
      <screenshot>
        <caption>Ocean skin (Search in Music Store)</caption>
        <image>https://aqualung.jeremyevans.net/images/ocean.png</image>
      </screenshot>
    </screenshots>
    <url type="homepage">%url</url>
</component>
EOF
install -D -p -m 644 %name.appdata.xml %buildroot%_datadir/metainfo/%name.appdata.xml
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%name.appdata.xml

mkdir -p %buildroot%_docdir/%name-%version/
mv %buildroot%_docdir/%name/* %buildroot%_docdir/%name-%version/
rmdir %buildroot%_docdir/%name

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING
%_bindir/%name
%_datadir/%name/
%_man1dir/%name.1*
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/metainfo/%name.appdata.xml

%changelog
* Wed Feb 26 2025 Andrew A. Vasilyev <andy@altlinux.org> 2.0-alt1
- Initial build for ALT.

