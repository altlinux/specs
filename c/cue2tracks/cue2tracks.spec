Name: cue2tracks
Version: 0.2.16
Release: alt1

Summary: Tool for splitting audio CD image to tracks with cue sheet info

License: GPLv2
Group: File tools
Url: http://code.google.com/p/cue2tracks/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# FIXME:
# /usr/bin/cue2tracks: line 1798: syntax error near unexpected token `}'
Autoreq: yes, noshell

Source: https://cue2tracks.googlecode.com/files/%name-%version.tar

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
* Mon Mar 31 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2.16-alt1
- initial build for ALT Linux Sisyphus
