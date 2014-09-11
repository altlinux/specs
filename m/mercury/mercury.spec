Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mercury
%define version 1.0
%global namedreltag -alpha-6
%global namedversion %{version}%{?namedreltag}
Name:           mercury
Version:        1.0
Release:        alt1_0.15.alpha6jpp7
Summary:        Replacement for the Maven Artifact subsystem
License:        ASL 2.0
URL:            http://maven.apache.org/mercury/mercury-artifact/
# svn export http://svn.apache.org/repos/asf/maven/mercury/tags/mercury-1.0-alpha-6
# tar czf mercury-1.0-alpha-6.tar.gz mercury-1.0-alpha-6
Source0:        %{name}-%{namedversion}.tar.gz

Patch0:         0001-Make-it-build.patch
Patch1:         0001-Replace-plexus.lang-dependency-with-plexus.i18n.patch

BuildRequires:  classworlds
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  junit
BuildRequires:  log4j
BuildRequires:  maven-local
BuildRequires:  maven-site-plugin
BuildRequires:  maven-archiver
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-wagon
BuildRequires:  plexus-archiver
BuildRequires:  plexus-compiler
BuildRequires:  plexus-digest
BuildRequires:  plexus-i18n
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  tomcat-servlet-3.0-api
BuildRequires:  velocity

BuildArch:      noarch
Source44: import.info

%description
Maven Mercury is a replacement for the Maven Artifact subsystem, and a
complete replacement for the HTTP/HTTPS/DAV/DAVS portions of the existing
transport.

This package only contains Logging, Artifact, External Dependencies and
Event Framework. Transports, Mercury Repositories, Crypto, Metadata, Ant
Tasks, Shared Utilities, Maven resolusion comparison, Wagon provider
and Plexus Component are not provided.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
Javadoc HTML documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1 -b .build
%patch1 -p1 -b .lang

%build
find -name '*.java' -exec grep -l org.codehaus.plexus.lang '{}' \; |
        xargs perl -ni mercury-lang-i18n.pl

%mvn_file :%{name}-artifact %{name}/artifact
%mvn_file :%{name}-event %{name}/event
%mvn_file :%{name}-external %{name}/external
%mvn_file :%{name}-logging %{name}/logging

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc release.notes.txt ./src/licenses/apache.txt

%files javadoc -f .mfiles-javadoc
%doc ./src/licenses/apache.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.15.alpha6jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.12.alpha6jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.11.alpha6jpp7
- update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.4.alpha6jpp7
- new version

