%define _check_contents_method relaxed

Name:    trivy-java-db
Version: 20250429
Release: alt1

Summary: The DB is used in Trivy to discover information about jars without GAV inside them.
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
mkdir -p %buildroot%_sharedstatedir/trivy/java-db

install -m 0644 java-db/metadata.json %buildroot%_sharedstatedir/trivy/java-db/metadata.json
install -m 0644 java-db/trivy-java.db %buildroot%_sharedstatedir/trivy/java-db/trivy-java.db

%pre
groupadd -r -f _trivy > /dev/null 2>&1 ||:
useradd -M -r -d %_sharedstatedir/%name -g _trivy -s /dev/null -c 
"Trivy Java DB services" _trivy > /dev/null 2>&1 ||:

%post
SYSTEMCTL_BIN=systemctl
if sd_booted && "$SYSTEMCTL_BIN" -q is-active trivy; then
        %post_systemd_postponed trivy
fi

%files
%doc LICENSE
%attr(0755,_trivy,_trivy) %dir %_sharedstatedir/trivy
%attr(0755,_trivy,_trivy) %dir %_sharedstatedir/trivy/java-db
%attr(0644,_trivy,_trivy) %_sharedstatedir/trivy/java-db/*

%changelog
* Tue Apr 29 2025 Aleksandr Gamzin <gamzin@altlinux.org> 20250429-alt1
- Add java-db
- Add cronbuild update script and cronbuild options
- Add Licence
- 20250429-alt1

