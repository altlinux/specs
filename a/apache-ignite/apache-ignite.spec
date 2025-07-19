%def_without bootstrap

Name:    apache-ignite
Version: 3.0.0
Release: alt3

Summary: Distributed database for high-performance computing
License: Apache-2.0
Group:   Databases
Url:     https://ignite.apache.org

ExclusiveArch: x86_64 aarch64 loongarch64

Source: %name-%version-src.zip
Source1: gradle-8.7-rc-4-bin.zip
Source2: gradle-cache.tar

BuildRequires(pre): /proc rpm-build-java
BuildRequires: jpackage-11-compat
BuildRequires: maven-local
BuildRequires: unzip

AutoReqProv: yes, noosgi-fc

%description
Apache Ignite 3 is a distributed database for high-performance computing.

* ACID TRANSACTIONS: Ignite can operate in a strongly consistent mode that
provides full support for distributed ACID transactions executed at the
Serializable isolation level.

* DISTRIBUTED SQL: Use Ignite as a traditional SQL database by leveraging JDBC
drivers, ODBC drivers, or the native SQL APIs that are available for Java, C#,
C++, and other programming languages.

* COMPUTE API: With traditional databases, for in-place calculations, you use
stored procedures that are written in a language such as PL/SQL. With Ignite,
you use modern JVM languages to develop and execute custom tasks across your
distributed database.

* SCHEMA-DRIVEN ARCHITECTURE: Ignite built around schema-driven model ensuring
consistency between DDL, internal models and data.

* PLUGABLE STORAGE ENGINES: Ignite's modular architecture enables the
customization of underlying data and metadata storage, offering in-memory
storage and RocksDB as default options.

* UNIFIED CLI TOOL AND REST API: Management tools now include built-in CLI and
REST API allowing simple access and configuration of Ignite cluster.

%package -n ignite3-cli
Summary: Command-line interface for Apache Ignite
Group: Databases
Requires: java >= 11

%description -n ignite3-cli
%summary

%package -n ignite3-java-client
Summary: Apache Ignite Java Client
Group: Development/Java

%description -n ignite3-java-client
%summary

%package -n ignite3-db
Summary: Apache Ignite
Group: Databases
Requires: java >= 11

%description -n ignite3-db
%summary

%prep
%setup -n %name-%version-src
unzip %SOURCE1
test -d ~/.gradle && rm -rf ~/.gradle
test -d ~/.m2 && rm -rf ~/.m2
%if_without bootstrap
tar xf %SOURCE2 -C ~
%endif

%build
export PATH=$PATH:$PWD/gradle-8.7-rc-4/bin
%global gradle_target buildRpm
%if_without bootstrap
gradle --no-daemon --offline %gradle_target
%else
gradle --no-daemon %gradle_target
%endif

%install
mkdir -p %buildroot
cwd="$PWD/packaging"
cd %buildroot
rpm2cpio $cwd/cli/build/distributions/ignite3-cli-%version.noarch.rpm | cpio -idmv
rpm2cpio $cwd/db/build/distributions/ignite3-db-%version.noarch.rpm | cpio -idmv
rpm2cpio $cwd/client/java/build/distributions/ignite3-java-client-%version.noarch.rpm | cpio -idmv

mkdir -p %buildroot%_sharedstatedir/ignite3db
mkdir -p %buildroot%_logdir/ignite3db

# Install service file
install -Dpm 0644 %buildroot%_libexecdir/ignite3db/ignite3db.service %buildroot%_unitdir/ignite3db.service

%pre -n ignite3-db
getent group ignite >/dev/null || /usr/sbin/groupadd -r ignite
getent passwd ignite >/dev/null || /usr/sbin/useradd -r \
  -g ignite -d %_sharedstatedir/ignite3db -s /bin/bash -c "Apache Ignite user" ignite

%preun -n ignite3-db
%preun_service ignite3db.service

%post -n ignite3-db
%post_service ignite3db.service

%files -n ignite3-db
%doc README.md RELEASE* docs examples
%config(noreplace) %attr(0640,ignite,ignite) %_sysconfdir/ignite3db/ignite-config.conf
%config(noreplace) %attr(0640,ignite,ignite) %_sysconfdir/ignite3db/ignite.java.util.logging.properties
%config(noreplace) %attr(0640,ignite,ignite) %_sysconfdir/ignite3db/vars.env
%_unitdir/ignite3db.service
%_libexecdir/ignite3db
%attr(0750,ignite,ignite) %_sharedstatedir/ignite3db
%attr(0750,ignite,ignite) %_logdir/ignite3db

%files -n ignite3-cli
%_bindir/ignite3
%_sysconfdir/bash_completion.d/ignite_completion.sh
%_libexecdir/ignite3

%files -n ignite3-java-client
%_libexecdir/ignite3-java-client

%changelog
* Sat Jul 19 2025 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt3
- Fixed homedir for user ignite (ALT #55250).
- Requires java >= 11 for ignite3-db (ALT #55251).

* Sun Jul 06 2025 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Strictly build with Java 11.

* Sat Jul 05 2025 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus.
