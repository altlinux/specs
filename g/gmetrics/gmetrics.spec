Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname GMetrics

Name:          gmetrics
Version:       0.6
Release:       alt1_7jpp7
Summary:       Groovy library that provides reports and metrics for Groovy code
License:       ASL 2.0
Url:           http://gmetrics.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}/%{oname}-%{version}-bin.tar.gz
# remove gmaven
# remove codenarc
# change artifactId groovy-all in groovy
Patch0:        gmetrics-0.5-pom.patch
# replace runtime 1.5 witn runtime 1.8
# add groovy-all deps with generic version
Patch1:        gmetrics-0.6-antrun-plugin.patch


BuildRequires: ant
BuildRequires: groovy
BuildRequires: log4j
# groovy-all embedded libs
BuildRequires: antlr
BuildRequires: apache-commons-cli
BuildRequires: objectweb-asm
BuildRequires: fusesource-pom
BuildRequires: slf4j

# depend on rhbz#914056 BuildRequires: gmaven
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-enforcer-plugin

BuildArch:     noarch
Source44: import.info

%description
GMetrics provides calculation and reporting of size and
complexity metrics for Groovy source code, by scanning the
code with an Ant Task, applying a set of metrics, and
generating an HTML or XML report of the results.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}

# clean up
find . -name "*.jar" -delete
find . -name "*.class" -delete
rm -rf docs/*
%patch0 -p0
%patch1 -p0

sed -i "s|pom.version|project.version|" pom.xml

chmod 644 README.txt

for d in CHANGELOG.txt LICENSE.txt NOTICE.txt README.txt ; do
  sed -i 's/\r//' $d
done

%build

%mvn_file :%{oname} %{name}
%mvn_file :%{oname} %{oname}
# test skipped require Codenarc, circular deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.txt LICENSE.txt NOTICE.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_5jpp7
- new release

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_2jpp7
- new version

