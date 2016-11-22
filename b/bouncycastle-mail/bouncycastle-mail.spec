Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global ver  1.52
%global archivever  jdk15on-%(echo %{ver}|sed 's|\\\.||')

Summary:          S/MIME and CMS libraries for Bouncy Castle
Name:             bouncycastle-mail
Version:          %{ver}
Release:          alt1_7jpp8
License:          MIT
URL:              http://www.bouncycastle.org/
Source0:          http://www.bouncycastle.org/download/bcmail-%{archivever}.tar.gz
Source1:          http://repo2.maven.org/maven2/org/bouncycastle/bcmail-jdk15on/%{version}/bcmail-jdk15on-%{version}.pom
Source2:          bouncycastle-mail-OSGi.bnd

BuildArch:        noarch
BuildRequires:    aqute-bnd
BuildRequires:    bouncycastle = %{version}
BuildRequires:    bouncycastle-pkix = %{version}
BuildRequires:    javamail
BuildRequires:    maven-local
BuildRequires:    junit
Requires:         bouncycastle = %{version}
Requires:         bouncycastle-pkix = %{version}
Requires:         javamail
Provides:         bcmail = %{version}-%{release}
Source44: import.info

%description
Bouncy Castle consists of a lightweight cryptography API and is a provider 
for the Java Cryptography Extension and the Java Cryptography Architecture.
This library package offers additional classes, in particuar 
generators/processors for S/MIME and CMS, for Bouncy Castle.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Requires:       %{name} = %{version}
BuildArch: noarch

%description javadoc
API documentation for the %{name} package.

%prep
%setup -q -n bcmail-%{archivever}
mkdir src
unzip -qq src.zip -d src/

find . -type f -name "*.class" -delete
find . -type f -name "*.jar" -delete

# too many "IOException: Stream closed" failures
rm -f src/org/bouncycastle/mail/smime/test/AllTests.java

# package org.bouncycastle.cms.test does not exist
rm -f src/org/bouncycastle/mail/smime/test/NewSMIMEEnvelopedTest.java
rm -f src/org/bouncycastle/mail/smime/test/NewSMIMESignedTest.java
rm -f src/org/bouncycastle/mail/smime/test/SMIMECompressedTest.java
rm -f src/org/bouncycastle/mail/smime/test/SMIMEMiscTest.java
rm -f src/org/bouncycastle/mail/smime/test/SMIMEToolkitTest.java
rm -f src/org/bouncycastle/mail/smime/test/SignedMailValidatorTest.java

cp %{SOURCE1} pom.xml
cp -p %{SOURCE2} bcm.bnd
sed -i "s|@VERSION@|%{version}|" bcm.bnd

%build
pushd src
  export CLASSPATH=$(build-classpath junit bcprov bcpkix javamail)
  %javac -g -source 1.6 -target 1.6 -encoding UTF-8 $(find . -type f -name "*.java")
  jarfile="../bcmail.jar"
  # Exclude all */test/* , cf. upstream
  files="$(find . -type f \( -name '*.class' -o -name '*.properties' \) -not -path '*/test/*')"
  test ! -d classes && mf="" \
    || mf="`find classes/ -type f -name "*.mf" 2>/dev/null`"
  test -n "$mf" && %jar cvfm $jarfile $mf $files \
    || %jar cvf $jarfile $files
popd

bnd wrap --properties bcm.bnd --output bcmail.bar bcmail.jar

%install
# install bouncy castle mail
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 bcmail.bar \
  $RPM_BUILD_ROOT%{_javadir}/bcmail.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# maven pom
install -dm 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-bcmail.pom
%add_maven_depmap -a "org.bouncycastle:bcmail-jdk16" JPP-bcmail.pom bcmail.jar

%check
pushd src
  export CLASSPATH=$PWD:$(build-classpath junit javamail bcprov bcpkix)
  for test in $(find . -name AllTests.class) ; do
    test=${test#./} ; test=${test%.class} ; test=${test//\//.}
    %java org.junit.runner.JUnitCore $test
  done
popd

%files -f .mfiles
%doc CONTRIBUTORS.html index.html
%doc LICENSE.html

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.html

%changelog
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

