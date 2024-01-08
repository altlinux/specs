Name:       cproc
Version:    2022.12.14
Release:    alt1
Group:      Development/C
Source:     %name-%version.tar
License:    ISC

Summary:    Small C compliler
URL:        https://sr.ht/~mcf/cproc/

# Automatically added by buildreq on Sat Aug 21 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 python3-base sh4
BuildRequires: python3 qbe

ExclusiveArch: x86_64 aarch64 riscv64

%description
CProc is a [C11] compiler using [QBE] as a backend.
Several GNU C extensions are also implemented.

%prep
%setup
sed -i 's/\*-linux-\*gnu\*)/*-alt-linux|&/' configure

%build
./configure --prefix=%_prefix
make bootstrap

%install
%makeinstall_std

%files
%doc doc README*
%_bindir/*
%_man1dir/*

%check
make check

%changelog
* Mon Jan 08 2024 Fr. Br. George <george@altlinux.org> 2022.12.14-alt1
- Build latest version up to Dec 2023

* Wed Jan 12 2022 Fr. Br. George <george@altlinux.ru> 2021.12.06-alt1
- Version up

* Sat Aug 21 2021 Fr. Br. George <george@altlinux.ru> 2021.08.20-alt1
- Initial build for ALT
