Name:    nexus
Version: 3.42.0
Release: alt1

Summary: Cloud-Native Binary Artifact Management
License: EPL-1.0
Group:   System/Configuration/Packaging
URL:	 https://www.sonatype.com/products/sonatype-nexus-repository
VCS:     https://github.com/sonatype/nexus-public

Source0: %name-%version.tar
Source1: m2.tar
Source2: node.tar
Source3: nexus.service

Patch0: nexus-alt-node-build.patch

ExclusiveArch: x86_64

%filter_from_requires /\/etc\/default\/locale/d
%filter_from_requires /\/etc\/default\/rcS/d
%filter_from_requires /\/usr\/libexec\/nexus\/bin\/nexus/d

BuildRequires(pre): /proc rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-11-compat
BuildRequires: unzip
BuildRequires: git-core

AutoReqProv: yes, noosgi-fc
Requires: java-11-openjdk-headless

%description
Manage, store, and distribute software applications, AI/ML models, and
components with speed, reliability, and control at scale. Our industry-leading
binary artifact repository tool is trusted by millions - including 70 percent
of the Fortune 100.

%prep
%setup
%autopatch -p1
# Use karaf.version 4.3.7 because org.apache.karaf.features.core-4.3.6.jar is corrupted
subst 's|karaf.version>4.3.6|karaf.version>4.3.7|' pom.xml
test -d ~/.m2 && rm -rf ~/.m2
tar xf %SOURCE1 -C ~
tar xf %SOURCE2

%build
mvn clean install -DskipTests

%install
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_runtimedir/%name

unzip -q assemblies/nexus-base-template/target/nexus-base-template-*.zip \
      -d %buildroot%_libexecdir/%name/.nexus-tmp

mv %buildroot%_libexecdir/%name/.nexus-tmp/nexus-base-template-*/* \
   %buildroot%_libexecdir/%name/

rm -rf %buildroot%_libexecdir/%name/.nexus-tmp
install -Dpm 0644 %SOURCE3 %buildroot%_unitdir/nexus.service

%post
%systemd_post %name.service

%preun
%systemd_preun %name.service

%files
%doc *.md LICENSE.txt
%_libexecdir/%name
%config(noreplace) %_unitdir/%name.service

%changelog
* Sat Dec 27 2025 Evgeniy Serov <scala@altlinux.org> 3.42.0-alt1
- Initial build for Sisyphus.
