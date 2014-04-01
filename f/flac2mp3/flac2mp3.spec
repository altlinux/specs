Name: flac2mp3
Version: 0.3.0
Release: alt1

Summary: Tool to convert audio files from flac to mp3 format including the copying of tags

License: GPLv2
Group: File tools
Url: http://robinbowes.github.io/flac2mp3/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# https://github.com/robinbowes/flac2mp3
Source: %name-%version.tar

# Automatically added by buildreq on Mon Mar 31 2014 (-bi)
# optimized out: perl-Encode perl-Number-Compare perl-Text-Glob python-base python3 python3-base
BuildRequires: perl-File-Find-Rule perl-File-Which perl-FreezeThaw perl-MP3-Tag perl-Parallel-ForkManager perl-Audio-FLAC-Header

Requires: flac lame

%description
flac2mp3 is a perl script that will search for flac files
within a directory hierarchy and convert them all to mp3 format,
creating a matching directory structure in the process.

%prep
%setup

%install
install -D %name.pl %buildroot%_bindir/%name

%files
%doc changelog.txt readme.txt todo.txt
%_bindir/%name

%changelog
* Mon Mar 31 2014 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- initial build for ALT Linux Sisyphus
