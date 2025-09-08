%define _check_contents_method relaxed

Name:    trivy-java-db
Version: 20250904
Release: alt1

Summary: The DB is used in Trivy to discover information about jars without GAV inside them.
License: Apache-2.0
Group:   Other

Source: %name-%version.tar
BuildArch: noarch

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_sharedstatedir/trivy/java-db

install -m 0644 java-db/metadata.json %buildroot%_sharedstatedir/trivy/java-db/metadata.json
install -m 0644 java-db/trivy-java.db %buildroot%_sharedstatedir/trivy/java-db/trivy-java.db

%files
%doc LICENSE
%dir %_sharedstatedir/trivy
%dir %_sharedstatedir/trivy/java-db
%_sharedstatedir/trivy/java-db/*

%changelog
* Thu Sep 04 2025 Aleksandr Gamzin <gamzin@altlinux.org> 20250904-alt1
- Remove user from package, trivy-java-db can not work on server side
- 20250904-alt1

* Tue Apr 29 2025 Aleksandr Gamzin <gamzin@altlinux.org> 20250429-alt1
- Add java-db
- Add cronbuild update script and cronbuild options
- Add Licence
- 20250429-alt1

