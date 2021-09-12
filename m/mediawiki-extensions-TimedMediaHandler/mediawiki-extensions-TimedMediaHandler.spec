%define ShortName TimedMediaHandler

Name: mediawiki-extensions-%ShortName
Version: 1.36
Release: alt1

Summary: Mediawiki extension for isplay audio and video files in wiki pages

License: GPLv2
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

BuildArch: noarch

%setup_mediawiki_ext %version %ShortName

# Source-url: https://gerrit.wikimedia.org/r/plugins/gitiles/mediawiki/extensions/TimedMediaHandler/+archive/refs/heads/%MWREL.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-mediawiki >= 0.2
BuildRequires(pre): rpm-build-intro

Requires: mediawiki-common >= %mwversion

AutoReq:yes,noosgi
AutoProv:yes,noosgi


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
* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 1.36-alt1
- switch to build according to MW version

* Mon Sep 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Fri Oct 10 2014 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus
