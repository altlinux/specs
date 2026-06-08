%define _unpackaged_files_terminate_build 1
%def_with check

Name: gleam
Version: 1.17.0
Release: alt1

Summary: A friendly language for building type-safe, scalable systems!
License: Apache-2.0
Group: Development/Other
Vcs: https://github.com/gleam-lang/gleam
Url: https://gleam.run/

ExcludeArch: %ix86

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-alt.patch

Requires: erlang
Requires: erlang-otp-devel

BuildRequires: rust-cargo
BuildRequires: /proc
%if_with check
BuildRequires: git
BuildRequires: clippy
BuildRequires: erlang
BuildRequires: erlang-devel
BuildRequires: elixir
BuildRequires: node
BuildRequires: rebar
%endif

%description
The power of a type system, the expressiveness of functional programming,
and the reliability of the highly concurrent, fault tolerant Erlang runtime,
with a familiar and modern syntax.

%package wasm
Summary: Webassembly for gleam
Group: Development/Other

%description wasm
%summary

%prep
%setup -a1
%patch0 -p1

%build
cargo build %_smp_mflags --offline --release

%install
install -Dp target/release/%name -t %buildroot%_bindir
install -Dp target/release/lib%{name}_wasm.so -t %buildroot%_libdir

%check
%make test

%files
%doc README.md LICENCE
%_bindir/%name

%files wasm
%_libdir/lib%{name}_wasm.so

%changelog
* Fri Jun 05 2026 Artem Krasovskiy <aibure@altlinux.org> 1.17.0-alt1
- New version 1.17.0.

* Tue Mar 17 2026 Artem Krasovskiy <aibure@altlinux.org> 1.15.0-alt1
- New version 1.15.0.

* Wed Feb 04 2026 Artem Krasovskiy <aibure@altlinux.org> 1.14.0-alt1
- New version 1.14.0.

* Fri Nov 07 2025 Artem Krasovskiy <aibure@altlinux.org> 1.13.0-alt1
- New version 1.13.0.

* Thu Aug 21 2025 Artem Krasovskiy <aibure@altlinux.org> 1.12.0-alt1
- New version 1.12.0

* Tue Jun 17 2025 Artem Krasovskiy <aibure@altlinux.org> 1.11.1-alt1
- Initial build
