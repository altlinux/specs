Name:    clevis
Version: 11
Release: alt1
Summary: Automated Encryption Framework

License: Apache 2.0
Group:   System/Libraries
URL:     https://github.com/latchset/clevis
Source:  clevis-%{version}.tar.gz

BuildRequires: libjose-devel meson

%description
Clevis is a plugable framework for automated decryption.
It can be used to provide automated decryption of data
or even automated unlocking of LUKS volumes.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/clevis
%_bindir/clevis-decrypt-sss
%_bindir/clevis-encrypt-sss

%changelog
* Mon Oct 01 2018 Oleg Solovyov <mcpain@altlinux.org> 11-alt1
- initial build

