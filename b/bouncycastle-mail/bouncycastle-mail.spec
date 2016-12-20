Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global ver  1.54
%global archivever  jdk15on-%(echo %{ver}|sed 's|\\\.||')

Summary:          S/MIME and CMS libraries for Bouncy Castle
Name:             bouncycastle-mail
Version:          %{ver}
Release:          alt1_1jpp8
License:          MIT
URL:              http://www.bouncycastle.org/

# Source tarball contains everything except test suite rousources
Source0:          http://www.bouncycastle.org/download/bcmail-%{archivever}.tar.gz
# Test suite resources are found in this jar
Source1:          http://www.bouncycastle.org/download/bctest-%{archivever}.jar

Source2:          http://repo2.maven.org/maven2/org/bouncycastle/bcmail-jdk15on/%{version}/bcmail-jdk15on-%{version}.pom
Source3:          bouncycastle-mail-OSGi.bnd

BuildArch:        noarch
BuildRequires:    aqute-bnd
BuildRequires:    java-devel
BuildRequires:    javapackages-local
BuildRequires:    junit
BuildRequires:    mvn(org.bouncycastle:bcpkix-jdk15on) = %{version}
BuildRequires:    mvn(org.bouncycastle:bcprov-jdk15on) = %{version}
BuildRequires:    javamail
Requires:         mvn(org.bouncycastle:bcpkix-jdk15on) = %{version}
Requires:         mvn(org.bouncycastle:bcprov-jdk15on) = %{version}
Requires:         javamail
Source44: import.info

%description
Bouncy Castle consists of a lightweight cryptography API and is a provider 
for the Java Cryptography Extension and the Java Cryptography Architecture.
This library package offers additional classes, in particuar 
generators/processors for S/MIME and CMS, for Bouncy Castle.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for the %{name} package.

%prep
%setup -q -n bcmail-%{archivever}

# Unzip source and test suite resources
mkdir src
unzip -qq src.zip -d src/
unzip -qq %{SOURCE1} 'org/bouncycastle/mail/*' -x '*.class' '*.properties' -d src

cp -p %{SOURCE2} pom.xml

# Remove provided binaries
find . -type f -name "*.class" -delete
find . -type f -name "*.jar" -delete

cp -p %{SOURCE3} bcm.bnd
sed -i "s|@VERSION@|%{version}|" bcm.bnd

%mvn_file :bcmail-jdk15on bcmail
%mvn_alias :bcmail-jdk15on "org.bouncycastle:bcmail-jdk16"

%build
pushd src
  export CLASSPATH=$(build-classpath junit bcprov bcpkix javamail)
  javac -g -source 1.6 -target 1.6 -encoding UTF-8 $(find . -type f -name "*.java")
  jarfile="../bcmail.jar"
  # Exclude all */test/* , cf. upstream
  files="$(find . -type f \( -name '*.class' -o -name '*.properties' \) -not -path '*/test/*')"
  test ! -d classes && mf="" \
    || mf="`find classes/ -type f -name "*.mf" 2>/dev/null`"
  test -n "$mf" && jar cfm $jarfile $mf $files \
    || jar cf $jarfile $files
popd
bnd wrap -p bcm.bnd -o bcmail.bar bcmail.jar
mv bcmail.bar bcmail.jar
%mvn_artifact pom.xml bcmail.jar

%install
%mvn_install -J javadoc

%check
pushd src
  export CLASSPATH=$PWD:$(build-classpath junit hamcrest/core javamail bcprov bcpkix)
  for test in $(find . -name AllTests.class) ; do
    test=${test#./} ; test=${test%.class} ; test=${test//\//.}
    java org.junit.runner.JUnitCore $test
  done
popd

%files -f .mfiles
%doc CONTRIBUTORS.html index.html
%doc LICENSE.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE.html

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1_7jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1_6jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.46-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.46-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.46-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1_6jpp7
- fc release

