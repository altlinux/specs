%define defphp php%php_defver

Name: m4b-tool
Version: 0.5.2
Release: alt1

Summary: m4b-tool is a command line utility to merge, split and chapterize audiobook files such as mp3, ogg, flac, m4a or m4b

License: MIT
Group: File tools
Url: https://github.com/sandreas/m4b-tool

# Source-url: https://github.com/sandreas/m4b-tool/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar
Source2: box.phar
Source3: composer.phar


Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-features >= 0.8
BuildRequires(pre): rpm-build-php >= 8.4

#composer
# fdkaac
BuildRequires: ffmpeg mp4v2-utils git-core
BuildRequires: /usr/bin/php
BuildRequires: %defphp-intl %defphp-mbstring %defphp-zip %defphp-curl %defphp-dom %defphp-simplexml %defphp-openssl

Requires: %defphp-intl %defphp-mbstring
Requires: ffmpeg mp4v2-utils

%description
m4b-tool is a is a wrapper for ffmpeg and mp4v2 to merge,
split or and manipulate audiobook files with chapters.
Although m4b-tool is designed to handle m4b files,
nearly all audio formats should be supported, e.g. mp3, aac, ogg, alac and flac.

%prep
%setup -a1

# Build need git repo
git init
git config user.email "you@example.com"
git config user.name "Your Name"
git add .
git commit -am "Fix for build"
git tag "%version"

%build
echo "Generating PHAR ..."
cp %SOURCE3 composer.phar
chmod +x composer.phar
php -d phar.readonly=off %SOURCE2 compile --composer-bin=./composer.phar

%install
mkdir -p %buildroot/%_bindir/
install -m755 dist/m4b-tool.phar %buildroot%_bindir/%name

#check
#test "$(%buildroot%_bindir/wp cli version)" = "m4b-tool %version"

%files
%_bindir/%name

%changelog
* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2
- fix Source-url tag format
- remove obsolete patch
- use external box.phar for PHAR building

* Sun Feb 02 2025 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt5
- use php_defver

* Sat Aug 12 2023 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt4
- use php8.1 if php7.4 is missed

* Fri May 28 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt3
- add patch fix issue https://github.com/sandreas/m4b-tool/issues/47
- add Requires: ffmpeg mpeg4ip-tools

* Fri Feb 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt2
- fix vendor dir packing

* Wed Jan 20 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- initial build for ALT Sisyphus
