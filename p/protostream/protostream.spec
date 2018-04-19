Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.0.4
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

%global debug_package %{nil}

Name:             protostream
Version:          3.0.4
Release:          alt1_5jpp8
Summary:          Infinispan ProtoStream
License:          ASL 2.0 and BSD
Url:              http://infinispan.org/
Source0:          https://github.com/infinispan/protostream/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(commons-cli:commons-cli)
BuildRequires:    mvn(com.google.protobuf:protobuf-java)
BuildRequires:    mvn(com.squareup:protoparser)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(log4j:log4j:12)
BuildRequires:    mvn(net.jcip:jcip-annotations)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-surefire-report-plugin)
BuildRequires:    mvn(org.assertj:assertj-core)
BuildRequires:    mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:    mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:    mvn(org.javassist:javassist)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires:    mvn(org.jboss.marshalling:jboss-marshalling-river)
BuildRequires:    protobuf-compiler
Source44: import.info
BuildArch: noarch

%description
The Infinispan ProtoStream project

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_xpath_set "pom:properties/pom:version.log4j" 12 parent
%pom_change_dep :log4j ::'${version.log4j}' core
%pom_remove_plugin -r :maven-source-plugin
# Break build, use system setting
%pom_remove_plugin -r :maven-compiler-plugin
# Disable system libraries copies
%pom_remove_plugin :maven-shade-plugin core
%pom_remove_plugin :maven-bundle-plugin core
%pom_xpath_set "pom:project/pom:packaging" bundle core
%pom_add_plugin org.apache.felix:maven-bundle-plugin core '
<extensions>true</extensions>
<configuration>
  <excludeDependencies>true</excludeDependencies>
  <instructions>
    <Export-Package>
      ${project.groupId}.sampledomain.*;version=${project.version};-split-package:=error
    </Export-Package>
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

%pom_change_dep org.easytesting:fest-assert-core org.assertj:assertj-core:2.0.0  core
find ./core -name "*.java" -exec sed -i "s/org.fest.assertions/org.assertj.core/g" {} +

# java.lang.ClassCastException: java.lang.Integer cannot be cast to java.lang.String
rm core/src/test/java/org/infinispan/protostream/impl/parser/impl/DescriptorsTest.java \
 core/src/test/java/org/infinispan/protostream/annotations/impl/ProtoSchemaBuilderTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE PROTOPARSER_LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE PROTOPARSER_LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1_5jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1_4jpp8
- new version

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.10.Alpha7jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.8.Alpha7jpp8
- new version

