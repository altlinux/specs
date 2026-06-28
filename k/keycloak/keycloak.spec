Name:    keycloak
Version: 26.6.4
Release: alt1

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
Patch3: 0001-Exclude-base-theme-from-settings.patch

BuildRequires(pre): /proc rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
# For kiota
BuildRequires: libicu

Requires: java-21-openjdk
Requires(post): cert-sh-functions

AutoReqProv: yes, noosgi-fc

%description
Keycloak provides user federation, strong authentication, user management,
fine-grained authorization, and more.

%prep
%setup
%autopatch -p1
test -d ~/.m2 && rm -rf ~/.m2
test -d js/node_modules && rm -rf js/{node,node_modules}
tar xf %SOURCE2 -C ~
%pom_disable_module test-framework
%pom_disable_module tests
# Unpack node modules
tar xf %SOURCE3
mkdir -p js/libs/keycloak-admin-client/.kiota/v1.31.1
cp js/kiota-binary/kiota js/libs/keycloak-admin-client/.kiota/v1.31.1

%build
#mvn -pl quarkus/deployment,quarkus/dist -am -DskipTests clean install
#export KIOTA_SKIP_VERSION_CHECK=true
#export KIOTA_DOWNLOAD_DIR="$PWD/js/kiota-binary"
export KIOTA_VERSION=v1.31.1
pushd quarkus
mvn -f ../pom.xml clean install -am -DskipTestsuite -DskipExamples -DskipTests -DskipProtoLock=true
popd

%install
mkdir -p %buildroot%_libexecdir/%name/data
tar xf quarkus/dist/target/%name-%version.tar.gz --strip=1 -C %buildroot%_libexecdir/%name
mkdir -p %buildroot%_sysconfdir
mv %buildroot%_libexecdir/%name/conf %buildroot%_sysconfdir/%name
install -Dpm 0755 %SOURCE1 %buildroot%_bindir/kc.sh
install -Dpm 0644 %SOURCE4 %buildroot%_unitdir/keycloak.service
mkdir -p %buildroot%_sharedstatedir/%name
mkdir -p %buildroot%_sysconfdir/%name/ssl/{private,certs}

%pre
getent group keycloak >/dev/null || /usr/sbin/groupadd -r keycloak
getent passwd keycloak >/dev/null || /usr/sbin/useradd -r \
  -g keycloak -d %_sharedstatedir/%name -s /bin/bash -c "Keycloak" keycloak

%preun
%preun_service keycloak

%post
# Generate SSL key
if [ ! -e /etc/keycloak/ssl/certs/keycloak.pem ]; then
  SSLDIR=%_sysconfdir/%name/ssl cert-sh generate keycloak ||:
  chown keycloak:keycloak %_sysconfdir/%name/ssl/private/keycloak.* ||:
  chmod 640 %_sysconfdir/%name/ssl/private/keycloak.* ||:
fi
# Copy template configuration
test -f /usr/share/keycloak/conf/keycloak.conf && cp -f /usr/share/keycloak/conf/keycloak.conf /etc/keycloak/keycloak.conf
# Set hostname
HOST="$(hostname -f)"
grep -q ^hostname /etc/keycloak/keycloak.conf || subst "s|^#hostname=.*|hostname=$HOST|" /etc/keycloak/keycloak.conf
# Fix path to new location of SSL key
grep -q '^https-certificate-file=/var/lib/ssl' /etc/keycloak/keycloak.conf && subst 's|^https-certificate-file=.*|https-certificate-file=/etc/keycloak/ssl/certs/keycloak.pem|' /etc/keycloak/keycloak.conf
grep -q '^https-certificate-key-file=/var/lib/ssl' /etc/keycloak/keycloak.conf && subst 's|^https-certificate-key-file=.*|https-certificate-key-file=/etc/keycloak/ssl/private/keycloak.pem|' /etc/keycloak/keycloak.conf
# Rebuild instance
/usr/bin/kc.sh build &>/dev/null ||:
chown -R keycloak:keycloak %_libexecdir/%name/data
%post_service keycloak

%files
%doc README.md
%attr(0750,keycloak,keycloak) %dir %_sysconfdir/%name
%attr(0750,keycloak,keycloak) %dir %_sysconfdir/%name/truststores
%attr(0750,keycloak,keycloak) %dir %_sysconfdir/%name/ssl
%attr(0750,keycloak,keycloak) %dir %_sysconfdir/%name/ssl/certs
%attr(0750,keycloak,keycloak) %dir %_sysconfdir/%name/ssl/private
%config(noreplace) %attr(0660,keycloak,keycloak) %_sysconfdir/%name/%name.conf
%config(noreplace) %attr(0660,keycloak,keycloak) %_sysconfdir/%name/cache-ispn.xml
%config(noreplace) %_unitdir/keycloak.service
%_bindir/kc.sh
%doc %_sysconfdir/%name/README.md
%_libexecdir/%name
%attr(0750,keycloak,keycloak) %dir %_libexecdir/%name/data
%attr(0750,keycloak,keycloak) %dir %_libexecdir/%name/lib/quarkus
%attr(0750,keycloak,keycloak) %dir %_sharedstatedir/%name

%changelog
* Fri Jun 26 2026 Andrey Cherepanov <cas@altlinux.org> 26.6.4-alt1
- New version (fixes: CVE-2026-9099, CVE-2026-9083, CVE-2026-9086,
  CVE-2026-9705, CVE-2026-9795, CVE-2026-9799, CVE-2026-9800, CVE-2026-11800).

* Sat Jun 06 2026 Andrey Cherepanov <cas@altlinux.org> 26.6.3-alt1
- New version (fixes: CVE-2026-0707, CVE-2026-4800, CVE-2026-4874,
  CVE-2026-7500, CVE-2026-8830, CVE-2026-8922, CVE-2026-9087, CVE-2026-9088,
  CVE-2026-9704, CVE-2026-9791, CVE-2026-9792, CVE-2026-9794, CVE-2026-9801,
  CVE-2026-9802, CVE-2026-37977, CVE-2026-42581).

* Sun May 31 2026 Andrey Cherepanov <cas@altlinux.org> 26.6.2-alt2
- Built with java-21-openjdk-devel.

* Wed May 20 2026 Andrey Cherepanov <cas@altlinux.org> 26.6.2-alt1
- New version (fixes: CVE-2026-0636, CVE-2026-3505, CVE-2026-4628,
  CVE-2026-4630, CVE-2026-5588, CVE-2026-5598, CVE-2026-6856, CVE-2026-7307,
  CVE-2026-7504, CVE-2026-7507, CVE-2026-7571, CVE-2026-33870, CVE-2026-33871,
  CVE-2026-37978, CVE-2026-37979, CVE-2026-37980, CVE-2026-37981,
  CVE-2026-37982).

* Wed May 13 2026 Andrey Cherepanov <cas@altlinux.org> 26.6.1-alt2
- Made /usr/lib/keycloak/lib/quarkus writeable for user keycloak.

* Mon Apr 20 2026 Andrey Cherepanov <cas@altlinux.org> 26.6.1-alt1
- New version (fixes: CVE-2026-4366, CVE-2026-4633).

* Wed Apr 08 2026 Andrey Cherepanov <cas@altlinux.org> 26.6.0-alt1
- New version.

* Fri Apr 03 2026 Andrey Cherepanov <cas@altlinux.org> 26.5.7-alt1
- New version (fixes: CVE-2025-14083, CVE-2026-1002, CVE-2026-3429,
  CVE-2026-4634, CVE-2026-4636, CVE-2026-3872, CVE-2026-4282).

* Thu Mar 19 2026 Andrey Cherepanov <cas@altlinux.org> 26.5.6-alt1
- New version (fixes: CVE-2026-1180, CVE-2026-1035, CVE-2025-14777,
  CVE-2025-14082, CVE-2026-3121, CVE-2026-3190, CVE-2026-3911,
  CVE-2026-2366).

* Fri Mar 06 2026 Andrey Cherepanov <cas@altlinux.org> 26.5.5-alt1
- New version (fixes: CVE-2026-3047, CVE-2026-3009, CVE-2026-2603,
  CVE-2026-2092).
- Fix path to new location of SSL key in /etc/keycloak/keycloak.conf.

* Sun Feb 22 2026 Andrey Cherepanov <cas@altlinux.org> 26.5.4-alt1
- New version (fixes: CVE-2026-1190, CVE-2026-0707, CVE-2025-5416,
  CVE-2026-2575, CVE-2026-2733).
- Run service under non-privileged user (ALT #57787).
- Used certificates from /etc/keycloak/ssl.

* Tue Feb 10 2026 Andrey Cherepanov <cas@altlinux.org> 26.5.3-alt1
- New version (fixes: CVE-2026-1609, CVE-2026-1529, CVE-2026-1486,
  CVE-2025-14778).

* Mon Jan 26 2026 Andrey Cherepanov <cas@altlinux.org> 26.5.2-alt1
- New version (fixes: CVE-2025-67735).

* Thu Jan 15 2026 Andrey Cherepanov <cas@altlinux.org> 26.5.1-alt1
- New version.

* Wed Jan 07 2026 Andrey Cherepanov <cas@altlinux.org> 26.5.0-alt1
- New version.

* Thu Dec 11 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.7-alt3
- Required strictly java-21-openjdk.

* Thu Dec 11 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.7-alt2
- Mentioned https://github.com/advisories/GHSA-93vm-mqpw-8wh3 (fixes: CVE-2025-13467).

* Tue Dec 02 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.7-alt1
- New version.

* Wed Nov 26 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.6-alt1
- New version.

* Thu Nov 13 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.5-alt2
- Rebuilt with Java 21.x.

* Wed Nov 12 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.5-alt1
- New version.

* Sat Nov 08 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.4-alt1
- New version.

* Fri Nov 07 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.3-alt1
- New version.

* Fri Oct 24 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.2-alt1
- New version.

* Sun Oct 19 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.1-alt1
- New version.

* Wed Oct 01 2025 Andrey Cherepanov <cas@altlinux.org> 26.4.0-alt1
- New version (fixes: CVE-2025-48924, CVE-2025-7962).

* Thu Sep 25 2025 Andrey Cherepanov <cas@altlinux.org> 26.3.5-alt1
- New version (fixes: CVE-2025-58057, CVE-2025-58056).

* Sat Sep 13 2025 Andrey Cherepanov <cas@altlinux.org> 26.3.4-alt1
- New version.

* Sat Aug 23 2025 Andrey Cherepanov <cas@altlinux.org> 26.3.3-alt1
- New version.

* Fri Aug 22 2025 Andrey Cherepanov <cas@altlinux.org> 26.3.2-alt1
- New version (fixes: CVE-2025-49574, CVE-2025-7365, CVE-2025-5416).
- Excluded base theme drom settings.

* Sat May 31 2025 Andrey Cherepanov <cas@altlinux.org> 26.2.5-alt1
- New version.

* Fri May 09 2025 Andrey Cherepanov <cas@altlinux.org> 26.2.4-alt1
- New version.

* Mon May 05 2025 Andrey Cherepanov <cas@altlinux.org> 26.2.3-alt1
- New version.

* Fri May 02 2025 Andrey Cherepanov <cas@altlinux.org> 26.2.2-alt1
- New version.
- Security fixes:
  + CVE-2025-3910 Two factor authentication bypass
  + CVE-2025-3501 Keycloak hostname verification

* Fri Apr 25 2025 Andrey Cherepanov <cas@altlinux.org> 26.2.1-alt1
- New version.

* Sat Apr 12 2025 Andrey Cherepanov <cas@altlinux.org> 26.2.0-alt1
- New version.
- Security fixes:
  + CVE-2024-12397 - HTTP Request Smuggling in io.quarkus.http:quarkus-http-core dist/quarkus

* Wed Mar 19 2025 Andrey Cherepanov <cas@altlinux.org> 26.1.4-alt1
- New version.

* Sun Mar 02 2025 Andrey Cherepanov <cas@altlinux.org> 26.1.3-alt1
- New version.
- Security fixes:
  + CVE-2025-0736 Error during JGroups channel creation may reveal secure information
  + CVE-2024-47072 XStream is vulnerable to a Denial of Service attack due to stack overflow from a manipulated binary input stream

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
