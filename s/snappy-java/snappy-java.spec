Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# empty debuginfo
%global debug_package %nil

Name:             snappy-java
Version:          1.0.5
Release:          alt1_6jpp8
Summary:          Fast compressor/decompresser
License:          ASL 2.0
URL:              http://xerial.org/snappy-java/
Source0:          https://github.com/xerial/snappy-java/archive/%{version}.tar.gz

Patch0:           snappy-java-1.0.5-build.patch

BuildRequires:    libstdc++-devel-static
BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:org.osgi.core)
BuildRequires:    libsnappy-devel
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

# Remove prebuilt libraries
find -name "*.jnilib" -print -delete
find -name "*.dll" -print -delete
find -name "*.so" -print -delete
find -name "*.h" -print -delete

%patch0 -p1

# Modify pom
%pom_change_dep org.osgi:core org.apache.felix:org.osgi.core
%pom_xpath_remove "pom:dependency[pom:scope = 'test']"
%pom_xpath_remove "pom:build/pom:extensions"
%pom_xpath_remove "pom:Bundle-NativeCode"

# Unwanted
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-source-plugin

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
       <exec executable="make">
        <arg line="%{?_smp_mflags}
        JAVA_HOME=%{_jvmdir}/java
        JAVA=%{_jvmdir}/java/bin/java
        JAVAC=%{_jvmdir}/java/bin/javac
        JAVAH=%{_jvmdir}/java/bin/javah"/>
       </exec>
      </target>
    </configuration>
    <goals>
      <goal>run</goal>
    </goals>
  </execution>
</executions>'

chmod 644 NOTICE README.md
sed -i 's/\r//' LICENSE NOTICE README.md

%build
CXXFLAGS="${CXXFLAGS:-%optflags}"
export CXXFLAGS

# no xerial-core package available
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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

