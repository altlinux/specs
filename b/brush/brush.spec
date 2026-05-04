%define _unpackaged_files_terminate_build 1

# https://github.com/reubeno/brush/issues/429
%def_without check

Name: brush
Version: 0.4.0
Release: alt1

Summary: Bash/POSIX-compatible shell implemented in Rust

License: MIT
Group: Shells
Url: https://github.com/reubeno/brush

# Source-url: https://github.com/reubeno/brush/archive/refs/tags/brush-shell-v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

# Source2-url: https://github.com/reubeno/brush/releases/download/brush-shell-v%version/brush-docs.tar.gz
Source2: %name-docs-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
brush is a modern bash and POSIX compatible shell
written in Rust. Run your existing scripts and .bashrc unchanged
with syntax highlighting and auto-suggestions built in.

%prep
%setup -a1 -a2

cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
install -Dm 755 target/release/brush -t %buildroot%_bindir
install -Dm 644 man/brush.1 -t %buildroot%_man1dir

%check
%rust_test

%post
# Add brush to the list of allowed shells in /etc/shells
if ! grep %_bindir/brush %_sysconfdir/shells >/dev/null; then
    echo %_bindir/brush >>%_sysconfdir/shells
fi

%postun
# Remove brush from the list of allowed shells in /etc/shells
if [ $1 -eq 0 ]; then
    grep -v %_bindir/brush %_sysconfdir/shells >%_sysconfdir/brush.tmp
    mv %_sysconfdir/brush.tmp %_sysconfdir/shells
fi

%files
%_bindir/brush
%_man1dir/brush.1*
%doc LICENSE

%changelog
* Mon May 04 2026 Boris Yumankulov <boria138@altlinux.org> 0.4.0-alt1
- initial build for ALT Sisyphus
