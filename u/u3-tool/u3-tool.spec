Name: u3-tool
Version: 0.3
Release: alt1

Summary:  U3 Flash disk feature control tool
License: GPLv2+
Group: System/Kernel and hardware

Url: http://sourceforge.net/projects/u3-tool/
Source: %name-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

%description
A tool for controlling the special features
of a "U3 smart drive" USB Flash disk, e.g.
SanDisk Cruzer and some others.

This program can:
* just remove CD part (freeing up ~6MB)
* replace CD image
* change virtual CD allocated size and completely remove it
* enable and disable U3 security
* destroy or change password of a secured U3 device
* obtain various device information

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_sbindir/*
%_man1dir/*
%doc AUTHORS ChangeLog README TODO

%changelog
* Wed Aug 25 2010 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- built for ALT Linux

