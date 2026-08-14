Name:    uwhat
Version: 0.3.0
Release: alt1

Summary: Human-friendly USB device lister
License: GPL-3.0-only
Group:   System/Kernel and hardware
URL:     https://github.com/sniner/uwhat

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
A human-friendly USB device lister. Think of it as a modern alternative to
lsusb - designed to show you what's actually plugged into your machine,
not kernel internals.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Fri Aug 14 2026 Sergey Palcheh <minergenon@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
