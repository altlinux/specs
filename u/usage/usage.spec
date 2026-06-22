%define _unpackaged_files_terminate_build 1

%def_with check

Name: usage
Version: 3.5.2
Release: alt1

Summary: A specification for CLIs
License: MIT
Group: Development/Tools
Url: https://usage.jdx.dev
VCS: https://github.com/jdx/usage

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: node
BuildRequires: fish
BuildRequires: zsh
%endif

%description
Usage is a spec and CLI for defining CLI tools. Arguments, flags,
environment variables, and config files can all be defined in a Usage
spec. It can be thought of like OpenAPI (swagger) for CLIs. Here are
some potential reasons for defining your CLI with a Usage spec:

- Generate autocompletion scripts
- Generate markdown documentation
- Generate man pages
- Use an advanced arg parser in any language
- Scaffold one spec into different CLI frameworks-even different
languages
- [coming soon] Host your CLI documentation on usage.sh

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
export PATH="%buildroot%_bindir:$PATH"

# skip unstable powershell integration test
%rust_test -- --skip test_powershell_completion_integration

%files
%doc CHANGELOG.md README.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_man1dir/%name.1.*

%changelog
* Mon Jun 22 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.5.2-alt1
- Updated to version 3.5.2.

* Tue May 19 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.3.0-alt1
- Updated to version 3.3.0.

* Thu Apr 30 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.2.1-alt1
- Updated to version 3.2.1.

* Thu Apr 09 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.2.0-alt1
- Initial build for ALT.

