%define ShortName TimedMediaHandler

Name: mediawiki-extensions-%ShortName
Version: 0.4.0
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Mediawiki extension for isplay audio and video files in wiki pages
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL2

BuildPreReq: rpm-build-mediawiki >= 0.2
BuildPreReq: rpm-build-intro
Requires: mediawiki-common >= 1.15.1-alt4

Requires: mediawiki-extensions-MwEmbedSupport >= 0.3.0

AutoReq:yes,noosgi
AutoProv:yes,noosgi
# fixme
#add_findprov_skiplist /usr/share/mediawiki/extensions/TimedMediaHandler/MwEmbedModules/EmbedPlayer/binPlayers/cortado/

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://git.wikimedia.org/zip/?r=mediawiki/extensions/%ShortName&h=REL1_23&format=zip
Source: %name-%version.tar

%description
The TimedMediaHandler extension allows you to display
audio and video files in wiki pages, using the same syntax
as for image files. It includes the Kaltura HTML5 Player,
which supports integrated standard timed text support,
real time stream switching between multiple WebM and Ogg
derivatives and many other features.
TMH server side support includes multiple transcode profiles,
php based medata parsing via PEAR Ogg / OggHandler and getID3
for WebM files, and integrates with mediaWiki's jobQueue system
for scheduling transcoding jobs.

%prep
%setup
%remove_repo_info

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files

%changelog
* Fri Oct 10 2014 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus
