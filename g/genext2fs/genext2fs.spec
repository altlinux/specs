Name: genext2fs
Version: 1.4.1
Release: alt1

Summary: genext2fs creates a virtual ext2 file system in a single file
Copyright: GPL
Group: File tools

URL: http://genext2fs.sourceforge.net/
Source: http://dl.sourceforge.net/genext2fs/genext2fs-%version.tar.gz

%description
genext2fs generates an ext2 filesystem as a normal (non-root) user. It does
not require you to mount the image file to copy files on it, nor does it
require that you become the superuser to make device nodes.

Warning! genext2fs has been designed for embedded systems. As such, it will
generate a filesystem for single-user usage: all files/directories/etc...
will belong to UID/GID 0

%prep
%setup -q

%build
CC=gcc \
%configure
%make

%install
%make_install install DESTDIR=%buildroot

%files
%doc device_table.txt
%_bindir/*
%_man8dir/*

%changelog
* Mon Jun 11 2007 Victor Forsyuk <force@altlinux.org> 1.4.1-alt1
- 1.4.1

* Fri Feb 04 2004 Alexander V. Nikolaev <avn@altlinux.org> 1.3-alt1
- Initial revision.
