%define oname FlashMP3
%define major 1.15
%define revision 0.91

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: FlashMP3 embeds a simple Flash-player for playback of mp3-files
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: mediawiki-common >= 1.15.1-alt4

# http://www.mediawiki.org/wiki/Extension:%oname
# http://wordpress.org/extend/plugins/audio-player/
Source0: %oname-%version.tar

%description
FlashMP3 embeds a simple Flash-player for playback of
mp3-files. It is based on the great Audio Player Wordpress plugin by
1pixelout. It can handle multiple local and/or remote files in one
player and multiple players on each site. The appearance of the player
is highly customizable. It is also possible to use the nice last.fm
player with the files hosted there. It works on a label, artist, album
or song-level.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Sat May 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.0.91-alt1
- initial build for ALT Linux Sisyphus

