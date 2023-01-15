%def_with keyutils
# too old kernel in hasher
%def_disable check

Name: ndctl
Version: 75
Release: alt1

Summary: Manage NVDIMM subsystem devices (Non-volatile Memory)
License: LGPL-2.1
Group: System/Base
Url: https://github.com/pmem/ndctl

Vcs: https://github.com/pmem/ndctl.git
Source: %url/archive/v%version/%name-%version.tar.gz

Requires: lib%name = %EVR
Requires: libdaxctl = %EVR
Requires: kmod

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(libkmod)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(iniparser) >= 4.1
%{?_with_keyutils:BuildRequires: pkgconfig(libkeyutils)}
%{?_with_bash:BuildRequires: bash-completion >= 2.0}
BuildRequires: asciidoctor asciidoc xmlto

%description
Utility library for managing the "libnvdimm" subsystem. The "libnvdimm"
subsystem defines a kernel device model and control message interface for
platform NVDIMM resources like those defined by the ACPI 6+ NFIT (NVDIMM
Firmware Interface Table).

%package -n lib%name
Summary: Management library for "libnvdimm" subsystem devices (Non-volatile Memory)
License: LGPLv2
Group: System/Libraries
Requires: libdaxctl = %EVR

%description -n lib%name
Libraries for %name.

%package -n lib%name-devel
Summary: Development files for libndctl
License: LGPLv2
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%package -n daxctl
Summary: Manage Device-DAX instances
License: GPLv2
Group: System/Base
Requires: lib%name = %EVR
Requires: libdaxctl = %EVR
Requires: udev

%description -n daxctl
The daxctl utility provides enumeration and provisioning commands for
the Linux kernel Device-DAX facility. This facility enables DAX mappings
of performance / feature differentiated memory without need of a
filesystem.

%package -n libdaxctl
Summary: Management library for "Device DAX" devices
License: LGPLv2
Group: System/Libraries

%description -n libdaxctl
Device DAX is a facility for establishing DAX mappings of performance
feature-differentiated memory. libdaxctl provides an enumeration
control API for these devices.

%package -n libdaxctl-devel
Summary: Development files for libdaxctl
License: LGPLv2
Group: Development/C
Requires: libdaxctl = %EVR

%description -n libdaxctl-devel
This package contains libraries and header files for
developing applications that use libdaxctl, a library for enumerating
"Device DAX" devices.  Device DAX is a facility for establishing DAX
mappings of performance / feature-differentiated memory.

%package -n cxl
Summary: Manage CXL devices
Group: System/Base
License: GPLv2
Requires: libcxl = %EVR

%description -n cxl
The cxl utility provides enumeration and provisioning commands for
the Linux kernel CXL devices.

%package -n libcxl
Summary: Management library for CXL devices
License: LGPLv2
Group: System/Libraries

%description -n libcxl
libcxl is a library for enumerating and communicating with CXL devices.

%package -n libcxl-devel
Summary: Development files for libcxl
License: LGPLv2
Group: Development/C
Requires: libcxl = %EVR

%description -n libcxl-devel
This package contains libraries and header files for developing
applications that use libcxl is a library for enumerating and
communicating with CXL devices.

%prep
%setup
sed -i 's|/usr\(/bin/systemd-escape\)|\1|' daxctl/90-daxctl-device.rules

%build
%meson \
	-Dversion-tag='%version' \
	%{?_disable_keyutils:-Dkeyutils=false} \
	-Dbashcompletiondir=%_datadir/bash-completion/completions
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%_man1dir/%{name}*
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/keys
%_sysconfdir/%name/keys/keys.readme
%dir %_sysconfdir/%name.conf.d
%config(noreplace) %_sysconfdir/%name.conf.d/monitor.conf
%config(noreplace) %_sysconfdir/%name.conf.d/%name.conf
%config(noreplace) %_sysconfdir/modprobe.d/nvdimm-security.conf
%_unitdir/%name-monitor.service
%_datadir/bash-completion/completions/cxl
%_datadir/bash-completion/completions/daxctl
%_datadir/bash-completion/completions/%name

%files -n lib%name
%_libdir/lib%name.so.*
%doc README.md

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/lib%name.pc

%files -n daxctl
%_bindir/daxctl
%dir %_sysconfdir/daxctl.conf.d
%_udevrulesdir/90-daxctl-device.rules
%_sysconfdir/daxctl.conf.d/daxctl.example.conf
%_unitdir/daxdev-reconfigure@.service
%_man1dir/daxctl*
%dir %_datadir/daxctl
%_datadir/daxctl/daxctl.conf

%files -n libdaxctl
%_libdir/libdaxctl.so.*
%doc README.md

%files -n libdaxctl-devel
%_includedir/daxctl/
%_libdir/libdaxctl.so
%_pkgconfigdir/libdaxctl.pc

%files -n cxl
%_bindir/cxl
%_man1dir/cxl*

%files -n libcxl
%_libdir/libcxl.so.*
%doc README.md

%files -n libcxl-devel
%_includedir/cxl/
%_libdir/libcxl.so
%_pkgconfigdir/libcxl.pc
%_man3dir/*cxl*

%changelog
* Sun Jan 15 2023 Yuri N. Sedunov <aris@altlinux.org> 75-alt1
- 75

* Sat Oct 08 2022 Yuri N. Sedunov <aris@altlinux.org> 74-alt1.1
- daxctl/90-daxctl-device.rules: /usr/bin/systemd-escape -> /bin/systemd-escape

* Wed Aug 24 2022 Yuri N. Sedunov <aris@altlinux.org> 74-alt1
- 74

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 73-alt1
- 73 (ported to Meson build system)

* Fri Jan 07 2022 Yuri N. Sedunov <aris@altlinux.org> 72.1-alt1
- 72.1

* Sat Dec 18 2021 Yuri N. Sedunov <aris@altlinux.org> 72-alt1
- 72
- new *cxl* subpackages

* Wed Dec 23 2020 Yuri N. Sedunov <aris@altlinux.org> 71.1-alt1
- 71.1

* Sun Dec 20 2020 Yuri N. Sedunov <aris@altlinux.org> 71-alt1
- 71

* Thu Oct 29 2020 Yuri N. Sedunov <aris@altlinux.org> 70.1-alt1
- 70.1

* Sat Jul 25 2020 Yuri N. Sedunov <aris@altlinux.org> 69-alt1
- 69

* Wed Mar 25 2020 Yuri N. Sedunov <aris@altlinux.org> 68-alt1
- 68
- fixed License tag

* Wed Oct 30 2019 Yuri N. Sedunov <aris@altlinux.org> 67-alt1
- 67

* Fri Aug 09 2019 Yuri N. Sedunov <aris@altlinux.org> 66-alt1
- 66

* Sun May 12 2019 Yuri N. Sedunov <aris@altlinux.org> 65-alt1
- 65

* Thu Feb 07 2019 Yuri N. Sedunov <aris@altlinux.org> 64.1-alt1
- 64.1

* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 63-alt1
- 63

* Wed Aug 01 2018 Yuri N. Sedunov <aris@altlinux.org> 61.2-alt1
- 61.2

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 60.3-alt1
- 60.3

* Sat May 12 2018 Yuri N. Sedunov <aris@altlinux.org> 60.1-alt1
- first build for Sisyphus

