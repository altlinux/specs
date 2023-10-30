Name:    trivy-db
Version: 20231030
Release: alt1

Summary: Database for Trivy
License: Apache-2.0
Group:   Other

Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_sharedstatedir/trivy/db

install -m 0655 db/metadata.json %buildroot%_sharedstatedir/trivy/db/metadata.json
install -m 0655 db/trivy.db %buildroot%_sharedstatedir/trivy/db/trivy.db

%files
%doc LICENSE
%attr(0755,_trivy,_trivy) %dir %_sharedstatedir/trivy
%attr(0755,_trivy,_trivy) %dir %_sharedstatedir/trivy/db
%attr(0655,_trivy,_trivy) %dir %_sharedstatedir/trivy/db/metadata.json
%attr(0655,_trivy,_trivy) %dir %_sharedstatedir/trivy/db/trivy.db

%changelog
* Mon Oct 30 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 20231030-alt1
- repocop cronbuild 20231030. At your service.

* Wed Oct 25 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 20231025-alt1
- Initial build
