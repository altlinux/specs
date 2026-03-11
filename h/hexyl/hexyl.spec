%define _unpackaged_files_terminate_build 1

Name:           hexyl
Version:        0.17.0
Release:        alt1

Summary:        A command-line hex viewer.
License:        MIT
Group:          File tools
URL:            https://github.com/sharkdp/hexyl

Source:         %name-%version.tar
Source1:        vendor.tar

Patch:          %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust

%description
Hexyl is a hex viewer for the terminal.
It uses a colored output to distinguish different categories
of bytes (NULL bytes, printable ASCII characters,
ASCII whitespace characters, other ASCII characters and non-ASCII).

%prep
%setup -a 1 -q
%patch -p1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/*
%doc README.md CHANGELOG.md

%changelog
* Mon Feb 16 2026 Sergey Savelev <medovi@altlinux.org> 0.17.0-alt1
- New version 0.17.0.
- Use macro %%rust_prep.

* Wed Feb 26 2025 Sergey Savelev <medovi@altlinux.org> 0.16.0-alt1
- Initial build for Sisyphus.
