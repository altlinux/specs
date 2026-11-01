%define ffmpeg_tag e95fc79
%define ffmpeg_version 7.1.2

# ALT release suffix (e.g. .release.4, .hotfix.2, .rc1).
# Set to %nil when the upstream version has no suffix.
%define version_suffix .pulse
# Upstream tag/source-tarball suffix, dash-separated (e.g. -release.4, -hotfix.2, -rc1).
# Set to %nil when the upstream version has no suffix.
%define upstream_suffix -pulse

Name: sharpemu
Version: 0.0.7
Release: alt2%{version_suffix}

Summary: PlayStation 5 emulator
License: GPL-2.0-or-later
Group: Emulators

Url: https://%name.app
Vcs: https://github.com/sharpemu/sharpemu
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/sharpemu/sharpemu/archive/v%version%{upstream_suffix}/%name-%version%{upstream_suffix}.tar.gz
Source0: %name-%version%{upstream_suffix}.tar
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
# libSkiaSharp (published from the NuGet cache into runtimes/linux-x64/native)
# links against system fontconfig and harfbuzz; the test suite loads it and
# renders system fonts, so a fontconfig setup with a real font is needed as well.
BuildRequires: libfontconfig1
BuildRequires: fontconfig
BuildRequires: fonts-ttf-dejavu
BuildRequires: libharfbuzz
# Framework-dependent build: run on the system .NET runtime instead of
# embedding Microsoft's prebuilt one from the NuGet cache (ALT #61284).
# The apphost resolves the runtime from DOTNET_ROOT, /etc/dotnet/install_location*
# or /usr/share/dotnet, but ALT installs dotnet into %_libdir/dotnet, hence
# the DOTNET_ROOT wrapper in the file section.
Requires: dotnet-runtime-10.0
# find-requires now sees the NEEDED entries of the published native libraries,
# but keep them explicit as a safety net against resolver/skiplist changes.
Requires: libfontconfig1
Requires: libharfbuzz

%description
SharpEmu is a PlayStation 5 emulator for Windows, Linux and macOS written in C#.
It uses AOT compilation and high-level emulation to run PS5 games.

%add_findreq_skiplist %_libexecdir/%name/plugins/*

%prep
%setup -n %name-%version%{upstream_suffix} -a 1 -b 2
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
    --enable-decoder=aac,aac_latm,atrac3,atrac3p,atrac9,bink,bink2,binkaudio_dct,binkaudio_rdft,mp3,opus,pcm_s16le,pcm_s8,h264,hevc,mpeg4,mpeg2video,mjpeg,mjpegb \
    --enable-encoder=pcm_s16le,ffv1,mpeg4,ljpeg,mjpeg \
    --enable-muxer=avi \
    --enable-demuxer=bink,h265,h264,m4v,mp3,mpegvideo,mpegps,mjpeg,mov,avi,aac,pmp,oma,pcm_s16le,pcm_s8,wav \
    --enable-parser=h264,hevc,mpeg4video,mpegaudio,mpegvideo,mjpeg,aac,aac_latm \
    --enable-protocol=file \
    --enable-bsf=mjpeg2jpeg
%make_build
popd

# Pack FFmpeg shared libraries into zip for MSBuild to skip download.
# Must exist before "dotnet build": since v0.0.3-release.4 the project
# fetches this archive in both Build and Publish targets.
FFMPEG_RUNTIME=artifacts/obj/SharpEmu.CLI/ffmpeg-runtime/%ffmpeg_tag/linux-x64
%__mkdir_p $FFMPEG_RUNTIME
zip -j $FFMPEG_RUNTIME/ffmpeg-linux-x64.zip \
    ../ffmpeg-%ffmpeg_version/libavcodec/libavcodec.so* \
    ../ffmpeg-%ffmpeg_version/libavformat/libavformat.so* \
    ../ffmpeg-%ffmpeg_version/libavutil/libavutil.so* \
    ../ffmpeg-%ffmpeg_version/libswscale/libswscale.so* \
    ../ffmpeg-%ffmpeg_version/libswresample/libswresample.so* \
    ../ffmpeg-%ffmpeg_version/libavfilter/libavfilter.so*

# Build SharpEmu
# Framework-dependent restore: foreign-RID runtime/host packs are pruned from
# the NuGet cache. The linux-x64 runtime packs stay because upstream's
# Directory.Build.props pins RuntimeIdentifier for the CLI project, so restore
# resolves them into the lock file — but nothing from them is published: the
# app runs on the system dotnet-runtime-10.0. The linux-x64 apphost pack ships
# inside the SDK itself.
dotnet restore SharpEmu.slnx --packages .packages -r linux-x64 -p:SelfContained=false -p:NuGetAudit=false
dotnet build SharpEmu.slnx -c Release --no-restore

%check
dotnet test SharpEmu.slnx -c Release --no-build --verbosity normal

%install
# Install FFmpeg to buildroot
pushd ../ffmpeg-%ffmpeg_version
%makeinstall_std
popd

# Build and publish SharpEmu
# Framework-dependent: no runtime is embedded (Requires: dotnet-runtime-10.0);
# PublishSingleFile is disabled as well, so the native libraries stay plain
# files and their dependencies are visible to find-requires.
dotnet publish src/SharpEmu.CLI/SharpEmu.CLI.csproj -c Release --self-contained false -r linux-x64 -p:PublishSingleFile=false --no-restore

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
%__cat > %buildroot%_bindir/%name <<'EOF'
#!/bin/sh
# The apphost resolves the runtime from DOTNET_ROOT, /etc/dotnet/install_location*
# or /usr/share/dotnet; ALT installs .NET into %_libdir/dotnet.
DOTNET_ROOT=%_libdir/dotnet
export DOTNET_ROOT
exec %_libexecdir/%name/SharpEmu "$@"
EOF
chmod +x %buildroot%_bindir/%name

%__install -Dm644 %SOURCE3 %buildroot%_desktopdir/%name.desktop
%__install -Dm644 assets/images/logo.png %buildroot%_pixmapsdir/%name.png

%files
%doc LICENSE.txt README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_libexecdir/%name/

%changelog
* Sun Nov 01 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.7-alt2.pulse
- Build framework-dependent against the system dotnet-runtime-10.0 instead of
  embedding Microsoft's prebuilt runtime from the NuGet cache (closes: #61284)

* Sun Nov 01 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.7-alt1.pulse
- Update to v0.0.7-pulse
- Drop the user data directory patch: accepted upstream (PR #1108)

* Mon Oct 19 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.6-alt2.mono
- Update the user data directory patch: also route the trophy cache, game
  art cache, .zar cache and downloaded game patches there

* Mon Oct 19 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.6-alt1.mono
- Update to v0.0.6-mono
- Enable FFmpeg built-in Opus decoder (AJM audio jobs, ffmpeg-core e95fc79)

* Sun Oct 18 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.5-alt2.nexus.release.2
- Store user-writable data (settings, caches, saves, logs) in the XDG data
  directory on Linux instead of the read-only install directory

* Fri Oct 09 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.5-alt1.nexus.release.2
- Update to v0.0.5-nexus-release.2

* Sat Oct 03 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.5-alt1.nexus
- Update to v0.0.5-nexus
- Fix Url tag (point to sharpemu.app)
- Add missing fontconfig and harfbuzz dependencies (new SkiaSharp runtime)

* Sat Sep 26 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.4-alt1.release.2
- Update to v0.0.4-release.2

* Tue Sep 22 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.4-alt1
- Update to v0.0.4

* Sat Sep 19 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.3-alt1.release.4
- Update to v0.0.3-release.4

* Sat Aug 01 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.3-alt1
- Initial build for ALT Linux
