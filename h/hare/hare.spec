Name:           hare
Version:        2022.05.17
Release:        alt1
Group:          Development/Other
Source:         %name-%version.tar
URL:            https://harelang.org
Summary:        Hare is a systems programming language
License:        GPLv3
# git clone     https://git.sr.ht/~sircmpwn/hare
# cd hare; git archive --prefix=hare-`git log -1 --format='%as' | tr - .`/ --output=../RPM/SOURCES/hare-`git log -1 --format='%as' | tr - .`.tar HEAD

ExclusiveArch:  x86_64
Patch:          ld-pipeexec.patch

# Automatically added by buildreq on Thu May 19 2022
# optimized out: libgpg-error python3-base sh4
BuildRequires: git-core harec scdoc qbe

%description
Hare is a systems programming language designed to be simple, stable,
and robust. Hare uses a static type system, manual memory management,
and a minimal runtime. It is well-suited to writing operating systems,
system tools, compilers, networking software, and other low-level, high
performance tasks.

%prep
%setup
%patch -p0

%build
cp config.example.mk config.mk
%make PREFIX=%_prefix
PATH=`pwd`/.bin:$PATH
%make docs/html

%install
%makeinstall_std PREFIX=%_prefix DESTDIR=%buildroot

%files
%doc README*
%doc docs/html
%_bindir/*
%_usrsrc/%name
%_man1dir/*

%check
make check

%changelog
* Thu May 19 2022 Fr. Br. George <george@altlinux.org> 2022.05.17-alt1
- Initial build for ALT
