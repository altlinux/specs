%define _unpackaged_files_terminate_build 1

Name:           amp
Version:        0.7.1
Release:        alt2

Summary:        A complete text editor for terminal
License:        GPL-3.0
Group:          Editors
URL:            https://amp.rs/
VCS:            https://github.com/jmacdonald/amp

Source:         %name-%version.tar
Source1:        vendor.tar

Patch:          %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires:      git-core
BuildRequires: oniguruma-devel
BuildRequires: libgit2-devel

%description
Amp is a modern text editor for the terminal.
It is heavily inspired by Vi/Vim, taking its core interaction model,
simplifying it, and bundling in the essential features required
for comfortable everyday use.

%prep
%setup -a 1 -q
%patch -p1
%rust_prep

%build
export CFLAGS="-std=gnu17"
export CC="gcc -std=gnu17"
%rust_build

%install
%rust_install

%check
export CFLAGS="-std=gnu17"
export CC="gcc -std=gnu17"
%rust_test

%files
%_bindir/*
%doc README.md CHANGELOG.md LICENSE

%changelog
* Tue May 19 2026 Sergey Savelev <medovi@altlinux.org> 0.7.1-alt2
- Fixed build with gcc15 using -std=gnu17

* Fri Nov 21 2025 Sergey Savelev <medovi@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
