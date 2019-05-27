Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          hessian
Summary:       Java implementation of a binary protocol for web services 
Version:       4.0.38
Release:       alt1_6jpp8
Epoch:         1
License:       ASL 1.1
URL:           http://hessian.caucho.com/
Source0:       http://caucho.com/download/%{name}-%{version}-src.jar
Source1:       http://repo1.maven.org/maven2/com/caucho/%{name}/%{version}/%{name}-%{version}.pom
Source2:       hessian-license.txt

BuildRequires: maven-local
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:     noarch
Source44: import.info

%description
This is the Java implementation of Caucho's Hession binary transport
protocol for web services.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -c

mkdir src
mv com src/
# Remove useless files
rm -r META-INF
# NO test suite
rm -r src/com/caucho/hessian/test

cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE2} apache.license
%pom_change_dep :servlet-api javax.servlet:javax.servlet-api:3.1.0

# Useless tasks
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%pom_xpath_set pom:properties/pom:project.build.sourceEncoding UTF-8

%pom_xpath_set "pom:project/pom:packaging" bundle
%pom_add_plugin org.apache.felix:maven-bundle-plugin:3.0.1 . "
<extensions>true</extensions>
<configuration>
  <excludeDependencies>true</excludeDependencies>
  <instructions>
    <Bundle-SymbolicName>\${project.groupId}.\${project.artifactId}</Bundle-SymbolicName>
    <Bundle-Name>\${project.name}</Bundle-Name>
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

%mvn_config buildSettings/compilerSource 1.8

%mvn_file com.caucho:%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference apache.license

%files javadoc -f .mfiles-javadoc
%doc --no-dereference apache.license

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.0.38-alt1_6jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.0.38-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.0.38-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.0.38-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt1_4jpp7
- new version

* Sun Sep 21 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.0.8-alt2_1jpp5
- fixed Sisyphus build 

* Fri Jul 25 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.0.8-alt2_1jpp1.7
- rebuild with java 1.4.2

* Mon Jul 09 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.0.8-alt1_1jpp1.7
- converted from JPackage by jppimport script

