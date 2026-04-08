%def_without bootstrap

Name:    opensearch
Version: 3.6.0
Release: alt1

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
# Fix trailing newline for /etc/sysconfig/opensearch
echo >> distribution/packages/src/common/env/opensearch

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

# List all using jars by it names to CLASSPATH
cp="$(find %buildroot%_datadir/%name/lib/ -name \*.jar -maxdepth 1 | sed 's|%buildroot||' | tr '\n' ':' | sed 's/:$//')"
subst "s|^OPENSEARCH_CLASSPATH=.*$|OPENSEARCH_CLASSPATH='${cp}'|" %buildroot%_datadir/%name/bin/opensearch-env

%pre
getent group opensearch >/dev/null || /usr/sbin/groupadd -r opensearch
getent passwd opensearch >/dev/null || /usr/sbin/useradd -r \
  -g opensearch -d %_sharedstatedir/%name -s /bin/bash -c "Opensearch" opensearch

%preun
%preun_service %name.service

%post
# Fix config file for 3.1.0 during upgrade from previous releases
if grep -q '^18-:-Djava.security.manager=' /etc/opensearch/jvm.options ; then
	subst '/^18-:-Djava.security.manager=/d' /etc/opensearch/jvm.options
	subst '/^-Djava.util.concurrent.ForkJoinPool.common.threadFactory=/d' /etc/opensearch/jvm.options ||:
	echo '21-:-javaagent:agent/opensearch-agent.jar' >> /etc/opensearch/jvm.options
	echo '#21-:--add-opens=java.base/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED' >> /etc/opensearch/jvm.options
fi
if [ ! -e /usr/share/opensearch/modules/cache-common/plugin-security.policy ]; then
	mkdir -p /usr/share/opensearch/modules/cache-common/
	cat > /usr/share/opensearch/modules/cache-common/plugin-security.policy <<EOF.
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * The OpenSearch Contributors require contributions made to
 * this file be licensed under the Apache-2.0 license or a
 * compatible open source license.
 */

grant {
  permission java.lang.RuntimePermission "accessClassInPackage.sun.misc";
  permission java.lang.RuntimePermission "createClassLoader";
};
EOF.
fi
# Prevent use old version of jars
for i in aggs-matrix-stats-client-2 analysis-common-2 cache-common-2 geo-2 ingest-common-2 ingest-geoip-2 ingest-user-agent-2 lang-expression-2 lang-mustache-client-2 lang-painless-2 mapper-extras-client-2 opensearch-dashboards-2 opensearch-dissect-2 opensearch-grok-2 opensearch-rest-client-2 opensearch-scripting-painless-spi-2 opensearch-ssl-config-2 parent-join-client-2 percolator-client-2 rank-eval-client-2 reindex-client-2 repository-url-2 search-pipeline-common-2 systemd-2 transport-netty4-client-2 geoip2-4.2 jackson-annotations-2.17 jackson-databind-2.17 maxmind-db-3.1 lucene-expressions-9 compiler-0.9.13 netty-buffer-4.1.11 netty-codec-4.1.11 netty-codec-http-4.1.11 netty-common-4.1.11 netty-handler-4.1.11 netty-resolver-4.1.11 netty-transport-4.1.11 netty-transport-native-unix-common-4.1.11 joni-2.2.1 httpclient-4 httpcore-4 jcodings-1.0.58
do
	find /usr/share/opensearch/modules -name ${i}\*.jar -exec mv '{}' '{}.old' ';'
done

# Restart service
%post_service %name.service

# Restore backup copy of old jars
find /usr/share/opensearch/modules -name \*.old | while read i;do mv "${i}" "${i//.old}";done

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
* Wed Apr 08 2026 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version.

* Sat Feb 14 2026 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version.

* Thu Dec 18 2025 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Sat Nov 01 2025 Andrey Cherepanov <cas@altlinux.org> 3.3.2-alt1
- New version.

* Fri Oct 24 2025 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- New version.

* Wed Oct 15 2025 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version.

* Sun Aug 24 2025 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version.

* Sat Jul 19 2025 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt3
- Fixed upgrade from previous releases.

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
