Name: nettee
Version: 0.1.9.1
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: nettee is a network "tee" program
License: GPLv2+
Group: Networking/Other

Url: http://saf.bio.caltech.edu/nettee.html
Source: http://saf.bio.caltech.edu/pub/software/linux_or_unix_tools/nettee-%version.tar.gz
Patch1: nettee-0.1.9.1-openoptions.patch

%description
nettee is a network "tee" program. It can typically transfer data between N nodes
at (nearly) the full bandwidth provided by the switch which connects them. It is
handy for cloning nodes or moving large database files.

%prep
%setup
%patch1 -p1

%build
rm -f nettee
%__cc %optflags -D_LARGEFILE64_SOURCE -o nettee nettee.c

%install
install -Dp -m 0755 nettee %buildroot%_bindir/nettee
install -Dp -m 0644 nettee.1 %buildroot%_man1dir/nettee.1

%files
%_bindir/*
%_man1dir/*

%changelog
* Sat Jul 25 2009 Victor Forsyuk <force@altlinux.org> 0.1.9.1-alt1
- Initial build.
