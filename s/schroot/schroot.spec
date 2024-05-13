%define _unpackaged_files_terminate_build 1

Name: schroot
Version: 1.6.10
Release: alt2.2
Summary: Execute commands in a chroot environment
Group: Development/Tools
License: GPLv3+
Url: http://packages.debian.org/schroot
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
Source: %name-%version.tar

# Fedora patches
Patch0: schroot-pam.patch
Patch1: schroot-default-config-path.patch
Patch3: schroot-gcc8-assert-fix.patch

# Debian patches
Patch10: Add-support-for-more-compression-formats.patch
Patch11: Add-SESSION_SOURCE-and-CHROOT_SESSION_SOURCE.patch
Patch12: 10mount-Move-mount-directory-to-var-run.patch
Patch13: Support-union-mounts-with-overlay-as-in-Linux-4.0.patch
Patch14: GCC5-fixes-on-regexes.patch
Patch15: schroot-mount-make-bind-mounts-private.patch
Patch16: schroot-mount-resolve-mount-destinations-while-chrooted.patch
Patch17: fix-test-suite-with-usrmerge.patch
Patch18: Unmount-everything-that-we-can-instead-of-giving-up.patch
Patch19: fix-killprocs.patch
Patch20: fix-bash-completion.patch

# ALT patches
Patch50: schroot-alt-configs.patch
Patch51: schroot-fix-man-building.patch
Patch52: schroot-alt-fix-for-boost-1.85.0.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: cppunit-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-devel
BuildRequires: libpam0-devel
BuildRequires: liblockdev-devel
BuildRequires: libuuid-devel
BuildRequires: gettext
BuildRequires: liblvm2-devel
BuildRequires: doxygen graphviz
BuildRequires: po4a >= 0.40

%filter_from_requires /mdconfig/d

%description
schroot allows users to execute commands or interactive shells in
different chroots.  Any number of named chroots may be created, and
access permissions given to each, including root access for normal
users, on a per-user or per-group basis.  Additionally, schroot can
switch to a different user in the chroot, using PAM for
authentication and authorisation.  All operations are logged for
security.

Several different types of chroot are supported, including normal
directories in the filesystem, and also block devices.  Sessions,
persistent chroots created on the fly from files (tar with optional
compression and zip) and LVM snapshots are also supported.

schroot supports kernel personalities, allowing the programs run
inside the chroot to have a different personality.  For example,
running 32-bit chroots on 64-bit systems, or even running binaries
from alternative operating systems such as SVR4 or Xenix.

schroot also integrates with sbuild, to allow building packages with
all supported chroot types, including session-managed chroot types
such as LVM snapshots.

schroot shares most of its options with dchroot, but offers vastly
more functionality.

%package -n dchroot
Group: Development/Tools
Summary: Older tool similar to schroot

%description -n dchroot
dchroot allows users to execute commands or interactive shells in different 
chroots. Users can move between chroots as necessary.  Enhanced
functionality is available in the next generation tool called schroot.

%prep
%setup -q

%patch0 -p0
%patch1 -p0
%patch3 -p1 -b .gcc8

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

%patch50 -p1
%patch51 -p1
%patch52 -p1

# Release-Date and Released-By fields are taken from Debian tarball for this version
cat > VERSION << END
Package: schroot
Version: %version
Release-Date: 05 May 2014
Released-By: Roger Leigh <rleigh@codelibre.net>
Git-Tag: release/schroot-%version
END

%build
%cmake \
	-Ddebug=OFF \
	-Ddchroot=ON \
	-Ddchroot-dsa=OFF \
	-Dbash_completion_dir=/usr/share/bash-completion/completions \
	-Duuid=ON \
	-Dlvm-snapshot=ON \
	-DLVCREATE_EXECUTABLE=/sbin/lvcreate \
	-DLVREMOVE_EXECUTABLE=/sbin/lvremove

%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_localstatedir/schroot/session
mkdir -p %buildroot%_localstatedir/schroot/mount
mkdir -p %buildroot%_sysconfdir/schroot/chroot.d

# get rid of uneeded include and library files
rm -rf %buildroot%_includedir
rm -f %buildroot%_libdir/pkgconfig/sbuild.pc
rm -f %buildroot%_libdir/libsbuild.la
rm -f %buildroot%_libdir/libsbuild.so*
rm -f %buildroot%_libdir/libsbuild.a

rm -rf %buildroot%_sysconfdir/schroot/buildd
rm -rf %buildroot%_sysconfdir/schroot/sbuild
rm -f %buildroot%_bindir/schroot-sbuild

rm -rf %buildroot%_mandir/de
rm -rf %buildroot%_mandir/fr

%find_lang %name

%files -f %name.lang
%doc COPYING AUTHORS HACKING NEWS README THANKS TODO
%dir %_bindir/schroot
%dir %_sysconfdir/schroot
%dir %_sysconfdir/schroot/chroot.d
%config(noreplace) %_sysconfdir/schroot/schroot.conf
%config(noreplace) %_sysconfdir/pam.d/schroot
%dir %_sysconfdir/schroot/default
%dir %_sysconfdir/schroot/desktop
%dir %_sysconfdir/schroot/minimal
%dir %_sysconfdir/schroot/setup.d
%_sysconfdir/schroot/default/*
%_sysconfdir/schroot/desktop/*
%_sysconfdir/schroot/minimal/*
%_sysconfdir/schroot/setup.d/*
%dir %_prefix/libexec/schroot
%_prefix/libexec/schroot/schroot-listmounts
%_prefix/libexec/schroot/schroot-mount
%dir %_localstatedir/schroot
%dir %_localstatedir/schroot/session
%dir %_localstatedir/schroot/mount
%dir %_localstatedir/schroot/union
%dir %_localstatedir/schroot/union/overlay
%dir %_localstatedir/schroot/union/underlay
%dir %_localstatedir/schroot/unpack
%_datadir/bash-completion/completions/schroot
%_datadir/%name/setup/common-config
%_datadir/%name/setup/common-data
%_datadir/%name/setup/common-functions
%_man1dir/schroot*
%_man5dir/schroot-script-config*
%_man5dir/schroot-setup*
%_man5dir/schroot.conf*
%_man7dir/schroot-faq*

%files -n dchroot
%doc COPYING AUTHORS HACKING NEWS README THANKS TODO
%_bindir/dchroot
%_man1dir/dchroot*

%changelog
* Mon May 13 2024 Ivan A. Melnikov <iv@altlinux.org> 1.6.10-alt2.2
- NMU: fix building with boost 1.85.0

* Wed Mar 13 2024 Ivan A. Melnikov <iv@altlinux.org> 1.6.10-alt2.1
- NMU: get rid of generated dependency on /sbin/mdconfig,
  which used only on FreeBSD (fixes rebuilding).

* Wed Feb 09 2022 Andrey Limachko <liannnix@altlinux.org> 1.6.10-alt2
- Fix man building

* Mon Jun 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.10-alt1
- Updated to upstream version 1.6.10.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4.23-alt1.qa7
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.4.23-alt1.5.1
- rebuild with boost 1.57.0

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.23-alt1.5
- Rebuilt with Boost 1.53.0

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.23-alt1.4
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.23-alt1.3
- Rebuilt with Boost 1.51.0

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.23-alt1.2
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.23-alt1.1
- Rebuilt with Boost 1.48.0

* Sat Jul 23 2011 Evgeny Sinelnikov <sin@altlinux.ru> 1.4.23-alt1
- Initial build for Sisyphus based on Fedora release 1.4.21-2
