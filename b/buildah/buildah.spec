%global provider        github
%global provider_tld    com
%global project         containers
%global repo            buildah
# https://github.com/containers/buildah
%global provider_prefix %provider.%provider_tld/%project/%repo
%global import_path     %provider_prefix

%global _unpackaged_files_terminate_build 1

Name: buildah
Version: 1.29.0
Release: alt1
Summary: A command line tool used to creating OCI Images
Group: Development/Other
License: Apache-2.0
Url: https://%provider_prefix
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: go-md2man
BuildRequires: libgpgme-devel
BuildRequires: libdevmapper-devel
BuildRequires: libbtrfs-devel
BuildRequires: libassuan-devel
BuildRequires: libseccomp-devel
BuildRequires: glib2-devel
#BuildRequires: shadow-utils-subid-devel
Requires: runc >= 1.0.0
Requires: containers-common
Requires: slirp4netns >= 0.3
Requires: tzdata

%description
The buildah package provides a command line tool which can be used to
* create a working container from scratch
or
* create a working container from an image as a starting point
* mount/umount a working container's root file system for manipulation
* save container's root file system layer to create a new image
* delete a working container or an image

%prep
%setup
%patch -p1
sed -i '/docs install/d' Makefile

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export VERSION=%version
export GIT_COMMIT=%release
export BRANCH=altlinux
export GOMD2MAN=go-md2man

%golang_prepare
pushd .gopath/src/%import_path
#%%golang_build cmd/%name
%make all PREFIX=%_prefix
popd

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

pushd .gopath/src/%import_path
#%%golang_install
# rm -rf -- %buildroot%_datadir
%make DESTDIR=%buildroot PREFIX=%prefix install
%make DESTDIR=%buildroot PREFIX=%prefix install.completions
%make DESTDIR=%buildroot PREFIX=%prefix -C docs install
popd

%files
%doc LICENSE
%doc README.md
%_bindir/%name
%_man1dir/*
%_datadir/bash-completion/completions/*

%changelog
* Fri Jan 27 2023 Alexey Shabalin <shaba@altlinux.org> 1.29.0-alt1
- new version 1.29.0

* Sun Jan 22 2023 Alexey Shabalin <shaba@altlinux.org> 1.28.2-alt1
- new version 1.28.2

* Sat Oct 08 2022 Alexey Shabalin <shaba@altlinux.org> 1.28.0-alt1
- new version 1.28.0

* Mon Sep 26 2022 Alexey Shabalin <shaba@altlinux.org> 1.27.2-alt1
- new version 1.27.2

* Wed Jun 15 2022 Alexey Shabalin <shaba@altlinux.org> 1.26.1-alt1
- new version 1.26.1

* Fri Apr 08 2022 Alexey Shabalin <shaba@altlinux.org> 1.25.1-alt1
- new version 1.25.1

* Fri Mar 25 2022 Alexey Shabalin <shaba@altlinux.org> 1.24.2-alt1
- new version 1.24.2

* Fri Jan 28 2022 Alexey Shabalin <shaba@altlinux.org> 1.24.0-alt1
- 1.24.0

* Mon Nov 15 2021 Alexey Shabalin <shaba@altlinux.org> 1.23.1-alt1
- new version 1.23.1

* Fri Sep 03 2021 Alexey Shabalin <shaba@altlinux.org> 1.22.3-alt1
- new version 1.22.3

* Fri Jun 11 2021 Alexey Shabalin <shaba@altlinux.org> 1.21.1-alt1
- 1.21.1

* Tue May 18 2021 Alexey Shabalin <shaba@altlinux.org> 1.20.1-alt1
- 1.20.1

* Fri Mar 12 2021 Alexey Shabalin <shaba@altlinux.org> 1.19.8-alt1
- 1.19.8

* Fri Jan 29 2021 Alexey Shabalin <shaba@altlinux.org> 1.19.2-alt1
- 1.19.2

* Tue Dec 08 2020 Alexey Shabalin <shaba@altlinux.org> 1.18.0-alt1
- 1.18.0

* Tue Nov 10 2020 Alexey Shabalin <shaba@altlinux.org> 1.16.5-alt1
- 1.16.5

* Sat Sep 19 2020 Alexey Shabalin <shaba@altlinux.org> 1.16.1-alt2
- add tzdata to Requires

* Thu Sep 17 2020 Alexey Shabalin <shaba@altlinux.org> 1.16.1-alt1
- new version 1.16.1
- Add(): fix handling of relative paths with no ContextDir

* Wed Sep 09 2020 Alexey Shabalin <shaba@altlinux.org> 1.16.0-alt1
- new version 1.16.0

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.15.0-alt1
- new version 1.15.0

* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.9-alt1
- new version 1.14.9

* Fri May 01 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.8-alt1
- new version 1.14.8

* Thu Apr 02 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.5-alt1
- new version 1.14.5 (Fixes: CVE-2020-10696)

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.3-alt1
- new version 1.14.3

* Thu Feb 20 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.0-alt1
- 1.14.0

* Tue Jan 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.13.1-alt1
- 1.13.1

* Sun Dec 22 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.0-alt1
- 1.12.0

* Wed Dec 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.6-alt1
- 1.11.6

* Mon Oct 07 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.3-alt1
- 1.11.3

* Sun Sep 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.2-alt1
- Initial build for ALT

