Epoch: 0
Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global gittag r1rv80
%global classname org.bouncycastle.jce.provider.BouncyCastleProvider
%global profilen 1.8
%global profile %(echo %{profilen} | sed "s/\\.//g" )
%global jdkon jdk%{profile}on

Summary:          Bouncy Castle Cryptography APIs for Java
Name:             bouncycastle
Version:          1.80
Release:          alt1
License:          MIT
URL:              https://www.bouncycastle.org

Source0:          https://github.com/bcgit/bc-java/archive/%{gittag}.tar.gz

# POMs from Maven Central
Source1:          https://repo1.maven.org/maven2/org/bouncycastle/bcprov-%{jdkon}/%{version}/bcprov-%{jdkon}-%{version}.pom
Source2:          https://repo1.maven.org/maven2/org/bouncycastle/bcpkix-%{jdkon}/%{version}/bcpkix-%{jdkon}-%{version}.pom
Source3:          https://repo1.maven.org/maven2/org/bouncycastle/bcpg-%{jdkon}/%{version}/bcpg-%{jdkon}-%{version}.pom
Source4:          https://repo1.maven.org/maven2/org/bouncycastle/bcmail-%{jdkon}/%{version}/bcmail-%{jdkon}-%{version}.pom
Source5:          https://repo1.maven.org/maven2/org/bouncycastle/bctls-%{jdkon}/%{version}/bctls-%{jdkon}-%{version}.pom
Source6:          https://repo1.maven.org/maven2/org/bouncycastle/bcutil-%{jdkon}/%{version}/bcutil-%{jdkon}-%{version}.pom
Source7:          https://repo1.maven.org/maven2/org/bouncycastle/bcjmail-%{jdkon}/%{version}/bcjmail-%{jdkon}-%{version}.pom

# Script to fetch POMs from Maven Central
Source8:          get-poms.sh

Patch0:           jmail.packages.patch

BuildArch:        noarch

BuildRequires:    aqute-bnd
BuildRequires:    ant
BuildRequires:    ant-junit
#                 For bcmail
BuildRequires:    jakarta-activation1
BuildRequires:    jakarta-mail1
#                 For bcjmail
BuildRequires:    jakarta-activation
BuildRequires:    jakarta-mail
BuildRequires:    javapackages-local

Requires(post):   javapackages-tools
Requires(postun): javapackages-tools

Provides:         bcprov = %{version}-%{release}
Source44: import.info

%description
The Bouncy Castle Crypto package is a Java implementation of cryptographic
algorithms. This jar contains JCE provider and lightweight API for the
Bouncy Castle Cryptography APIs for JDK 1.5 to JDK 1.8.

%package pkix
Group: System/Libraries
Summary: Bouncy Castle PKIX, CMS, EAC, TSP, PKCS, OCSP, CMP, and CRMF APIs

%description pkix
The Bouncy Castle Java APIs for CMS, PKCS, EAC, TSP, CMP, CRMF, OCSP, and
certificate generation. This jar contains APIs for JDK 1.5 to JDK 1.8. The
APIs can be used in conjunction with a JCE/JCA provider such as the one
provided with the Bouncy Castle Cryptography APIs.

%package pg
Group: System/Libraries
Summary: Bouncy Castle OpenPGP API

%description pg
The Bouncy Castle Java API for handling the OpenPGP protocol. The APIs can be
used in conjunction with a JCE/JCA provider such as the one provided with the
Bouncy Castle Cryptography APIs.

%package mail
Group: System/Libraries
Summary: Bouncy Castle S/MIME API

%description mail
The Bouncy Castle Java S/MIME APIs for handling S/MIME protocols. The APIs can
be used in conjunction with a JCE/JCA provider such as the one provided with
the Bouncy Castle Cryptography APIs. The JavaMail API and the Java activation
framework will also be needed.

%package jmail
Group: System/Libraries
Summary: Bouncy Castle Jakarta S/MIME API

%description jmail
The Bouncy Castle Java S/MIME APIs for handling S/MIME protocols. The APIs can
be used in conjunction with a JCE/JCA provider such as the one provided with
the Bouncy Castle Cryptography APIs. The Jakarta Mail API and the Jakarta
activation framework will also be needed.

%package tls
Group: System/Libraries
Summary: Bouncy Castle JSSE provider and TLS/DTLS API

%description tls
The Bouncy Castle Java APIs for TLS and DTLS, including a provider for the
JSSE.

%package util
Group: System/Libraries
Summary: Bouncy Castle ASN.1 Extension and Utility APIs

%description util
The Bouncy Castle Java APIs for ASN.1 extension and utility APIs used to
support bcpkix and bctls.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for the Bouncy Castle Cryptography APIs.

%prep
%setup -q -n bc-java-%{gittag}
%patch0 -p1

for x in `find | grep  -e  x_pkcs7_signature.java  -e PKCS7ContentHandler.java -e multipart_signed.java` ; do
  sed "s/getTransferData.ActivationDataFlavor/getTransferData(DataFlavor/g" -i $x
  sed "s/            ActivationDataFlavor df,/            DataFlavor df,/g"  -i $x
done

# Remove bundled binary libs
find . -type f -name "*.class" -exec rm -f {} \;
find . -type f -name "*.jar" -exec rm -f {} \;

# Not shipping lw/lcrypto (lightweight crypto) jar
sed -i -e '/target="build-lw"/d' ant/jdk%{profile}+.xml
sed -i -e '/target="javadoc-lw"/d' ant/jdk%{profile}+.xml

cp -p %{SOURCE1} bcprov.pom
cp -p %{SOURCE2} bcpkix.pom
cp -p %{SOURCE3} bcpg.pom
cp -p %{SOURCE4} bcmail.pom
cp -p %{SOURCE5} bctls.pom
cp -p %{SOURCE6} bcutil.pom
cp -p %{SOURCE7} bcjmail.pom

# this test needs additional dependeces
rm -v prov/src/test/java/org/bouncycastle/jce/provider/test/X509LDAPCertStoreTest.java
# and those depends on it
rm -v prov/src/test/java/org/bouncycastle/jce/provider/test/RegressionTest.java
rm -v prov/src/test/java/org/bouncycastle/jce/provider/test/SimpleTestTest.java
rm -v prov/src/test/java/org/bouncycastle/jce/provider/test/AllTests.java

%build
ant -f ant/jdk%{profile}+.xml \
  -Djunit.jar.home=$(build-classpath junit) \
  -Dmail.jar.home=$(build-classpath jakarta-mail1/jakarta.mail) \
  -Dactivation.jar.home=$(build-classpath jakarta-activation1/jakarta.activation) \
  -Djmail.jar.home=$(build-classpath jakarta-mail/jakarta.mail) \
  -Djactivation.jar.home=$(build-classpath jakarta-activation) \
  -Drelease.debug=true -Dbc.javac.source=1.8 -Dbc.javac.target=1.8 \
  clean build-provider build #test

cat > bnd.bnd <<EOF
-classpath=bcprov.jar,bcutil.jar,bcpkix.jar,bcpg.jar,bcmail.jar,bcjmail.jar,bctls.jar
Export-Package: *;version=%{version}
EOF

for bc in bcprov bcutil bcpkix bcpg bcmail bcjmail bctls ; do
  # Make into OSGi bundle
  bnd wrap -b $bc -v %{version} -p bnd.bnd -o $bc.jar build/artifacts/jdk%{profilen}/jars/$bc-%{jdkon}-*.jar

  # Request Maven installation
  %mvn_file ":$bc-%{jdkon}" $bc
  %mvn_package ":$bc-%{jdkon}" $bc
  %mvn_alias ":$bc-%{jdkon}" "org.bouncycastle:$bc-jdk16" "org.bouncycastle:$bc-jdk15" \
  "org.bouncycastle:$bc-jdk16on" "org.bouncycastle:$bc-jdk15on"

  %mvn_artifact $bc.pom $bc.jar
done

%install
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d/2000-%{classname}

%mvn_install -J build/artifacts/jdk%{profilen}/javadoc

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
if [ "$1" -eq 0 ] ; then

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

%files -f .mfiles-bcprov
%doc --no-dereference build/artifacts/jdk%{profilen}/bcprov-%{jdkon}-*/LICENSE.html
%doc docs/ *.html
%{_sysconfdir}/java/security/security.d/2000-%{classname}

%files pkix -f .mfiles-bcpkix
%doc --no-dereference build/artifacts/jdk%{profilen}/bcpkix-%{jdkon}-*/LICENSE.html

%files pg -f .mfiles-bcpg
%doc --no-dereference build/artifacts/jdk%{profilen}/bcpg-%{jdkon}-*/LICENSE.html

%files mail -f .mfiles-bcmail
%doc --no-dereference build/artifacts/jdk%{profilen}/bcmail-%{jdkon}-*/LICENSE.html

%files jmail -f .mfiles-bcjmail
%doc --no-dereference build/artifacts/jdk%{profilen}/bcjmail-%{jdkon}-*/LICENSE.html

%files tls -f .mfiles-bctls
%doc --no-dereference build/artifacts/jdk%{profilen}/bctls-%{jdkon}-*/LICENSE.html

%files util -f .mfiles-bcutil
%doc --no-dereference build/artifacts/jdk%{profilen}/bcutil-%{jdkon}-*/LICENSE.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.html

%changelog
* Thu Jan 29 2026 Anton Meleshnikov <alton@altlinux.org> 0:1.80-alt1
- new version (thanks fedora for the spec and the patch)

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 0:1.70-alt1_4jpp11
- new version

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0:1.68-alt1_2jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:1.67-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.65-alt1_4jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:1.63-alt1_2jpp8
- new version

* Wed Jun 12 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.61-alt1_1jpp8
- new version

* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.58-alt2_3jpp8
- e2k build w/o javadoc & tests

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.58-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.58-alt1_1jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.54-alt1_3jpp8
- new jpp release

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

