Name:     libvzsock
Version:  7.0.3
Release:  alt2

Summary:  libvzsock is a helper library for networking connections code generalization.
License:  LGPLv2.1+
Group:    Other
Url:      https://src.openvz.org/scm/ovz/libvzsock.git

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source:   %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64

BuildRequires: libssl-devel openssl libkrb5-devel

%description
%summary

%package devel
Summary: Virtuozzo socket development library
Group: Development/C
Requires: %name = %version-%release

%description devel
Virtuozzo socket development library

%prep
%setup
%patch -p1

%build
%add_optflags %optflags_shared
%make_build CFLAGS="$RPM_OPT_FLAGS"
make CFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall_std

%files
%_libdir/*.so.*
%_datadir/%name

%files devel
%_libdir/libvzsock.so
%_libdir/libvzsock.a
%dir %_includedir/vz
%_includedir/vz/*.h

%changelog
* Mon Aug 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.3-alt2
- preserve debug info

* Thu Aug 01 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.3-alt1
- Initial build for Sisyphus
