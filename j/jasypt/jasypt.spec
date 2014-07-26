# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          jasypt
Version:       1.9.0
Release:       alt2_2jpp7
Summary:       Java Simplified Encryption
Group:         Development/Java
License:       ASL 2.0
Url:           http://www.jasypt.org/
# svn export https://jasypt.svn.sourceforge.net/svnroot/jasypt/tags/jasypt/jasypt-1.9.0 jasypt-1.9.0
# tar czf jasypt-1.9.0-src-svn.tar.gz jasypt-1.9.0
Source0:       %{name}-%{version}-src-svn.tar.gz
# force tomcat-servlet-3.0-api use
Source1:       %{name}-%{version}-depmap
# remove maven-gpg-plugin
# fix encoding (changed US-ASCII in UTF-8)
# fix bouncycastle: artifactId version
# add commons-logging for test
# add icu4j systemPath
# fix compiler plugin target/source 1.5 
Patch0:        %{name}-%{version}-pom.patch
# remove internal commons-codec 1.3
Patch1:        %{name}-%{version}-use-system-commons-codec.patch
# tks to jhernand
# system commons-codec 1.4 support
Patch2:        %{name}-%{version}-StandardStringDigester.patch
Patch3:        %{name}-%{version}-StandardPBEStringEncryptor.patch

BuildRequires: jpackage-utils

# test deps
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: bouncycastle
BuildRequires: junit
# main deps
BuildRequires: apache-commons-codec
BuildRequires: icu4j
BuildRequires: tomcat-servlet-3.0-api

BuildRequires: maven
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      apache-commons-codec
Requires:      icu4j
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Java library which enables encryption
in java apps with minimum effort.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0
%patch3 -p0

%build

mvn-rpmbuild -Dmaven.test.skip=true  -Dmaven.local.depmap.file=%{SOURCE1} -D_javadir=%{_javadir} install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api/jasypt/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc *.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%changelog
* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt2_2jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_4jpp7
- update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_2jpp7
- new version

