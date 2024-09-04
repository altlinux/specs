# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: kopia
Version: 0.17.0
Release: alt1
Summary: Backup tool with fast, incremental backups, client-side end-to-end encryption, compression and data deduplication (CLI)
License: Apache-2.0
Group: Archiving/Backup
Url: https://kopia.io
Vcs: https://github.com/kopia/kopia

Source: %name-%version.tar
Patch3500: %name-0.15.0-loongarch64.patch
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
%patch3500 -p1
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
* Wed Sep 04 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.0-alt1
- Update to v0.17.0 (2024-04-15).

* Sun Mar 10 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.15.0-alt2
- NMU: fixed FTBFS on LoongArch.

* Tue Jan 30 2024 Vitaly Chikunov <vt@altlinux.org> 0.15.0-alt1
- First import v0.15.0 (2023-10-18).
