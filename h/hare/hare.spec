%def_with check

Name: hare
Version: 0.24.2
Release: alt1
Epoch: 1

Summary: Hare is a systems programming language
License: MPL-2.0
Group: Development/Other
Url: https://harelang.org
Vcs: https://git.sr.ht/~sircmpwn/hare

Source: %name-%version.tar
Patch0: 0001-Change-ld-to-ld.bfd.patch
Patch1: 0002-Skip-test-if-no-leapsec-data-avaible.patch
Patch2: 0003-Do-not-check-the-pseudoterminal-in-hasher.patch

BuildRequires: harec = %version
BuildRequires: scdoc >= 1.11.3
BuildRequires: qbe >= 1.2

Requires: harec = %version

ExclusiveArch: x86_64 aarch64

%description
Hare is a systems programming language designed to be simple, stable,
and robust. Hare uses a static type system, manual memory management,
and a minimal runtime. It is well-suited to writing operating systems,
system tools, compilers, networking software, and other low-level, high
performance tasks.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp configs/linux.mk config.mk
%make ARCH=%_arch DEFAULT_TARGET=%_arch

%install
%make PREFIX=%buildroot%prefix \
ARCH=%_arch DEFAULT_TARGET=%_arch \
install

%check
%make ARCH=%_arch DEFAULT_TARGET=%_arch check

%files
%_bindir/%name
%_bindir/%{name}doc
%doc %_usrsrc/%name/stdlib
%_man1dir/*
%_man5dir/*

%changelog
* Fri Jan 31 2025 Ulysses Apokin <ulysses@altlinux.org> 1:0.24.2-alt1
- New version.

* Thu May 19 2022 Fr. Br. George <george@altlinux.org> 2022.05.17-alt1
- Initial build for ALT
