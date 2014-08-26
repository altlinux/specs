Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          jasypt
Version:       1.9.0
Release:       alt2_6jpp7
Summary:       Java Simplified Encryption
License:       ASL 2.0
Url:           http://www.jasypt.org/
# svn export https://jasypt.svn.sourceforge.net/svnroot/jasypt/tags/jasypt/jasypt-1.9.0 jasypt-1.9.0
# tar czf jasypt-1.9.0-src-svn.tar.gz jasypt-1.9.0
Source0:       %{name}-%{version}-src-svn.tar.gz
# remove internal commons-codec 1.3
Patch0:        %{name}-%{version}-use-system-commons-codec.patch
# tks to jhernand
# system commons-codec 1.4 support
Patch1:        %{name}-%{version}-StandardStringDigester.patch
Patch2:        %{name}-%{version}-StandardPBEStringEncryptor.patch


# test deps
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: bouncycastle
BuildRequires: junit
# main deps
BuildRequires: apache-commons-codec
BuildRequires: icu4j
BuildRequires: tomcat-servlet-3.0-api

BuildRequires: maven-local
BuildRequires: maven-assembly-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-provider-junit4

BuildArch:     noarch
Source44: import.info

%description
Java library which enables encryption
in java apps with minimum effort.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0

%pom_remove_plugin :maven-gpg-plugin
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:reportOutputDirectory"
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-resources-plugin']/pom:configuration"
%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-resources-plugin']" "
<configuration>
  <encoding>UTF-8</encoding>
</configuration>"
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration"
%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']" "
<configuration>
  <source>1.5</source>
  <target>1.5</target>
  <encoding>UTF-8</encoding>
</configuration>"

%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:groupId='org.bouncycastle']/pom:artifactId" bcprov-jdk16
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:groupId='org.bouncycastle']/pom:version" 1.46
%pom_add_dep commons-logging:commons-logging::test

# force tomcat-servlet-3.0-api use
%pom_remove_dep javax.servlet:servlet-api
%pom_add_dep org.apache.tomcat:tomcat-servlet-api::provided

%build
%mvn_file :%{name} %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt2_4jpp7
- new release

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt2_2jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_4jpp7
- update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_2jpp7
- new version

