Name: orbuculum
Version: 1.12
Release: alt2

Summary: Cortex-M code instrumentation for the masses
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/orbcode/orbuculum

Source: %name-%version-%release.tar

BuildRequires: binutils-devel libncurses-devel libusb-devel

%description
Orbuculum is a set of tools for decoding and presenting output flows
from the Debug pins of a CORTEX-M CPU.

%prep
%setup

%build
make

%install
install -pm0755 -D ofiles/orbuculum %buildroot%_bindir/orbuculum
install -pm0755 ofiles/{orbcat,orbdump,orbfifo,orbstat,orbtop} %buildroot%_bindir/

%global _customdocdir %_defaultdocdir/%name

%files
%doc CHANGES* CONTRIBUTORS COPYING README* Docs Support
%_bindir/*

%changelog
* Fri Nov 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt2
- V1.12-120-gce9ff2c

* Thu Jan 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- initial
