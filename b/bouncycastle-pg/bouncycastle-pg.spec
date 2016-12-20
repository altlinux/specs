Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global ver 1.54
%global archivever  jdk15on-%(echo %{ver}|sed 's|\\\.||')

Name:          bouncycastle-pg
Version:       %{ver}
Release:       alt1_1jpp8
Summary:       Bouncy Castle OpenPGP API
# modified BZIP2 library org/bouncycastle/apache/bzip2 ASL 2.0
License:       ASL 2.0 and MIT
URL:           http://www.bouncycastle.org/

# Source tarball contains everything except test suite rousources
Source0:       http://www.bouncycastle.org/download/bcpg-%{archivever}.tar.gz
# Test suite resources are found in this jar
Source1:       http://www.bouncycastle.org/download/bctest-%{archivever}.jar

Source2:       http://repo2.maven.org/maven2/org/bouncycastle/bcpg-jdk15on/%{version}/bcpg-jdk15on-%{version}.pom
Source3:       bouncycastle-pg-build.xml
Source4:       bouncycastle-pg-OSGi.bnd

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: aqute-bnd
BuildRequires: javapackages-local
BuildRequires: junit
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on) = %{version}
Requires:      mvn(org.bouncycastle:bcprov-jdk15on) = %{version}

BuildArch:     noarch
Source44: import.info

%description
The Bouncy Castle Java API for handling the OpenPGP protocol. This
jar contains the OpenPGP API for JDK 1.6. The APIs can be used in 
conjunction with a JCE/JCA provider such as the one provided with the
Bouncy Castle Cryptography APIs.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n bcpg-%{archivever}

# Unzip source and test suite resources
mkdir -p src/java src/test
unzip -qq src.zip -d src/java
unzip -qq %{SOURCE1} 'org/bouncycastle/openpgp/*' -x '*.class' -d src/java

mkdir -p src/test/org/bouncycastle/openpgp/examples
mv src/java/org/bouncycastle/openpgp/test \
  src/test/org/bouncycastle/openpgp/
mv src/java/org/bouncycastle/openpgp/examples/test \
  src/test/org/bouncycastle/openpgp/examples/

# Remove provided binaries and apidocs
find . -type f -name "*.class" -exec rm -f {} \;
find . -type f -name "*.jar" -exec rm -f {} \;
rm -rf docs/* javadocs/*

cp -p %{SOURCE3} build.xml
cp -p %{SOURCE4} bcpg.bnd
sed -i "s|@VERSION@|%{version}|" build.xml bcpg.bnd

# this test fails: source encoding error
rm src/test/org/bouncycastle/openpgp/test/PGPUnicodeTest.java
sed -i "s|suite.addTestSuite(PGPUnicodeTest.class);|//&|" \
  src/test/org/bouncycastle/openpgp/test/AllTests.java

%build
mkdir lib
build-jar-repository -s -p lib bcprov junit ant/ant-junit aqute-bnd
ant -Dbc.test.data.home=$(pwd)/src/test jar javadoc

%install
%mvn_file org.bouncycastle:bcpg-jdk15on bcpg
%mvn_alias org.bouncycastle:bcpg-jdk15on org.bouncycastle:bcpg-jdk16 org.bouncycastle:bcpg-jdk15
%mvn_artifact %{SOURCE2} build/bcpg.jar
%mvn_install -J build/apidocs

%files -f .mfiles
%doc CONTRIBUTORS.html index.html
%doc LICENSE.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE.html

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1_9jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1_8jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.46-alt3_10jpp7
- new release

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.46-alt3_9jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.46-alt3_8jpp7
- fixed build

* Sun Sep 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.46-alt2_8jpp7
- fixed build with new slf4j

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1_8jpp7
- fc release

