%define oname TimedMediaHandler
%define mwversion 1.46
%define commit 632d48c
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: MediaWiki extension to display audio and video files in wiki pages

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7
Obsoletes: mediawiki-extensions-MwEmbedSupport < 0.3.0-alt2

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

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
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,jsdoc.json,composer.lock}
# no transcoding without ffmpeg configured by the administrator
echo '$wgEnableTranscode = false;' >> %buildroot%_mediawiki_settings_dir/50-%oname.php

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- update to REL1_46 snapshot 632d48c (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- version follows the MediaWiki version (extension.json says 0.6.0)
- the snapshot has vendor/getid3 (the old package had none)
- disable transcoding in the package config ($wgEnableTranscode = false)
- Obsoletes: mediawiki-extensions-MwEmbedSupport (merged into TimedMediaHandler)
- dropped BuildRequires: rpm-build-intro (no %%remove_repo_info: the snapshot has no repo info)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 1.36-alt1
- switch to build according to MW version

* Mon Sep 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Fri Oct 10 2014 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus
