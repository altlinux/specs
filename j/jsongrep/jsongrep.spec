%define _unpackaged_files_terminate_build 1
%define binname jg

Name: jsongrep
Version: 0.9.0
Release: alt1

Summary: A path query language for JSON, YAML, TOML, and other serialization formats
License: MIT
Group: Development/Tools
Url: https://crates.io/crates/jsongrep
Vcs: https://github.com/micahkepe/jsongrep

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust
BuildRequires: rust-cargo

%description
command-line tool and Rust library for fast querying of JSON, YAML, TOML,
JSONL, CBOR, and MessagePack documents using regular path expressions.

%prep
%setup -a 1

install -D %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
#%%rust_install doesn't work here
install -Dm 755 "target/release/%binname" "%buildroot%_bindir/%binname"

%files
%doc README.md LICENSE
%_bindir/%binname

%changelog
* Fri Jun 05 2026 Vladislav Glinkin <smasher@altlinux.org> 0.9.0-alt1
- New version

* Wed Apr 01 2026 Vladislav Glinkin <smasher@altlinux.org> 0.8.1-alt1
- Initial build for ALT

