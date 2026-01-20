%global prj_name geopmdpy

Name: geopmd
Version: 3.2.2
Release: alt1

Summary: GEOPM daemon
Group: System/Configuration/Other
License: BSD-3-Clause

URL: https://geopm.github.io
VCS: https://github.com/geopm/geopm.git
Source0: %name-%version.tar
ExclusiveArch: x86_64

BuildRequires: gcc
BuildRequires: libgrpc-devel
BuildRequires: libgeopmd-devel = %version
BuildRequires: libprotobuf-devel
BuildRequires: protobuf-compiler
BuildRequires: grpc-plugins
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-dasbus
BuildRequires: python3-module-docstring-parser
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-psutil
BuildRequires: python3-module-grpcio
BuildRequires: python3-module-protobuf
BuildRequires: libgio-devel
BuildRequires: rpm-build-vm
Requires: python3-module-cffi
Requires: python3-module-protobuf
Requires: geopmd-cli = %version
Requires: geopm-cli = %version
Requires: python3-module-%prj_name = %EVR

%description
GEOPM (Global Extensible Open Power Manager) daemon provides system-wide
power and energy management service. It monitors hardware performance
and power consumption, allowing optimization of system settings for
efficiency or performance objectives through D-Bus interface.

%package -n python3-module-%prj_name
Group: System/Configuration/Other
Summary: Python bindings for GEOPM daemon

%description -n python3-module-%prj_name
Python 3 bindings for GEOPM daemon (libgeopmd). Provides high-level
Python API for interacting with GEOPM power management service,
including monitoring, configuration, and optimization tools.

%prep
%setup -q %name-%version
pushd %prj_name
echo %version > %prj_name/VERSION
./protoc-gen.sh
sed -i 's/usr\/bin/usr\/sbin/g' geopm.service
popd

%build
pushd %prj_name
%pyproject_build
popd

%install
pushd %prj_name
%pyproject_install
mkdir -p %buildroot%_sysconfdir/geopm
chmod 0700 %buildroot%_sysconfdir/geopm
mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/geopmd %buildroot%_sbindir/
install -D -p -m 644 io.github.geopm.xml %buildroot%_datadir/dbus-1/interfaces/io.github.geopm.xml
install -D -p -m 644 io.github.geopm.conf %buildroot%_datadir/dbus-1/system.d/io.github.geopm.conf
install -D -p -m 644 geopm.service %buildroot%_unitdir/geopm.service
popd

%check
pushd %prj_name/test
vm-run --cpu=4 --kvm=cond --user --heredoc << 'EOF'
export LD_LIBRARY_PATH=%buildroot%_libdir:$LD_LIBRARY_PATH
PYTHONPATH=%buildroot%python3_sitelibdir python3 -m unittest discover -p 'Test*.py' -v
EOF
popd

%post -n geopmd
%systemd_post geopm.service

%preun -n geopmd
%systemd_preun geopm.service

%postun -n geopmd
%systemd_postun_with_restart geopm.service

%files
%doc README.md
%_sbindir/geopmd
%_datadir/dbus-1/interfaces/io.github.geopm.xml
%_datadir/dbus-1/system.d/io.github.geopm.conf
%_unitdir/geopm.service

%files -n python3-module-%prj_name
%_bindir/geopmaccess
%_bindir/geopmexporter
%_bindir/geopmread
%_bindir/geopmsession
%_bindir/geopmwrite
%python3_sitelibdir/%prj_name
%python3_sitelibdir/_libgeopmd_py_cffi.abi3.so
%python3_sitelibdir/%prj_name-*.dist-info

%changelog
* Thu Jan 15 2026 Danila Skachedubov <skachedubov@altlinux.org> 3.2.2-alt1
- first build for ALT
