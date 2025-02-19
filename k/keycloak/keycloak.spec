Name:    keycloak
Version: 26.1.2
Release: alt2

Summary: Open Source Identity and Access Management For Modern Applications and Services
License: Apache-2.0
Group:   System/Servers
Url:     https://github.com/keycloak/keycloak

Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: x86_64

Source: %name-%version.tar
Source1: kc.sh
Source2: m2.tar
Source3: node.tar
Source4: keycloak.service
Patch0: keycloak-alt-remove-javaPathHelper.patch
Patch1: keycloak-alt-pathes.patch
Patch2: keycloak-alt-ssl-certificates.patch

BuildRequires(pre): /proc rpm-build-java
BuildRequires: jpackage-17-compat
BuildRequires: maven-local

Requires: java >= 17.0.0

AutoReqProv: yes, noosgi-fc

%description
Keycloak provides user federation, strong authentication, user management,
fine-grained authorization, and more.

%prep
%setup
%autopatch -p1
test -d ~/.m2 && rm -rf ~/.m2
tar xf %SOURCE2 -C ~
tar xf %SOURCE3
%pom_disable_module test-framework
%pom_disable_module tests

%build
#mvn -pl quarkus/deployment,quarkus/dist -am -DskipTests clean install
pushd quarkus
mvn -f ../pom.xml clean install -am -DskipTestsuite -DskipExamples -DskipTests -DskipProtoLock=true
popd

%install
mkdir -p %buildroot%_libexecdir/%name
tar xf quarkus/dist/target/%name-%version.tar.gz --strip=1 -C %buildroot%_libexecdir/%name
mkdir -p %buildroot%_sysconfdir
mv %buildroot%_libexecdir/%name/conf %buildroot%_sysconfdir/%name
install -Dpm 0755 %SOURCE1 %buildroot%_bindir/kc.sh
install -Dpm 0644 %SOURCE4 %buildroot%_unitdir/keycloak.service

%preun
%preun_service keycloak

%post
test -f /usr/share/keycloak/conf/keycloak.conf && cp -f /usr/share/keycloak/conf/keycloak.conf /etc/keycloak/keycloak.conf
/usr/bin/kc.sh build &>/dev/null ||:
%post_service keycloak

%files
%doc README.md
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/cache-ispn.xml
%config(noreplace) %_unitdir/keycloak.service
%_bindir/kc.sh
%dir %_sysconfdir/%name
%doc %_sysconfdir/%name/README.md
%dir %_sysconfdir/%name/truststores
%_libexecdir/%name

%changelog
* Wed Feb 19 2025 Andrey Cherepanov <cas@altlinux.org> 26.1.2-alt2
- (%%post) Copy configuration files from /usr/share/keycloak/conf.
- Mention CVE-2024-7260, fixed in 24.0.7.

* Tue Feb 11 2025 Andrey Cherepanov <cas@altlinux.org> 26.1.2-alt1
- New version.
- Security fixes:
  + CVE-2024-11736 Unrestricted admin use of system and environment variables
  + CVE-2024-11734 Denial of Service in Keycloak Server via Security Headers
  + CVE-2024-10451 Sensitive Data Exposure in Keycloak Build Process
  + CVE-2024-10270 Potential Denial of Service
  + CVE-2024-10492 Keycloak path trasversal
  + CVE-2024-9666  Keycloak proxy header handling Denial-of-Service (DoS) vulnerability
  + CVE-2024-10039 Bypassing mTLS validation
  + CVE-2021-44549 org.eclipse.angus/angus-mail: Enabling Secure Server Identity Checks for Safer SMTPS Communication
  + CVE-2024-8883 Vulnerable Redirect URI Validation Results in Open Redirect
  + CVE-2024-8698 Improper Verification of SAML Responses Leading to Privilege Escalation in Keycloak
  + CVE-2024-7341 Session fixation in the SAML adapters

* Sun May 26 2024 Andrey Cherepanov <cas@altlinux.org> 24.0.4-alt2
- Moved config to /etc/keycloak.
- Marked config file as %%config(noreplace) (ALT #50434).
- Moved keycloak homedir to /usr/lib/keycloak.
- Added service file

* Thu May 09 2024 Andrey Cherepanov <cas@altlinux.org> 24.0.4-alt1
- New version.

* Sat Apr 27 2024 Andrey Cherepanov <cas@altlinux.org> 24.0.3-alt1
- Initial build for Sisyphus (ALT #44193).
