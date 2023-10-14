Name: encargs
Version: 0.3
Release: alt1

Summary: Execute an encoded command line

License: GPL-2.0
Group: File tools
URL: https://github.com/bonktree/encargs

# This program can interpret meson.build files, and we would like to avoid
# dependency on python3.
BuildRequires: muon rpm-macros-muon
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
muon_fix_setup() {
   if [ "$#" -ge 4 ]; then
       case $1:$2 in
       meson:setup)
           __s="$3"; __b="$4"; shift 4
           %_bindir/muon meson setup "$__b" "$__s" "$@"
           return
       ;;
       *) break ;;
       esac
   fi
   %_bindir/muon "$@"
}
%define __muon muon_fix_setup
%muon_meson
%define __muon %_bindir/muon
%muon_build

%install
%define __muon %_bindir/muon
%muon_install

%check
%define __muon %_bindir/muon
%muon_test

%files
%_bindir/encargs

%changelog
* Sat Oct 14 2023 Arseny Maslennikov <arseny@altlinux.org> 0.3-alt1
- Initial build for ALT Sisyphus.
