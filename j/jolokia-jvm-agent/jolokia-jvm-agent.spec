Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name jolokia

# Filter requires for the Java Agent as deps are bundled within.
%global tools_or_json_simple com\\.googlecode\\.json-simple:json-simple.*|com\\.sun:tools.*
%global mvn_requires_filter .*mvn\\(%{tools_or_json_simple}\\)


Name:          jolokia-jvm-agent
Version:       1.6.2
Release:       alt1_10jpp11
Summary:       Jolokia JVM Agent

License:       ASL 2.0
URL:           https://jolokia.org

Source0:       https://github.com/rhuss/jolokia/releases/download/v%{version}/%{base_name}-%{version}-source.tar.gz
# See https://github.com/rhuss/jolokia/pull/413, namespace json simple
# so as to reduce problems related to classloading for apps using json_simple
# See also: https://github.com/rhuss/jolokia/issues/398
Patch1:        0001-Shade-json-simple-for-JVM-agent-jar.patch

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(com.googlecode.json-simple:json-simple)
# jolokia core depends on the servlet API
BuildRequires: mvn(javax.servlet:servlet-api)

Provides:      bundled(com.googlecode.json-simple:json-simple) = 1.1.1
Source44: import.info
%filter_from_requires /^%{mvn_requires_filter}$/d

%description
Jolokia JVM Agent.

%prep
%setup -q -n %{base_name}-%{version}
%patch1 -p1
# Only build the jolokia-jvm artefact.
%pom_disable_module it
%pom_disable_module client
%pom_disable_module tools/test-util
%pom_disable_module war agent
%pom_disable_module war-unsecured agent
%pom_disable_module jsr160 agent
%pom_disable_module osgi agent
%pom_disable_module osgi-bundle agent
%pom_disable_module jmx agent
%pom_disable_module jvm-spring agent
%pom_disable_module mule agent

%pom_xpath_remove pom:project/pom:build/pom:extensions pom.xml
%pom_xpath_remove pom:project/pom:reporting pom.xml

# Change compiler source/target version to JDK 8 level
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8" pom.xml
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8" pom.xml
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8" agent/jvm/pom.xml
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8" agent/jvm/pom.xml

# Remove scope=system for com.sun:tools
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:scope" agent/jvm
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:systemPath" agent/jvm

%build
%mvn_build -f -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc NOTICE

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.6.2-alt1_10jpp11
- update

* Tue Oct 08 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_2jpp8
- new version

