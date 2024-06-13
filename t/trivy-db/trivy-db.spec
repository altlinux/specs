Name:    trivy-db
Version: 20240613
Release: alt2

Summary: Database for Trivy
License: Apache-2.0
Group:   Other

Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-macros-systemd

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_sharedstatedir/trivy/db

install -m 0644 db/metadata.json %buildroot%_sharedstatedir/trivy/db/metadata.json
install -m 0644 db/trivy.db %buildroot%_sharedstatedir/trivy/db/trivy.db

%pre
groupadd -r -f _trivy > /dev/null 2>&1 ||:
useradd -M -r -d %_sharedstatedir/%name -g _trivy -s /dev/null -c "Trivy services" _trivy > /dev/null 2>&1 ||:

%post
SYSTEMCTL_BIN=systemctl
if sd_booted && "$SYSTEMCTL_BIN" -q is-active trivy ; then
        %post_systemd_postponed trivy
fi

%files
%doc LICENSE
%attr(0755,_trivy,_trivy) %dir %_sharedstatedir/trivy
%attr(0755,_trivy,_trivy) %dir %_sharedstatedir/trivy/db
%attr(0644,_trivy,_trivy) %_sharedstatedir/trivy/db/*

%changelog
* Thu Jun 13 2024 Cronbuild Service <cronbuild@altlinux.org> 20240613-alt2
- repocop cronbuild 20240613. At your service.

* Wed Jun 05 2024 Cronbuild Service <cronbuild@altlinux.org> 20240605-alt2
- repocop cronbuild 20240605. At your service.

* Sat Jun 01 2024 Cronbuild Service <cronbuild@altlinux.org> 20240601-alt2
- repocop cronbuild 20240601. At your service.

* Mon May 27 2024 Cronbuild Service <cronbuild@altlinux.org> 20240527-alt2
- repocop cronbuild 20240527. At your service.

* Fri May 17 2024 Cronbuild Service <cronbuild@altlinux.org> 20240517-alt2
- repocop cronbuild 20240517. At your service.

* Sun May 12 2024 Cronbuild Service <cronbuild@altlinux.org> 20240512-alt2
- repocop cronbuild 20240512. At your service.

* Wed May 08 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 20240508-alt2
- repocop cronbuild 20240508. At your service.

* Tue Mar 26 2024 Cronbuild Service <cronbuild@altlinux.org> 20240326-alt2
- repocop cronbuild 20240326. At your service.

* Tue Feb 20 2024 Cronbuild Service <cronbuild@altlinux.org> 20240220-alt2
- repocop cronbuild 20240220. At your service.

* Tue Feb 13 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 20240208-alt2
- Fix package name trivy-db-tool typo

* Thu Feb 08 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 20240208-alt1
- repocop cronbuild 20240208. At your service.

* Mon Jan 22 2024 Alexey Shabalin <shaba@altlinux.org> 20231228-alt5
- Fix post script

* Fri Jan 12 2024 Alexey Shabalin <shaba@altlinux.org> 20231228-alt4
- Restart trivy service if active only

* Thu Jan 11 2024 Alexey Shabalin <shaba@altlinux.org> 20231228-alt3
- Add useradd _trivy to %%pre
- Fix perm on files
- Revert "Add trivy-server dependency" in 20231228-alt2
- Restart trivy service at transaction end

* Fri Dec 29 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 20231228-alt2
- Add trivy-server dependency

* Thu Dec 28 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 20231228-alt1
- repocop cronbuild 20231228. At your service.

* Mon Oct 30 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 20231030-alt1
- repocop cronbuild 20231030. At your service.

* Wed Oct 25 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 20231025-alt1
- Initial build
