Name: orbuculum
Version: 1.12
Release: alt1

Summary: Cortex-M code instrumentation for the masses
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/orbcode/orbuculum

Source: %name-%version-%release.tar

BuildRequires: binutils-devel libelf-devel libusb-devel

%description
Orbuculum is a set of tools for decoding and presenting output flows
from the Debug pins of a CORTEX-M CPU.

%prep
%setup

%build
make WITH_FPGA=0

%install
install -pm0755 -D ofiles/orbuculum %buildroot%_bindir/orbuculum
install -pm0755 ofiles/{orbcat,orbdump,orbstat,orbtop} %buildroot%_bindir/

%global _customdocdir %_defaultdocdir/%name

%files
%doc CHANGES* CONTRIBUTORS COPYING README* Docs Support
%_bindir/*

%changelog
* Thu Jan 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- initial
