%global pkg_name github.com/docker/compose/v2

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

%define binname docker-compose

Name:		docker-compose-v2
Version:	2.14.1
Release:	alt1
Summary:	Multi-container orchestration for Docker

Group:		Development/Tools
License:	Apache-2.0
URL:		https://github.com/docker/compose

Packager:	Vladimir Didenko <cow@altlinux.org>

Source0: %name-%version.tar

ExclusiveArch: %go_arches

Requires: docker-cli >= 20.10.11-alt2

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Docker Compose is a tool for running multi-container applications
on Docker defined using the Compose file format. A Compose file is
used to define how the one or more containers that make up your
application are configured. Once you have a Compose file, you can
create and start your application with a single command: docker compose up.

%prep
%setup -q

%build
export VERSION=%version
export BUILD_TAGS=e2e,kube
export PKG_NAME=%pkg_name

go build -ldflags "-s -w -X ${PKG_NAME}/internal.Version=${VERSION}" -mod=vendor -tags "$BUILD_TAGS" -o %binname cmd/main.go

%install
# install main binary
mkdir -p -- %buildroot%{_libexecdir}/docker/cli-plugins
install -Dpm0755 %binname %buildroot%{_libexecdir}/docker/cli-plugins

%files
%doc docs
%{_libexecdir}/docker/cli-plugins/%binname

%changelog
* Mon Dec 19 2022 Vladimir Didenko <cow@altlinux.org> 2.14.1-alt1
- New version

* Tue Nov 29 2022 Vladimir Didenko <cow@altlinux.org> 2.13.0-alt1
- New version

* Thu Oct 20 2022 Vladimir Didenko <cow@altlinux.org> 2.12.0-alt1
- New version

* Fri Oct 14 2022 Vladimir Didenko <cow@altlinux.org> 2.11.2-alt1
- New version

* Thu Sep 15 2022 Vladimir Didenko <cow@altlinux.org> 2.11.0-alt1
- New version

* Wed Aug 24 2022 Vladimir Didenko <cow@altlinux.org> 2.10.0-alt1
- New version

* Tue Aug 2 2022 Vladimir Didenko <cow@altlinux.org> 2.9.0-alt1
- New version

* Tue Jul 26 2022 Vladimir Didenko <cow@altlinux.org> 2.7.0-alt1
- New version

* Tue Jun 28 2022 Vladimir Didenko <cow@altlinux.org> 2.6.1-alt1
- New version

* Fri Jun 3 2022 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- New version

* Fri May 6 2022 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt1
- New version

* Mon Apr 11 2022 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- New version

* Thu Mar 10 2022 Vladimir Didenko <cow@altlinux.org> 2.3.3-alt1
- New version

* Tue Jan 11 2022 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- New version

* Wed Dec 1 2021 Vladimir Didenko <cow@altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus
