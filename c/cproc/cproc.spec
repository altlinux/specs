Name:       cproc
# git log -1 --format='%as' | tr - .  
Version:    2021.12.06
Release:    alt1
Group:      Development/C
# git clone     https://git.sr.ht/~mcf/cproc
# cd cproc; git archive --prefix=cproc-`git log -1 --format='%as' | tr - .`/ --output=../RPM/SOURCES/cproc-`git log -1 --format='%as' | tr - .`.tar HEAD
Source:     %name-%version.tar
License:    ISC

Summary:    Small C compliler
URL:        https://sr.ht/~mcf/cproc/

# Automatically added by buildreq on Sat Aug 21 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 python3-base sh4
BuildRequires: python3 qbe

# TODO: check if qbe if armh-ready (buggy as of 2021.07.06)
ExclusiveArch: x86_64

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

%check
make check

%changelog
* Wed Jan 12 2022 Fr. Br. George <george@altlinux.ru> 2021.12.06-alt1
- Version up

* Sat Aug 21 2021 Fr. Br. George <george@altlinux.ru> 2021.08.20-alt1
- Initial build for ALT
