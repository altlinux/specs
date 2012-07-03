BuildRequires: /proc
BuildRequires: jpackage-compat
%global hgcheckout 20110130hg

Name:    mchange-commons
Version: 0.2
Release: alt1_0.5.20110130hgjpp7
Summary: A collection of general purpose utilities for c3p0
License: LGPLv2
URL:     http://sourceforge.net/projects/c3p0
Group:   Development/Java

BuildRequires: java-javadoc 
BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: junit
BuildRequires: ant-junit
BuildRequires: log4j

Requires: jpackage-utils

# This software is unreleased so generate tarball from upstream source control:
# $  hg clone http://c3p0.hg.sourceforge.net:8000/hgroot/c3p0/mchange-commons && tar -czf mchange-commons-20110130hg.tar.gz mchange-commons
Source0: %{name}-%{hgcheckout}.tar.gz

# Patch the build to include javadocs
Patch0: mchange-commons-javadoc.patch

# Patch to build with JDBC 4.1/Java 7
Patch1: mchange-commons-jdbc-4.1.patch

# Remove one of the tests that intermittently fails
Patch2: mchange-commons-remove-weakness-test.patch

BuildArch: noarch
Source44: import.info

%description
Originally part of c3p0, mchange-commons is a set of general purpose 
utilities.

%package javadoc
Summary:       API documentation for %{name}
Group:         Development/Java
Requires:      jpackage-utils
Requires:      java-javadoc
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}

%patch0 -p0 -b .orig
%patch1 -p0 -b .jdbc41
%patch2 -p0 -b .testweakness

# remove all binary bits
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dbuild.sysclasspath=first \
  -Djunit.jar.file=`build-classpath junit` \
  -Dlog4j.jar.file=`build-classpath log4j`
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 javadoc

%install
# jar
install -pD -T build/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_0.5.20110130hgjpp7
- fc version

