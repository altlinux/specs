Name: cue2tracks
Version: 0.2.17
Release: alt1

Summary: Tool for splitting audio CD image to tracks with cue sheet info

License: GPLv2
Group: File tools
Url: https://github.com/ar-lex/cue2tracks

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Autoreq: yes, noshell

# Source-url: https://github.com/ar-lex/cue2tracks/archive/v%version.tar.gz
Source: %name-%version.tar

%description
Tool for splitting audio CD image to tracks with cue sheet info.

%prep
%setup

%install
install -D %name %buildroot%_bindir/%name

%files
%doc AUTHORS README TODO
%_bindir/%name

%changelog
* Fri Jun 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.17-alt1
- new version 0.2.17 (with rpmrb script)

* Mon Mar 31 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2.16-alt1
- initial build for ALT Linux Sisyphus
