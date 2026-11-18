Name: viddy
Version: 1.3.1
Release: alt1

Summary: A modern watch command
License: MIT
Group: Monitoring
Url: https://github.com/sachaos/viddy
Vcs: https://github.com/sachaos/viddy.git

Source0: %name-%version.tar
Source1: vendor.tar
# Use system sqlite3
Patch0: viddy-1.3.1-alt-system-sqlite.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(sqlite3)

%description
Viddy periodically runs a command and displays its output, in the
same role as watch(1). Between updates it can highlight differences,
including deletions. Past output is kept and can be rewound
(time machine mode), searched and scrolled with vim-style keys.
Key bindings and colors are configurable.

%prep
%setup -a1
%autopatch -p1
%rust_prep

%build
export VERGEN_GIT_DESCRIBE=%release
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Tue Oct 13 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
