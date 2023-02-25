Name: virt_cacard
Version: 1.2.1
Release: alt1

Summary: Virtual CAC provides PCSC accessible virtual smart card

License: LGPLv2
Group: System/Base
Url: https://github.com/Jakuje/virt_cacard

# Source-url: https://github.com/Jakuje/virt_cacard/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: libcacard-devel

%description
Virtual CAC using libcacard, virtualsmartcard's vpcd and softhsm2
to provide PCSC accessible virtual smart card.

%prep
%setup
%__subst 's|noinst_PROGRAMS|bin_PROGRAMS|' Makefile.am

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/%name

%changelog
* Sat Feb 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Sisyphus
