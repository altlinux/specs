%define _unpackaged_files_terminate_build 1

%def_with check

Name: mise
Version: 2026.10.25
Release: alt1

Summary: Dev tools, env vars, and tasks in one CLI
License: MIT
Group: Development/Tools
URL: https://mise.jdx.dev
VCS: https://github.com/jdx/mise

# rustc: memory allocation failure during mise linking
ExcludeArch: %ix86

Source: %name-%version.tar
Source1: vendor.tar

Requires: usage
# https://bugzilla.altlinux.org/58938
Requires: libatomic1

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(openssl)
BuildRequires: cmake
BuildRequires: clang-devel

%if_with check
BuildRequires: git
BuildRequires: /dev/pts
%endif

%description
Mise installs a project's tools, sets its environment variables, and runs its
tasks from one mise.toml that works in your shell, editor, and CI. With mise
bootstrap, it can also set up a whole machine: packages, dotfiles, and services.

%prep
%setup -a1
%rust_prep

%build
%rust_build
./target/release/%name completion bash > %name.bash
./target/release/%name completion fish > %name.fish
./target/release/%name completion zsh > %name.zsh

%install
%rust_install
install -Dm 644 man/man1/%name.1 %buildroot%_man1dir/%name.1
install -Dm 644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name

# disable mise self update
install -Dm 644 /dev/null %buildroot%_libexecdir/%name/.disable-self-update

%check
# skip tests that require network access
%rust_test -- \
    --skip mise_binary_services_aube_node_gyp_bootstrap_trampoline \
    --skip system_install::tests::archive_boundary

%files
%doc CHANGELOG.md README.md SECURITY.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_libexecdir/%name
%_man1dir/%name.1.*

%changelog
* Mon Nov 02 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2026.10.25-alt1
- Updated to version 2026.10.25.
- Cleaned up the spec file.

* Sat Jul 18 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2026.7.7-alt1
- Updated to version 2026.7.7.

* Mon Jun 22 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2026.6.12-alt1
- Updated to version 2026.6.12.
- Added libatomic1 to requires (Closes: #58938).

* Mon May 18 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2026.5.11-alt1
- Updated to version 2026.5.11.

* Thu Apr 30 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2026.4.27-alt1
- Updated to version 2026.4.27.

* Thu Apr 09 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2026.4.5-alt1
- Initial build for ALT.
