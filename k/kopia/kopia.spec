# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: kopia
Version: 0.23.1
Release: alt1
Summary: Backup tool with fast, incremental backups, client-side end-to-end encryption, compression and data deduplication (CLI)
License: Apache-2.0
Group: Archiving/Backup
Url: https://kopia.io
Vcs: https://github.com/kopia/kopia

Source: %name-%version.tar
BuildRequires: golang
%{?!_without_check:%{?!_disable_check:
BuildRequires: openssh-common
}}

%description
Kopia is a fast and secure open-source backup/restore tool that allows
you to create encrypted snapshots of your data and save the snapshots
to remote or cloud storage of your choice, to network-attached storage
or server, or locally on your machine. Kopia does not 'image' your
whole machine. Rather, Kopia allows you to backup/restore any and all
files/directories that you deem are important or critical.

%prep
%setup
# loongarch64 compatibility.
sed -i -E 's/([|&]{2} !?)riscv64/& \1loong64/' fs/localfs/local_fs_{32,64}bit.go
# Remove out-of-band auto-update functionality.
# https://github.com/kopia/kopia/issues/3617
for i in $(grep ^func cli/update_check.go | grep -Po '\b\S+(?=\()'); do
	for f in $(grep -l --exclude=update_check.go -e "$i" -r cli); do
		sed -i "/$i/d" "$f"
	done
done
sed -i '/check-for-updates/d' cli/command_repository_connect.go
rm cli/update_check.go
rm tests/end_to_end_test/auto_update_test.go

%build
%define import_path github.com/kopia/kopia
%define build_info %release%{?disttag::%disttag}
%ifnarch armh %ix86 loongarch64 riscv64
# -buildmode=pie requires external (cgo) linking, but cgo is not enabled
export CGO_ENABLED=0
%endif
go build -v -buildmode=pie -ldflags "
	-X %import_path/repo.BuildVersion=%version
	-X %import_path/repo.BuildInfo=%build_info
	-X %import_path/repo.BuildGitHubRepo=kopia/kopia
	"
for i in bash zsh; do
	./kopia --completion-script-$i > completion.$i
done

%install
install -Dp kopia -t %buildroot%_bindir
install -Dpm644 completion.bash -T %buildroot%_datadir/bash-completion/completions/%name
install -Dpm644 completion.zsh  -T %buildroot%_datadir/zsh/site-functions/_%name

%check
%buildroot%_bindir/kopia --version | grep -P '^\Q%version build: %release\E[: ]'
## Upstream tests.
%ifnarch ppc64le i586 armh
# Tests fail on them, but this does not mean it is completely non-working.
# https://github.com/kopia/kopia/issues/3601
go test -tags testing ./...
%endif
## Smoke test.
PATH=%buildroot%_bindir:$PATH
export KOPIA_PASSWORD=kopia
REPO=/tmp/repo
kopia repository create filesystem --path=$REPO
kopia repository connect filesystem --path=$REPO
kopia snapshot create .
cd ..
kopia snapshot restore --snapshot-time latest $OLDPWD x
diff -qr $OLDPWD x

%files
%doc LICENSE README.md site/content/docs
%_bindir/kopia
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name

%changelog
* Sat Jun 27 2026 Daniel Zagaynov <kotopesutility@altlinux.org> 0.23.1-alt1
- Update to v0.23.1 (2026-06-15).

* Tue May 12 2026 Vitaly Chikunov <vt@altlinux.org> 0.23.0-alt1
- Update to v0.23.0 (2026-05-08).

* Wed Dec 03 2025 Vitaly Chikunov <vt@altlinux.org> 0.22.3-alt1
- Update to v0.22.3 (2025-12-02).

* Wed Nov 26 2025 Vitaly Chikunov <vt@altlinux.org> 0.22.2-alt1
- Update to v0.22.2 (2025-11-25).

* Tue Nov 18 2025 Vitaly Chikunov <vt@altlinux.org> 0.22.0-alt1
- Update to v0.22.0 (2025-11-17).

* Tue Jul 22 2025 Vitaly Chikunov <vt@altlinux.org> 0.21.1-alt1
- Update to v0.21.1 (2025-07-22).

* Mon May 26 2025 Vitaly Chikunov <vt@altlinux.org> 0.20.1-alt1
- Update to v0.20.1 (2025-05-25).

* Tue Feb 04 2025 Vitaly Chikunov <vt@altlinux.org> 0.19.0-alt1
- Update to v0.19.0 (2025-01-22).

* Thu Nov 21 2024 Vitaly Chikunov <vt@altlinux.org> 0.18.2-alt1
- Update to v0.18.2 (2024-11-19).

* Wed Sep 04 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.0-alt1
- Update to v0.17.0 (2024-04-15).

* Sun Mar 10 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.15.0-alt2
- NMU: fixed FTBFS on LoongArch.

* Tue Jan 30 2024 Vitaly Chikunov <vt@altlinux.org> 0.15.0-alt1
- First import v0.15.0 (2023-10-18).
