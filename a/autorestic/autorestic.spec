# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: autorestic
Version: 1.8.3
Release: alt1
Summary: Config driven, easy backup CLI for restic
License: Apache-2.0
Group: Archiving/Backup
Url: https://autorestic.vercel.app/
Vcs: https://github.com/cupcakearmy/autorestic
Requires: restic

Source: %name-%version.tar
BuildRequires: golang

%description
Autorestic is a wrapper around the amazing restic. While being amazing
the restic CLI can be a bit overwhelming and difficult to manage if
you have many different locations that you want to backup to multiple
locations. This utility is aimed at making this easier.

%prep
%setup
# Do not allow to bypass RPM. These were only meaningful if it's installed
# via GitHub.
rm cmd/install.go cmd/upgrade.go

%build
%ifnarch armh %ix86 loongarch64 riscv64
export CGO_ENABLED=0
%endif
export GOFLAGS='-buildmode=pie'
go build -v

%install
install -Dp autorestic -t %buildroot%_bindir
for i in bash zsh fish; do
	./autorestic completion $i > completion.$i
done
install -Dpm644 completion.bash -T %buildroot%_datadir/bash-completion/completions/%name
install -Dpm644 completion.zsh  -T %buildroot%_datadir/zsh/site-functions/_%name
install -Dpm644 completion.fish -T %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
%buildroot%_bindir/autorestic --version | grep -Fx 'autorestic version %version'
%buildroot%_bindir/autorestic --help
go test -count=1 -cover %{?_is_lp64:-race} -v ./...

%files
%doc CHANGELOG.md DEVELOPMENT.md LICENSE README.md docs/pages
%_bindir/autorestic
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Thu Aug 29 2024 Vitaly Chikunov <vt@altlinux.org> 1.8.3-alt1
- Update to v1.8.3 (2024-08-28).

* Wed Apr 03 2024 Vitaly Chikunov <vt@altlinux.org> 1.8.2-alt1
- Update to v1.8.2 (2024-03-28).

* Wed Mar 13 2024 Vitaly Chikunov <vt@altlinux.org> 1.8.1-alt1
- Update to v1.8.1 (2024-03-13).

* Sat Feb 10 2024 Vitaly Chikunov <vt@altlinux.org> 1.7.11-alt1
- Update to v1.7.11 (2024-02-09).

* Mon Jan 22 2024 Vitaly Chikunov <vt@altlinux.org> 1.7.10-alt1
- First import v1.7.10 (2024-01-11).
