Name:          file5
Version:       5.36
Release:       alt1
Summary:       An utility for determining file types
Summary(ru_RU.UTF-8): Утилита для определения типов файлов
License:       BSD-style
Group:         File tools
Url:           http://www.darwinsys.com/file/
# VCS:         https://github.com/file/file.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Patch:         rename-misc-to-file5.patch
BuildRequires(pre): zlib-devel

%description
The file command is "a file type guesser", that is, a command-line tool that
tells you in words what kind of data a file contains. Unlike most GUI systems,
command-line UNIX systems - with this program leading the charge - don't rely on
filename extentions to tell you the type of a file, but look at the file's
actual contents. This is, of course, more reliable, but requires a bit of I/O.

The original file command shipped with Bell Labs UNIX (here is a man page from
Research 4th Edition, 1973, obtained from the PDP-11 Unix Preservation Society),
but was unavailable in source form to the masses before Ian's reimplementation.

This file command (and magic file) was originally written by Ian Darwin (who
still contributes occasionally) and is now maintained by a group of developers
lead by Christos Zoulas. Announcements of new releases are made on the "file"
mailing list.


%prep
%setup
%patch -p1

%build
%autoreconf
%configure --enable-static --disable-shared --program-suffix=5
%make

%install
%makeinstall_std
rm %buildroot%_includedir/*
rm %buildroot%_libdir/*

%check
%make -k check

%files
%_bindir/%name
%_datadir/%name/magic.mgc
%_man1dir/*
%_man3dir/*
%_man4dir/*
%doc COPYING MAINT README

%changelog
* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 5.36-alt1
- New file5 package based on original file.
