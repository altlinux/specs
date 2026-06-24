Name:    kafka
Version: 4.3.1
Release: alt1

Summary: Apache Kafka is a distributed event store and stream-processing platform
License: Apache-2.0
Group:   System/Servers
Url:     https://github.com/apache/kafka

ExclusiveArch: x86_64 aarch64 loongarch64

Source: %name-%version.tar
# cd gradle; rm -rf build-scan-data daemon native notifications workers caches/8.* .tmp/
Source1: gradle-cache.tar
Source4: kafka.logrotate
Source5: kafka.service
Source6: kafka.sysconfig

Patch0: kafka-pathes.patch
Patch1: kafka-alt-use-gradle-8.x.patch
Patch2: kafka-alt-use-java-21.patch

BuildRequires(pre): /proc rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: gradle

AutoReqProv: yes, noosgi-fc
Requires: java-21-openjdk
Requires(preun): java-21-openjdk
Requires(post): java-21-openjdk
# Require native library and override bad library from vendoring jar
Requires: libzstd-jni

%description
Apache Kafka is a distributed event store and stream-processing platform. It is
an open-source system developed by the Apache Software Foundation written in
Java and Scala. The project aims to provide a unified, high-throughput,
low-latency platform for handling real-time data feeds.

%prep
%setup
%autopatch -p1
test -d ~/.gradle && rm -rf ~/.gradle
tar xf %SOURCE1 -C ~
rm -rf bin/windows

%build
gradle releaseTarGz --offline

%install
mkdir -p %buildroot%_libexecdir/%name
tar xf core/build/distributions/kafka_2.13-%version.tgz \
       -C %buildroot%_libexecdir/%name \
       --strip-components=1

# Specify the CLASSPATH with explicit file names
sed -i "/shopt -u nullglob/a CLASSPATH=$(find %buildroot%_libexecdir/%name/libs | sed 's|%buildroot||' | tr '\n' ':')" %buildroot%_libexecdir/%name/bin/kafka-run-class.sh

# Move config to /etc
mkdir -p %buildroot%_sysconfdir
mv %buildroot%_libexecdir/%name/config %buildroot%_sysconfdir/%name
ln -s ../../../etc/kafka %buildroot%_libexecdir/%name/config

# Install other files
install -Dpm0644 %SOURCE4 %buildroot%_logrotatedir/%name
install -Dpm0644 %SOURCE5 %buildroot%_unitdir/%name.service
install -Dpm0644 %SOURCE6 %buildroot%_sysconfdir/sysconfig/%name
mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_sharedstatedir/%name

%pre
getent group kafka >/dev/null || /usr/sbin/groupadd -r kafka
getent passwd kafka >/dev/null || /usr/sbin/useradd -r \
  -g kafka -d %_sharedstatedir/%name -s /bin/bash -c "Kafka" kafka

%preun
%preun_service %name.service

%post
if [ "$(getent passwd kafka | cut -f6 -d:)" = "/usr/kafka" ];then
	# Fix user homedir
	subst 's|/usr/kafka|/var/lib/kafka|' /etc/passwd
fi
# Generate meta.properties if needed
if [ ! -e %_logdir/%name/meta.properties ]; then
	su - kafka -c '/usr/lib/kafka/bin/kafka-storage.sh format -t $(/usr/lib/kafka/bin/kafka-storage.sh random-uuid) -c /etc/kafka/server.properties --standalone'
fi
%post_service %name.service

%files
%doc README.md
%_libexecdir/%name
%_unitdir/%name.service
%attr(0750,kafka,kafka) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_logrotatedir/%name
%attr(0755,kafka,kafka) %dir %_logdir/%name
%attr(0750,kafka,kafka) %dir %_sharedstatedir/%name

%changelog
* Wed Jun 24 2026 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version (fixes: CVE-2026-41115).

* Thu May 21 2026 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.
- Migrate from early versions.

* Tue Apr 14 2026 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt4
- Used JAVA_HOME with OpenJDK 21 in kafka-run-class.sh (ALT #58054).

* Tue Apr 07 2026 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt3
- BR: java-21-openjdk-devel.

* Tue Apr 07 2026 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt2
- Mentioned vulnerabilities (fixes: CVE-2025-48734, CVE-2025-58057,
  CVE-2025-48924, CVE-2026-24281, CVE-2026-24308, CVE-2024-29371,
  CVE-2025-67030, CVE-2024-6763, CVE-2025-11143, CVE-2025-12183,
  CVE-2025-66566, CVE-2026-33558, CVE-2026-33557, CVE-2026-35554).

* Wed Feb 18 2026 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version.

* Tue Feb 03 2026 Andrey Cherepanov <cas@altlinux.org> 4.1.1-alt1
- New version.

* Wed Dec 17 2025 Andrey Cherepanov <cas@altlinux.org> 3.9.1-alt3
- Built strictly with Java 21.

* Thu Nov 13 2025 Andrey Cherepanov <cas@altlinux.org> 3.9.1-alt2
- Rebuilt with Java 21.x.

* Wed Nov 12 2025 Andrey Cherepanov <cas@altlinux.org> 3.9.1-alt1
- New version (fixes: CVE-2025-27819, CVE-2025-27818, CVE-2025-27817).

* Tue Jun 03 2025 Ivan Khanas <xeno@altlinux.org> 3.9.0-alt2
- Rebuild with system gradle.

* Sun Mar 02 2025 Andrey Cherepanov <cas@altlinux.org> 3.9.0-alt1
- New version.

* Fri Dec 20 2024 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1
- New version.
- Security fix: CVE-2024-56128.

* Fri Dec 20 2024 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt2
- Require native libzstd-jni.

* Sun Jul 28 2024 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version (fixes: CVE-2024-31141).

* Thu Jul 04 2024 Ivan A. Melnikov <iv@altlinux.org> 3.7.1-alt1.1
- NMU: Buid on loongarch64.

* Tue Jul 02 2024 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.

* Fri May 24 2024 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus.
