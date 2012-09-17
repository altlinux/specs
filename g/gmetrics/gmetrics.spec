BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname GMetrics
%global with_gmaven 0
Name:          gmetrics
Version:       0.5
Release:       alt1_2jpp7
Summary:       Groovy library that provides reports and metrics for Groovy code
Group:         Development/Java
License:       ASL 2.0
Url:           http://gmetrics.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/gmetrics/gmetrics-0.5/GMetrics-0.5-bin.tar.gz
Source1:       gmetrics-0.5-build.xml
Source2:       gmetrics-0.5-build.properties
# remove gmaven
# remove codenarc
# change artifactId groovy-all in groovy
Patch0:        gmetrics-0.5-pom.patch
# replace runtime 1.5 witn runtime 1.8
# add groovy-all deps
Patch1:        gmetrics-0.5-enable-gmaven.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: groovy
BuildRequires: log4j
# groovy-all bundled libs
BuildRequires: antlr
BuildRequires: apache-commons-cli
BuildRequires: objectweb-asm
%if %with_gmaven
BuildRequires: gmaven
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
%endif

Requires:      ant
Requires:      apache-commons-cli
Requires:      groovy
Requires:      log4j

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
GMetrics provides calculation and reporting of size and
complexity metrics for Groovy source code, by scanning the
code with an Ant Task, applying a set of metrics, and
generating an HTML or XML report of the results.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}

# clean up
find . -name "*.jar" -delete
find . -name "*.jar" -delete
rm -rf docs/*
%patch0 -p0
%if !%with_gmaven
# in fedora haven't gmaven yet
cp -pr %{SOURCE1} build.xml
cp -pr %{SOURCE2} build.properties
%else
%patch1 -p0
%endif

chmod 644 README.txt

for d in CHANGELOG.txt LICENSE.txt NOTICE.txt README.txt ; do
  sed -i 's/\r//' $d
done

%build

%if !%with_gmaven
ant
%else
# test skipped require Codenarc, circular deps
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate
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
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_2jpp7
- new version

