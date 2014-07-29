# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname CodeNarc
%global with_gmaven 0
Name:          codenarc
Version:       0.17
Release:       alt1_3jpp7
Summary:       Groovy library that provides static analysis features for Groovy code
Group:         Development/Java
License:       ASL 2.0
Url:           http://codenarc.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/codenarc/codenarc/CodeNarc%%20Version%%20%{version}/CodeNarc-%{version}-bin.tar.gz
Source1:       codenarc-%{version}-build.xml
Source2:       codenarc-%{version}-build.properties
# remove gmaven
# change artifactId groovy-all in groovy
Patch0:        codenarc-0.17-pom.patch
# remove @Override
# unavailable method in groovy 1.8.x (...)
Patch1:        codenarc-0.17-groovy18.patch
# replace runtime 1.7 witn runtime 1.8
# add groovy-all deps
Patch2:        codenarc-0.17-enable-gmaven.patch

BuildRequires: jpackage-utils

BuildRequires: antlr
BuildRequires: apache-commons-cli
BuildRequires: objectweb-asm

BuildRequires: ant
BuildRequires: cobertura
BuildRequires: gmetrics
BuildRequires: groovy
BuildRequires: log4j

%if %with_gmaven
# https://bugzilla.redhat.com/show_bug.cgi?id=841833
BuildRequires: gmaven
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
# test deps
BuildRequires: junit

%endif

Requires:      ant
Requires:      cobertura
Requires:      gmetrics
Requires:      groovy
Requires:      log4j

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
CodeNarc is a static analysis tool for Groovy source code,
enabling monitoring and enforcement of many coding standards
and best practices. CodeNarc applies a set of Rules
(predefined and/or custom) that are applied to each Groovy
file, and generates an HTML report of the results, including
a list of rules violated for each source file, and a count
of the number of violations per package and for the whole
project.

%package javadoc
Group:         Development/Java
Summary:       Groovydoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains groovydoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}

find . -name "*.jar" -delete
find . -name "*.class" -delete
rm -rf docs/*

%patch0 -p0
%patch1 -p1


%if !%with_gmaven
# in fedora haven't gmaven yet
cp -pr %{SOURCE1} build.xml
cp -pr %{SOURCE2} build.properties
%else
%patch2 -p0
%endif

chmod 644 README.txt
for d in CHANGELOG.txt LICENSE.txt NOTICE.txt README.txt ; do
  sed -i 's/\r//' $d
done

%build

%if !%with_gmaven
ant
%else
mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.failure.ignore=true install javadoc:aggregate
%endif

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{oname}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar


(
  cd %{buildroot}%{_javadir}
  ln -sf %{name}.jar %{oname}.jar
)

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{oname}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc CHANGELOG.txt LICENSE.txt NOTICE.txt README.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_3jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_2jpp7
- new version

