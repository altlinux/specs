%define oname chironfs

Name: fuse-chironfs
Version: 1.1.1
Release: alt1.qa2

Summary: Replication Filesystem

Group: System/Kernel and hardware
License: GPL v3
Url: http://www.furquim.org/chironfs/index.en.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://chironfs.googlecode.com/files/%oname-%version.tar.bz2
Patch: %name-%version.patch

Requires: fuse

# manually removed: rpm-build-java rpm-build-mono rpm-build-seamonkey rpm-macros-fillup xorg-sdk
# Automatically added by buildreq on Mon Dec 08 2008
BuildRequires: libfuse-devel

%description
Chiron FS is a FUSE based filesystem that implements replication
at the filesystem level like RAID 1 does at the device level. The
replicated filesystem may be of any kind you want; the only.
requisite is that you mount it. There is no need for special
configuration files; the setup is as simple as one mount command
(or one line in fstab).

%prep
%setup -n %oname-%version
%patch

%build
%configure
%make

%install
%makeinstall_std

%files
%_bindir/chironfs
%_bindir/chirctl
%_man8dir/chironfs.8*
%_docdir/%oname/

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.qa2
- Fixed build

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for fuse-chironfs

* Thu Jan 14 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Mon Dec 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
