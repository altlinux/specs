Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             jacorb
Version:          2.3.1
Release:          alt1_16jpp8
Summary:          The Java implementation of the OMG's CORBA standard
Group:            Development/Other
License:          LGPLv2
URL:              http://www.jacorb.org/index.html

Source0:          http://www.jacorb.org/releases/%{version}/jacorb-%{version}-src.zip
Source1:          http://central.maven.org/maven2/org/jacorb/jacorb-parent/%{version}/jacorb-parent-%{version}.pom
Source2:          http://central.maven.org/maven2/org/jacorb/jacorb/%{version}/jacorb-%{version}.pom
Source3:          http://central.maven.org/maven2/org/jacorb/jacorb-idl-compiler/%{version}/jacorb-idl-compiler-%{version}.pom

# These methods are not implemented in the current 
Patch0:           jacorb-2.3.1-Implement-a-few-methods-in-GSSUPContextSpi-to-make-i.patch

# Set proper versions
Patch1:           jacorb-2.3.1-version.patch

# Fix "error: unmappable character for encoding ASCII" JDK issues
Patch2:           jacorb-2.3.1-Set-encoding-to-UTF-8-when-generating-javadoc.patch

# Remove the Class-Path entry to fix class-path-in-manifest issue
Patch3:           jacorb-2.3.1-Removed-Class-Path-entry-from-MANIFEST.MF.patch

# This patch resets the port of the primary address to zero when an
# IORInterceptor adds a TAG_CSI_SEC_MECH_LIST component with transport
# protection requirements (SSL), as it should be per the CSI v2 specification.
Patch4:           jacorb-2.3.1-primaddress_port.patch

# read_boolean() now only adjusts positions if the chunk_end_pos == pos,
# no longer calling handle_chunking(). The problem with handle_chunking()
# is that it aligns the current position and this can cause CDRInputStream
# to "skip" valid boolean values, as those are not padded.
Patch5:           jacorb-2.3.1-read_boolean.patch

# Support for JDK 8
Patch6:           JDK8-support.patch

BuildArch:        noarch

BuildRequires:    javapackages-local
BuildRequires:    ant
BuildRequires:    antlr-tool
BuildRequires:    avalon-logkit
BuildRequires:    bsh
BuildRequires:    slf4j
Source44: import.info

%description
This package contains the Java implementation of the OMG's CORBA standard

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jacorb-%{version}

cp %{SOURCE1} jacorb-parent.pom
cp %{SOURCE2} jacorb.pom
cp %{SOURCE3} jacorb-idl-compiler.pom

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.zip' -exec rm -f '{}' \;

%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p1

# No xdoclet available
sed -i 's|,notification||' src/org/jacorb/build.xml

ln -s $(build-classpath antlr) lib/antlr-2.7.2.jar
ln -s $(build-classpath slf4j/api) lib/slf4j-api-1.5.6.jar

%mvn_alias "org.jacorb:" "jacorb:"

%build

# due to javadoc x86_64 out of memory
subst 's,maxmemory="256m",maxmemory="512m",' build.xml
export CLASSPATH=$(build-classpath avalon-logkit slf4j/api)

sed -i "s|>avalon<|>avalon-logkit<|g" jacorb-idl-compiler.pom

%pom_remove_dep "tanukisoft:wrapper" jacorb.pom
%pom_remove_dep "picocontainer:picocontainer" jacorb.pom
%pom_remove_dep "nanocontainer:nanocontainer" jacorb.pom
%pom_remove_dep "nanocontainer:nanocontainer-remoting" jacorb.pom

ant all doc

%install
%mvn_artifact jacorb-parent.pom
%mvn_artifact jacorb.pom lib/jacorb.jar
%mvn_artifact jacorb-idl-compiler.pom lib/idl.jar

%mvn_install -J doc/api

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc doc/LICENSE

%files javadoc -f .mfiles-javadoc
%doc doc/LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_16jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_15jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_9jpp7
- new release

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_5jpp7
- new release

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

