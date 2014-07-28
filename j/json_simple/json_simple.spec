# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:           json_simple
Version:        1.1.1
Release:        alt2_4jpp7
Summary:        Simple Java toolkit for JSON

Group:          Development/Java
License:        ASL 2.0
URL:            http://code.google.com/p/json-simple/
# svn export http://json-simple.googlecode.com/svn/tags/tag_release_1_1_1/ json-simple-1.1.1
# tar czf json-simple-1.1.1-src-svn.tar.gz json-simple-1.1.1
Source0:        json-simple-1.1.1-src-svn.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  junit4

Requires:       jpackage-utils
Source44: import.info

%description
JSON.simple is a simple Java toolkit for JSON. You can use JSON.simple 
to encode or decode JSON text. 
  * Full compliance with JSON specification (RFC4627) and reliable 
  * Provides multiple functionalities such as encode, decode/parse 
    and escape JSON text while keeping the library lightweight 
  * Flexible, simple and easy to use by reusing Map and List interfaces 
  * Supports streaming output of JSON text 
  * Stoppable SAX-like interface for streaming input of JSON text 
  * Heap based parser 
  * High performance (see performance testing) 
  * No dependency on external libraries 
  * Both of the source code and the binary are JDK1.2 compatible 

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n json-simple-%{version}
find . -name '*.jar' -exec rm -f '{}' \;
# All the files have dos line endings, remove them.
find . -type f -exec %{__sed} -i 's/\r//' {} \;

%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 target/json-simple-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc AUTHORS.txt ChangeLog.txt LICENSE.txt README.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2jpp7
- new version

