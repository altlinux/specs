%global import_path github.com/moby/buildkit
Name:     buildkit
Version:  0.31.0
Release:  alt1

Summary:  BuildKit is a toolkit for converting source code to build artifacts
License:  Apache-2.0
Group:    Other
Url:      https://github.com/moby/buildkit

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires: containerd

%description
BuildKit is a toolkit for converting source code to build artifacts in an
efficient, expressive and repeatable manner.

%package rootless
Summary: Use buildkit rootless
Group: Other
Requires: rootlesskit %name slirp4netns

%description rootless
%summary

%prep
%setup
sed 's|/usr/local|/usr|' -i examples/systemd/{system,user}/*.service

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
export LDFLAGS="${LDFLAGS:-} -X %import_path/version.Version=%version -X %import_path/version.Revision="
%golang_build cmd/buildkitd cmd/buildctl

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dm 0644 examples/systemd/system/* -t %buildroot%_unitdir
install -Dm 0644 examples/systemd/user/* -t %buildroot%_user_unitdir

%post
%post_service %name

%preun
%preun_service %name

%files rootless
%_user_unitdir/buildkit*

%files
%_bindir/*
%_unitdir/buildkit*
%doc *.md
%doc docs

%changelog
* Fri Jun 19 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.31.0-alt1
- new version 0.31.0

* Wed May 13 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.30.0-alt1
- new version 0.30.0

* Mon Apr 20 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.29.0-alt1
- new version 0.29.0

* Mon Apr 06 2026 Alexander Danilov <admsasha@altlinux.org> 0.28.1-alt1
- new version 0.28.1

* Wed Mar 04 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.28.0-alt1
- new version 0.28.0

* Fri Jan 30 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.27.1-alt1
- new version 0.27.1

* Fri Jan 23 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.27.0-alt1
- new version 0.27.0

* Wed Jan 14 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.26.3-alt1
- new version 0.26.3
- add rootless package

* Tue Nov 18 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.26.1-alt1
- new version 0.26.1

* Mon Nov 17 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.26.0-alt1
- new version 0.26.0

* Wed Nov 05 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.25.2-alt1
- new version 0.25.2

* Thu Oct 23 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.25.1-alt1
- new version 0.25.1

* Fri Sep 05 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.24.0-alt1
- new version 0.24.0

* Wed Jul 02 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.23.2-alt1
- new version 0.23.2

* Fri Jun 20 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.23.1-alt1
- new version 0.23.1

* Wed Jun 18 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.23.0-alt1
- new version 0.23.0

* Fri May 23 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.22.0-alt1
- new version 0.22.0

* Wed Apr 30 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.21.1-alt1
- new version 0.21.1

* Mon Apr 14 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.20.2-alt1
- new version 0.20.2

* Thu Mar 06 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.20.1-alt1
- new version 0.20.1

* Fri Feb 21 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.20.0-alt1
- new version 0.20.0

* Tue Jan 21 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.19.0-alt1
- new version 0.19.0

* Wed Dec 18 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.18.2-alt1
- new version 0.18.2

* Mon Dec 09 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.18.1-alt1
- new version 0.18.1

* Wed Nov 27 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.18.0-alt1
- new version 0.18.0

* Fri Nov 22 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.2-alt1
- new version 0.17.2

* Fri Nov 08 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.1-alt1
- new version 0.17.1

* Thu Oct 31 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Mon Sep 16 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Mon Aug 19 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.2-alt1
- new version 0.15.2

* Wed Aug 14 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.1-alt1
- new version 0.15.1

* Mon Jun 24 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Wed Jun 12 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Sat Apr 27 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.2-alt1
- new version 0.13.2

* Tue Mar 19 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.1-alt1
- new version 0.13.1

* Mon Feb 05 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.5-alt1
- new version 0.12.5

* Mon Dec 04 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.4-alt1
- new version 0.12.4

* Wed Nov 15 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.3-alt1
- new version 0.12.3

* Mon Sep 11 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.2-alt1
- new version 0.12.2

* Tue Feb 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus
