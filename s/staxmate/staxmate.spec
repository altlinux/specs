Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          staxmate
Version:       2.3.0
Release:       alt1_5jpp8
Summary:       Light-weight Java framework for streaming XML processing
License:       BSD
URL:           https://github.com/FasterXML/StaxMate
Source0:       https://github.com/FasterXML/StaxMate/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(javax.xml.stream:stax-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)
BuildRequires: mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
StaxMate is a light-weight framework that
adds convenience to streaming XML-processing
without significant additional overhead. It
builds on top of a Stax (JSR-173) compliant
XML processors such as Woodstox or Sjsxp
(default Stax implementation of JDK 1.6) and
offers two basic abstractions: Cursors, which
build on XMLStreamReaders and Output objects,
which build on XMLStreamWriters.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n StaxMate-%{name}-%{version}
find . -name '*.jar' -delete
find . -name '*.class' -delete

# Unwanted
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :cobertura-maven-plugin

# these tests fails
#rm src/test/java/org/codehaus/staxmate/dom/TestDOMConverter.java \
# src/test/java/org/codehaus/staxmate/out/TestBinary.java

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3jpp8
- java8 mass update

