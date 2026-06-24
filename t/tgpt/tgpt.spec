%define _unpackaged_files_terminate_build 1

Name: tgpt
Version: 2.11.1
Release: alt1

Summary: AI Chatbots in terminal for free
License: GPL-3.0
Group: Development/Other
URL: https://github.com/aandrew-me/tgpt
VCS: https://github.com/aandrew-me/tgpt

Source: %name-%version.tar
Source1: vendor.tar
Patch: alt-remove-update-command.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
tgpt is a Cross-platform Command-Line Interface (CLI) tool
that allows you to use AI in your Terminal.

%prep
%setup -a1
%patch -p1

%build
CGO_ENABLED=0 \
GOARCH=%go_hostarch \
go build -mod=vendor \
         -o ./build/tgpt-linux-%go_hostarch

%install
install -Dm 0755 build/tgpt-linux-%go_hostarch %buildroot%_bindir/tgpt

%files
%_bindir/tgpt
%doc README.md LICENSE

%changelog
* Wed Jun 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.11.1-alt1
- Updated to version 2.11.1.
- Removed update command.

* Wed Feb 18 2026 Ivan A. Melnikov <iv@altlinux.org> 2.11.0-alt2
- NMU: Use %%go_hostarch macro to derive the architecture name for go
  (fixes FTBFS on loongarch64).

* Sun Jan 25 2026 Ilya Muhamadeev <nicourced@altlinux.org> 2.11.0-alt1
- Initial build.
