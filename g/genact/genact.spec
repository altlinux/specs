Name: genact
Version: 1.5.1
Release: alt1

Summary: A nonsense activity generator
License: MIT
Group: Games/Other
Url: https://github.com/svenstaro/genact
Vcs: https://github.com/svenstaro/genact

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo

%description
Genact is a nonsense activity generator that displays fake activity
in a terminal to impress people or to look busy.

%prep
%setup -a 1
%autopatch -p1
%rust_prep

%build
%rust_build

%install
cargo install %_smp_mflags --offline --no-track --path .

%files
%_bindir/genact
%doc README.md

%changelog
* Thu May 28 2026 Vladislav Tatjanin <l27001@altlinux.org> 1.5.1-alt1
- Initial build.

