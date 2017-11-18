BuildRequires: apache-parent
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/asciidoc /usr/bin/source-highlight boost-devel boost-filesystem-devel boost-program_options-devel gcc-c++ pkgconfig(liblzma) zlib-devel
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             avro
Version:          1.7.6
Release:          alt2_2jpp8
Summary:          Data serialization system
License:          ASL 2.0
URL:              http://avro.apache.org

# svn export http://svn.apache.org/repos/asf/avro/tags/release-1.7.6/ avro-1.7.6
# find avro-1.7.6/ -name '*.jar' -delete -or -name '*.dll' -print -delete
# tar cJf avro-1.7.6-CLEAN.tar.xz avro-1.7.6
Source0:          avro-%{version}-CLEAN.tar.xz
Patch0:           avro-1.7.6-ipc-changes-for-jetty-upgrade.patch
Patch1:           avro-1.7.6-jdk8.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(com.thoughtworks.paranamer:paranamer)
BuildRequires:    mvn(io.netty:netty:3)
BuildRequires:    mvn(org.apache.hadoop:hadoop-client)
BuildRequires:    mvn(org.apache.maven:maven-project)
BuildRequires:    mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:    mvn(org.apache.thrift:libthrift)
BuildRequires:    mvn(org.codehaus.jackson:jackson-core-asl)
BuildRequires:    mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires:    mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:    mvn(org.eclipse.jetty:jetty-server)
BuildRequires:    mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:    mvn(org.eclipse.jetty:jetty-util)
BuildRequires:    mvn(org.slf4j:slf4j-api)
BuildRequires:    mvn(org.slf4j:slf4j-simple)
BuildRequires:    mvn(org.tukaani:xz)
BuildRequires:    mvn(org.xerial.snappy:snappy-java)
Source44: import.info

%description
Apache Avro is a data serialization system.

Avro provides:

* Rich data structures.
* A compact, fast, binary data format.
* A container file, to store persistent data.
* Remote procedure call (RPC).
* Simple integration with dynamic languages. Code generation is not required
  to read or write data files nor to use or implement RPC protocols. Code
  generation as an optional optimization, only worth implementing for
  statically typed languages.

%package compiler
Group: Development/Java
Summary:          Apache Avro Compiler

%description  compiler
Avro Compilers for Avro IDL and Avro Specific Java API

%package ipc
Group: Development/Java
Summary:          Apache Avro IPC

%description  ipc
Avro inter-process communication components

%package mapred
Group: Development/Java
Summary:          Apache Avro Mapred API
Requires:         hadoop-client
Requires:         hadoop-mapreduce

%description  mapred
An org.apache.hadoop.mapred compatible API
for using Avro Serialization in Hadoop

%package maven-plugin
Group: Development/Java
Summary:          Apache Avro Maven Plugin

%description  maven-plugin
Avro Maven plugin for Avro IDL and Specific API Compilers

%package parent
Group: Development/Java
Summary:          Apache Avro Java parent POM

%description  parent
Avro parent POM Java project

%package protobuf
Group: Development/Java
Summary:          Apache Avro Protobuf Compatibility

%description  protobuf
Permit serialization of Protobuf-generated classes as Avro data.

%package thrift
Group: Development/Java
Summary:          Apache Avro Thrift Compatibility

%description  thrift
Permit serialization of Thrift-generated classes as Avro data.

%package toplevel
Group: Development/Java
Summary:          Apache Avro Toplevel POM

%description  toplevel
Apache Avro Toplevel POM

%package trevni
Group: Development/Java
Summary:          Trevni Java
Requires:         avro-mapred

%description  trevni
Trevni: A Column File Format

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# Unsupported features
%pom_disable_module archetypes lang/java

%pom_disable_module tools lang/java

%pom_xpath_set pom:properties/pom:hadoop2.version 2.0.5-alpha lang/java
%pom_xpath_set pom:properties/pom:jetty.version 9.0.3.v20130506 lang/java
%pom_xpath_set pom:properties/pom:jetty-servlet-api.version 3.1.0 lang/java
%pom_change_dep -r :junit-dep :junit lang/java

# Use netty 3 compat package
%pom_xpath_set pom:properties/pom:netty.version 3 lang/java

# Remove panamer plugin for test jar generation
%pom_remove_plugin com.thoughtworks.paranamer:paranamer-maven-plugin lang/java/avro

# package org.tukaani.xz does not exist
%pom_add_dep org.tukaani:xz lang/java/avro

# Need explicit maven-artifact declaration
%pom_add_dep org.apache.maven:maven-artifact lang/java/maven-plugin

# Remove ipc tests from mapred
%pom_remove_dep :avro-ipc lang/java/mapred
%pom_add_dep org.apache.avro:avro-ipc:%{version} lang/java/mapred

# Disable default-jar execution of maven-jar-plugin, which is causing
# problems with version 3.0.0 of the plugin.
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions/pom:execution[pom:id = 'main']" lang/java/mapred
for mod in mapred trevni/avro; do
    %pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
        <execution>
          <id>default-jar</id>
          <phase>skip</phase>
        </execution>" lang/java/${mod}
done
 
%mvn_package ":trevni-doc"  __noinstall
%mvn_package ":trevni-avro" trevni
%mvn_package ":trevni-core" trevni
%mvn_package ":trevni-java" trevni
%mvn_package ":trevni-avro::hadoop2:" trevni
%mvn_package ":avro-mapred::hadoop2:" avro-mapred

%build

%mvn_build -sf -- -Dhadoop.version=2 -P hadoop2 -Dcheckstyle.skip=true

%install
%mvn_install

%files -f .mfiles-avro
%doc README.txt
%doc LICENSE.txt NOTICE.txt

%files compiler -f .mfiles-avro-compiler
%doc LICENSE.txt NOTICE.txt

%files ipc -f .mfiles-avro-ipc
%doc LICENSE.txt NOTICE.txt

%files mapred -f .mfiles-avro-mapred
%doc LICENSE.txt NOTICE.txt

%files maven-plugin -f .mfiles-avro-maven-plugin
%doc LICENSE.txt NOTICE.txt

%files parent -f .mfiles-avro-parent
%doc LICENSE.txt NOTICE.txt

%files protobuf -f .mfiles-avro-protobuf
%doc LICENSE.txt NOTICE.txt

%files thrift -f .mfiles-avro-thrift
%doc LICENSE.txt NOTICE.txt

%files toplevel -f .mfiles-avro-toplevel
%doc LICENSE.txt NOTICE.txt

%files trevni -f .mfiles-trevni
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt2_2jpp8
- added BR: apache-parent for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt1_1jpp8
- new version

* Wed Feb 24 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.5-alt1_13jpp8
- full build

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt3_6jpp7
- new release

* Thu Jul 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_4jpp7
- new version

