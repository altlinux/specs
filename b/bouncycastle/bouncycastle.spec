Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global ver  1.46
%global archivever  jdk16-%(echo %{ver}|sed 's|\\\.||')
%global classname   org.bouncycastle.jce.provider.BouncyCastleProvider

Summary:          Bouncy Castle Crypto Package for Java
Name:             bouncycastle
Version:          %{ver}
Release:          alt3_6jpp7
Group:            System/Libraries
License:          MIT
URL:              http://www.%{name}.org/
# Use original sources from here on out.
Source0:          http://www.bouncycastle.org/download/bcprov-%{archivever}.tar.gz
Source1:          http://repo2.maven.org/maven2/org/bouncycastle/bcprov-jdk16/%{version}/bcprov-jdk16-%{version}.pom
BuildRequires:    jpackage-utils >= 1.5
Requires:         jpackage-utils >= 1.5
Requires(post):   jpackage-utils >= 1.7
Requires(postun): jpackage-utils >= 1.7
BuildArch:        noarch
BuildRequires:    junit4

Provides:         bcprov = %{version}-%{release}
Source44: import.info

%description
The Bouncy Castle Crypto package is a Java implementation of cryptographic
algorithms. The package is organised so that it contains a light-weight API
suitable for use in any environment (including the newly released J2ME) with
the additional infrastructure to conform the algorithms to the JCE framework.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch:      noarch
Requires:       bouncycastle = %{?epoch:%epoch:}%{version}-%{release}
Requires:       jpackage-utils

%description javadoc
API documentation for the %{name} package.

%prep
%setup -q -n bcprov-%{archivever}

# Remove provided binaries
find . -type f -name "*.class" -exec rm -f {} \;
find . -type f -name "*.jar" -exec rm -f {} \;

mkdir src
unzip -qq src.zip -d src/

%build
pushd src
  export CLASSPATH=$(build-classpath junit4)
  %javac -g -source 1.6 -target 1.6 -encoding UTF-8 $(find . -type f -name "*.java")
  jarfile="../bcprov-%{version}.jar"
  # Exclude all */test/* files except org.bouncycastle.util.test, cf. upstream
  files="$(find . -type f \( -name '*.class' -o -name '*.properties' \) -not -path '*/test/*')"
  files="$files $(find . -type f -path '*/org/bouncycastle/util/test/*.class')"
  files="$files $(find . -type f -path '*/org/bouncycastle/jce/provider/test/*.class')"
  files="$files $(find . -type f -path '*/org/bouncycastle/ocsp/test/*.class')"
  test ! -d classes && mf="" \
    || mf="`find classes/ -type f -name "*.mf" 2>/dev/null`"
  test -n "$mf" && jar cvfm $jarfile $mf $files \
    || %jar cvf $jarfile $files
popd

%install
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d/2000-%{classname}

# install bouncy castle provider
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 bcprov-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/bcprov-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf bcprov-%{version}.jar bcprov.jar
popd
  install -dm 755 $RPM_BUILD_ROOT%{_javadir}/gcj-endorsed
  pushd $RPM_BUILD_ROOT%{_javadir}/gcj-endorsed
    ln -sf ../bcprov-%{version}.jar bcprov-%{version}.jar
  popd

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# maven pom
install -dm 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-bcprov.pom
%add_to_maven_depmap org.bouncycastle bcprov-jdk16 %{version} JPP bcprov

%check
pushd src
  export CLASSPATH=$PWD:$(build-classpath junit4)
  for test in $(find . -name AllTests.class) ; do
    test=${test#./} ; test=${test%.class} ; test=${test//\//.}
    # TODO: failures; get them fixed and remove || :
    %java org.junit.runner.JUnitCore $test || :
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

:

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
:

%files
%doc *.html
%{_javadir}/bcprov.jar
%{_javadir}/bcprov-%{version}.jar
  %{_javadir}/gcj-endorsed/bcprov-%{version}.jar
%{_sysconfdir}/java/security/security.d/2000-%{classname}
%{_mavenpomdir}/JPP-bcprov.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}/

%changelog
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

