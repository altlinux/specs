Name: start-or-find-x
Version: 1.0
Release: alt1

Summary: Start new X session, or preferably find a running one
License: Public domain
Group: System/X11

Url: http://git.altlinux.org/people/mike/packages/?p=start-or-find-x.git
Source0: start-or-find-x.sh
Source1: README
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
This script would try its best to:
- either switch to the first user's X session running;
- or start a new one.

If started or sourced from a shell with display available,
just fast-forward to a shell.

It was written in (and for) home environment where a family
would use the same system and sometimes one might end up with
several sessions fired up and a hard time to find which one
was the needed one; now you can just source this script at 
the end of corresponding shell profile files to get things
going along nicely.

%prep

%install
install -pD -m755 %SOURCE0 %buildroot%_bindir/%name
cp -a %SOURCE1 .

%files
%_bindir/*
%doc README

%changelog
* Wed Apr 16 2008 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- initial release

