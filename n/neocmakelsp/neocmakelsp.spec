Name: neocmakelsp
Version: 0.10.4
Release: alt1

Summary: CMake LSP implementation
License: MIT
Group: Development/Other
URL: https://neocmakelsp.github.io
VCS: https://github.com/neocmakelsp/neocmakelsp

Requires: cmake

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
* Mon Jul 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.10.4-alt1
- 0.10.4 released

* Thu Jun 04 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.10.3-alt1
- 0.10.3 released

* Fri Apr 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.10.2-alt1
- 0.10.2 released

* Mon Mar 02 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.10.1-alt1
- 0.10.1 released

* Mon Jan 26 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.10.0-alt1
- 0.10.0 released

* Mon Jan 26 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.2-alt1
- 0.9.2 released

* Mon Jan 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.1-alt1
- 0.9.1 released

* Mon Nov 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.0-alt1
- initial
