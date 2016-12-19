Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          auto
Version:       1.1
Release:       alt1_3jpp8
Summary:       A collection of source code generators for Java
License:       ASL 2.0
URL:           https://github.com/google/auto
Source0:       https://github.com/google/auto/archive/auto-value-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.squareup:javawriter)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

%if 0
# Test deps
BuildRequires: mvn(com.google.code.findbugs:jsr305:1.3.9)
BuildRequires: mvn(junit:junit)
# Unavailable test deps
BuildRequires: mvn(com.google.dagger:dagger:2.0)
BuildRequires: mvn(com.google.dagger:dagger-compiler:2.0)
BuildRequires: mvn(com.google.guava:guava-testlib:18.0)
BuildRequires: mvn(com.google.inject:guice:4.0-beta)
BuildRequires: mvn(com.google.testing.compile:compile-testing:0.6)
BuildRequires: mvn(com.google.truth:truth:0.25)
%endif

BuildArch:     noarch
Source44: import.info

%description
The Auto sub-projects are a collection of code generators
that automate those types of tasks.

%package common
Group: Development/Java
Summary:       Auto Common Utilities

%description common
Common utilities for creating annotation processors.

%package factory
Group: Development/Java
Summary:       JSR-330-compatible factories

%description factory
A source code generator for JSR-330-compatible factories.

%package service
Group: Development/Java
Summary:       Provider-configuration files for ServiceLoader

%description service
A configuration/meta-data generator for
java.util.ServiceLoader-style service
providers.

%package value
Group: Development/Java
Summary:       Auto Value

%description value
Immutable value-type code generation for Java 1.6+.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n auto-auto-value-%{version}
find -name '*.class' -print -delete
find -name '*.jar' -print -delete

%pom_xpath_inject "pom:project" "
<modules>
  <module>common</module>
  <module>factory</module>
  <module>service</module>
  <module>value</module>
</modules>"

%pom_xpath_set "pom:project/pom:version" %{version}
for p in common factory service value ;do
%pom_xpath_set "pom:parent/pom:version" %{version} ${p}
%pom_xpath_set "pom:project/pom:version" %{version} ${p}
%pom_xpath_remove "pom:dependency[pom:scope = 'test']" ${p}
done

%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin
%pom_remove_plugin :maven-shade-plugin value
%pom_remove_plugin :maven-invoker-plugin value
%pom_remove_plugin :maven-invoker-plugin factory

%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-service']/pom:version" %{version} factory
%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-common']/pom:version" %{version} factory
%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-common']/pom:version" %{version} service
%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-common']/pom:version" %{version} value
%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-service']/pom:version" %{version} value

%build

# Unavailable test deps
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-%{name}-parent
%dir %{_javadir}/%{name}
%doc README.md
%doc LICENSE.txt

%files common -f .mfiles-%{name}-common
%doc common/README.md
%doc LICENSE.txt

%files factory -f .mfiles-%{name}-factory
%doc factory/README.md
%doc LICENSE.txt

%files service -f .mfiles-%{name}-service
%doc service/README.md
%doc LICENSE.txt

%files value -f .mfiles-%{name}-value
%doc value/README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3jpp8
- new version

