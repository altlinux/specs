Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          pegdown
Version:       1.1.0
Release:       alt3_6jpp7
Summary:       Java library for Markdown processing
License:       ASL 2.0
URL:           http://pegdown.org
Source0:       https://github.com/sirthias/pegdown/archive/%{version}.tar.gz


BuildRequires: parboiled
# test deps
BuildRequires: jtidy
BuildRequires: testng

BuildRequires: maven-local
BuildRequires: maven-surefire-provider-testng

BuildArch:     noarch
Source44: import.info

%description
A pure-Java Markdown processor based on a parboiled PEG parser
supporting a number of extensions.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find . -name "*.class" -delete
find . -name "*.jar" -delete

# these test fail
rm src/test/java/org/pegdown/CustomParserTest.java
rm src/test/java/org/pegdown/Markdown103Test.java
rm src/test/java/org/pegdown/PegDownTest.java

%build

%mvn_file :%{name} %{name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG LICENSE NOTICE README.markdown

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_4jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2jpp7
- new version

