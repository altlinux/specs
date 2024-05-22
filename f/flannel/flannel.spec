
%global import_path github.com/flannel-io/flannel
%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name: flannel
Version: 0.25.1
Release: alt2

Summary: flannel is a network fabric for containers
License: Apache-2.0
Group: Development/Other
Url: https://github.com/flannel-io/flannel
ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: flanneld.sysconfig
Source2: flanneld.service
Source3: flannel-docker.conf
Source4: flannel-tmpfiles.conf
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc

%description
Flannel is a simple and easy way to configure
a layer 3 network fabric designed for Kubernetes.

%prep
%setup
%patch -p1

%build
export GOFLAGS="-mod=vendor"

CGO_ENABLED=1 go build -ldflags " \
    -X %import_path/pkg/version.Version=%version \
    " -o dist ./...

%install
install -D -p -m 755 dist/flannel %buildroot%_sbindir/flanneld
install -D -p -m 644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/flanneld
install -D -p -m 644 %SOURCE2 %buildroot%_unitdir/flanneld.service
install -D -p -m 644 %SOURCE3 %buildroot%_unitdir/docker.service.d/flannel.conf
install -D -p -m 755 dist/mk-docker-opts.sh %buildroot%_libexecdir/flannel/mk-docker-opts.sh
install -D -p -m 0755 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf

%files
%doc LICENSE README.md Documentation
%_sbindir/flanneld
%_unitdir/flanneld.service
%_unitdir/docker.service.d/flannel.conf
%dir %_libexecdir/flannel
%_libexecdir/flannel/mk-docker-opts.sh
%config(noreplace) %_sysconfdir/sysconfig/flanneld
%_tmpfilesdir/%name.conf

%changelog
* Wed May 22 2024 Alexander Stepchenko <geochip@altlinux.org> 0.25.1-alt2
- Add CVE fixes information to the changelog.

* Sat May 18 2024 Alexander Stepchenko <geochip@altlinux.org> 0.25.1-alt1
- 0.24.2 -> 0.25.1

* Fri Jan 19 2024 Alexander Stepchenko <geochip@altlinux.org> 0.24.2-alt1
- 0.23.0 -> 0.24.2 (Fixes: CVE-2023-48795)
- fix flannel displaying wrong version information
- use full url in the Url directive

* Wed Nov 29 2023 Alexander Stepchenko <geochip@altlinux.org> 0.23.0-alt1
- 0.22.3 -> 0.23.0 (Fixes: CVE-2023-44487, CVE-2023-39325)

* Wed Oct 04 2023 Alexander Stepchenko <geochip@altlinux.org> 0.22.3-alt1
- 0.22.0 -> 0.22.3

* Wed Jul 05 2023 Alexander Stepchenko <geochip@altlinux.org> 0.22.0-alt1
- 0.21.4 -> 0.22.0

* Mon Mar 27 2023 Alexey Shabalin <shaba@altlinux.org> 0.21.4-alt1
- New version 0.21.4.

* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 0.20.2-alt1
- new version 0.20.2

* Mon Sep 26 2022 Alexey Shabalin <shaba@altlinux.org> 0.19.2-alt1
- new version 0.19.2

* Wed Jun 15 2022 Alexey Shabalin <shaba@altlinux.org> 0.18.1-alt1
- new version 0.18.1

* Fri Jun 03 2022 Alexey Shabalin <shaba@altlinux.org> 0.18.0-alt1
- new version 0.18.0

* Mon Apr 11 2022 Alexey Shabalin <shaba@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Thu Feb 03 2022 Alexey Shabalin <shaba@altlinux.org> 0.16.3-alt1
- new version 0.16.3

* Fri Jan 28 2022 Alexey Shabalin <shaba@altlinux.org> 0.16.2-alt1
- new version 0.16.2

* Wed Dec 22 2021 Alexey Shabalin <shaba@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Thu Dec 02 2021 Alexey Shabalin <shaba@altlinux.org> 0.15.1-alt1
- new version 0.15.1

* Sat Sep 04 2021 Alexey Shabalin <shaba@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Sat Nov 14 2020 Alexey Shabalin <shaba@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Mon Jul 15 2019 Alexey Shabalin <shaba@altlinux.org> 0.11.0-alt1
- 0.11.0

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2
- NMU: remove %%ubt from release

* Sun May 13 2018 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- Initial package
