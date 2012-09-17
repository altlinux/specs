BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           mercury
Version:        1.0
Release:        alt1_0.4.alpha6jpp7
Summary:        Replacement for the Maven Artifact subsystem

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/mercury/mercury-artifact/
# svn export http://svn.apache.org/repos/asf/maven/mercury/tags/mercury-1.0-alpha-6
# tar czf mercury-1.0-alpha-6.tar.gz mercury-1.0-alpha-6
Source0:        mercury-%{version}-alpha-6.tar.gz
Patch0:         0001-Make-it-build.patch
Patch1:         0001-Replace-plexus.lang-dependency-with-plexus.i18n.patch

BuildRequires:  classworlds
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  jpackage-utils
BuildRequires:  junit4
BuildRequires:  log4j
BuildRequires:  maven
BuildRequires:  maven2-common-poms
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-shared
BuildRequires:  maven-archiver
BuildRequires:  maven-surefire
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-wagon
BuildRequires:  plexus-archiver
BuildRequires:  plexus-compiler
BuildRequires:  plexus-container-default
BuildRequires:  plexus-digest
BuildRequires:  plexus-i18n
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  servlet_2_4_api
BuildRequires:  velocity

Requires:       jpackage-utils
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
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc HTML documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}-alpha-6
%patch0 -p1 -b .build
%patch1 -p1 -b .lang


%build
find -name '*.java' -exec grep -l org.codehaus.plexus.lang '{}' \; |
        xargs perl -ni mercury-lang-i18n.pl

mvn-rpmbuild install javadoc:aggregate \
        -Dmaven.test.skip=true \


%install
install -d $RPM_BUILD_ROOT%{_javadir}/mercury
for S in logging artifact external event
do
        # Code
        install -p -m644 mercury-$S/target/mercury-$S-%{version}-alpha-6.jar \
                $RPM_BUILD_ROOT%{_javadir}/mercury/$S.jar
done
# Javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/mercury
cp -a target/site/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/mercury

%files
%{_javadir}/mercury
%doc release.notes.txt ./src/licenses/apache.txt

%files javadoc
%{_javadocdir}/mercury


%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.4.alpha6jpp7
- new version

