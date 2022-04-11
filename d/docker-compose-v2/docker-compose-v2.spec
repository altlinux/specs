%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

%define binname docker-compose

Name:		docker-compose-v2
Version:	2.4.1
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
export GIT_TAG=%version
export BUILD_TAGS=e2e,kube
make -f builder.Makefile

%install
# install main binary
mkdir -p -- %buildroot%{_libexecdir}/docker/cli-plugins
install -Dpm0755 bin/%binname %buildroot%{_libexecdir}/docker/cli-plugins

%files
%doc docs
%{_libexecdir}/docker/cli-plugins/%binname

%changelog
* Mon Apr 11 2022 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- New version

* Thu Mar 10 2022 Vladimir Didenko <cow@altlinux.org> 2.3.3-alt1
- New version

* Tue Jan 11 2022 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- New version

* Wed Dec 1 2021 Vladimir Didenko <cow@altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus
