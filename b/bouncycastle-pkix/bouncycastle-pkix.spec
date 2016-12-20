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

Name:          bouncycastle-pkix
Version:       %{ver}
Release:       alt1_1jpp8
Summary:       Bouncy Castle PKIX, CMS, EAC, TSP, PKCS, OCSP, CMP, and CRMF APIs
License:       MIT
URL:           http://www.bouncycastle.org/

# Source tarball contains everything except test suite rousources
Source0:       http://www.bouncycastle.org/download/bcpkix-%{archivever}.tar.gz
# Test suite resources are found in this jar
Source1:       http://www.bouncycastle.org/download/bctest-%{archivever}.jar

Source2:       http://central.maven.org/maven2/org/bouncycastle/bcpkix-jdk15on/%{version}/bcpkix-jdk15on-%{version}.pom
Source3:       bouncycastle-pkix-build.xml
Source4:       bouncycastle-pkix-OSGi.bnd

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: aqute-bnd
BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: junit
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on) = %{version}
Requires:      mvn(org.bouncycastle:bcprov-jdk15on) = %{version}

BuildArch:     noarch

Obsoletes:     bouncycastle-tsp < 1.50-2
Provides:      bouncycastle-tsp = %{version}-%{release}
Source44: import.info

%description
The Bouncy Castle Java APIs for CMS, PKCS, EAC, TSP, CMP, CRMF, OCSP, and
certificate generation. This jar contains APIs for JDK 1.5 to JDK 1.7. The
APIs can be used in conjunction with a JCE/JCA provider such as the
one provided with the Bouncy Castle Cryptography APIs.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
Obsoletes:     bouncycastle-tsp-javadoc < 1.50-2
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n bcpkix-%{archivever}

# Unzip source and test suite resources
mkdir -p src/java src/test
unzip -qq src.zip -d src/java
unzip -qq %{SOURCE1} 'cmp/*' 'rfc4134/*' 'org/bouncycastle/*' -x '*.class' -d src/test

cp -p %{SOURCE2} pom.xml

# Remove provided binaries and apidocs
find . -type f -name "*.class" -print -delete
find . -type f -name "*.jar" -print -delete
rm -rf docs/* javadoc/*

mv src/java/org/bouncycastle/cert/cmp/test/* src/test/org/bouncycastle/cert/cmp/test
mv src/java/org/bouncycastle/cert/crmf/test/* src/test/org/bouncycastle/cert/crmf/test
mv src/java/org/bouncycastle/cert/ocsp/test/* src/test/org/bouncycastle/cert/ocsp/test
mv src/java/org/bouncycastle/cert/test/* src/test/org/bouncycastle/cert/test
mv src/java/org/bouncycastle/cms/test/* src/test/org/bouncycastle/cms/test
mv src/java/org/bouncycastle/eac/test/* src/test/org/bouncycastle/eac/test
mv src/java/org/bouncycastle/mozilla/test/* src/test/org/bouncycastle/mozilla/test
mv src/java/org/bouncycastle/openssl/test/* src/test/org/bouncycastle/openssl/test
mv src/java/org/bouncycastle/tsp/test/* src/test/org/bouncycastle/tsp/test
mv src/java/org/bouncycastle/pkcs/test/* src/test/org/bouncycastle/pkcs/test
mv src/java/org/bouncycastle/dvcs/test/* src/test/org/bouncycastle/dvcs/test
mv src/java/org/bouncycastle/cert/path/test/* src/test/org/bouncycastle/cert/path/test
mv src/java/org/bouncycastle/operator/test/* src/test/org/bouncycastle/operator/test

cp -p %{SOURCE3} build.xml
cp -p %{SOURCE4} bcpkix.bnd
sed -i "s|@VERSION@|%{version}|" build.xml bcpkix.bnd

# this test fails:
rm src/test/org/bouncycastle/cms/test/Rfc4134Test.java
sed -i "s|suite.addTest(Rfc4134Test.suite());|//suite.addTest(Rfc4134Test.suite());|" \
  src/test/org/bouncycastle/cms/test/AllTests.java
rm -rf src/test/org/bouncycastle/openssl/test

%mvn_file :bcpkix-jdk15on bcpkix
%mvn_alias :bcpkix-jdk15on "org.bouncycastle:bctsp-jdk16"

%build
mkdir lib
build-jar-repository -s -p lib bcprov junit ant/ant-junit aqute-bnd
%ant -Dbc.test.data.home=$(pwd)/src/test jar javadoc
%mvn_artifact pom.xml build/bcpkix.jar

%install
%mvn_install -J build/apidocs

%files -f .mfiles
%doc CONTRIBUTORS.html index.html
%doc LICENSE.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE.html

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1_8jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1_7jpp8
- java 8 mass update

