Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          aalto-xml
Version:       1.0.0
Release:       alt1_4jpp8
Summary:       Ultra-high performance non-blocking XML processor (Stax/Stax2, SAX/SAX2)
# Source files without license headers https://github.com/FasterXML/aalto-xml/issues/38
# See https://github.com/FasterXML/jackson-modules-base/issues/18, from main developer:
# "To whoever it concerns: policy of the Jackson project is to only include licensing information as project
# level metadata (in repo, pom.xml, artifact within source and binary jars), and not as headers in source files.
# Licensing is Apache License 2.0, for Jackson 2.x as indicated by various artifacts, and we have no plans to change this."
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/AaltoHome
Source0:       https://github.com/FasterXML/aalto-xml/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml:oss-parent:pom:)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)

BuildArch:     noarch
Source44: import.info

%description
The Aalto XML processor is a StAX XML processor implementation. It
is not directly related to other existing mature implementations
(such as Woodstox or Sun Java Streaming XML Parser), although it
did come about as a prototype for evaluating implementation strategies
that differ from those traditionally used for Java-based parsers.

Two main goals (above and beyond stock StAX/SAX API implementation) are:

A. Ultra-high performance parsing by making the Common Case Fast
  (similar to original RISC manifesto). This may mean limiting
  functionality, but never compromising correctness. XML 1.0
  compliance is not sacrificed for speed.

A. Allowing non-block, asynchronous parsing: it should be possible to
  "feed" more input and incrementally get more XML events out, without
  forcing the current thread to block on I/O read operation.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
# Cleanup
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

sed -i 's/\r//' src/main/resources/META-INF/LICENSE
sed -i 's/\r//' release-notes/asl/*
mv release-notes/asl/ASL2.0 LICENSE
mv release-notes/asl/LICENSE NOTICE

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- new version

