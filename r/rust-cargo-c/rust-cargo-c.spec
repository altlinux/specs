Name: rust-cargo-c
Version: 0.9.16
Release: alt1

Summary: Cargo applet to build and install C-ABI compatible dynamic and static libraries
License: MIT
Group: Development/Other
Url: https://github.com/lu-zero/cargo-c

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc
BuildRequires: libssl-devel

%description
%summary
It produces and installs a correct pkg-config file, a static library and a dynamic
library, and a C header to be used by any C (and C-compatible) software.

%prep
%setup
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 vendor
%else
tar xf %SOURCE1
%endif

%build
export CARGO_HOME=${PWD}/cargo
cargo build --release

%install
mkdir -p %buildroot%_bindir
install -pm0755 target/release/cargo-capi %buildroot%_bindir/
install -pm0755 target/release/cargo-cbuild %buildroot%_bindir/
install -pm0755 target/release/cargo-cinstall %buildroot%_bindir/
install -pm0755 target/release/cargo-ctest %buildroot%_bindir/

%files
%doc LICENSE README.md
%_bindir/cargo-c*

%changelog
* Fri Jan 27 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.16-alt1
- 0.9.16 released

* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.15-alt1
- 0.9.15 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.14-alt1
- 0.9.14 released

* Mon Oct  3 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.13-alt1
- 0.9.13 released

* Tue Aug 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.11-alt1
- 0.9.11 released

* Thu May 12 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9-alt1
- 0.9.9 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.8-alt1
- 0.9.8 released

* Fri Nov 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.5-alt1
- initial

# Local Variables:
# compile-command: "share_network=1 gear-hsh --commit --mountpoints=/proc --build-args=\'--define \"bootstrap please\"\'"
# End:
