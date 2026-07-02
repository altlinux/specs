Name: narcolepsyd
Version: 0.1.0
Release: alt1

Summary: Idle power optimizer for Linux laptops with Intel hybrid CPUs
License: Apache-2.0
Group: System/Kernel and hardware
Url: https://github.com/obra/narcolepsyd
VCS: https://github.com/obra/narcolepsyd.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
narcolepsyd is an idle power optimizer for Linux laptops with Intel
hybrid CPUs (Alder Lake and newer).  It monitors keyboard and touchpad
input; when you stop interacting with your laptop, it aggressively parks
CPU cores, caps frequencies and disables turbo to reduce power
consumption.  When you touch any input device, everything is restored
instantly.  The display stays on and the network stays connected.

%prep
%setup
%rust_prep

%build
%rust_build

%install
%rust_install
install -Dpm 0644 dist/narcolepsyd.service %buildroot%_unitdir/narcolepsyd.service

%files
%doc README.md
%_bindir/narcolepsyd
%_unitdir/narcolepsyd.service

%changelog
* Thu Jul 02 2026 Andrey Limachko <liannnix@altlinux.org> 0.1.0-alt1
- initial build for ALT Linux
