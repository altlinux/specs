Name: neocmakelsp
Version: 0.9.0
Release: alt1

Summary: CMake LSP implementation
License: MIT
Group: Development/Other
Url: https://neocmakelsp.github.io
VCS: https://github.com/neocmakelsp/neocmakelsp

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc

%description
CMake LSP implementation based on Tower and Tree-sitter.

%prep
%setup -a1
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
%endif

%build
cargo build --release

%install
install -pm0755 -D target/release/neocmakelsp \
        %buildroot%_bindir/neocmakelsp

%files
%doc LICENSE README.*
%_bindir/neocmakelsp

%changelog
* Mon Nov 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.0-alt1
- initial
