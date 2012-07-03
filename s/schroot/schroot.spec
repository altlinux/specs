Name: schroot
Version: 1.4.23
Release: alt1.2
Summary: Execute commands in a chroot environment
Group: Development/Tools
License: GPLv3+
Url: http://packages.debian.org/schroot
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: cppunit-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-devel
BuildRequires: libpam0-devel
BuildRequires: liblockdev-devel
BuildRequires: libuuid-devel
BuildRequires: gettext

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
%patch -p1

%build
./bootstrap
%configure --disable-rpath --enable-static --disable-shared --enable-dchroot --localstatedir=%_var
%make

%install
make install DESTDIR=%buildroot
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

%find_lang %name

%files -f %name.lang
%doc COPYING ABOUT-NLS AUTHORS ChangeLog HACKING INSTALL NEWS README THANKS TODO
%dir %_bindir/schroot
%dir %_sysconfdir/schroot
%dir %_sysconfdir/schroot/chroot.d
%config(noreplace) %_sysconfdir/schroot/schroot.conf
%config(noreplace) %_sysconfdir/pam.d/schroot
%dir %_sysconfdir/schroot/default
%dir %_sysconfdir/schroot/desktop
%dir %_sysconfdir/schroot/minimal
%dir %_sysconfdir/schroot/setup.d
%_sysconfdir/bash_completion.d/schroot
%_sysconfdir/schroot/default/*
%_sysconfdir/schroot/desktop/*
%_sysconfdir/schroot/minimal/*
%_sysconfdir/schroot/setup.d/*
%dir %_libexecdir/schroot
%_libexecdir/schroot/schroot-listmounts
%_libexecdir/schroot/schroot-mount
%_libexecdir/schroot/schroot-releaselock
%dir %_localstatedir/schroot
%dir %_localstatedir/schroot/session
%dir %_localstatedir/schroot/mount
%dir %_localstatedir/schroot/union
%dir %_localstatedir/schroot/union/overlay
%dir %_localstatedir/schroot/union/underlay
%dir %_localstatedir/schroot/unpack
%_datadir/%name/setup/common-data
%_datadir/%name/setup/common-functions
%_man1dir/schroot*
%_man5dir/schroot-script-config*
%_man5dir/schroot-setup*
%_man5dir/schroot.conf*
%_man7dir/schroot-faq*

%files -n dchroot
%doc COPYING ABOUT-NLS AUTHORS ChangeLog HACKING INSTALL NEWS README THANKS TODO
%_bindir/dchroot
%_mandir/man1/dchroot*

%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.23-alt1.2
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.23-alt1.1
- Rebuilt with Boost 1.48.0

* Sat Jul 23 2011 Evgeny Sinelnikov <sin@altlinux.ru> 1.4.23-alt1
- Initial build for Sisyphus based on Fedora release 1.4.21-2
