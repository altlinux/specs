Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit e5dc3b04eeb9c7107f5a2b80c2b0f43434722cfd
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%bcond_with javadoc

Name:          apache-log4j-extras
Version:       1.2.17.1
Release:       alt1_18jpp11
Summary:       Apache Extras Companion for Apache log4j
License:       ASL 2.0

URL:           http://logging.apache.org/log4j/extras
Source0:       https://github.com/apache/log4j-extras/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.rat:apache-rat-plugin)
BuildRequires: mvn(org.hsqldb:hsqldb)

Requires:      mvn(log4j:log4j:1.2.17)
Source44: import.info

%description
Apache Extras Companion for Apache log4j is a collection of appenders, 
filters, layouts, and receivers for Apache log4j 1.2

%if %{with javadoc}
%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.
%endif


%prep
%setup -qn log4j-extras-%{commit}
# Cleanup
find . -name '*.class' -delete
find . -name '*.jar' -delete

# Unnecessary plugins
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-site-plugin

%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:groupId='hsqldb']/pom:groupId" org.hsqldb

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%build
%if %{without javadoc}
args="-j"
%endif
# Tests disabled because of failures
%mvn_build $args -- -DskipTests -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%dir %{_javadir}/%{name}

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE
%endif

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.2.17.1-alt1_18jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.17.1-alt1_15jpp8
- fc update

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.17.1-alt1_13jpp8
- explicit build with java8

* Mon Jan 28 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.17.1-alt1_12jpp8
- new version

