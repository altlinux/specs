Name: chrpath
Version: 0.16
Release: alt1

Summary: Dynamic library load path editor
License: GPLv2+
Group: Development/Other
Url: https://alioth.debian.org/projects/chrpath/

# https://alioth.debian.org/frs/download.php/file/3979/%name-%version.tar.gz
Source: %name-%version.tar

%description
chrpath changes, lists or removes the rpath or runpath setting in a
binary.  The rpath, or runpath if it is present, is where the runtime
linker should look for the libraries needed for a program.

%prep
%setup

%build
%{expand:%%add_optflags %(getconf LFS_CFLAGS)}
%configure
%make_build

%install
%makeinstall_std doc_DATA=

%check
%make_build check

%files
%_bindir/*
%_mandir/man?/*
%doc AUTHORS NEWS README

%changelog
* Sun Jan 17 2016 Dmitry V. Levin <ldv@altlinux.org> 0.16-alt1
- 0.13 -> 0.16.

* Fri Apr 19 2013 Dmitry V. Levin <ldv@altlinux.org> 0.13-alt2
- Merged patches from Fedora.
- Built with LFS support enabled.

* Wed Oct 06 2004 Dmitry V. Levin <ldv@altlinux.org> 0.13-alt1
- Updated to 0.13.

* Tue Dec 16 2003 Dmitry V. Levin <ldv@altlinux.org> 0.12-alt1
- Updated to 0.12.
- Fixed program return code (#3379).

* Sun Dec 01 2002 Dmitry V. Levin <ldv@altlinux.org> 0.10-alt1
- Updated to 0.10
- Run testsuit (which was added in this version).

* Tue Oct 29 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9-alt1
- Updated to 0.9

* Thu Aug 01 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
- 0.6
- Corrected manpage.

* Fri Oct 26 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.4-alt1
- 0.4

* Thu Oct 18 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.3-alt1
- Initial revision.
