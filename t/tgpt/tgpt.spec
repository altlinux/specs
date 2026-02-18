%define _unpackaged_files_terminate_build 1

Name: tgpt
Version: 2.11.0
Release: alt2

Summary: tool that allows you to use AI in your Terminal
License: GPL-3.0
Group: Communications
Vcs: https://github.com/aandrew-me/tgpt
URL: https://github.com/aandrew-me/tgpt.git

Source: %name-%version.tar
Source2: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: golang

%description
tgpt is a Cross-platform Command-Line Interface (CLI) tool that allows you to
use AI in your Terminal.

%prep
%setup -a2

%build
CGO_ENABLED=0 \
GOARCH=%go_hostarch \
go build -mod=vendor -trimpath -ldflags="-s -w" -o ./build/tgpt-linux-%go_hostarch

%install
install -Dm 0755 build/tgpt-linux-%go_hostarch %buildroot%_bindir/tgpt

%files
%doc README.md LICENSE
%_bindir/tgpt

%changelog
* Wed Feb 18 2026 Ivan A. Melnikov <iv@altlinux.org> 2.11.0-alt2
- NMU: Use %%go_hostarch macro to derive the architecture name for go
  (fixes FTBFS on loongarch64).

* Sun Jan 25 2026 Ilya Muhamadeev <nicourced@altlinux.org> 2.11.0-alt1
- Initial build.
