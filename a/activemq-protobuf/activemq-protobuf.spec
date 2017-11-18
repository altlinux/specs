BuildRequires: apache-parent
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          activemq-protobuf
Version:       1.1
Release:       alt4_14jpp8
Summary:       ActiveMQ Protocol Buffers
License:       ASL 2.0
Url:           http://activemq.apache.org/
# svn export http://svn.apache.org/repos/asf/activemq/activemq-protobuf/tags/activemq-protobuf-1.1
# tar czf activemq-protobuf-1.1-src-svn.tar.gz activemq-protobuf-1.1
Source0:       activemq-protobuf-1.1-src-svn.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)

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

%mvn_file :%{name} activemq/protobuf
%mvn_file :%{name}-test activemq/protobuf-test

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/activemq
%doc README.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_14jpp8
- added BR: apache-parent for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_14jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_13jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_12jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_10jpp8
- java 8 mass update

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

