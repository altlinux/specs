Name: crtools-ovz
Version: 3.12.5.50
Release: alt1

Summary: Utility to checkpoint/restore tasks for OpenVZ containers
License: GPL-2.0-only
Group: System/Configuration/Other
Url: http://criu.org

# VCS: https://src.openvz.org/scm/ovz/criu.git
Source: criu-%version.tar

Provides: criu-ovz = %EVR
Conflicts: crtools
ExclusiveArch: x86_64

BuildRequires: libnet2-devel
BuildRequires: libprotobuf-c-devel %_bindir/protoc-c
BuildRequires: libprotobuf-devel protobuf-compiler
BuildRequires: asciidoc xmlto %_bindir/a2x
BuildRequires: libnftables-devel
BuildRequires: libgnutls-devel

BuildRequires: python3-devel
BuildRequires: glibc-devel
BuildRequires: libnl-devel
BuildRequires: libcap-devel
# BuildRequires: libselinux-devel
BuildRequires(pre): rpm-build-python3

Requires: nftables util-linux

%description
An utility to checkpoint/restore tasks for OpenVZ containers.

%prep
%setup -n criu-%version

%build
export CFLAGS="%optflags"
%make_build \
	PREFIX=%prefix V=1 all docs

%install
%makeinstall_std \
	PREFIX=%prefix LIBDIR=%_libdir LIBEXECDIR=%_libexecdir SYSTEMDUNITDIR=%_unitdir

mv %buildroot%_sbindir/criu{,-ovz}
ln -s criu-ovz %buildroot%_sbindir/criu
ln -s criu-ovz %buildroot%_sbindir/crtools
ln -s criu.8 %buildroot%_man8dir/crtools.8

find %buildroot -name 'lib*.a' -delete

rm -f %buildroot%_bindir/crit
rm -rf %buildroot%python3_sitelibdir_noarch
rm -f %buildroot%_man1dir/crit.1*
rm -f %buildroot%_libdir/libcriu.so.2*
rm -f %buildroot%_libdir/libcompel.so.1*
rm -rf %buildroot%_includedir/criu
rm -rf %buildroot%_includedir/compel
rm -f %buildroot%_libdir/*.so
rm -f %buildroot%_pkgconfigdir/criu.pc

%files
%doc README.md COPYING CREDITS
%_sbindir/criu
%_sbindir/criu-ovz
%_sbindir/crtools
%_bindir/compel
%_libexecdir/criu
%_libexecdir/compel
%_man1dir/compel.1*
%_man8dir/criu.8*
%_man8dir/crtools.8*

%changelog
* Fri Oct 30 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.50-alt1
- 3.12.5.50

* Mon Oct 12 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.46-alt1
- 3.12.5.46

* Mon Oct 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.44-alt1
- 3.12.5.44

* Fri Oct 02 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.43-alt1
- 3.12.5.43

* Wed Sep 30 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.41-alt1
- 3.12.5.41
- remove all extra packages not needed for OpenVZ

* Mon Sep 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.40-alt1
- 3.12.5.40

* Fri Sep 11 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.38-alt1
- Initial build for ALT from Virtuozzo fork of criu, spec based on crtool.

