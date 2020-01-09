Name: atf-sunxi
Version: 2.2
Release: alt1

Summary: ARM Trusted Firmware
License: BSD
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

%def_without debug

%description
ARM Trusted Firmware provides a reference implementation of secure world
software for ARMv8-A, including Exception Level 3 (EL3) software.
This release provides initial support for the Allwinner A64/H5/H6 SoC families.

%prep
%setup

%build
%make_build PLAT=sun50i_a64 %{?_with_debug:DEBUG=1} bl31
%make_build PLAT=sun50i_h6 %{?_with_debug:DEBUG=1} bl31

%install
install -pm0644 -D build/sun50i_a64/%{?_with_debug:debug}%{!?_with_debug:release}/bl31.bin \
	%buildroot%_datadir/atf/sun50i_a64/bl31.bin
install -pm0644 -D build/sun50i_h6/%{?_with_debug:debug}%{!?_with_debug:release}/bl31.bin \
	%buildroot%_datadir/atf/sun50i_h6/bl31.bin

%files
%_datadir/atf/sun50i_a64/bl31.bin
%_datadir/atf/sun50i_h6/bl31.bin

%changelog
* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2 released

* Mon Apr 15 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- 2.1 released

* Fri Jan 25 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt1
- 2.0-686-ga1d1d24b

* Mon Oct 02 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1
- initial
