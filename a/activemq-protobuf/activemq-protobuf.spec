Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          activemq-protobuf
Version:       1.1
Release:       alt3_6jpp7
Summary:       ActiveMQ Protocol Buffers
License:       ASL 2.0
Url:           http://activemq.apache.org/
# svn export http://svn.apache.org/repos/asf/activemq/activemq-protobuf/tags/activemq-protobuf-1.1
# tar czf activemq-protobuf-1.1-src-svn.tar.gz activemq-protobuf-1.1
Source0:       activemq-protobuf-1.1-src-svn.tar.gz


BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)

BuildRequires: junit

BuildRequires: maven-local
BuildRequires: javacc-maven-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-surefire-provider-junit4

BuildArch:     noarch
Source44: import.info

%description
A Simpler Protocol Buffer Java API.
Comes with a built in proto file
compiler and Java source code generator.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%pom_remove_plugin :ianal-maven-plugin
%pom_remove_plugin :rat-maven-plugin
%pom_remove_plugin :taglist-maven-plugin
%pom_remove_plugin :maven-assembly-plugin

sed -i 's|${artifactId}|${project.artifactId}|' pom.xml
sed -i 's|${groupId}|${project.groupId}|' pom.xml
sed -i 's|${version}|${project.version}|' pom.xml activemq-protobuf-test/pom.xml

chmod 644 LICENSE

%build

%mvn_file :%{name} activemq/protobuf
%mvn_file :%{name}-test activemq/protobuf-test
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/activemq
%doc LICENSE NOTICE README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_4jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp7
- new version

