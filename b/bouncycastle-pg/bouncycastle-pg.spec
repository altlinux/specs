# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global ver 146
%global archivever  jdk16-%(echo %{ver}|sed 's|\\\.||')
Name:          bouncycastle-pg
Version:       1.46
Release:       alt3_8jpp7
Summary:       Bouncy Castle OpenPGP API
Group:         Development/Java
License:       MIT
URL:           http://www.bouncycastle.org/
Source0:       http://www.bouncycastle.org/download/bcpg-%{archivever}.tar.gz
Source1:       http://repo2.maven.org/maven2/org/bouncycastle/bcpg-jdk16/%{version}/bcpg-jdk16-%{version}.pom
Source2:       bouncycastle-pg-%{version}-01-build.xml
Source3:       bouncycastle-pg-%{version}-OSGi.bnd

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: ant-junit4 ant-junit
BuildRequires: aqute-bnd
BuildRequires: junit4

BuildRequires: bouncycastle = %{version}

Requires:      bouncycastle = %{version}

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
The Bouncy Castle Java API for handling the OpenPGP protocol. This
jar contains the OpenPGP API for JDK 1.6. The APIs can be used in 
conjunction with a JCE/JCA provider such as the one provided with the
Bouncy Castle Cryptography APIs.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n bcpg-%{archivever}
# fixing incomplete source directory structure
mkdir -p src/java src/test
unzip -qq src.zip -d src/java

mkdir -p src/test/org/bouncycastle/openpgp/test
mv src/java/org/bouncycastle/openpgp/test/* \
  src/test/org/bouncycastle/openpgp/test
mkdir -p src/test/org/bouncycastle/openpgp/examples/test
mv src/java/org/bouncycastle/openpgp/examples/test/* \
  src/test/org/bouncycastle/openpgp/examples/test

# Remove provided binaries and apidocs
find . -type f -name "*.class" -exec rm -f {} \;
find . -type f -name "*.jar" -exec rm -f {} \;
rm -rf docs/*

cp -p %{SOURCE2} build.xml
cp -p %{SOURCE3} bcpg.bnd

# this test fails: bc.test.data.home property not set
rm src/test/org/bouncycastle/openpgp/test/DSA2Test.java
sed -i "s|suite.addTestSuite(DSA2Test.class);|//suite.addTestSuite(DSA2Test.class);|" \
  src/test/org/bouncycastle/openpgp/test/AllTests.java

%build

%ant jar javadoc

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 build/bcpg.jar %{buildroot}%{_javadir}/bcpg.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-bcpg.pom
%add_maven_depmap JPP-bcpg.pom bcpg.jar

%files
%{_javadir}/bcpg.jar
%{_mavenpomdir}/JPP-bcpg.pom
%{_mavendepmapfragdir}/%{name}
%doc *.html

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.html

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.46-alt3_8jpp7
- fixed build

* Sun Sep 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.46-alt2_8jpp7
- fixed build with new slf4j

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1_8jpp7
- fc release

