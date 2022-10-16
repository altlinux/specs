%define optflags_lto %nil
%define sover 1
%def_without check

Name: apparmor
Version: 3.0.7
Release: alt2

Summary: Name-based Mandatory Access Control

License: GPL-2.0-or-later and LGPL-2.1-or-later
Group: System/Base
Url: https://apparmor.net

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: flex gcc-c++ perl-Pod-Checker python3-module-setuptools swig
BuildRequires: libstdc++-devel
%{?_with_check:BuildRequires: dejagnu}

%description
AppArmor is a Mandatory Access Control (MAC) mechanism which uses the
Linux Security Module (LSM) framework. The confinement's restrictions
are mandatory and are not bound to identity, group membership, or object
ownership. The protections provided are in addition to the kernel's
regular access control mechanisms (including DAC) and can be used to
restrict the superuser.

%package -n libapparmor%sover
Summary: Apparmor library
Group: System/Libraries

%description -n libapparmor%sover
AppArmor is a Mandatory Access Control (MAC) mechanism which uses the
Linux Security Module (LSM) framework. The confinement's restrictions
are mandatory and are not bound to identity, group membership, or object
ownership. The protections provided are in addition to the kernel's
regular access control mechanisms (including DAC) and can be used to
restrict the superuser.

%package -n libapparmor-devel
Summary: Development files for libapparmor
Group: System/Libraries

%description -n libapparmor-devel
%summary.

%package -n libapparmor-devel-doc
Summary: Documantaion for AppArmor API
Group: System/Libraries

%description -n libapparmor-devel-doc
%summary.

%package -n python3-module-apparmor
Summary: Python module for AppArmor
Group: Development/Python3
BuildArch: noarch
# IDK why this happens, filter needless dependency to make the package really noarch
%filter_from_requires /^\/usr\/lib\/python3\/site-packages/d

%description -n python3-module-apparmor
%summary.

%package -n python3-module-libapparmor
Summary: Python module for libapparmor
Group: Development/Python3

%description -n python3-module-libapparmor
%summary.

%prep
%setup
%patch -p1

%build
pushd libraries/libapparmor
%autoreconf
%configure \
	--with-python \
	#
%make_build
popd

make -C utils

make -C binutils

make -C parser

make -C profiles

%install
%makeinstall_std -C libraries/libapparmor
%makeinstall_std -C utils
%makeinstall_std -C binutils
%makeinstall_std -C profiles
%makeinstall_std SBIN="%buildroot/sbin" APPARMOR_BIN_PREFIX="%buildroot/lib/apparmor" -C parser

mkdir -p %buildroot/lib/systemd/system
mv %buildroot/usr/lib/systemd/system/apparmor.service %buildroot/lib/systemd/system

rm %buildroot%_libdir/libapparmor.a

# relocate library to /%%_lib
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/libapparmor.so; do
	t=$(readlink "$f")
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/libapparmor.so.* %buildroot/%_lib

%find_lang apparmor

%check
make check -C libraries/libapparmor
make check -C parser
make check -C binutils

make -C profiles check-parser

%post
if [ $1 -ge 2 ]; then
	/sbin/service apparmor condrestart ||:
else
	/sbin/chkconfig --add apparmor ||:
fi

%preun
if [ $1 = 0 ]; then
	/sbin/chkconfig --del apparmor ||:
fi

%files -f apparmor.lang
%config(noreplace) %_sysconfdir/apparmor
%dir %_sysconfdir/apparmor.d
%dir %_sysconfdir/apparmor.d/disable
%dir %_sysconfdir/apparmor.d/local
%_sysconfdir/apparmor.d/abi
%_sysconfdir/apparmor.d/abstractions
%_sysconfdir/apparmor.d/tunables

/sbin/*
/usr/sbin/*
/lib/apparmor
%_bindir/*
%_datadir/apparmor
%_man1dir/*
%_man7dir/*
%_man8dir/*

%_initdir/apparmor
%_unitdir/apparmor.service

%files -n libapparmor%sover
/%_lib/libapparmor.so.%sover
/%_lib/libapparmor.so.%sover.*

%files -n libapparmor-devel
%_includedir/aalogparse/aalogparse.h
%_includedir/sys/apparmor.h
%_includedir/sys/apparmor_private.h
%_pkgconfigdir/libapparmor.pc
%_libdir/libapparmor.so

%files -n libapparmor-devel-doc
%_man2dir/*
%_man3dir/*

%files -n python3-module-apparmor
%python3_sitelibdir_noarch/apparmor
%python3_sitelibdir_noarch/apparmor-%version-py3*.egg-info

%files -n python3-module-libapparmor
%python3_sitelibdir/LibAppArmor
%python3_sitelibdir/LibAppArmor-%version-py3*.egg-info

%changelog
* Sun Oct 16 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.7-alt2
- SysVInit: Added condrestart.
- Added post-install and pre-uninstall scripts.
- Fixed configs.
- Fixed license.

* Sat Oct 15 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.7-alt1
- Initial build with a basic support for ALT Sisyphus.
