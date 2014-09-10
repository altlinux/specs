# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          xml-maven-plugin
Version:       1.0
Release:       alt5_9jpp7
Summary:       Maven XML Plugin
Group:         Development/Java
License:       ASL 2.0
Url:           http://mojo.codehaus.org/xml-maven-plugin/
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/xml-maven-plugin/1.0/xml-maven-plugin-1.0-source-release.zip

BuildRequires: mojo-parent

BuildRequires: apache-rat-plugin
BuildRequires: maven-local
BuildRequires: maven-changes-plugin
BuildRequires: maven-checkstyle-plugin
BuildRequires: maven-clean-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-plugin-cobertura

BuildRequires: plexus-component-api
BuildRequires: plexus-io
BuildRequires: plexus-resources
BuildRequires: plexus-utils
BuildRequires: saxon
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
BuildRequires: xml-commons-resolver

BuildArch:     noarch
Source44: import.info

%description
A plugin for various XML related tasks like validation and transformation.

%package javadoc
Group: Development/Java
Summary:       Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

for d in LICENSE NOTICE ; do
  iconv -f iso8859-1 -t utf-8 $d.txt > $d.txt.conv && mv -f $d.txt.conv $d.txt
  sed -i 's/\r//' $d.txt
done

rm -rf src/it/mojo-1438-validate

# Add the version
sed -i 's|stylesheet |stylesheet version="1.0" |'  src/it/it8/src/main/xsl/it8.xsl

# In maven 3, the functionality we need has been moved to maven-core
%pom_remove_dep org.apache.maven:maven-project
%pom_add_dep org.apache.maven:maven-core

%build
%mvn_build -f -- install

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_7jpp7
- new release

* Sat Jul 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_4jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_4jpp7
- fixed build

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4jpp7
- new version

