Name: samurai
Version: 1.3
Release: alt0.1.git737f702

Summary: ninja-compatible build tool written in C
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/michaelforney/samurai
Vcs: https://git.sr.ht/~mcf/samurai.git

Source: %name-%version.tar

#BuildRequires:

%description
samurai is a ninja-compatible build tool written in C99 with a focus on simplicity, speed, and portability.

%prep
%setup

%build
export CC=gcc
export CFLAGS="%optflags"
%make_build

%install
%makeinstall_std PREFIX=/usr

%files
%doc *.md
%_bindir/*
%_man1dir/*

%changelog
* Thu May 01 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.3-alt0.1.git737f702
- update from upstream/master

* Wed Apr 30 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.2-alt1
- Initial build for ALT.
