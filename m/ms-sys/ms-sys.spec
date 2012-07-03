Name: ms-sys
Version: 2.1.4
Release: alt1

Summary: Linux program for writing Microsoft compatible boot records.
License: GPL
Group: System/Configuration/Hardware

Packager: Alexey Gladkov <legion@altlinux.ru>

URL: http://ms-sys.sourceforge.net/
Source: %name-%version.tar

BuildRequires: gettext-tools

%description
Linux program for writing Microsoft compatible boot records. This program does the same as Microsoft "fdisk /mbr" to a
hard disk or "sys d:" to a floppy or FAT32 partition except that it does not copy any system files, only the boot
record is written

%prep
%setup -q

%build
%make_build

%install
mkdir -p %buildroot
%make_install \
	PREFIX=%buildroot/%prefix \
	MANDIR=%buildroot/%_mandir \
	install
%find_lang %name

%files -f %name.lang
%_bindir/*
%_mandir/man?/*
%doc CHANGELOG CONTRIBUTORS COPYING README TODO

%changelog
* Tue Oct 06 2009 Alexey Gladkov <legion@altlinux.ru> 2.1.4-alt1
- New version (2.1.4).

* Tue Dec 20 2005 Dimitry V. Ketov <dketov@altlinux.ru> 2.0.0-alt2
- %find_lang macro usage fix

* Mon Dec 20 2004 Dimitry V. Ketov <dketov@altlinux.ru> 2.0.0-alt1
- First release for Sisyphus
