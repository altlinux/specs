Epoch: 0
Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global ver 1.54
%global archivever jdk15on-%(echo %{ver}|sed 's|\\\.||')
%global classname org.bouncycastle.jce.provider.BouncyCastleProvider

Summary:          Bouncy Castle Crypto Package for Java
Name:             bouncycastle
Version:          %{ver}
Release:          alt1_2jpp8
License:          MIT
URL:              http://www.bouncycastle.org

# Source tarball contains everything except test suite rousources
Source0:          http://www.bouncycastle.org/download/bcprov-%{archivever}.tar.gz
# Test suite resources are found in this jar
Source1:          http://www.bouncycastle.org/download/bctest-%{archivever}.jar

Source2:          http://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/%{ver}/bcprov-jdk15on-%{ver}.pom
Source3:          bouncycastle-OSGi.bnd

BuildRequires:    aqute-bnd
BuildRequires:    java-devel
BuildRequires:    junit
BuildRequires:    javapackages-local

BuildArch:        noarch

Provides:         bcprov = %{version}-%{release}
Source44: import.info

%description
The Bouncy Castle Crypto package is a Java implementation of cryptographic
algorithms. The package is organized so that it contains a light-weight API
suitable for use in any environment (including the newly released J2ME) with
the additional infrastructure to conform the algorithms to the JCE framework.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for the %{name} package.

%prep
%setup -q -n bcprov-%{archivever}

# Unzip source and test suite resources
mkdir src
unzip -qq src.zip -d src/
unzip -qq %{SOURCE1} 'PKITS/*' 'org/bouncycastle/*' -x '*.class' -d src

cp -p %{SOURCE2} pom.xml

# Remove provided binaries
find . -type f -name "*.class" -exec rm -f {} \;
find . -type f -name "*.jar" -exec rm -f {} \;

cp -p %{SOURCE3} bc.bnd
sed -i "s|@VERSION@|%{version}|" bc.bnd

%mvn_file :bcprov-jdk15on bcprov
%mvn_alias :bcprov-jdk15on "bouncycastle:bcprov-jdk15" "org.bouncycastle:bcprov-jdk16" "org.bouncycastle:bcprov-jdk15"

%build
pushd src
  export CLASSPATH=$(build-classpath junit)
  javac -g -source 1.6 -target 1.6 -encoding UTF-8 $(find . -type f -name "*.java")
  jarfile="../bcprov.jar"
  # Exclude all */test/* files except org.bouncycastle.util.test, cf. upstream
  files="$(find . -type f \( -name '*.class' -o -name '*.properties' \) -not -path '*/test/*')"
  files="$files $(find . -type f -path '*/org/bouncycastle/util/test/*.class')"
  test ! -d classes && mf="" \
    || mf="`find classes/ -type f -name "*.mf" 2>/dev/null`"
  test -n "$mf" && jar cfm $jarfile $mf $files \
    || jar cf $jarfile $files
popd
bnd wrap -p bc.bnd -o bcprov.bar bcprov.jar
mv bcprov.bar bcprov.jar
%mvn_artifact pom.xml bcprov.jar

%install
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d/2000-%{classname}

%mvn_install -J javadoc

%check
# There was 1 failure:
# 1) testJCE(org.bouncycastle.jce.provider.test.AllTests$SimpleTestTest)
# junit.framework.AssertionFailedError: CertPathValidator:
# Exception: org.bouncycastle.jce.exception.ExtCertPathValidatorException:
# Could not validate certificate: certificate expired on 20160803124921GMT+00:00
pushd src
  export CLASSPATH=$PWD:$(build-classpath junit hamcrest/core)
  for test in $(find . -name AllTests.class) ; do
    test=${test#./} ; test=${test%.class} ; test=${test//\//.}
    # TODO: failures; get them fixed and remove || :
    java -Dbc.test.data.home=$(pwd) org.junit.runner.JUnitCore $test || :
  done
popd

%post
{
  # Rebuild the list of security providers in classpath.security
  suffix=security/classpath.security
  secfiles="/usr/lib/$suffix /usr/lib64/$suffix"

  for secfile in $secfiles
  do
    # check if this classpath.security file exists
    [ -f "$secfile" ] || continue

    sed -i '/^security\.provider\./d' "$secfile"

    count=0
    for provider in $(ls /etc/java/security/security.d)
    do
      count=$((count + 1))
      echo "security.provider.${count}=${provider#*-}" >> "$secfile"
    done
  done
} || :

%postun
if [ $1 -eq 0 ] ; then

  {
    # Rebuild the list of security providers in classpath.security
    suffix=security/classpath.security
    secfiles="/usr/lib/$suffix /usr/lib64/$suffix"

    for secfile in $secfiles
    do
      # check if this classpath.security file exists
      [ -f "$secfile" ] || continue

      sed -i '/^security\.provider\./d' "$secfile"

      count=0
      for provider in $(ls /etc/java/security/security.d)
      do
        count=$((count + 1))
        echo "security.provider.${count}=${provider#*-}" >> "$secfile"
      done
    done
  } || :

fi

%files -f .mfiles
%doc CONTRIBUTORS.html index.html
%doc LICENSE.html
%{_sysconfdir}/java/security/security.d/2000-%{classname}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.html

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.54-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.52-alt1_8jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.52-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.46-alt3_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.46-alt3_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.46-alt3_6jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.46-alt2_6jpp7
- fc release

* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.46-alt2_3jpp6
- fixed provides

* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.46-alt1_3jpp6
- new jpp release

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.43-alt1_1jpp6
- new version

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.37-alt1_5jpp1.7
- converted from JPackage by jppimport script

