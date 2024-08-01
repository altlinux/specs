%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%global import_path github.com/restic/restic
Name:     restic
Version: 0.17.0
Release: alt1
Summary:  Fast, secure, efficient backup program
License:  BSD-2-Clause
Group:    Archiving/Backup
Vcs:      https://github.com/restic/restic
Url:      https://restic.net/

Source:   %name-%version.tar
BuildRequires: golang
%{?!_without_check:%{?!_disable_check:
BuildRequires: python3
}}

%description
restic is a backup program that is fast, efficient and secure.

Saving a backup on the same machine is nice but not a real backup
strategy. Therefore, restic supports the following backends for storing
backups natively:

  Local directory
  sftp server (via SSH)
  HTTP REST server (protocol, rest-server)
  Amazon S3 (or compatible such as Minio server)
  OpenStack Swift
  BackBlaze B2
  Microsoft Azure Blob Storage
  Google Cloud Storage
  And many other services via the rclone Backend

%prep
%setup
grep -Fx %version VERSION

%build
# build.go cannot be used because of `-trimpath`.
go build -v -buildmode=pie -ldflags '-X main.version=%version' ./cmd/restic

%install
install -Dp restic -t %buildroot%_bindir
install -Dpm633 doc/man/*.1 -t %buildroot/%_man1dir
mkdir -p %buildroot%_datadir/{zsh/site-functions,bash-completion/completions,fish/vendor_completions.d}
%buildroot%_bindir/%name generate --zsh-completion %buildroot%_datadir/zsh/site-functions/_%name
%buildroot%_bindir/%name generate --bash-completion %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name generate --fish-completion %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
PATH=%buildroot%_bindir:$PATH
restic version
## Upstream tests.
# No user xattrs support on tmpfs on Linux before 6.6
# https://github.com/restic/restic/issues/4646
printf '6.6\n%s\n' $(uname -r) | sort -CV || {
	sed -i '/rtest.Assert/s/n2.ExtendedAttributes/test.ExtendedAttributes/' internal/restic/node_test.go
	sed -i '/rtest.Assert/s/nodeActual.sameExtendedAttributes(node)/true/' internal/restic/node_xattr_all_test.go
}
# Some tests have hardcoded 'python' name https://github.com/restic/restic/issues/4968
mkdir /usr/src/bin
ln -s %__python3 -T /usr/src/bin/python
# Cannot test with fusermount in Hasher.
RESTIC_TEST_FUSE=0 \
go test ./...
## Smoke test.
export RESTIC_PASSWORD=testic
restic --repo ../test init
restic --repo ../test backup .
restic --repo ../test restore latest -t ../x
cd ../x
restic --repo ../test backup .
S=($(restic --repo ../test snapshots | grep localhost | cut -d' ' -f1))
restic --repo ../test diff ${S[*]}
restic --repo ../test check --read-data
cd ..
diff -qr %name-%version x

%files
%define _customdocdir %_docdir/%name
%doc LICENSE *.md doc/*.rst doc/images
%_bindir/*
%_man1dir/*.1*
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Thu Aug 01 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.0-alt1
- Update to v0.17.0 (2024-07-26).

* Fri Jul 05 2024 Vitaly Chikunov <vt@altlinux.org> 0.16.5-alt1
- Update to v0.16.5 (2024-07-01).

* Tue Feb 06 2024 Vitaly Chikunov <vt@altlinux.org> 0.16.4-alt1
- Update to v0.16.4 (2024-02-04).
- Fixes (non-default) 'max' compression level bug in 0.16.3. You can use
  'restic check --read-data' to make sure you're not affected.

* Sat Jan 20 2024 Vitaly Chikunov <vt@altlinux.org> 0.16.3-alt1
- Update to v0.16.3 (2024-01-14).
- spec: Add more testing, update %%description, change build method, install
  documentation.

* Tue Oct 31 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.2-alt1
- new version 0.16.2

* Tue Aug 01 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Wed Apr 26 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.2-alt1
- new version 0.15.2

* Thu Feb 02 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.1-alt1
- new version 0.15.1

* Thu Jan 19 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Aug 26 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Fri Apr 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.1-alt1
- new version 0.13.1

* Tue Mar 29 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Wed Jan 26 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.1-alt1
- Update to v0.12.1.
- Add completions

* Wed Feb 17 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.0-alt1
- Update to v0.12.0.

* Sun Nov 08 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.0-alt1
- Update to v0.11.0.

* Sun Mar 15 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.6-alt1
- Update to v0.9.6.
- Add some tests into %%check.

* Fri Mar 15 2019 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus
