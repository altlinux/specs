Name: unionfs_utils
Version:       0.2.1
License:       GPL
Group: 	       System/Kernel and hardware
Release:       alt1
Source0:       %name-%version.tar
URL:	       http://www.fsl.cs.sunysb.edu/project-unionfs.html
Summary:       Utilities to operate w/ unionfs
Conflicts: unionfs-utils

BuildRequires: glibc-devel-static libuuid-devel

%description
Unionfs is a stackable unification file system, which can appear to
merge the contents of several directories (branches), while keeping
their physical content separate.  Unionfs is useful for unified source
tree management, merged contents of split CD-ROM, merged separate
software package directories, data grids, and more.  Unionfs allows
any mix of read-only and read-write branches, as well as insertion and
deletion of branches anywhere in the fan-out.  To maintain Unix
semantics, Unionfs handles elimination of duplicates, partial-error
conditions, and more.  This release also includes additional
preliminary features that were specifically designed for security
applications, such as snapshotting and sandboxing.

unionctl is used to control a unionfs file system.
uniondbg  runs  unionfs  debugging ioctls.

%prep
%setup -q

%build
%__autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README 
%_sbindir/*
%_mandir/man8/*

%changelog
* Tue Mar 11 2008 Anton Farygin <rider@altlinux.ru> 0.2.1-alt1
- first build new generation of unionfs_utils for Sisyphus


