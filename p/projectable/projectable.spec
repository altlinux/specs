Name: projectable
Version: 1.3.2
Release: alt1
License: MIT

Summary: A TUI file manager built for projects

Group: File tools

Url: https://github.com/dzfrias/projectable
Vcs: https://github.com/dzfrias/projectable.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

BuildRequires: perl-IPC-Cmd

%description
projectable is a highly configurable TUI file manager
built for projects. You can do handle all your project's
file-based needs from a comfortable and smooth interface.

Instead of exploring the depths of your most nested directory,
open a file simply from the projectable file listing!

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
install -Dm 755 target/release/prj %buildroot%_bindir/prj

%files
%_bindir/prj

%changelog
* Thu Apr 24 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.3.2-alt1
- Initial build
