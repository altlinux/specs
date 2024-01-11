Name:    trivy-db
Version: 20231228
Release: alt3

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
%post_systemd_postponed trivy

%files
%doc LICENSE
%attr(0755,_trivy,_trivy) %dir %_sharedstatedir/trivy
%attr(0755,_trivy,_trivy) %dir %_sharedstatedir/trivy/db
%attr(0644,_trivy,_trivy) %_sharedstatedir/trivy/db/*

%changelog
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
