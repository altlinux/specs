%def_without bootstrap

Name:    opensearch
Version: 3.1.0
Release: alt2

Summary: Open source distributed and RESTful search engine
License: Apache-2.0
Group:   Other
Url:     https://github.com/opensearch-project/OpenSearch

Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: x86_64

Source: %name-%version.tar
Source2: gradle-cache.tar
Source3: m2.tar
Patch0: opensearch-disable-test-reporting.patch
Patch1: opensearch-disable-network.patch
Patch2: opensearch-system-java.patch

BuildRequires(pre): /proc rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: gradle
BuildRequires: unzip
BuildRequires: jansi

AutoReqProv: yes, noosgi-fc
Requires: java-21-openjdk
Requires(preun): java-21-openjdk-headless
Requires(post): java-21-openjdk-headless

%description
%summary

%prep
%setup
%autopatch -p1
test -d ~/.gradle && rm -rf ~/.gradle
test -d ~/.m2 && rm -rf ~/.m2
%if_without bootstrap
tar xf %SOURCE2 -C ~
tar xf %SOURCE3 -C ~
subst 's|\.*/gradlew|gradle --offline --no-daemon|g' scripts/build.sh
%else
subst 's|\.*/gradlew|gradle --no-daemon|g' scripts/build.sh
%endif
# remove download native library
rm -rf ~/.gradle/native
# Do not build core plugins
subst '/core plugins/,$d' scripts/build.sh

%build
./scripts/build.sh -v %version -s false -a x64 -d rpm

%install
RPM="$PWD/artifacts/dist/opensearch-min-%version-no-jdk.x86_64.rpm"
mkdir -p %buildroot
cd %buildroot
rpm2cpio "$RPM" | cpio -idmv
rm -rf %buildroot%_datadir/opensearch/jdk
rm -rf %buildroot%_sysconfdir/init.d
touch %buildroot%_sysconfdir/%name/opensearch.keystore

# Adapt for old repositories
if [ "%_sysctldir" = "/lib/sysctl.d" ]; then
    mkdir -p %buildroot{%_sysctldir,%_unitdir,%_tmpfilesdir}
	mv %buildroot{%prefix,}%_sysctldir/%name.conf
	mv %buildroot{%prefix,}%_unitdir/%name.service
	mv %buildroot{%prefix,}%_tmpfilesdir/%name.conf
fi

%pre
getent group opensearch >/dev/null || /usr/sbin/groupadd -r opensearch
getent passwd opensearch >/dev/null || /usr/sbin/useradd -r \
  -g opensearch -d %_sharedstatedir/%name -s /bin/bash -c "Opensearch" opensearch

%preun
%preun_service %name.service

%post
%post_service %name.service

%files
%doc README.md
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysctldir/%name.conf
%attr(0750,opensearch,opensearch) %dir %_sysconfdir/%name
%ghost %attr(0660,opensearch,opensearch) %_sysconfdir/%name/opensearch.keystore
%config(noreplace) %attr(0660,opensearch,opensearch) %_sysconfdir/%name/log4j2.properties
%config(noreplace) %attr(0660,opensearch,opensearch) %_sysconfdir/%name/opensearch.yml
%config(noreplace) %attr(0660,opensearch,opensearch) %_sysconfdir/%name/jvm.options
%config(noreplace) %attr(0660,opensearch,opensearch) %_sysconfdir/%name/fips_java.security
%dir %_sysconfdir/%name/jvm.options.d/
%_unitdir/%name.service
%_datadir/opensearch
%attr(0755,opensearch,opensearch) %dir %_logdir/%name
%attr(0750,opensearch,opensearch) %dir %_sharedstatedir/%name
%config(noreplace) %_tmpfilesdir/%name.conf

%changelog
* Tue Jul 15 2025 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt2
- Strictly use java-21-openjdk-headless on upgrade and service run.

* Mon Jun 30 2025 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version (fixes: CVE-2025-27820).
- Built using system gradle.
- Requires java-21-openjdk.

* Wed Jun 18 2025 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Requires Java >= 21 for running.

* Tue Jun 10 2025 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version.

* Fri Feb 28 2025 Andrey Cherepanov <cas@altlinux.org> 2.19.1-alt1
- New version (fixes: CVE-2024-54160, CVE-2024-43794, CVE-2024-4068, CVE-2024-37890).

* Fri Nov 08 2024 Andrey Cherepanov <cas@altlinux.org> 2.18.0-alt1
- New version.

* Wed Oct 02 2024 Andrey Cherepanov <cas@altlinux.org> 2.17.1-alt1
- New version.

* Wed Sep 18 2024 Andrey Cherepanov <cas@altlinux.org> 2.17.0-alt1
- New version.

* Mon Aug 12 2024 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt1
- New version.
- Set home directory of opensearch user to /var/lib/opensearch.

* Sat Jul 27 2024 Andrey Cherepanov <cas@altlinux.org> 2.15.0-alt2
- Adapted to old repositories.

* Fri Jul 26 2024 Andrey Cherepanov <cas@altlinux.org> 2.15.0-alt1
- New version.

* Wed Jun 19 2024 Andrey Cherepanov <cas@altlinux.org> 2.14.0-alt1
- Initial build for Sisyphus.
