Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          auto
Version:       1.4.1
Release:       alt1_1jpp8
Summary:       A collection of source code generators for Java
License:       ASL 2.0
URL:           https://github.com/google/auto
Source0:       https://github.com/google/auto/archive/auto-value-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava:19.0)
BuildRequires:  mvn(com.squareup:javapoet)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
The Auto sub-projects are a collection of code generators
that automate those types of tasks.

%package common
Group: Development/Java
Summary:       Auto Common Utilities
# Obsoletes added in F30
Obsoletes:     %{name}-factory < %{version}-%{release}

%description common
Common utilities for creating annotation processors.

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

# Disable factory module due to missing dep:
# com.google.googlejavaformat:google-java-format
%pom_disable_module factory build-pom.xml

%pom_xpath_set "pom:project/pom:version" 3
for p in common factory service value ;do
%pom_xpath_set "pom:project/pom:version" %{version} ${p}
%pom_xpath_remove "pom:dependency[pom:scope = 'test']" ${p}
done

%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin
%pom_remove_plugin :maven-shade-plugin value
%pom_remove_plugin :maven-invoker-plugin value
%pom_remove_plugin :maven-invoker-plugin factory

%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-common']/pom:version" %{version} factory service value
%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-service']/pom:version" %{version} factory value
%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-value']/pom:version" %{version} factory

%mvn_package :build-only __noinstall

%build
# Unavailable test deps
%mvn_build -sf -- -f build-pom.xml

%install
%mvn_install

%files -f .mfiles-%{name}-parent
%dir %{_javadir}/%{name}
%doc README.md
%doc --no-dereference LICENSE.txt

%files common -f .mfiles-%{name}-common
%doc common/README.md
%doc --no-dereference LICENSE.txt

%files service -f .mfiles-%{name}-service
%doc service/README.md
%doc --no-dereference LICENSE.txt

%files value -f .mfiles-%{name}-value
%doc value/README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_1jpp8
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3jpp8
- new version

