Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          xml-maven-plugin
Version:       1.0.1
Release:       alt1_1jpp8
Summary:       Maven XML Plugin
License:       ASL 2.0
URL:           http://www.mojohaus.org/xml-maven-plugin/
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/xml-maven-plugin/%{version}/xml-maven-plugin-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-resources)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildRequires:  mvn(xml-resolver:xml-resolver)

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

# Add the version
sed -i 's|stylesheet |stylesheet version="1.0" |'  src/it/it8/src/main/xsl/it8.xsl

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_13jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_12jpp8
- new version

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

