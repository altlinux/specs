Name: tui-journal
Version: 0.16.1
Release: alt1
License: MIT

Summary: Your journal app if you live in a terminal

Group: File tools

Url: https://github.com/AmmarAbouZor/tui-journal
Vcs: https://github.com/AmmarAbouZor/tui-journal.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

%description
TUI-Journal is a terminal-based application written in Rust that allows
you to write and manage your journal/notes from within the comfort of your
terminal. It provides a simple and efficient interface for creating and
organizing your thoughts, ideas, and reflections. TUI-Journal supports two
different local back-ends: a plain text back-end in JSON format
and a database back-end using SQLite.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
install -Dm 755 target/release/tjournal %buildroot%_bindir/tjournal

%files
%_bindir/tjournal

%changelog
* Thu Jul 31 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.16.1-alt1
- new version 0.16.1 (with rpmrb script)

* Sat Jul 26 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.16.0-alt1
- new version 0.16.0 (with rpmrb script)

* Thu Apr 24 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.15.0-alt1
- Initial build
