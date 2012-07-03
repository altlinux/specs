Name: magicrescue
Version: 1.1.9
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Magic Rescue is a file carving tool that uses "magic bytes" in a file contents to recover data
License: GPLv2+
Group: Text tools

Url: http://www.student.dtu.dk/~s042078/magicrescue
Source: http://www.itu.dk/people/jobr/magicrescue/release/magicrescue-%version.tar.gz
Source1: magicrescue-rar-recipe

# Automatically added by buildreq on Mon Nov 16 2009
BuildRequires: libdb4-devel libgdbm-devel

%description
Magic Rescue scans a block device for file types it knows how to recover and
calls an external program to extract them. It looks at "magic bytes" in file
contents, so it can be used both as an undelete utility and for recovering a
corrupted drive or partition. As long as the file data is there, it will find
it.

It works on any file system, but on very fragmented file systems it can only
recover the first chunk of each file. Practical experience (this program was not
written for fun) shows, however, that chunks of 30-50MB are not uncommon.

%prep
%setup

%build
cp %SOURCE1 recipes/rar
subst 's@)/man/man1@)/share/man/man1@g' Makefile.in
subst 's@$(PREFIX)/share/magicrescue/tools@%buildroot%_libdir/magicrescue@g' Makefile.in
subst 's@prefix/share/magicrescue/tools@%_libdir/magicrescue@' config.d/80magicrescue_defs

%define _optlevel 3
./configure --prefix=/usr CFLAGS="%optflags"
%make_build

%install
install -d %buildroot/usr
%make_install PREFIX=%buildroot/usr install

# Due to usage of perl module that is not yet in repo...
rm -f %buildroot%_libdir/magicrescue/gimp-resave.pl

%files
%_bindir/*
%_datadir/magicrescue
%_libdir/magicrescue
%_man1dir/*

%changelog
* Wed Jun 16 2010 Victor Forsiuk <force@altlinux.org> 1.1.9-alt1
- 1.1.9
- Add recipe for rar archives (upstream forgot to add it to tarball).

* Mon Nov 16 2009 Victor Forsyuk <force@altlinux.org> 1.1.8-alt1
- Initial build.
