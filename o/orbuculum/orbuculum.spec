Name: orbuculum
Version: 2.2.0
Release: alt1

Summary: Cortex-M code instrumentation for the masses
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/orbcode/orbuculum

Source: %name-%version-%release.tar

BuildRequires: meson
BuildRequires: libSDL2-devel libcapstone-devel libczmq-devel
BuildRequires: libdwarf-devel libelf-devel libncurses-devel libusb-devel

%description
Orbuculum is a set of tools for decoding and presenting output flows
from the Debug pins of a CORTEX-M CPU.

%prep
%setup
sed -ri '/FN_SLEEPING_STR/ s,Sleeping,sleeping,' Inc/symbols.h

%build
%meson -Dversion-tag=%version-%release
%meson_build

%install
%meson_install

%files
%doc CHANGES* CONTRIBUTORS LICENSE README* Docs Support
%_udevrulesdir/*.rules
%_bindir/*
%_libdir/liborb.so.*
%_datadir/orbcode

%changelog
* Sun Sep 22 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.0-alt1
- 2.2.0 released

* Mon Jul  3 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Sun Feb 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt2
- avoid bursty output by reducing transfer sizes

* Fri Aug 19 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Fri Nov 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt2
- V1.12-120-gce9ff2c

* Thu Jan 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- initial
