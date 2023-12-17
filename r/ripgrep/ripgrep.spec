%define bin_name rg
%def_with check

Name: ripgrep
Version: 14.0.3
Release: alt2
Summary: Recursively searches directories for a regex pattern
License: MIT and Unlicense
Group: File tools
Url: https://github.com/BurntSushi/ripgrep
Source: %name-%version.tar
Source1: vendor.tar
Patch1: 0001-pcre2-sys-disable-JIT-on-LoongArch-not-supported.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: cargo-vendor-checksum
BuildRequires: diffstat

%ifarch i586 armh
%filter_from_requires /libc.so.6(GLIBC_PRIVATE)/d
%endif

%description
ripgrep is a line-oriented search tool that recursively searches
your current directory for a regex pattern.

%prep
%setup -a 1
%patch1 -p1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
diffstat -p1 -l %PATCH1 | sed -re 's@vendor/@@' | \
xargs cargo-vendor-checksum --files-in-vendor-dir

%build
# XXX: help pcre2-sys to disable JIT on LoongArch
export TARGET="%{_arch}-unknown-linux-gnu"
%rust_build --features=pcre2
./target/release/%bin_name --generate man > %bin_name.1
./target/release/%bin_name --generate complete-bash > %bin_name.bash
./target/release/%bin_name --generate complete-fish > %bin_name.fish
./target/release/%bin_name --generate complete-zsh > _%bin_name

%install
%rust_install %bin_name
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot/%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
install -m 0644 %bin_name.1 %buildroot%_man1dir
install -m 0644 %bin_name.bash %buildroot%_datadir/bash-completion/completions
install -m 0644 %bin_name.fish %buildroot%_datadir/fish/vendor_completions.d
install -m 0644 _%bin_name %buildroot/%_datadir/zsh/site-functions

%check
%rust_test

%files
%_bindir/%bin_name
%_man1dir/%bin_name.1.xz
%_datadir/bash-completion/completions/%bin_name.bash
%_datadir/zsh/site-functions/_%bin_name
%_datadir/fish/vendor_completions.d/%bin_name.fish
%doc COPYING LICENSE-MIT UNLICENSE

%changelog
* Sun Dec 17 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 14.0.3-alt2
- NMU: restored LoongArch support

* Thu Dec 14 2023 Alexander Makeenkov <amakeenk@altlinux.org> 14.0.3-alt1
- Updated to version 14.0.3.

* Wed Oct 04 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 13.0.0-alt3
- Support LoongArch architecture

* Tue Jul 20 2021 Mikhail Gordeev <obirvalger@altlinux.org> 13.0.0-alt2
- Add zsh and fish completions

* Sun Jun 13 2021 Alexander Makeenkov <amakeenk@altlinux.org> 13.0.0-alt1
- Updated to version 13.0.0

* Wed Feb 10 2021 Alexander Makeenkov <amakeenk@altlinux.org> 12.1.1-alt2
- Build with pcre2 support (closes: #39668)

* Fri Jun 12 2020 Alexander Makeenkov <amakeenk@altlinux.org> 12.1.1-alt1
- Initial build for ALT

