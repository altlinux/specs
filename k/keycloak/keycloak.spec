Name:    keycloak
Version: 24.0.4
Release: alt1

Summary: Open Source Identity and Access Management For Modern Applications and Services
License: Apache-2.0
Group:   Other
Url:     https://github.com/keycloak/keycloak

Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: x86_64

Source: %name-%version.tar
Source1: m2.tar
Source2: pnpm.tar
Source3: node.tar
Patch0: keycloak-alt-remove-javaPathHelper.patch

BuildRequires(pre): /proc rpm-build-java
BuildRequires: jpackage-17-compat
BuildRequires: maven-local

AutoProv: yes,noosgi

%description
Keycloak provides user federation, strong authentication, user management,
fine-grained authorization, and more.

%prep
%setup
%patch0 -p1
test -d ~/.m2 && rm -rf ~/.m2
tar xf %SOURCE1 -C ~
test -d ~/.local/share/pnpm && rm -rf ~/.local/share/pnpm
tar xf %SOURCE2 -C ~
tar xf %SOURCE3

%build
mvn -pl quarkus/deployment,quarkus/dist -am -DskipTests clean install

%install
mkdir -p %buildroot%_datadir/%name
tar xf quarkus/dist/target/%name-%version.tar.gz --strip=1 -C %buildroot%_datadir/%name

%files
%doc README.md
%_datadir/%name

%changelog
* Thu May 09 2024 Andrey Cherepanov <cas@altlinux.org> 24.0.4-alt1
- New version.

* Sat Apr 27 2024 Andrey Cherepanov <cas@altlinux.org> 24.0.3-alt1
- Initial build for Sisyphus (ALT #44193).
