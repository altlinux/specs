Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          hawtbuf
Version:       1.11
Release:       alt1_4jpp8
Summary:       A rich byte buffer library
License:       ASL 2.0
URL:           https://github.com/fusesource/hawtbuf/
Source0:       https://github.com/fusesource/hawtbuf/archive/%{name}-project-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.fusesource:fusesource-pom:pom:)

BuildArch:     noarch
Source44: import.info

%description
This library implements a simple interface with working with
byte arrays. It is a shame that the Java SDK did not come with
a built in class that was just simply a byte[], int offset,
int length class which provided a rich interface similar to
what the String class does for char arrays. This library
fills in that void by providing a Buffer class which does provide
that rich interface.

%package proto
Group: Development/Java
Summary:       A protobuf library

%description proto
HawtBuf Proto: A protobuf library.

%package protoc
Group: Development/Java
Summary:       A protobuf compiler as a maven plugin

%description protoc
HawtBuf Protoc: A protobuf compiler as a maven plugin.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-project-%{version}

%pom_remove_plugin :maven-assembly-plugin

%pom_xpath_set "pom:properties/pom:log4j-version" 1.2.17
%pom_xpath_remove pom:Private-Package

%mvn_package ":%{name}-project" %{name}

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc readme.md
%doc license.txt notice.md

%files proto -f .mfiles-%{name}-proto
%doc %{name}-proto/readme.md
%doc license.txt notice.md

%files protoc -f .mfiles-%{name}-protoc
%doc %{name}-protoc/readme.md
%doc license.txt notice.md

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_4jpp8
- java8 mass update

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.11-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3_5jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3_2jpp7
- fixed build

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt2_2jpp7
- fixed maven1 dependency

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_2jpp7
- initial build

