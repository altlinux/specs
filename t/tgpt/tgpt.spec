%define _unpackaged_files_terminate_build 1

%ifarch x86_64
%define arch amd64
%endif

%ifarch i586
%define arch 386
%endif

%ifarch aarch64
%define arch arm64
%endif

Name: tgpt
Version: 2.11.0
Release: alt1

Summary: tool that allows you to use AI in your Terminal
License: GPL-3.0
Group: Communications
Vcs: https://github.com/aandrew-me/tgpt
URL: https://github.com/aandrew-me/tgpt.git

Source: %name-%version.tar
Source2: vendor.tar

BuildRequires: golang

%description
tgpt is a Cross-platform Command-Line Interface (CLI) tool that allows you to
use AI in your Terminal.

%prep
%setup -a2

%build
CGO_ENABLED=0 \
GOARCH=%arch \
go build -mod=vendor -trimpath -ldflags="-s -w" -o ./build/tgpt-linux-%arch

%install
install -Dm 0755 build/tgpt-linux-%arch %buildroot%_bindir/tgpt

%files
%doc README.md LICENSE
%_bindir/tgpt

%changelog
* Sun Jan 25 2026 Ilya Muhamadeev <nicourced@altlinux.org> 2.11.0-alt1
- Initial build.
