Name: bgrep
Version: 1.0
Release: alt1

Summary: Binary Grep

License: BSD
Group: File tools
Url: https://github.com/rsharo/bgrep/

# Source-url: https://github.com/rsharo/bgrep/archive/refs/tags/bgrep-%version.tar.gz
Source: %name-%version.tar

BuildRequires: gnulib

%description
I'm terribly annoyed by the fact that grep(1) cannot look for binary strings.
I'm even more annoyed by the fact that a simple search for "binary grep"
doesn't yield a tool which could do that. So I gratuitously forked one.

Original work by tmbinc/bgrep

Feel free to modify, branch, fork, improve. Re-licenses as BSD.

%prep
%setup

%build
./bootstrap --gnulib-srcdir=/usr/share/gnulib --no-git
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
# due /dev/urandom?
#make check

%files
%_docdir/%name/README.md
%_bindir/bgrep

%changelog
* Sat Sep 04 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus

