Name: e2fsimage
Version: 0.2.2
Release: alt2
Summary: Create and populate an ext2 filesystem image as non-root user
License: %bsdstyle
Group: System/Kernel and hardware
URL: http://sourceforge.net/projects/%name
Source0: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.org>

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu Feb 21 2008
BuildRequires: libe2fs-devel

%description
%name creates an ext2 filesystem image by recursively copying the
files from the existing directory structure rootdir to the image-file.
Supported filetypes are: regular files, directorys, hard-links,
soft-links, block special devices, character special devices and fifos.


%prep
%setup
%patch -p1


%build
export prefix=%_prefix CFLAGS="%optflags"
./configure
%make_build


%install
install -d -m 0755 %buildroot{%_bindir,%_man1dir}
install -m 0755 src/%name %buildroot%_bindir/
gzip -dc man/%name.1.gz > %buildroot%_man1dir/%name.1


%files
%doc AUTHORS CHANGELOG COPYRIGHT
%_bindir/*
%_man1dir/*


%changelog
* Mon Nov 03 2008 Led <led@altlinux.ru> 0.2.2-alt2
- cleaned up spec

* Thu Feb 21 2008 Led <led@altlinux.ru> 0.2.2-alt1
- 0.2.2
- cleaned up spec
- fixed URL
- updated:
  + %name-0.2.2-symlinks-rootpath.patch
  + %name-0.2.2-blocksize.patch (partially fixed in upstream)
- removed %name-0.2.0-passwdfile.patch
- replaced %name-alt-configure.patch with
  %name-0.2.2-configure.patch
- fixed License

* Sat May 07 2005 Anton D. Kachalov <mouse@altlinux.org> 0.2.0-alt6.1
- multilib support

* Fri Apr 08 2005 Anton Farygin <rider@altlinux.ru> 0.2.0-alt6
- fixed memory corruption on big images

* Tue Apr 05 2005 Anton Farygin <rider@altlinux.ru> 0.2.0-alt5
- fixed segfault if path to desctination directory more than 69

* Wed Dec 08 2004 Anton Farygin <rider@altlinux.ru> 0.2.0-alt4
- disabled default blocksize (1024) into ext2fs_open
- added default blocksize (1024) into mke2fs.c

* Tue Dec 07 2004 Anton Farygin <rider@altlinux.ru> 0.2.0-alt3
- fixed symlink contents (used rootdir path)

* Thu Dec 02 2004 Anton Farygin <rider@altlinux.ru> 0.2.0-alt2
- fixed directory mode,owner and group

* Thu Jun 10 2004 Anton Farygin <rider@altlinux.ru> 0.2.0-alt1
- first build for Sisyphus

