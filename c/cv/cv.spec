Name: cv
Version: 0.3
Release: alt1

Summary: Coreutils Viewer
License: GPLv3+
Group: Text tools

Url: https://github.com/Xfennec/cv
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

%description
This tool can be described as a Tiny Dirty Linux Only C command
that looks for coreutils basic commands (cp, mv, dd, tar,
gzip/gunzip, cat, ...) currently running on your system and
displays the percentage of copied data.

It simply scans /proc for interesting commands, and then use fd/
and fdinfo/ directories to find opened files and seek position,
and reports status for the biggest file.

It's very light, and compatible with virtually any command.

%prep
%setup

%build
%make_build

%install
install -pDm755 %name %buildroot%_bindir/%name

%files
%_bindir/*
%doc README.md

%changelog
* Mon Jul 14 2014 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- initial release (thx Kirill Kolyshkin for a pointer)

