# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: rclone
Version: 1.74.3
Release: alt1
Summary: "rsync" for cloud storage
License: MIT
Group: Networking/File transfer
Vcs: https://github.com/rclone/rclone
Url: https://rclone.org/

Source: %name-%version.tar
BuildRequires: golang

%description
Rclone ("rsync for cloud storage") is a command-line program to sync
files and directories to and from different cloud storage providers:

  Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic,
  Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files,
  and many others.

%prep
%setup

%build
go build -v \
%ifarch loongarch64
	-tags math_big_pure_go \
%endif
	-buildmode=pie -ldflags=-X=github.com/rclone/rclone/fs.Version=%version
./%name completion bash %name.bash
./%name completion fish %name.fish
./%name completion zsh  %name.zsh

%install
install -Dp %name -t %buildroot%_bindir
install -Dpm644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dpm644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dpm644 %name.zsh  %buildroot%_datadir/zsh/site-functions/_%name
install -Dpm644 %name.1 -t %buildroot%_man1dir

%check
PATH=%buildroot%_bindir:$PATH
# Simplest
rclone version
rclone version | grep -Fx 'rclone %version'
# Some complicated algorithms
> /tmp/empty
rclone md5sum /tmp/empty	| grep -w d41d8cd98f00b204e9800998ecf8427e
rclone sha1sum /tmp/empty	| grep -w da39a3ee5e6b4b0d3255bfef95601890afd80709
rclone hashsum SHA-1 /tmp/empty	| grep -w da39a3ee5e6b4b0d3255bfef95601890afd80709
rclone hashsum MailruHash /tmp/empty | grep -w 0000000000000000000000000000000000000000
rclone hashsum CRC-32 /tmp/empty| grep -w 00000000
# Basic commands
rclone about .
rclone lsd . | grep -w vendor
rclone check . .			  # positive
! rclone check . .. 2>/dev/null	|| exit 2 # netagive
# Remote protocol and remote control
rclone --rc --rc-no-auth serve webdav --read-only . &
trap "kill $!" EXIT
sleep 1
rclone --webdav-url=http://127.0.0.1:8080/ check :webdav: .
rclone --webdav-url=http://127.0.0.1:8080/ copy :webdav:COPYING /tmp/
rclone rc core/stats | grep '"errors": 0,'
rclone rc core/quit
trap - EXIT
diff COPYING /tmp/COPYING

%files
%define _customdocdir %_docdir/%name
%doc COPYING *.md
%_bindir/%name
%_man1dir/%name.1*
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Tue Jun 16 2026 Mikhail Gordeev <obirvalger@altlinux.org> 1.74.3-alt1
- new version 1.74.3

* Mon Apr 27 2026 Vitaly Chikunov <vt@altlinux.org> 1.73.5-alt1
- Update to v1.73.5 (2026-04-19). (Fixes: CVE-2026-41176, CVE-2026-41179).

* Thu Jan 08 2026 Vitaly Chikunov <vt@altlinux.org> 1.72.1-alt1
- Update to v1.72.1 (2025-12-10). (Fixes: CVE-2025-61729).

* Thu Nov 27 2025 Vitaly Chikunov <vt@altlinux.org> 1.72.0-alt1
- Update to v1.72.0 (2025-11-21). (Fixes: CVE-2025-22869, CVE-2025-30204,
  CVE-2025-58181).

* Mon Mar 10 2025 Vitaly Chikunov <vt@altlinux.org> 1.69.1-alt1
- Update to v1.69.1 (2025-02-14). (Fixes: CVE-2024-52522). (ALT#53383).

* Wed Feb 28 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.65.2-alt1.1
- NMU: fixed FTBFS on LoongArch (use go implementation of math_big).

* Mon Feb 26 2024 Vitaly Chikunov <vt@altlinux.org> 1.65.2-alt1
- Update to v1.65.2 (2024-01-24). (ALT#49497).

* Sun Feb 05 2023 Vitaly Chikunov <vt@altlinux.org> 1.61.1-alt1
- Update to v1.61.1 (2022-12-23) (ALT#45130).

* Thu Jan 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.53.4-alt1
- New version 1.53.4 (Fixes: CVE-2020-28924).

* Wed Sep 09 2020 Vitaly Chikunov <vt@altlinux.org> 1.53.0-alt1
- Update v1.53.0 (2020-09-02).

* Mon Aug 10 2020 Vitaly Chikunov <vt@altlinux.org> 1.52.3-alt1
- New version 1.52.3

* Wed Jul 01 2020 Vitaly Chikunov <vt@altlinux.org> 1.52.2-alt1
- New version 1.52.2.

* Mon Jun 15 2020 Vitaly Chikunov <vt@altlinux.org> 1.52.1-alt1
- New version 1.52.1.

* Sun May 31 2020 Vitaly Chikunov <vt@altlinux.org> 1.52.0-alt1
- New version 1.52.0.

* Sun Mar 15 2020 Vitaly Chikunov <vt@altlinux.org> 1.51.0-alt1
- Update to v1.51.0.
- Add some %%check tests.

* Fri Mar 15 2019 Vitaly Chikunov <vt@altlinux.org> 1.46.0-alt1
- Initial build for Sisyphus
