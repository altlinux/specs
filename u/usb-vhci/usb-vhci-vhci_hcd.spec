Name: usb-vhci
Version: 1.15
Release: alt1

Summary: USB Virtual Host Controller Driver (VHCI)
License: GPLv2
Group: System/Kernel and hardware
BuildArch: noarch

Url: https://sourceforge.net/p/usb-vhci/vhci_hcd/ci/master/tree/
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-kernel kernel-headers-modules-std-def

%description
USB Virtual Host Controller Driver (VHCI)

%package -n kernel-source-%name
Summary: USB Virtual Host Controller Driver (VHCI) source.
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
USB Virtual Host Controller Driver (VHCI) source.

%prep
%setup -q

%build

%install
install -pDm0644 %_sourcedir/%name-%version.tar %kernel_srcdir/kernel-source-%name-%version.tar

%check
make KDIR=/lib/modules/*/build

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar

%files
%doc README COPYING

%changelog
* Fri Oct 18 2019 Andrew A. Vasilyev <andy@altlinux.org> 1.15-alt1
- Initial import for ALT.

