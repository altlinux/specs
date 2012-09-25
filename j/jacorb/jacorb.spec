Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             jacorb
Version:          2.3.1
Release:          alt1_3.20120215gitjpp7
Summary:          The Java implementation of the OMG's CORBA standard
Group:            Development/Java
License:          LGPLv2
URL:              http://www.jacorb.org/index.html

# git clone git://github.com/sguilhen/jacorb.git
# find jacorb/ -name '*.jar' -delete
# tar cafJ jacorb-20120215git5481b0.tar.xz jacorb
Source0:          jacorb-20120215git5481b0.tar.xz
Source1:          http://central.maven.org/maven2/org/jacorb/jacorb-parent/%{version}/jacorb-parent-%{version}.pom
Source2:          http://central.maven.org/maven2/org/jacorb/jacorb/%{version}/jacorb-%{version}.pom
Source3:          http://central.maven.org/maven2/org/jacorb/jacorb-idl-compiler/%{version}/jacorb-idl-compiler-%{version}.pom

# These methods are not implemented in the current 
Patch0:           0001-Implement-a-few-methods-in-GSSUPContextSpi-to-make-i.patch

# We need to modify the build script to build an intermediate jacorb.jar and use
# java.endorsed.dirs to point to the jar to override JDK classes
Patch1:           0002-Create-jacorb.jar-to-use-it-in-java.endorsed.dirs-pa.patch

# Fix "error: unmappable character for encoding ASCII" JDK issues
Patch2:           0003-Set-encoding-to-UTF-8-when-generating-javadoc.patch

# Remove the Class-Path entry to fix class-path-in-manifest issue
Patch3:           0004-Removed-Class-Path-entry-from-MANIFEST.MF.patch

# Remove unnecessary deps from POM since we don't have notification module available
Patch4:           jacorb-%{version}-notification-dependencies-removal.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    ant
BuildRequires:    antlr-tool
BuildRequires:    avalon-logkit
BuildRequires:    slf4j

Requires:         jpackage-utils
Requires:         antlr-tool
Requires:         avalon-logkit
Requires:         slf4j
Source44: import.info

%description
This package contains the Java implementation of the OMG's CORBA standard

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jacorb

cp %{SOURCE1} jacorb-parent.pom
cp %{SOURCE2} jacorb.pom
cp %{SOURCE3} jacorb-idl-compiler.pom

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0

# No xdoclet available
sed -i 's|,notification||' src/org/jacorb/build.xml

ln -s $(build-classpath antlr) lib/antlr-2.7.2.jar
ln -s $(build-classpath slf4j/api) lib/slf4j-api-1.5.6.jar

%build

# due to javadoc x86_64 out of memory
subst 's,maxmemory="256m",maxmemory="512m",' build.xml
export CLASSPATH=$(build-classpath avalon-logkit slf4j/api)

ant all doc

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/
install -pm 644 lib/jacorb.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -pm 644 lib/idl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-idl-compiler.jar

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 jacorb-parent.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-parent.pom
install -pm 644 jacorb.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 jacorb-idl-compiler.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-idl-compiler.pom

# DEPMAP
%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "jacorb:jacorb"
%add_maven_depmap JPP-%{name}-idl-compiler.pom %{name}-idl-compiler.jar -a "jacorb:jacorb-idl-compiler"

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc doc/LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc doc/LICENSE

%changelog
* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_3.20120215gitjpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt2_20jpp6
- built with java 6

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_20jpp6
- new jpp release

* Thu May 13 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_19jpp5
- jpp6 import

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_17jpp5
- new jpp release

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_11jpp5
- new version

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2.4-alt3_3jpp1.7
- rebuild with backport-util-concurrent 3

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.4-alt2_3jpp1.7
branch 4.0 compatible build

* Mon Oct 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.4-alt1_3jpp1.7
- converted from JPackage by jppimport script

