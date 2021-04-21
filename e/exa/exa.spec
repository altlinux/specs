%define _unpackaged_files_terminate_build 1

Name: exa
Version: 0.10.1
Release: alt1

Summary: A modern replacement for ls
License: MIT
Group: System/Base
Url: https://the.exa.website/

#Upstream: https://github.com/ogham/exa
Source: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: libgit2-devel
BuildRequires: cmake


%description
exa is a modern replacement for the venerable file-listing
command-line program ls that ships with Unix and Linux operating
systems, giving it more features and better defaults. It uses
colours to distinguish file types and metadata. It knows about
symlinks, extended attributes, and Git. And it's small, fast,
and just one single binary.

%prep
%setup -a1

mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --release %{?_smp_mflags} --all-targets --offline 

%install
install -D -m755 target/release/exa %buildroot%_bindir/exa

%files
%doc LICENCE
%doc README.md
%_bindir/*

%changelog
* Wed Apr 14 2021 Egor Ignatov <egori@altlinux.org> 0.10.1-alt1
- First build for ALT
