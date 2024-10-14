%global pkg_name github.com/docker/compose/v2

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

%define binname docker-compose

Name:		docker-compose-v2
Version:	2.29.7
Release:	alt2
Summary:	Multi-container orchestration for Docker

Group:		Development/Tools
License:	Apache-2.0
URL:		https://github.com/docker/compose

Packager:	Vladimir Didenko <cow@altlinux.org>

Source0: %name-%version.tar

ExclusiveArch: %go_arches

Requires: /usr/bin/docker

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
Provides: docker-compose = %version-%release
Obsoletes: docker-compose <= 1.29.2

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
* Mon Oct 14 2024 Vladimir Didenko <cow@altlinux.org> 2.29.7-alt2
- Obsolete docker-compose v1

* Fri Sep 20 2024 Vladimir Didenko <cow@altlinux.org> 2.29.7-alt1
- New version

* Tue Sep 17 2024 Vladimir Didenko <cow@altlinux.org> 2.29.5-alt1
- New version

* Wed Aug 14 2024 Vladimir Didenko <cow@altlinux.org> 2.29.2-alt1
- New version

* Fri Aug 2 2024 Vladimir Didenko <cow@altlinux.org> 2.29.1-alt2
- require /usr/bin/docker instead of docker-cli (closes: #51024)

* Wed Jul 24 2024 Vladimir Didenko <cow@altlinux.org> 2.29.1-alt1
- New version

* Mon Jul 22 2024 Vladimir Didenko <cow@altlinux.org> 2.29.0-alt1
- New version

* Fri Jun 28 2024 Vladimir Didenko <cow@altlinux.org> 2.28.1-alt1
- New version

* Mon Jun 24 2024 Vladimir Didenko <cow@altlinux.org> 2.28.0-alt1
- New version

* Mon Jun 10 2024 Vladimir Didenko <cow@altlinux.org> 2.27.1-alt1
- New version

* Sat Apr 27 2024 Vladimir Didenko <cow@altlinux.org> 2.27.0-alt1
- New version

* Wed Apr 3 2024 Vladimir Didenko <cow@altlinux.org> 2.26.1-alt1
- New version

* Tue Mar 26 2024 Vladimir Didenko <cow@altlinux.org> 2.26.0-alt1
- New version

* Thu Mar 21 2024 Vladimir Didenko <cow@altlinux.org> 2.25.0-alt1
- New version

* Tue Mar 12 2024 Vladimir Didenko <cow@altlinux.org> 2.24.7-alt1
- New version

* Tue Feb 27 2024 Vladimir Didenko <cow@altlinux.org> 2.24.6-alt1
- New version

* Mon Feb 5 2024 Vladimir Didenko <cow@altlinux.org> 2.24.5-alt1
- New version

* Fri Jan 26 2024 Vladimir Didenko <cow@altlinux.org> 2.24.3-alt1
- New version

* Tue Jan 23 2024 Vladimir Didenko <cow@altlinux.org> 2.24.2-alt1
- New version

* Mon Jan 15 2024 Vladimir Didenko <cow@altlinux.org> 2.24.0-alt1
- New version

* Thu Nov 23 2023 Vladimir Didenko <cow@altlinux.org> 2.23.3-alt1
- New version

* Fri Oct 27 2023 Vladimir Didenko <cow@altlinux.org> 2.23.0-alt1
- New version

* Thu Oct 12 2023 Vladimir Didenko <cow@altlinux.org> 2.22.0-alt1
- New version

* Wed Sep 6 2023 Vladimir Didenko <cow@altlinux.org> 2.21.0-alt1
- New version

* Wed Jul 26 2023 Vladimir Didenko <cow@altlinux.org> 2.20.2-alt1
- New version

* Fri Jul 7 2023 Vladimir Didenko <cow@altlinux.org> 2.19.1-alt1
- New version

* Thu Jun 22 2023 Vladimir Didenko <cow@altlinux.org> 2.19.0-alt1
- New version

* Tue May 23 2023 Vladimir Didenko <cow@altlinux.org> 2.18.1-alt1
- New version

* Wed May 3 2023 Vladimir Didenko <cow@altlinux.org> 2.17.3-alt1
- New version

* Tue Apr 4 2023 Vladimir Didenko <cow@altlinux.org> 2.17.2-alt1
- New version

* Mon Feb 13 2023 Vladimir Didenko <cow@altlinux.org> 2.16.0-alt1
- New version

* Thu Jan 12 2023 Vladimir Didenko <cow@altlinux.org> 2.15.1-alt1
- New version

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
