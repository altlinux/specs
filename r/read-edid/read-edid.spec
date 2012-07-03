Name: read-edid
Version: 2.0.0
Release: alt2
Group: System/Configuration/Other
License: GPL
Packager: Vladislav Zavjalov <slazav@altlinux.org>

Summary: Get monitor details

URL: http://polypux.org/projects/read-edid/

Source0: %name-%version.tar

# Automatically added by buildreq on Tue Sep 23 2008
BuildRequires: libx86-devel

%description
This package will try to read the monitor details directly from the
monitor. The program get-edid asks a VBE BIOS for the EDID data. The
program parse-edid parses the data and prints out a human readable
summary.

%prep
%setup

%build
%autoreconf
%configure
%make

%install
%makeinstall

%files
%_man1dir/*
%_sbindir/*

%changelog
* Tue Sep 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.0.0-alt2
- change Packager, rebuild with new libx86

* Tue Sep 23 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0-alt1
- New version (2.0.0).
- The lrmi code has been replaced by libx86 code.

* Tue Jul 17 2007 Alexey Gladkov <legion@altlinux.ru> 1.4.1-alt1
- First build for ALT Linux.
