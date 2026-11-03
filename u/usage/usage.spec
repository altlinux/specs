%define _unpackaged_files_terminate_build 1

%def_with check

Name: usage
Version: 7.1.5
Release: alt1

Summary: A specification for CLIs
License: MIT
Group: Development/Tools
URL: https://usage.jdx.dev
VCS: https://github.com/jdx/usage

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: node
BuildRequires: fish
BuildRequires: zsh
BuildRequires: /dev/pts
%endif

%description
Define your CLI once. Generate the tools around it.

Usage is a portable KDL specification, a command-line utility, and a
Rust framework. Describe commands, flags, arguments, and settings in one
place, then use that definition for parsing, help, shell completions,
Markdown docs, man pages, and typed clients.

%prep
%setup -a1
%rust_prep

%build
%rust_build
./target/release/%name --completions bash > %name.bash
./target/release/%name --completions fish > %name.fish
./target/release/%name --completions zsh > %name.zsh

%install
%rust_install
install -Dm 644 cli/assets/%name.1 %buildroot%_man1dir/%name.1
install -Dm 644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name

%check
export LC_ALL="C.UTF-8"
export PATH="%buildroot%_bindir:$PATH"

# skip unstable integration tests
%rust_test -- \
    --skip test_powershell_completion_integration \
    --skip the_long_flags_offered_are_the_reference_s

%files
%doc CHANGELOG.md README.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_man1dir/%name.1.*

%changelog
* Mon Nov 02 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 7.1.5-alt1
- Updated to version 7.1.5.
- Cleaned up the spec file.

* Sat Jul 18 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.5.5-alt1
- Updated to version 3.5.5.

* Mon Jun 22 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.5.2-alt1
- Updated to version 3.5.2.

* Tue May 19 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.3.0-alt1
- Updated to version 3.3.0.

* Thu Apr 30 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.2.1-alt1
- Updated to version 3.2.1.

* Thu Apr 09 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.2.0-alt1
- Initial build for ALT.
