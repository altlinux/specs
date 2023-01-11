
%global import_path github.com/flannel-io/flannel
%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name: flannel
Version: 0.20.2
Release: alt1
Summary: flannel is a network fabric for containers
Group: Development/Other
License: Apache-2.0
Url: https://%import_path
Source: %name-%version.tar
Source1: flanneld.sysconfig
Source2: flanneld.service
Source3: flannel-docker.conf
Source4: flannel-tmpfiles.conf

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc

%description
Flannel is a simple and easy way to configure
a layer 3 network fabric designed for Kubernetes.

%prep
%setup -q

%build
gofmt -w -r "x -> \"%{version}\"" version/version.go

%ifarch x86_64
CGO_ENABLED=1 \
%else
CGO_ENABLED=0 \
%endif
go build -ldflags " \
    -s -w \
    -X github.com/flannel-io/flannel/version.Version=%version \
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
