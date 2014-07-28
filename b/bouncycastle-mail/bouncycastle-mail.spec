# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global ver  1.46
%global archivever  jdk16-%(echo %{ver}|sed 's|\\\.||')

Summary:          S/MIME and CMS libraries for Bouncy Castle
Name:             bouncycastle-mail
Version:          %{ver}
Release:          alt2_7jpp7
Group:            System/Libraries
License:          MIT
URL:              http://www.bouncycastle.org/
Source0:          http://www.bouncycastle.org/download/bcmail-%{archivever}.tar.gz
Source1:          http://repo2.maven.org/maven2/org/bouncycastle/bcmail-jdk16/%{version}/bcmail-jdk16-%{version}.pom
Requires:         bouncycastle == %{version}
Requires:         bouncycastle >= 1.46-5
BuildRequires:    jpackage-utils >= 1.5
Requires:         jpackage-utils >= 1.5
Requires(post):   jpackage-utils >= 1.7
Requires(postun): jpackage-utils >= 1.7
BuildArch:        noarch
BuildRequires:    bouncycastle == %{version}
BuildRequires:    bouncycastle >= 1.46-5
BuildRequires:    javamail
Requires:         javamail
BuildRequires:    junit4

Provides:         bcmail = %{version}-%{release}
Source44: import.info

%description
Bouncy Castle consists of a lightweight cryptography API and is a provider 
for the Java Cryptography Extension and the Java Cryptography Architecture.
This library package offers additional classes, in particuar 
generators/processors for S/MIME and CMS, for Bouncy Castle.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
API documentation for the %{name} package.

%prep
%setup -q -n bcmail-%{archivever}
mkdir src
unzip -qq src.zip -d src/
# Remove provided binaries
find . -type f -name "*.class" -exec rm -f {} \;
find . -type f -name "*.jar" -exec rm -f {} \;

%build
pushd src
  export CLASSPATH=$(build-classpath junit4 bcprov javamail)
  %javac -g -source 1.6 -target 1.6 -encoding UTF-8 $(find . -type f -name "*.java")
  jarfile="../bcmail-%{version}.jar"
  # Exclude all */test/* , cf. upstream
  files="$(find . -type f \( -name '*.class' -o -name '*.properties' \) -not -path '*/test/*')"
  test ! -d classes && mf="" \
    || mf="`find classes/ -type f -name "*.mf" 2>/dev/null`"
  test -n "$mf" && %jar cvfm $jarfile $mf $files \
    || %jar cvf $jarfile $files
popd

%install
# install bouncy castle mail
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 bcmail-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/bcmail-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
  ln -sf bcmail-%{version}.jar bcmail.jar
popd
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/gcj-endorsed
pushd $RPM_BUILD_ROOT%{_javadir}/gcj-endorsed
  ln -sf ../bcmail-%{version}.jar bcmail-%{version}.jar
popd

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# maven pom
install -dm 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-bcmail.pom
%add_to_maven_depmap org.bouncycastle bcmail-jdk16 %{version} JPP bcmail

%check
pushd src
  export CLASSPATH=$PWD:$(build-classpath junit4 javamail bcprov)
  for test in $(find . -name AllTests.class) ; do
    test=${test#./} ; test=${test%.class} ; test=${test//\//.}
    # TODO: failures; get them fixed and remove || :
    %java org.junit.runner.JUnitCore $test || :
  done
popd

%files
%doc *.html
%{_javadir}/bcmail.jar
%{_javadir}/bcmail-%{version}.jar
%{_javadir}/gcj-endorsed/bcmail-%{version}.jar
%{_mavenpomdir}/JPP-bcmail.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.46-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.46-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1_6jpp7
- fc release

