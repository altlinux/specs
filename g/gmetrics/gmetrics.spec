Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oname GMetrics

Name:          gmetrics
Version:       0.7
Release:       alt1_4jpp8
Summary:       Groovy library that provides reports and metrics for Groovy code
License:       ASL 2.0
Url:           http://gmetrics.sourceforge.net/
Source0:       http://downloads.sourceforge.net/%{name}/%{oname}-%{version}-bin.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:12)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires: mvn(org.codehaus.groovy:groovy)
BuildRequires: mvn(org.codehaus.groovy:groovy-ant)
BuildRequires: mvn(org.codehaus.groovy:groovy-xml)
BuildRequires: mvn(org.codehaus.groovy:groovy-test)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
GMetrics provides calculation and reporting of size and
complexity metrics for Groovy source code, by scanning the
code with an Ant Task, applying a set of metrics, and
generating an HTML or XML report of the results.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}
# Cleanup
find . -name "*.jar" -delete
find . -name "*.class" -delete
rm -rf docs/*

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin

%pom_remove_plugin :gmaven-plugin
%pom_add_plugin org.codehaus.gmavenplus:gmavenplus-plugin:1.5 . "
 <executions>
  <execution>
   <goals>
    <goal>generateStubs</goal>
    <goal>testGenerateStubs</goal>
   </goals>
  </execution>
 </executions>"

%pom_remove_dep :CodeNarc
%pom_change_dep :log4j ::12

# package org.apache.tools.ant does not exist
%pom_add_dep org.apache.ant:ant:1.9.6 . "<optional>true</optional>"

#sed -i "s|pom.version|project.version|" pom.xml

chmod 644 README.txt

# Convert from dos to unix line ending
for file in CHANGELOG.txt LICENSE.txt NOTICE.txt README.txt ; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%mvn_file :%{oname} %{name} %{oname}

%build

# test skipped require Codenarc, circular deps
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.txt README.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_15jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_5jpp7
- new release

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_2jpp7
- new version

