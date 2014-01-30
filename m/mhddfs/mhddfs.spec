Name: mhddfs
Version: 0.1.39
Release: alt1

Summary: file system for unifying several mount points into one
License: GPLv3
Group: File tools

Url: http://mhddfs.uvw.ru
Packager: Evgenii Terechkov <evg@altlinux.org>

Source: %name-%version.tar

BuildRequires: libfuse-devel libattr-devel libuthash-devel

%description
This FUSE-based file system allows mount points (or directories) to be
combined, simulating a single big volume which can merge several hard
drives or remote file systems. It is like unionfs, but can choose the
drive with the most free space to create new files on, and can move
data transparently between drives.

%prep
%setup

%build
%make_build

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/*
%_man1dir/%name.*
%doc ChangeLog README*

%changelog
* Thu Jan 30 2014 Evgenii Terechkov <evg@altlinux.org> 0.1.39-alt1
- 0.1.39

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.37-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Aug 06 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1.37-alt1
- 0.1.37 (Closes: #23856).

* Wed Oct 15 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1.13-alt1
- 0.1.13.

* Thu Sep 18 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1.12-alt1
- Initial build for ALT Linux.
