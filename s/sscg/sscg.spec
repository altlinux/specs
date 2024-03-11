Name:    sscg
Version: 3.0.3
Release: alt1

Summary: Simple SSL certificate generator
License: %gpl3only
Group:   Security/Networking
Url:     https://github.com/sgallagher/sscg

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: libpath_utils-devel
BuildRequires: libtalloc-devel
BuildRequires: libpopt-devel
BuildRequires: help2man

%description
A utility to aid in the creation of more secure "self-signed"
certificates. The certificates created by this tool are generated in a
way so as to create a CA certificate that can be safely imported into a
client machine to trust the service certificate without needing to set
up a full PKI environment and without exposing the machine to a risk of
false signatures from the service certificate.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test -t 10

%files
%doc README.md Changelog.md
%_bindir/%name
%_man8dir/%name.*

%changelog
* Tue Feb 07 2023 Andrey Limachko <liannnix@altlinux.org> 3.0.3-alt1
- Initial build
