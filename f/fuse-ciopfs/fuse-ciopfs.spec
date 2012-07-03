%define oname ciopfs

Name: fuse-ciopfs
Version: 0.2
Release: alt1.qa1

Summary: case insensitive on purpose file system using FUSE

Group: System/Kernel and hardware
License: GPL v2
Url: http://www.brain-dump.org/projects/ciopfs/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.brain-dump.org/projects/%oname/%oname-%version.tar.bz2
Patch: %name-destdir.patch

Requires: fuse

# Automatically added by buildreq on Sun Jul 06 2008
BuildRequires: glib2-devel libattr-devel libfuse-devel

%description
CIOPFS is a stackable or overlay linux userspace file system (implemented
with fuse) which mounts a normal directory on a regular file system in
case insensitive fashion.

%prep
%setup -q -n %oname-%version
%patch

%build
%make_build

%install
%makeinstall_std PREFIX=%prefix

%files
%_bindir/%oname
/sbin/mount.%oname

%changelog
* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for fuse-ciopfs

* Sun Jul 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
