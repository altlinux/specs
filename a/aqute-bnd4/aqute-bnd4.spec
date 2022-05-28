%define oldname aqute-bnd
Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name:           aqute-bnd4
Version:        4.3.1
Release:        alt3_4jpp11
Summary:        BND Tool
# Part of jpm is under BSD, but jpm is not included in binary RPM
License:        ASL 2.0 or EPL-2.0
URL:            http://bnd.bndtools.org/
BuildArch:      noarch

Source0:        %{version}.REL.tar.gz
# removes bundled jars from upstream tarball
# run as:
# ./repack-tarball.sh
Source1:        repack-tarball.sh

# A custom aggregator pom to run the build
Source2:        parent.pom
# Poms from maven central since upstream uses gradle to build
Source3:        https://repo1.maven.org/maven2/biz/aQute/bnd/aQute.libg/%{version}/aQute.libg-%{version}.pom
Source4:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd/%{version}/biz.aQute.bnd-%{version}.pom
Source5:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/%{version}/biz.aQute.bndlib-%{version}.pom
Source6:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.annotation/%{version}/biz.aQute.bnd.annotation-%{version}.pom
Source7:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.exporters/%{version}/biz.aQute.bnd.exporters-%{version}.pom
Source8:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.reporter/%{version}/biz.aQute.bnd.reporter-%{version}.pom

# Remove support for remote and resolve commands since they bring more deps than we want
Patch0:         0001-Disable-removed-commands.patch

# Fix build failure against ant
Patch1:         0002-Fix-ant-compatibility.patch

# Fix unimplemented new APIs introduced in OSGi R7
Patch2:         0003-Port-to-OSGI-7.0.0.patch

# Twig is dead upstream, so patch out the option to use it for reports
Patch3:         0004-Patch-out-twig-plugin-for-report-generation.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.javaparser:javaparser-core) >= 3.14.16
BuildRequires:  mvn(jline:jline)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-mapping)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
# Requires self to generate OSGi metadata
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin:4)

# Explicit javapackages-tools requires since bnd script uses
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Source44: import.info

%description
The bnd tool helps you create and diagnose OSGi bundles.
The key functions are:
- Show the manifest and JAR contents of a bundle
- Wrap a JAR so that it becomes a bundle
- Create a Bundle from a specification and a class path
- Verify the validity of the manifest entries
The tool is capable of acting as:
- Command line tool
- File format
- Directives
- Use of macros

%package -n aqute-bndlib4
Group: Development/Java
Summary:        BND library

%description -n aqute-bndlib4
%{summary}.

%package -n bnd-maven-plugin4
Group: Development/Java
Summary:        BND Maven plugin

%description -n bnd-maven-plugin4
%{summary}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{oldname}
BuildArch: noarch

%description javadoc
API documentation for %{oldname}.

%prep
%setup -q -n bnd-%{version}.REL

rm gradlew*

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed 's/@VERSION@/%{version}/' %SOURCE2 > pom.xml
sed -i 's|${Bundle-Version}|%{version}|' biz.aQute.bndlib/src/aQute/bnd/osgi/bnd.info
sed -i -e '/-include/d' cnf/includes/jdt.bnd

# libg
pushd aQute.libg
cp -p %{SOURCE3} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_remove_dep :org.osgi.util.function
%pom_remove_dep :org.osgi.util.promise
%pom_add_dep org.osgi:osgi.cmpn
%pom_add_dep org.osgi:osgi.core
popd

# bnd
pushd biz.aQute.bnd
cp -p %{SOURCE4} pom.xml
sed -i -r 's/provided/compile/' pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
# add missing dep for ant tasks
%pom_add_dep org.apache.ant:ant
# remove support for remote and resolve commands
rm src/aQute/bnd/main/{RemoteCommand,ResolveCommand}.java
%pom_remove_dep :biz.aQute.resolve
%pom_remove_dep :biz.aQute.repository
%pom_remove_dep :biz.aQute.remote.api
%pom_remove_dep :snakeyaml
popd

# bndlib
pushd biz.aQute.bndlib
cp -p %{SOURCE5} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_remove_dep :org.osgi.util.function
%pom_remove_dep :org.osgi.util.promise
%pom_add_dep org.osgi:osgi.core
%pom_add_dep org.osgi:osgi.cmpn
%pom_add_dep biz.aQute.bnd:aQute.libg:%{version}
%pom_add_dep biz.aQute.bnd:biz.aQute.bnd.annotation:%{version}
%pom_add_plugin biz.aQute.bnd:bnd-maven-plugin:4 . "
<executions>
  <execution>
    <goals>
      <goal>bnd-process</goal>
    </goals>
  </execution>
</executions>"
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin . "
<configuration>
    <archive>
        <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    </archive>
</configuration>"
popd

# bnd.annotation
pushd biz.aQute.bnd.annotation
cp -p %{SOURCE6} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_add_dep org.osgi:osgi.core
%pom_add_dep org.osgi:osgi.cmpn
popd

# bnd.exporters
pushd biz.aQute.bnd.exporters
cp -p %{SOURCE7} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_add_dep org.osgi:osgi.core
%pom_add_dep org.osgi:osgi.cmpn
popd

# bnd.reporter
pushd biz.aQute.bnd.reporter
cp -p %{SOURCE8} pom.xml
%pom_add_parent biz.aQute.bnd:parent:%{version}
%pom_add_dep org.osgi:osgi.core
%pom_add_dep org.osgi:osgi.cmpn
# remove twig dep and friends (twig is dead upstream)
rm src/biz/aQute/bnd/reporter/plugins/transformer/JtwigTransformerPlugin.java
%pom_remove_dep org.jtwig:
%pom_remove_dep com.googlecode.concurrentlinkedhashmap:
%pom_remove_dep com.google.guava:
# uneeded dependency
%pom_remove_dep :commons-lang3
popd

# maven-plugins
mkdir -p maven/bnd-maven-plugin/src/main/java/aQute/bnd/maven/lib
cp -r biz.aQute.bnd.maven/src/aQute/bnd/maven/lib/configuration maven/bnd-maven-plugin/src/main/java/aQute/bnd/maven/lib/
pushd maven
%pom_remove_dep -r :biz.aQute.bnd.maven
# Unavailable reactor dependency - org.osgi.impl.bundle.repoindex.cli
%pom_disable_module bnd-indexer-maven-plugin
# Requires unbuilt parts of bnd
%pom_disable_module bnd-export-maven-plugin
%pom_disable_module bnd-reporter-maven-plugin
%pom_disable_module bnd-resolver-maven-plugin
%pom_disable_module bnd-run-maven-plugin
%pom_disable_module bnd-testing-maven-plugin
# Integration tests require Internet access
%pom_remove_plugin -r :maven-invoker-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_plugin -r :flatten-maven-plugin
popd

# Use compiler release flag when building on JDK >8 for correct cross-compiling
%pom_xpath_inject pom:project "
  <profiles>
    <profile>
      <id>jdk-release-flag</id>
      <activation>
        <jdk>[9,)</jdk>
      </activation>
      <properties>
        <maven.compiler.release>8</maven.compiler.release>
      </properties>
    </profile>
  </profiles>"

%mvn_alias biz.aQute.bnd:biz.aQute.bnd :bnd biz.aQute:bnd
%mvn_alias biz.aQute.bnd:biz.aQute.bndlib :bndlib biz.aQute:bndlib

%mvn_package biz.aQute.bnd:biz.aQute.bndlib bndlib
%mvn_package biz.aQute.bnd:biz.aQute.bnd.annotation bndlib
%mvn_package biz.aQute.bnd:aQute.libg bndlib
%mvn_package biz.aQute.bnd:bnd-shared-maven-lib maven
%mvn_package biz.aQute.bnd:bnd-maven-plugin maven
%mvn_package biz.aQute.bnd:bnd-baseline-maven-plugin maven
%mvn_package biz.aQute.bnd:parent __noinstall
%mvn_package biz.aQute.bnd:bnd-plugin-parent __noinstall

%mvn_compat_version : 4 %{version}

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8 -Dworkspace=$(pwd) \
  -Dorg.eclipse.jdt.core.compiler.source=1.8 -Dorg.eclipse.jdt.core.compiler.codegen.targetPlatform=1.8

%install
%mvn_install

install -d -m 755 %{buildroot}%{_sysconfdir}/ant.d
echo "aqute-bnd4 slf4j/api slf4j/simple osgi-annotation osgi-core osgi-compendium" >%{buildroot}%{_sysconfdir}/ant.d/%{oldname}

%jpackage_script aQute.bnd.main.bnd "" "" aqute-bnd4:slf4j/slf4j-api:slf4j/slf4j-simple:jline2/jline:jansi1/jansi:osgi-annotation:osgi-core:osgi-compendium bnd4 1

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{oldname}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{oldname}.conf

%files -f .mfiles
%doc --no-dereference LICENSE
%{_bindir}/bnd4
%config(noreplace) %{_sysconfdir}/ant.d/*
%config(noreplace,missingok) /etc/java/%{oldname}.conf

%files -n aqute-bndlib4 -f .mfiles-bndlib
%doc --no-dereference LICENSE

%files -n bnd-maven-plugin4 -f .mfiles-maven

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sat May 28 2022 Igor Vlasenko <viy@altlinux.org> 0:4.3.1-alt3_4jpp11
- nobootstrap; self-dependent build

* Fri May 27 2022 Igor Vlasenko <viy@altlinux.org> 0:4.3.1-alt2_4jpp11
- compat build (bootstrap)

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:4.3.1-alt1_4jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:4.3.1-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.5.0-alt1_8jpp8
- fc update

* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.5.0-alt1_6jpp8
- fixed build with osgi-compendium-7

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.5.0-alt1_5jpp8
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.5.0-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.5.0-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt1_7jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.3.0-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_3jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_2jpp8
- new versio

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt0.2jpp
- removed compatibility symlink

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt1_7jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

