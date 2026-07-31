%define ffmpeg_tag 2c92585
%define ffmpeg_version 7.1.2

Name: sharpemu
Version: 0.0.3
Release: alt1

Summary: PlayStation 5 emulator
License: GPL-2.0-or-later
Group: Emulators

Url: https://github.com/sharpemu/sharpemu
Vcs: https://github.com/sharpemu/sharpemu
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/sharpemu/sharpemu/archive/v%version/sharpemu-%version.tar.gz
Source0: %name-%version.tar
# Pre-cached NuGet packages (created on a machine with network access)
Source1: packages.tar
# https://ffmpeg.org/releases/ffmpeg-%ffmpeg_version.tar.xz
Source2: ffmpeg-%ffmpeg_version.tar
Source3: %name.desktop
# https://github.com/sharpemu/ffmpeg-core/raw/%ffmpeg_tag/bink2.patch
Patch0: bink2.patch

BuildRequires: /proc
BuildRequires: dotnet-sdk-10.0
BuildRequires: zip

%description
SharpEmu is a PlayStation 5 emulator for Windows, Linux and macOS written in C#.
It uses AOT compilation and high-level emulation to run PS5 games.

%add_findreq_skiplist %_libexecdir/%name/plugins/*

%prep
%setup -n %name-%version -a 1 -b 2
%patch0 -p1 -d ../ffmpeg-%ffmpeg_version

%build
# Build FFmpeg with only the codecs used by SharpEmu
pushd ../ffmpeg-%ffmpeg_version
./configure \
    --prefix=%_prefix \
    --libdir=%_libdir \
    --enable-shared \
    --disable-static \
    --enable-pic \
    --disable-gpl \
    --disable-nonfree \
    --disable-version3 \
    --disable-doc \
    --disable-asm \
    --disable-x86asm \
    --disable-autodetect \
    --disable-everything \
    --enable-decoder=aac,aac_latm,atrac3,atrac3p,atrac9,bink,bink2,binkaudio_dct,binkaudio_rdft,mp3,pcm_s16le,pcm_s8,h264,hevc,mpeg4,mpeg2video,mjpeg,mjpegb \
    --enable-encoder=pcm_s16le,ffv1,mpeg4,ljpeg,mjpeg \
    --enable-muxer=avi \
    --enable-demuxer=bink,h265,h264,m4v,mp3,mpegvideo,mpegps,mjpeg,mov,avi,aac,pmp,oma,pcm_s16le,pcm_s8,wav \
    --enable-parser=h264,hevc,mpeg4video,mpegaudio,mpegvideo,mjpeg,aac,aac_latm \
    --enable-protocol=file \
    --enable-bsf=mjpeg2jpeg
%make_build
popd

# Build SharpEmu
dotnet restore SharpEmu.slnx --packages .packages -p:NuGetAudit=false
dotnet build SharpEmu.slnx -c Release --no-restore

%check
dotnet test SharpEmu.slnx -c Release --no-build --verbosity normal

%install
# Install FFmpeg to buildroot
pushd ../ffmpeg-%ffmpeg_version
%makeinstall_std
popd

# Pack FFmpeg shared libraries into zip for MSBuild to skip download
FFMPEG_RUNTIME=artifacts/obj/SharpEmu.CLI/ffmpeg-runtime/%ffmpeg_tag/linux-x64
%__mkdir_p $FFMPEG_RUNTIME
zip -j $FFMPEG_RUNTIME/ffmpeg-linux-x64.zip %buildroot%_libdir/libavcodec.so* %buildroot%_libdir/libavformat.so* %buildroot%_libdir/libavutil.so* %buildroot%_libdir/libswscale.so* %buildroot%_libdir/libswresample.so* %buildroot%_libdir/libavfilter.so*

# Build and publish SharpEmu
dotnet publish src/SharpEmu.CLI/SharpEmu.CLI.csproj -c Release --self-contained true -r linux-x64 --no-restore

# Copy FFmpeg shared libraries into plugins directory
%__mkdir_p artifacts/publish/SharpEmu.CLI/Release/net10.0/linux-x64/plugins
%__cp -a %buildroot%_libdir/libavcodec.so* artifacts/publish/SharpEmu.CLI/Release/net10.0/linux-x64/plugins/
%__cp -a %buildroot%_libdir/libavformat.so* artifacts/publish/SharpEmu.CLI/Release/net10.0/linux-x64/plugins/
%__cp -a %buildroot%_libdir/libavutil.so* artifacts/publish/SharpEmu.CLI/Release/net10.0/linux-x64/plugins/
%__cp -a %buildroot%_libdir/libswscale.so* artifacts/publish/SharpEmu.CLI/Release/net10.0/linux-x64/plugins/
%__cp -a %buildroot%_libdir/libswresample.so* artifacts/publish/SharpEmu.CLI/Release/net10.0/linux-x64/plugins/
%__cp -a %buildroot%_libdir/libavfilter.so* artifacts/publish/SharpEmu.CLI/Release/net10.0/linux-x64/plugins/

# Clean up FFmpeg install from buildroot
%__rm -rf %buildroot%_libdir/libavcodec*
%__rm -rf %buildroot%_libdir/libavformat*
%__rm -rf %buildroot%_libdir/libavutil*
%__rm -rf %buildroot%_libdir/libavdevice*
%__rm -rf %buildroot%_libdir/libavfilter*
%__rm -rf %buildroot%_libdir/libswscale*
%__rm -rf %buildroot%_libdir/libswresample*
%__rm -rf %buildroot%_includedir/libav*
%__rm -rf %buildroot%_includedir/libsw*
%__rm -rf %buildroot%_libdir/pkgconfig/libav*
%__rm -rf %buildroot%_libdir/pkgconfig/libsw*
%__rm -rf %buildroot%_bindir/ff*
%__rm -rf %buildroot%_datadir/ffmpeg
%__rm -rf %buildroot%_mandir

# Install SharpEmu
%__mkdir_p %buildroot%_libexecdir/%name
%__cp -a artifacts/publish/SharpEmu.CLI/Release/net10.0/linux-x64/* %buildroot%_libexecdir/%name/
%__rm -rf %buildroot%_libexecdir/%name/LICENSE.txt
%__rm -rf %buildroot%_libexecdir/%name/licenses

%__mkdir_p %buildroot%_bindir
%__ln_s %_libexecdir/%name/SharpEmu %buildroot%_bindir/%name

%__install -Dm644 %SOURCE3 %buildroot%_desktopdir/%name.desktop
%__install -Dm644 assets/images/logo.png %buildroot%_pixmapsdir/%name.png

%files
%doc LICENSE.txt README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%dir %_libexecdir/%name
%_libexecdir/%name/plugins
%_libexecdir/%name/SharpEmu

%changelog
* Sat Aug 01 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.3-alt1
- Initial build for ALT Linux
