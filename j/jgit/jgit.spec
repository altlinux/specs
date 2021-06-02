Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global gittag 5.8.1.202007141445-r

Name:           jgit
Version:        5.8.1
Release:        alt1_1jpp11
Summary:        A pure java implementation of git

# We don't ship the EPL-licensed Eclipse features in this package
License:        BSD
URL:            https://www.eclipse.org/jgit/
Source0:        https://git.eclipse.org/c/jgit/jgit.git/snapshot/jgit-%{gittag}.tar.xz

# Set the correct classpath for the command line tools
Patch0: 0001-Ensure-the-correct-classpath-is-set-for-the-jgit-com.patch

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.googlecode.javaewah:JavaEWAH)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.i2p.crypto:eddsa)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.sshd:sshd-osgi) >= 2.4.0
BuildRequires:  mvn(org.apache.sshd:sshd-sftp) >= 2.4.0
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on) >= 1.65
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on) >= 1.65
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on) >= 1.65
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.tukaani:xz)

# Runtime requirements
Requires:       bouncycastle >= 1.65
Requires:       apache-sshd >= 1:2.4.0
Requires:       jzlib
Source44: import.info

%description
A pure Java implementation of the Git version control system and command
line interface.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -n jgit-%{gittag} -q
%patch0 -p1

# Disable multithreaded build
rm .mvn/maven.config

# Disable "errorprone" compiler that is not available in distro
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:executions/pom:execution[pom:id='compile-with-errorprone']" pom.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:executions/pom:execution[pom:id='default-compile']/pom:configuration" pom.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:dependencies" pom.xml

# Use newer Felix dep
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core:\${osgi-core-version}:provided

# Remove unnecessary plugins for RPM builds
%pom_disable_module org.eclipse.jgit.coverage
%pom_disable_module org.eclipse.jgit.benchmarks
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin -r :japicmp-maven-plugin

# Avoid failures due to lack of jacoco
sed -i -e 's/@{argLine}//' $(find -name pom.xml)

# Don't attach shell script artifact
%pom_remove_plugin org.codehaus.mojo:build-helper-maven-plugin org.eclipse.jgit.pgm

# Don't have spring-boot
%pom_remove_plugin :spring-boot-maven-plugin org.eclipse.jgit.pgm
%pom_xpath_remove "pom:plugins/pom:plugin/pom:executions/pom:execution[pom:id='create_jgit']" org.eclipse.jgit.pgm
sed -i -e 's/org\.springframework\.boot\.loader\.JarLauncher/org.eclipse.jgit.pgm.Main/' \
  org.eclipse.jgit.pgm/jgit.sh

# Relax junit restriction
sed -i -e '/org\.junit/s/4\.13/4.12/' $(grep -r -l --include MANIFEST.MF org.junit)

# Relax jsch restriction
sed -i -e '/jsch/s/1\.55/1.54/' org.eclipse.jgit.junit.ssh/META-INF/MANIFEST.MF

# Relax servlet restriction
sed -i -e '/javax\.servlet/s/4\.0\.0/5.0.0/' org.eclipse.jgit.lfs.server/META-INF/MANIFEST.MF org.eclipse.jgit.pgm/META-INF/MANIFEST.MF
sed -i -e '/javax\.servlet/s/3\.2\.0/5.0.0/' org.eclipse.jgit.junit.http/META-INF/MANIFEST.MF org.eclipse.jgit.http.server/META-INF/MANIFEST.MF

# Remove unnecessary dep on org.apache.log4j
%pom_remove_dep log4j:log4j . org.eclipse.jgit.pgm
%pom_change_dep org.slf4j:slf4j-log4j12 org.slf4j:slf4j-simple . org.eclipse.jgit.pgm

# No need to build test modules if we aren't running tests
sed -i -e '/\.test<\/module>/d' pom.xml

# Never install test jars
%mvn_package ":*.test" __noinstall

%build
# Don't run tests due to missing dependencies
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Pjavac -Dsource=1.8

%install
%mvn_install

# Install CLI invoker script
install -dm 755 %{buildroot}%{_bindir}
install -m 755 org.eclipse.jgit.pgm/jgit.sh %{buildroot}%{_bindir}/jgit

# Ant task configuration
install -dm 755 %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/jgit <<EOF
jgit/org.eclipse.jgit jgit/org.eclipse.jgit.ant slf4j/slf4j-api slf4j/slf4j-simple jzlib jsch commons-compress xz-java javaewah httpcomponents/httpcore httpcomponents/httpclient commons-logging commons-codec eddsa apache-sshd/sshd-osgi apache-sshd/sshd-sftp
EOF

%files -f .mfiles
%doc --no-dereference LICENSE
%doc README.md
%{_bindir}/jgit
%config(noreplace) %{_sysconfdir}/ant.d/jgit

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 5.8.1-alt1_1jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

