Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: maven-clean-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          hawtbuf
Version:       1.9
Release:       alt3_7jpp7
Summary:       A rich byte buffer library
License:       ASL 2.0
URL:           https://github.com/fusesource/hawtbuf/
Source0:       https://github.com/fusesource/hawtbuf/archive/%{name}-project-%{version}.tar.gz


BuildRequires: mvn(org.fusesource:fusesource-pom)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)

# test deps
BuildRequires: junit
BuildRequires: log4j

BuildRequires: maven-local
BuildRequires: javacc-maven-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-plugin
BuildRequires: maven-surefire-provider-junit4

# B/R for maven-archiver
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components)

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

%build
%mvn_package ":%{name}-project" %{name}
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%dir %{_javadir}/%{name}
%doc license.txt notice.md readme.md

%files proto -f .mfiles-%{name}-proto
%doc license.txt notice.md %{name}-proto/readme.md

%files protoc -f .mfiles-%{name}-protoc
%doc license.txt notice.md %{name}-protoc/readme.md

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
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

