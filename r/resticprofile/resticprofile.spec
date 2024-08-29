# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: resticprofile
Version: 0.28.0
Release: alt1
Summary: Configuration profiles manager and scheduler for restic backup
License: GPL-3.0-only
Group: Archiving/Backup
Url: https://creativeprojects.github.io/resticprofile/
Vcs: https://github.com/creativeprojects/resticprofile
Requires: restic

Source: %name-%version.tar
Source1: hugo-theme-relearn-0.tar
Patch: %name-%version.patch
BuildRequires: golang

%description
%summary.

%prep
%setup
tar xf %SOURCE1 -C docs/themes
%autopatch -p1

%build
%ifnarch armh %ix86 loongarch64
# -buildmode=pie requires external (cgo) linking, but cgo is not enabled
export CGO_ENABLED=0
%endif
export GOFLAGS="-buildmode=pie"
commit=$(awk '$2=="v%version" {print$1}' .gear/tags/list)
ldflags="-X main.version=%version-%release
	 -X main.commit=${commit:-unknown}
	 -X main.date=$(date -I)
	 -X 'main.builtBy=%distribution'"
go build -v -x -tags no_self_update -o resticprofile -ldflags "$ldflags"

%install
install -Dp resticprofile %buildroot%_bindir/resticprofile
mkdir -p %buildroot%_datadir/%name
cp -r contrib examples -t %buildroot%_datadir/%name
pushd %buildroot%_datadir
  mkdir -p bash-completion/completions zsh/site-functions
  mv %name/contrib/completion/bash-completion.sh -T bash-completion/completions/%name
  mv %name/contrib/completion/zsh-completion.sh  -T zsh/site-functions/_%name
  rmdir %name/contrib/completion
popd

%check
%buildroot%_bindir/resticprofile version | grep -P '^%name \w+ \Q%version-%release\E\s'
%buildroot%_bindir/resticprofile version -v
%buildroot%_bindir/resticprofile --help
# Tests are not automatically runnable due to multiple failures (network,
# systemd, crontab, modules are missing). Run for a manual inspection.
go test ./... || true

%files
%doc LICENSE README.md docs/content
%_bindir/resticprofile
%_datadir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name

%changelog
* Thu Aug 29 2024 Vitaly Chikunov <vt@altlinux.org> 0.28.0-alt1
- Update to v0.28.0 (2024-08-17).

* Wed Jul 10 2024 Vitaly Chikunov <vt@altlinux.org> 0.27.1-alt1
- Update to v0.27.1 (2024-07-08).

* Fri Jun 28 2024 Vitaly Chikunov <vt@altlinux.org> 0.27.0-alt1
- Update to v0.27.0 (2024-06-25).

* Wed Feb 28 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.26.0-alt1.1
- NMU: fixed FTBFS on LoongArch (-buildmode=pie requires CGO here).

* Wed Feb 21 2024 Vitaly Chikunov <vt@altlinux.org> 0.26.0-alt1
- Update to v0.26.0 (2024-02-20).

* Sat Feb 10 2024 Vitaly Chikunov <vt@altlinux.org> 0.25.0-alt1
- Update to v0.25.0 (2024-02-07). (Fixes CVE-2023-48795).

* Mon Jan 22 2024 Vitaly Chikunov <vt@altlinux.org> 0.24.0-alt1
- First import v0.24.0 (2023-10-24).
