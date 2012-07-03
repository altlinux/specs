Name: txt2man
Version: 1.5.6
Release: alt1
Summary: Convert flat ASCII text to man page format

Group: Text tools
License: GPLv2+
Url: http://mvertes.free.fr/txt2man/
Source0: http://mvertes.free.fr/download/%name-%version.tar.gz
#Fixes bug with bashisms in /bin/sh script, see http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=473696
#Patch0:         txt2man-1.5.5-fixbashisms.patch

# Fixes same bug as above, but code was changed in new release so old patch
# no longer worked.
Patch1: txt2man-1.5.6-fixbashisms.patch
Patch2: txt2man-1.5.6-alt-Makefile.patch

BuildArch: noarch

%description
tx2man is a shell script using gnu awk, that should run on any
Unix-like system. The syntax of the ASCII text is very straightforward
and looks very much like the output of the man(1) program.

%prep
%setup
#patch0 -p1
%patch1
%patch2 -p2

%build
#no build needed

%install
%makeinstall

%files
%doc COPYING Changelog README
%_bindir/*
%_man1dir/*

%changelog
* Tue Aug 30 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.6-alt1
- Initial build from Fedora

