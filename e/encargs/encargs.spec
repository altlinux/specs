Name: encargs
Version: 0.3
Release: alt2

Summary: Execute an encoded command line

License: GPL-2.0
Group: File tools
URL: https://github.com/bonktree/encargs

# This program can interpret meson.build files, and we would like to avoid
# dependency on python3.
BuildRequires: muon
# This version has a correct implementation of %%muon_meson.
BuildRequires: rpm-macros-muon >= 0.2.0-alt2
BuildRequires: gcc

Source: %name-%version.tar

%description
encargs takes a printable-encoded operand as its only non-option argument,
decodes it and interprets the result as a NUL-separated command line to be
passed to execv(3). It leaves its standard input untouched. It is vaguely
analogous to POSIX xargs: where xargs -0 takes word lists from standard input,
encargs takes a single word list from its first argument, though the NUL byte
is a word separator in the input of encargs.
The supported printable encodings are picked such that the encoded data is not
mangled by UNIX shell word split.

%prep
%setup

%build
%muon_meson
%muon_build

%install
%muon_install

%check
%muon_test

%files
%_bindir/encargs

%changelog
* Thu Mar 28 2024 Arseny Maslennikov <arseny@altlinux.org> 0.3-alt2
- Drop macro cludges; no functional change for users.

* Sat Oct 14 2023 Arseny Maslennikov <arseny@altlinux.org> 0.3-alt1
- Initial build for ALT Sisyphus.
