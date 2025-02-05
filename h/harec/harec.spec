%def_with check

Name: harec
Version: 0.24.2
Release: alt1
Epoch: 1

Summary: Hare language compiler written in C11 for POSIX-compatible systems
License: GPLv3
Group: Development/Other
Url: https://git.sr.ht/~sircmpwn/harec

Source: %name-%version.tar

BuildRequires: qbe >= 1.2

ExclusiveArch: x86_64 aarch64

%description
Harec includes a minimal runtime under rt which is suitable for running
the test suite, but not recommended for production use. See
docs/runtime.txt for details on how to provide your own runtime
implementation, or use the Hare standard library.

%prep
%setup
sed -i "s/\$(ARCH)/%_arch/g" makefiles/linux.mk

%build
cp configs/linux.mk config.mk
%make ARCH=%_arch DEFAULT_TARGET=%_arch

%install
%make ARCH=%_arch DEFAULT_TARGET=%_arch \
PREFIX=%buildroot%_prefix \
install

%check
%make ARCH=%_arch DEFAULT_TARGET=%_arch check

%files
%_bindir/%name

%changelog
* Thu Jan 30 2025 Ulysses Apokin <ulysses@altlinux.org> 1:0.24.2-alt1
- New version.

* Thu May 19 2022 Fr. Br. George <george@altlinux.org> 2022.05.17-alt1
- Initial build for ALT
