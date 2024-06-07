%global _unpackaged_files_terminate_build 1
%global import_path github.com/containers/podman
%define _libexecdir %_usr/libexec
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define _systemdgeneratordir %_prefix/lib/systemd/system-generators

Name:     podman
Version:  5.1.1
Release:  alt1

Summary:  Manage pods, containers, and container images
License:  Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
Group:    System/Configuration/Other
Vcs:      https://github.com/containers/podman.git
Url:      https://podman.io/

Source:   %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang rpm-macros-systemd
BuildRequires: rpm-build-golang golang >= 1.20
BuildRequires: go-md2man man-db
BuildRequires: libseccomp-devel glib2-devel libgpgme-devel libgpg-error-devel libbtrfs-devel
BuildRequires: libgio-devel libostree-devel libselinux-devel libdevmapper-devel
BuildRequires: libassuan-devel libsystemd-devel libsubid-devel
BuildRequires: /proc

Conflicts: filesystem < 3

Requires: catatonit
Requires: conmon >= 2.1.7
Requires: containers-common-extra
Requires: gvisor-tap-vsock
%ifnarch %e2k %arm %ix86
Requires: netavark >= 1.6.0 aardvark-dns
%endif
Requires: oci-runtime
Requires: xz
Requires: shadow-submap

%description
%summary.

%package docker
Summary:  Emulate Docker CLI using podman
Group:    System/Configuration/Other
BuildArch: noarch
Requires: %name = %EVR
Conflicts: docker-ce
Conflicts: docker-ee
Conflicts: docker-engine
Conflicts: docker-cli
Conflicts: moby-engine

%description docker
%summary.

%package remote
Group:    System/Configuration/Other
Summary: (Experimental) Remote client for managing %name containers
Requires: %name = %EVR

%description remote
Remote client for managing %name containers.

%name-remote uses the libpod REST API to connect to a %name client to
manage pods, containers and container images. %name-remote supports ssh
connections as well.

%prep
%setup
%autopatch -p1

%build
export CGO_CFLAGS=$CFLAGS

%ifnarch %ix86 %mips32 %arm
export CGO_CFLAGS+=" -D_FILE_OFFSET_BITS=64"
%endif

%ifarch x86_64
# Builds only on x86_64 with this flag
export CGO_CFLAGS+=" -m64 -mtune=generic"
export CGO_CFLAGS+=" -fcf-protection=full"
%endif

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export RELEASE_VERSION=v%version
export RELEASE_NUMBER=%version
export GIT_COMMIT=%release

%golang_prepare

pushd .gopath/src/%import_path
#%%make test/version/version
go build -o test/version/version ./test/version/
%make_build PREFIX=%_prefix ETCDIR=%_sysconfdir TMPFILESDIR=%_tmpfilesdir SYSTEMDDIR=%_unitdir MODULESLOADDIR=%_modulesloaddir
%make docs docker-docs
popd

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"
export RELEASE_VERSION=v%version
export RELEASE_NUMBER=%version
export GIT_COMMIT=%release

pushd .gopath/src/%import_path
%make DESTDIR=%buildroot PREFIX=%_prefix ETCDIR=%_sysconfdir TMPFILESDIR=%_tmpfilesdir MODULESLOADDIR=%_modulesloaddir \
    SYSTEMDDIR=%_unitdir SYSTEMDGENERATORSDIR=%_systemdgeneratordir USERSYSTEMDGENERATORSDIR=%_systemdusergeneratordir \
    install.bin \
    install.remote \
    install.modules-load \
    install.man \
    install.completions \
    install.systemd \
    install.docker \
    install.docker-docs
popd

echo br_netfilter >> %buildroot%_modulesloaddir/podman-iptables.conf
rm -f %buildroot%_man5dir/dockerignore*
rm -f %buildroot%_man5dir/dockerfile*

%files
%_bindir/%name
%_bindir/%{name}sh
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish
%_unitdir/*
%_userunitdir/*
%_systemdgeneratordir/*
%_systemdusergeneratordir/*
%_modulesloaddir/*
%_man1dir/*
%_man5dir/*
%exclude %_man1dir/%name-remote*
%exclude %_man1dir/docker*
%doc *.md
%_tmpfilesdir/%name.conf
%_libexecdir/%name
%files remote
%_bindir/%name-remote
%_man1dir/%name-remote*
%_man1dir/docker-remote*
%_datadir/bash-completion/completions/%name-remote
%_datadir/fish/vendor_completions.d/%name-remote.fish
%_datadir/zsh/site-functions/_%name-remote

%files docker
%config(noreplace) %_sysconfdir/profile.d/%name-docker.*
%_bindir/docker
%_man1dir/docker*
%exclude %_man1dir/docker-remote*
%_tmpfilesdir/%name-docker.conf
%_datadir/user-tmpfiles.d/%name-docker.conf

%changelog
* Fri Jun 07 2024 Alexey Shabalin <shaba@altlinux.org> 5.1.1-alt1
- New version 5.1.1.

* Fri May 31 2024 Alexey Shabalin <shaba@altlinux.org> 5.1.0-alt1
- New version 5.1.0.

* Fri May 17 2024 Alexey Shabalin <shaba@altlinux.org> 5.0.3-alt1
- New version 5.0.3 (Fixes: CVE-2024-3727).

* Tue Apr 23 2024 Arseny Maslennikov <arseny@altlinux.org> 5.0.2-alt1.1
- NMU: Made the system unit generator compatible with merged-usr.
  Added a conflict on filesystem < 3 for the same reason.
  See https://altlinux.org/Usrmerge for more information.

* Fri Apr 19 2024 Alexey Shabalin <shaba@altlinux.org> 5.0.2-alt1
- New version 5.0.2.

* Wed Apr 17 2024 Alexey Shabalin <shaba@altlinux.org> 5.0.1-alt2
- v5.0 branch snapshot.

* Mon Apr 15 2024 Alexey Shabalin <shaba@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Fri Mar 22 2024 Alexey Shabalin <shaba@altlinux.org> 5.0.0-alt1
- New version 5.0.0 (Fixes: CVE-2024-1753).

* Fri Mar 15 2024 Ivan A. Melnikov <iv@altlinux.org> 4.9.3-alt1.1
- NMU: Fix build on loongarch64.

* Sat Feb 17 2024 Alexey Shabalin <shaba@altlinux.org> 4.9.3-alt1
- New version 4.9.3.

* Fri Feb 09 2024 Alexey Shabalin <shaba@altlinux.org> 4.9.2-alt1
- New version 4.9.2.

* Mon Jan 15 2024 Alexey Shabalin <shaba@altlinux.org> 4.8.3-alt2
- Add requires aardvark-dns as dns plugin.

* Wed Jan 10 2024 Alexey Shabalin <shaba@altlinux.org> 4.8.3-alt1
- New version 4.8.3 (Fixes: CVE-2023-48795 by vendoring golang.org/x/crypto v0.17.0).

* Mon Dec 25 2023 Alexey Shabalin <shaba@altlinux.org> 4.8.2-alt1
- New version 4.8.2.

* Tue Dec 05 2023 Alexey Shabalin <shaba@altlinux.org> 4.8.1-alt1
- New version 4.8.1.
- Add Requires: catatonit (ALT#47032).
- Add Requires: gvisor-tap-vsock.

* Fri Oct 06 2023 Alexey Shabalin <shaba@altlinux.org> 4.7.1-alt1
- New version 4.7.1.

* Wed Jul 05 2023 Alexey Shabalin <shaba@altlinux.org> 4.5.1-alt1
- New version 4.5.1.

* Tue May 16 2023 Alexey Shabalin <shaba@altlinux.org> 4.5.0-alt2
- Update Requires.

* Mon May 15 2023 Alexey Shabalin <shaba@altlinux.org> 4.5.0-alt1
- New version 4.5.0.
- Build with libsubid.

* Fri Apr 07 2023 Alexey Shabalin <shaba@altlinux.org> 4.4.4-alt1
- New version 4.4.4.

* Mon Mar 27 2023 Alexey Shabalin <shaba@altlinux.org> 4.4.3-alt1
- New version 4.4.3 (Fixes: CVE-2022-41723).

* Mon Feb 27 2023 Alexey Shabalin <shaba@altlinux.org> 4.4.2-alt1
- new version 4.4.2 (Fixes: CVE-2023-0778)

* Fri Jan 27 2023 Alexey Shabalin <shaba@altlinux.org> 4.3.1-alt1
- new version 4.3.1 (Fixes: CVE-2022-2989)

* Sat Oct 08 2022 Alexey Shabalin <shaba@altlinux.org> 4.2.1-alt1
- new version 4.2.1

* Sat Jul 30 2022 Alexey Shabalin <shaba@altlinux.org> 4.1.1-alt1
- new version 4.1.1

* Fri Jun 03 2022 Alexey Shabalin <shaba@altlinux.org> 4.1.0-alt1
- new version 4.1.0

* Fri Apr 08 2022 Alexey Shabalin <shaba@altlinux.org> 4.0.3-alt1
- new version 4.0.3 (Fixes: CVE-2022-27649, CVE-2022-1227, CVE-2022-27191, CVE-2022-27649)

* Wed Dec 22 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.4-alt1
- new version 3.4.4
- Add conflict with docker-cli (ALT#41569)

* Wed Dec 08 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.3-alt2
- add BR:rpm-macros-systemd

* Wed Dec 08 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.3-alt1
- new version 3.4.3 (Fixes: CVE-2021-4024, CVE-2021-41190)

* Mon Nov 15 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.2-alt1
- new version 3.4.2

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.1-alt1
- new version 3.4.1

* Mon Oct 11 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.0-alt1
- new version 3.4.0

* Fri Sep 03 2021 Alexey Shabalin <shaba@altlinux.org> 3.3.1-alt1
- new version 3.3.1

* Mon Jul 19 2021 Alexey Shabalin <shaba@altlinux.org> 3.2.3-alt1
- new version 3.2.3 (Fixes: CVE-2021-3602)

* Fri Jun 25 2021 Alexey Shabalin <shaba@altlinux.org> 3.2.1-alt1
- new version 3.2.1

* Thu Apr 22 2021 Alexey Shabalin <shaba@altlinux.org> 3.1.2-alt1
- new version 3.1.2 (Fixes: CVE-2021-20291, CVE-2021-20199)

* Tue Jan 19 2021 Alexey Shabalin <shaba@altlinux.org> 2.2.1-alt1
- new version 2.2.1

* Tue Dec 08 2020 Alexey Shabalin <shaba@altlinux.org> 2.2.0-alt1
- new version 2.2.0

* Tue Nov 10 2020 Alexey Shabalin <shaba@altlinux.org> 2.1.1-alt1
- new version 2.1.1 (Fixes: CVE-2020-14370)

* Wed Sep 09 2020 Alexey Shabalin <shaba@altlinux.org> 2.0.6-alt1
- new version 2.0.6

* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.9.2-alt1
- new version 1.9.2

* Tue Apr 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.9.0-alt1
- new version 1.9.0
- add podman-remote package
- use crun as default runtime
- add load br_netfilter kernel module
- package 87-podman-bridge.conflist as config(noreplace)
- fixed package user systemd units

* Tue Apr 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.8.2-alt2
- fix version in conmon requires

* Sat Mar 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.8.2-alt1
- new version 1.8.2

* Thu Mar 19 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.8.1-alt1
- new version 1.8.1

* Thu Dec 12 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.4-alt1
- new version 1.6.4

* Tue Oct 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.2-alt1
- new version 1.6.2

* Fri Sep 20 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.1-alt2
- Use make to build
- Add podman-docker subpackage

* Tue Sep 17 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.1-alt1
- new version 1.5.1

* Thu Jul 25 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.4-alt1
- new version 1.4.4

* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.2-alt1
- new version 1.1.2

* Mon Jan 07 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.1.2-alt1
- Initial build for Sisyphus
