%define _unpackaged_files_terminate_build 1

Name: taplo
Version: 0.10.0
Release: alt2

Summary: A TOML toolkit written in Rust
License: MIT
Group: File tools
Url: https://taplo.tamasfe.dev
Vcs: https://github.com/tamasfe/taplo

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust

ExcludeArch: i586 ppc64le armh

%description
Taplo CLI aims to be an one stop shop tool for working with TOML files
via the command line. The features include validation, formatting, and
querying TOML documents with a jq-like fashion.

%prep
%setup -a1
%rust_prep

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
     ./vendor/pprof/.cargo-checksum.json

%build
%rust_build --features lsp

%install
%rust_install
# Note that during the build, a libtaplo_lsp.so is also built,
# which does not seem to be used anywhere and cannot be linked through stable API.

pushd %buildroot
mkdir -pv .%_datadir/bash-completion/completions/ .%_datadir/zsh/site-functions/ .%_datadir/fish/vendor_completions.d/

.%_bindir/taplo completions bash > .%_datadir/bash-completion/completions/taplo
.%_bindir/taplo completions zsh > .%_datadir/zsh/site-functions/_taplo
.%_bindir/taplo completions fish > .%_datadir/fish/vendor_completions.d/taplo.fish
popd

%check
%rust_test

%files
%doc LICENSE README.md
%_bindir/taplo
%_datadir/bash-completion/completions/taplo
%_datadir/zsh/site-functions/_taplo
%_datadir/fish/vendor_completions.d/taplo.fish

%changelog
* Tue Oct 06 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.10.0-alt2
- Add shell completions (Closes: 60275).

* Tue Sep 09 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.10.0-alt1
- New version (0.10.0).

* Tue May 06 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.9.3-alt4
- Add lsp feature during build (Closes: 53928).
- Update vendored sources.
- Add remotes to upstream.

* Thu Dec 19 2024 Michael Chernigin <chernigin@altlinux.org> 0.9.3-alt3
- Exclude armh.

* Fri Nov 22 2024 Ilya Sorochan <k0tran@altlinux.org> 0.9.3-alt2
- Add patch for pprof crate to add support loongarch64.

* Wed Nov 20 2024 Michael Chernigin <chernigin@altlinux.org> 0.9.3-alt1
- Initial build for ALT Linux.
