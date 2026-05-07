%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: deepseek-tui
Version: 0.8.16
Release: alt1

Summary: Coding agent for DeepSeek models that runs in your terminal
License: MIT
Group: Development/Tools
Url: https://github.com/Hmbown/DeepSeek-TUI
Vcs: https://github.com/Hmbown/DeepSeek-TUI

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires: rust-cargo
BuildRequires: libdbus-devel

%description
Terminal coding agent for DeepSeek V4. It runs from the deepseek
command, streams reasoning blocks, edits local workspaces with approval
gates, and includes an auto mode that chooses both model and thinking
level per turn.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml

%build
cargo build %_smp_mflags --release --offline

%install
install -vpD -m0755 target/release/deepseek -t %buildroot%_bindir
install -vpD -m0755 target/release/deepseek-tui -t %buildroot%_bindir
install -vpD -m0755 target/release/deepseek-app-server -t %buildroot%_bindir

%files
%doc CHANGELOG.md LICENSE README.md
%_bindir/deepseek
%_bindir/deepseek-tui
%_bindir/deepseek-app-server

%changelog
* Thu May 07 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.16-alt1
- Packaged for ALT Sisyphus.
