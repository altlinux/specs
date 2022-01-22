Name: genext2fs
Version: 1.5.0
Release: alt2
Summary: genext2fs creates a virtual ext2 file system in a single file
License: GPL-2.0
Group: File tools
URL: https://github.com/bestouff/genext2fs
Source: %name-%version.tar

%description
genext2fs generates an ext2 filesystem as a normal (non-root) user. It does not
require you to mount the image file to copy files on it, nor does it require that
you become the superuser to make device nodes.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc AUTHORS README.md TODO device_table.txt
%_bindir/*
%_man8dir/*

%changelog
* Sat Jan 22 2022 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt2
- enable check

* Mon Aug 10 2020 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt1
- 1.5.0
- Fix License tag
- Update URL tag
- Cleaned up spec

* Sat Aug 10 2013 Led <led@altlinux.ru> 1.4.1-alt2
- cleaned up spec
- updates and fixes of upstream's SCM

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Jun 11 2007 Victor Forsyuk <force@altlinux.org> 1.4.1-alt1
- 1.4.1

* Fri Feb 04 2004 Alexander V. Nikolaev <avn@altlinux.org> 1.3-alt1
- Initial revision.
