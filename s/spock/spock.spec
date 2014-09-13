# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name spock
%define version 0.7
%global namedreltag  -groovy-1.8
%global namedversion %{version}%{?namedreltag}
%global nameddottag  %(echo %{?namedreltag} | tr - . )
Name:          spock
Version:       0.7
Release:       alt1_0.2.groovy.1.8jpp7
Summary:       A testing and specification framework
Group:         Development/Java
License:       ASL 2.0
URL:           http://code.google.com/p/spock/
# git clone git://github.com/spockframework/spock.git spock-0.6-groovy-1.8
# cd spock-0.6-groovy-1.8/ && git archive --format=tar --prefix=spock-0.6-groovy-1.8/ spock-0.6-groovy-1.8 | xz > spock-0.6-groovy-1.8-src-git.tar.xz
Source0:       https://github.com/spockframework/spock/archive/%{name}-%{namedversion}.tar.gz
Source1:       http://repo1.maven.org/maven2/org/spockframework/%{name}-core/%{namedversion}/%{name}-core-%{namedversion}.pom
Source2:       http://repo1.maven.org/maven2/org/spockframework/%{name}-guice/%{namedversion}/%{name}-guice-%{namedversion}.pom
Source3:       %{name}-%{namedversion}-build.xml


BuildRequires: ant
BuildRequires: antlr
BuildRequires: aopalliance
BuildRequires: apache-commons-cli
BuildRequires: cglib
BuildRequires: google-guice
BuildRequires: groovy
BuildRequires: hamcrest12
BuildRequires: junit
BuildRequires: objectweb-asm
BuildRequires: objenesis

BuildArch:     noarch
Source44: import.info

%description
Spock is a testing and specification framework for Java and
Groovy applications.

%package core
Group:         Development/Java
Summary:       Spock Framework - Core Module
Requires:      ant
Requires:      cglib
Requires:      groovy
Requires:      hamcrest12
Requires:      junit
Requires:      objectweb-asm
Requires:      objenesis

%description core
Spock Framework - Core Module.

%package guice
Group:         Development/Java
Summary:       Spock Framework - Guice Module
Requires:      google-guice
Requires:      %{name}-core = %{version}-%{release}

%description guice
Spock Framework - Guice Module provides support for
testing Guice 2/3 based applications.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}
find . -name "*.class" -delete
find . -name "*.jar" -delete
cp -p %{SOURCE1} core-pom.xml
%pom_add_dep org.hamcrest:hamcrest-library:1.3:compile core-pom.xml
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:groupId ='junit']/pom:artifactId" core-pom.xml
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:groupId ='junit']" \
 "<artifactId>junit</artifactId>" core-pom.xml
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:groupId ='org.codehaus.groovy']/pom:artifactId" core-pom.xml
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:groupId ='org.codehaus.groovy']" \
 "<artifactId>groovy</artifactId>" core-pom.xml
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:groupId ='cglib']/pom:artifactId" core-pom.xml
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:groupId ='cglib']" \
 "<artifactId>cglib</artifactId>" core-pom.xml
cp -p %{SOURCE2} guice-pom.xml

cp -p %{SOURCE3} build.xml

%build

ant build javadoc

%install

# TODO spring requires org.springframework:spring-test
mkdir -p %{buildroot}%{_javadir}
for m in core guice; do
  install -m 644 %{name}-${m}/build/libs/%{name}-${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-${m}.jar
done

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 core-pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-core.pom
%add_maven_depmap -f core JPP-%{name}-core.pom %{name}-core.jar
install -pm 644 guice-pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-guice.pom
%add_maven_depmap -f guice JPP-%{name}-guice.pom %{name}-guice.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/api/* %{buildroot}%{_javadocdir}/%{name}

%files core
%{_javadir}/%{name}-core.jar
%{_mavenpomdir}/JPP-%{name}-core.pom
%{_mavendepmapfragdir}/%{name}-core
%doc LICENSE NOTICE

%files guice
%{_javadir}/%{name}-guice.jar
%{_mavenpomdir}/JPP-%{name}-guice.pom
%{_mavendepmapfragdir}/%{name}-guice
%doc LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_0.2.groovy.1.8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_0.5.groovy.1.8jpp7
- new release

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_0.3.groovy.1.8jpp7
- merged junit-junit4

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_0.3%(echo -groovy-1.8 | tr - . )jpp7
- fixed build with new junit

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_0.3%(echo -groovy-1.8 | tr - . )jpp7
- new version

