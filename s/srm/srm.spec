Name: srm
Version: 1.2.11
Release: alt1
License: X11
Url: http://srm.sourceforge.net
Group: File tools

Source: %name-%version.tar.bz2

Summary: srm (secure rm) is a command-line compatible rm(1) which overwrites file contents before unlinking

%description
This is srm, a secure replacement for rm(1). Unlike the standard rm,
it overwrites the data in the target files before unlinking them. This
prevents recovery of the data by examining the raw block device. It
may also help frustrate physical examination of the disk, although
it's unlikely that it completely protects against this type of
recovery.

%prep
%setup
%autoreconf
%configure

%build
%make_build

%install
%makeinstall_std

%check
make test

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%_bindir/*
%_man1dir/*

%changelog
* Wed Feb 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.11-alt1
- Build for ALT
