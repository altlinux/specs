Name: qbe
Version: 1.1
Release: alt1
Epoch: 1
Group: Development/C
Source: %name-%version.tar.xz
Patch: return.patch
License: BSD

Summary: C Compiler Backend
Url: https://c9x.me/compile/
# TODO ppc64 if possible
ExclusiveArch: x86_64 aarch64 riscv64

%description
QBE aims to be a pure C embeddable backend that provides 70%% of the
performance of advanced compilers in 10%% of the code. Its small size
serves both its aspirations of correctness and our ability to
understand, fix, and improve it. It also serves its users by providing
trivial integration and great flexibility.

%prep
%setup
%patch -p1

%build
make CC=gcc
make CC=gcc -C minic clean minic

%install
install -D %name %buildroot%_bindir/%name
install -D minic/minic %buildroot%_bindir/%name-minic

%files
%doc doc README*
%_bindir/*

%check
make check

%changelog
* Mon Jan 08 2024 Fr. Br. George <george@altlinux.org> 1:1.1-alt1
- Autobuild version bump to 1.1

* Mon Jan 08 2024 Fr. Br. George <george@altlinux.org> 1.0-alt1
- Resurrect with author's versioning
