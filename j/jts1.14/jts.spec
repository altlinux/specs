%define oldname jts
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jts1.14
Version:       1.14
Release:       alt2_4jpp8
Summary:       Java Topology Suite
License:       LGPLv2+
URL:           http://sourceforge.net/projects/jts-topo-suite
# sh jts-create-tarball.sh < VERSION >
Source0:       %{oldname}-%{version}.tar.xz
Source1:       %{oldname}-create-tarball.sh

Patch0:        jts-1.14-jdom1.1.+.patch

BuildRequires: maven-local
BuildRequires: mvn(com.googlecode.json-simple:json-simple)
BuildRequires: mvn(jdom:jdom)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:     noarch
Source44: import.info

%description
The JTS Topology Suite is an API for modelling and
manipulating 2-dimensional linear geometry. It provides
numerous geometric predicates and functions. JTS
conforms to the Simple Features Specification for
SQL published by the Open GIS Consortium.

%package app
Group: Development/Java
Summary:       JTS - Applications & tools

%description app
Applications & tools for working with JTS.

%package example
Group: Development/Java
Summary:       JTS - Examples

%description example
Examples of working JTS code.

%package io
Group: Development/Java
Summary:       JTS - IO

%description io
JTS Extension for to assist in read / write operations.

%package parent
Group: Development/Java
Summary:       JTS - Parent POM

%description parent
JTS - Parent POM.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{oldname}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1

# Unavailable plugin
%pom_remove_plugin :nexus-staging-maven-plugin

# Uneeded tasks
%pom_remove_plugin :maven-gpg-plugin
for p in app core example io; do

%pom_remove_plugin :maven-source-plugin %{oldname}-${p}
%pom_remove_plugin :maven-javadoc-plugin %{oldname}-${p}
%pom_remove_plugin :maven-eclipse-plugin %{oldname}-${p}
%pom_remove_plugin :exec-maven-plugin %{oldname}-${p}

# Add OSGi support
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" %{oldname}-${p}
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 %{oldname}-${p} "
 <extensions>true</extensions>
  <configuration>
    <instructions>
      <Bundle-SymbolicName>\${project.groupId}.${p}</Bundle-SymbolicName>
      <Bundle-Name>\${project.artifactId}</Bundle-Name>
      <Bundle-Version>\${project.version}</Bundle-Version>
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
 </executions>"
done

# Uneeded module
%pom_disable_module %{oldname}-assembly-distribution
# Unavailable deps: com.esri:sde-sdk:9.1 com.esri:jpe-sdk:9.1 com.oracle:ojdbc5:11.1.0.7.0
%pom_disable_module %{oldname}-ora
%pom_disable_module %{oldname}-sde

%pom_remove_dep com.esri:sde-sdk %{oldname}-app
%pom_remove_dep -r :ojdbc5 %{oldname}-core %{oldname}-io
%pom_remove_dep com.vividsolutions:%{oldname}-ora %{oldname}-io

# Set Re-Sources location
for p in app core; do
%pom_xpath_inject pom:project/pom:build '
 <resources>
   <resource>
     <directory>src/main/java</directory>
     <excludes>
       <exclude>**/*.java</exclude>
       <exclude>**/package.html</exclude>
     </excludes>
   </resource>
 </resources>' %{oldname}-${p}
done

# https://sourceforge.net/p/jts-topo-suite/bugs/52/
sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," \
 doc/LICENSE.txt $(find . -type f -name "*.java")

# Convert from dos to unix line ending
for file in doc/LICENSE.txt README.txt; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

# Backward compatibility
%mvn_alias com.vividsolutions:%{oldname}-core com.vividsolutions:%{oldname}
%mvn_file :%{oldname}-core %{oldname}/%{oldname}-core %{oldname}
%mvn_compat_version : 1.8 1.13 1.14.0 %{version}

%build

# package junit.swingui does not exist
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-%{oldname}-core
%doc README.txt doc/JTS_Version_History.html
%doc --no-dereference doc/LICENSE.txt

%files app -f .mfiles-%{oldname}-app
%files example -f .mfiles-%{oldname}-example
%files io -f .mfiles-%{oldname}-io

%files parent -f .mfiles-%{oldname}-parent
%doc --no-dereference doc/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference doc/LICENSE.txt

%changelog
* Tue Jun 18 2019 Igor Vlasenko <viy@altlinux.ru> 1.14-alt2_4jpp8
- compat build

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_6jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_4jpp8
- java 8 mass update

