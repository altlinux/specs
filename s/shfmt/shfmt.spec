%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: shfmt
Version: 3.10.0
Release: alt1
Summary: Format shell programs
License: BSD-3-Clause
Group: Development/Tools
Url: https://github.com/mvdan/sh

Source: %name-%version.tar
BuildRequires: golang
BuildRequires: scdoc
%{?!_without_check:%{?!_disable_check:
BuildRequires: /dev/pts
}}

%description
shfmt formats (indents) shell scripts.

%prep
%setup

%build
%ifnarch armh %ix86 loongarch64 riscv64
export CGO_ENABLED=0
%endif
go build -v -buildmode=pie -ldflags='-X main.version=%version' ./cmd/shfmt
scdoc < cmd/%name/%name.1.scd > %name.1

%install
install -Dp shfmt -t %buildroot%_bindir
install -Dm0644 %name.1 -t %buildroot%_man1dir

%check
./shfmt -version | grep -Fx '%version'
go test ./...

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/shfmt
%_man1dir/shfmt.1.*

%changelog
* Sun Nov 24 2024 Vitaly Chikunov <vt@altlinux.org> 3.10.0-alt1
- Update to v3.10.0-4-g18ab714f (2024-11-19).
- spec: Clean up and simplify go build style.
- Do not package gosh binary as it's independent and just a proof-of-concept
  tool (shell).

* Wed Sep 11 2024 Alexey Shabalin <shaba@altlinux.org> 3.9.0-alt1
- NMU: fixed FTBFS:
  + update to 3.9.0
  + fix version info
  + not enable all test in %%check section (need revert this after fix tests)

* Tue Mar 12 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 3.5.1-alt2
- NMU: fixed FTBFS on LoongArch (updated vendored golang.org/x/sys)

* Tue Aug 02 2022 Ivan Alekseev <qwetwe@altlinux.org> 3.5.1-alt1
- Initial build
