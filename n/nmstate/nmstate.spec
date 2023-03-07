%define _unpackaged_files_terminate_build 1

Name: nmstate
Version: 2.1.4
Release: alt1
Summary: Declarative network manager API
Group: System/Configuration/Networking

License: LGPLv2+
Url: https://github.com/%name/%name
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-python3 rpm-macros-rust
BuildRequires: python3-devel python3-module-setuptools python3-module-yaml
BuildRequires: rpm-build-rust
BuildRequires: /proc

%description
Nmstate is a library with an accompanying command line tool that manages host
networking settings in a declarative manner and aimed to satisfy enterprise
needs to manage host networking through a northbound declarative API and multi
provider support on the southbound.

%package -n lib%name
Summary: C binding of nmstate
Group: System/Libraries
#Recommends: NetworkManager
# Avoid automatically generated profiles
#Recommends:     NetworkManager-config-server
Provides: %name-libs = %EVR

%description -n lib%name
C binding of nmstate.

%package -n lib%name-devel
Summary: Development files for nmstate
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files of nmstate C binding.

%package -n python3-module-lib%name
Summary: nmstate Python 3 API library
Group: Development/Python3
BuildArch: noarch
#Recommends: NetworkManager
#Recommends: NetworkManager-config-server
#Recommends: (nmstate-plugin-ovsdb if openvswitch)
# Use Suggests for NetworkManager-ovs and NetworkManager-team since it is only
# required for OVS and team support
#Suggests: NetworkManager-ovs
#Suggests: NetworkManager-team
Requires:  lib%name = %EVR

%description -n python3-module-lib%name
This package contains the Python 3 library for Nmstate.

%prep
%setup
%patch -p1
pushd rust
mkdir -p .cargo
cat >.cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
popd

%build
SKIP_PYTHON_INSTALL=1 PREFIX=%_prefix LIBDIR=%_libdir SYSCONFDIR=%_sysconfdir SYSTEMD_UNIT_DIR=%_unitdir %make
pushd rust/src/python
%python3_build
popd

%install
pushd rust/src/python
%python3_install
popd
SKIP_PYTHON_INSTALL=1 \
    PREFIX=%_prefix \
    LIBDIR=%_libdir \
    SYSCONFDIR=%_sysconfdir \
    SYSTEMD_UNIT_DIR=%_unitdir \
    %makeinstall_std

rm -f %buildroot%_libdir/*.{a,la}

%files
%doc README.md
%doc examples
%_bindir/*
%_man8dir/*
%_unitdir/*.service
%dir %_sysconfdir/%name
%_sysconfdir/%name/README

%files -n python3-module-lib%name
%python3_sitelibdir_noarch/lib%name
%python3_sitelibdir_noarch/%name-*.egg-info

%files -n lib%name
%_libdir/libnmstate.so.*

%files -n lib%name-devel
%_libdir/libnmstate.so
%_includedir/nmstate.h
%_pkgconfigdir/nmstate.pc

%changelog
* Wed Mar 01 2023 Alexey Shabalin <shaba@altlinux.org> 2.1.4-alt1
- Initial build.

