Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# empty debuginfo
%global debug_package %nil

Name:             snappy-java
Version:          1.1.2.4
Release:          alt2_8jpp8
Summary:          Fast compressor/decompresser
License:          ASL 2.0
URL:              http://xerial.org/snappy-java/
Source0:          https://github.com/xerial/snappy-java/archive/%{version}.tar.gz
# Not able to build snappy-java jni library with sbt:
# use sbt = 0.13.8 (use scala 2.11.6) available 0.13.1 (use scala 2.10.4)
# Too many missing plugins:
# com.etsy:sbt-checkstyle-plugin:0.4.3
# com.github.gseitz:sbt-release:1.0.0
# com.jsuereth:sbt-pgp:1.0.0
# com.typesafe.sbt:sbt-osgi:0.7.0
# de.johoop:findbugs4sbt:1.4.0
# de.johoop:jacoco4sbt:2.1.5
# org.xerial.sbt:sbt-sonatype:0.5.0
Source1:          http://central.maven.org/maven2/org/xerial/snappy/%{name}/%{version}/%{name}-%{version}.pom
Patch0:           snappy-java-1.1.2-build.patch
Patch1:           snappy-java-1.1.2.4-lsnappy.patch

BuildRequires:    gcc-c++
BuildRequires:    libstdc++-devel-static
BuildRequires:    libsnappy-devel

BuildRequires:    maven-local
BuildRequires:    mvn(com.sun:tools)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.felix:org.osgi.core)
BuildRequires:    mvn(org.apache.maven.plugins:maven-antrun-plugin)

Requires:         libsnappy
Source44: import.info

%description
A Java port of the snappy, a fast compresser/decompresser written in C++.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch:        noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
# Cleanup
find -name "*.class" -print -delete
find -name "*.jar" -print -delete
rm -r ./*sbt* project

# Remove prebuilt libraries
find -name "*.jnilib" -print -delete
find -name "*.dll" -print -delete
find -name "*.so" -print -delete
find -name "*.a" -print -delete
find -name "*.h" -print -delete

%patch0 -p1
%patch1 -p1

cp %{SOURCE1} pom.xml
%pom_change_dep org.osgi: org.apache.felix::1.4.0
%pom_xpath_remove "pom:dependency[pom:scope = 'test']"

# Build JNI library
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin . '
<dependencies>
 <dependency>
  <groupId>com.sun</groupId>
  <artifactId>tools</artifactId>
  <version>1.8.0</version>
 </dependency>
</dependencies>

<executions>
  <execution>
  <id>compile</id>
  <phase>process-classes</phase>
    <configuration>
      <target>
       <javac destdir="lib"
         srcdir="src/main/java"
         source="1.6" target="1.6" debug="on"
         classpathref="maven.plugin.classpath">
         <include name="**/OSInfo.java"/>
       </javac>
       <exec executable="make" failonerror="true">
        <arg line="%{?_smp_mflags}"/>
       </exec>
      </target>
    </configuration>
    <goals>
      <goal>run</goal>
    </goals>
  </execution>
</executions>'
# Add OSGi support
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-Activator>org.xerial.snappy.SnappyBundleActivator</Bundle-Activator>
    <Bundle-ActivationPolicy>lazy</Bundle-ActivationPolicy>
    <Bundle-SymbolicName>${project.groupId}.${project.artifactId}</Bundle-SymbolicName>
    <Bundle-Version>${project.version}</Bundle-Version>
    <Import-Package>org.osgi.framework,*</Import-Package>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.0 . '
<configuration>
 <source>1.6</source>
 <target>1.6</target>
</configuration>'

chmod 644 NOTICE README.md
# Convert from dos to unix line ending
for file in LICENSE NOTICE README.md; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%build

CXXFLAGS="${CXXFLAGS:-%optflags}"
export CXXFLAGS
# No test deps available:
#    org.xerial.java:xerial-core:2.1
#    org.xerial:xerial-core:3.2.3
#    org.scalatest:scalatest_2.11:2.2.0
#    com.novocode:junit-interface:0.10
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2.4-alt2_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2.4-alt2_6jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2.4-alt2_2jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2.4-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_6jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_5jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt3_5jpp7
- fixed build

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt1_3jpp7
- new version

