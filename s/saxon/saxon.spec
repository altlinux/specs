Epoch: 0
Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name saxon
%define version 9.4.0.9
# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
%global version_str %(sed -e 's/\\./-/g' <<<"%{version}")
%global version_major_minor %(sed -e 's/\\([0-9]*\\.[0-9]*\\)\\..*/\\1/g' <<<"%{version}")
%global version_major_minor_str %(sed -e 's/\\./-/g' <<<"%{version_major_minor}")
%global version_maven %(sed -e 's/\\(.*\\)\\.\\([0-9]*\\)/\\1-\\2/g' <<<"%{version}")
%global artifact_id Saxon-HE
Summary:        Java XPath, XSLT 2.0 and XQuery implementation
Name:           saxon
Version:        9.4.0.9
Release:        alt1_2jpp8
# net.sf.saxon.om.XMLChar is from ASL-licensed Xerces
# net/sf/saxon/option/jdom/ is MPLv1.1
# net/sf/saxon/serialize/codenorm/ is UCD
# net/sf/saxon/expr/sort/GenericSorter.java is MIT
# net/sf/saxon/expr/Tokenizer.java and few other bits are BSD
License:        MPLv1.0 and MPLv1.1 and ASL 1.1 and UCD and MIT
URL:            http://saxon.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/saxon/Saxon-HE/%{version_major_minor}/saxon%{version_str}source.zip
Source1:        %{name}.saxon.script
Source2:        %{name}.saxonq.script
Source3:        %{name}.build.script
Source4:        %{name}.1
Source5:        %{name}q.1
Source6:        https://downloads.sourceforge.net/project/saxon/Saxon-HE/%{version_major_minor}/saxon-resources%{version_major_minor_str}.zip
Source8:        http://www.mozilla.org/MPL/1.0/index.txt#/mpl-1.0.txt
Source9:        http://www.mozilla.org/MPL/1.0/index.txt#/mpl-1.1.txt
BuildRequires:  unzip
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  ant
BuildRequires:  javapackages-local
BuildRequires:  bea-stax-api
BuildRequires:  xml-commons-apis
BuildRequires:  xml-commons-resolver
BuildRequires:  xom
BuildRequires:  java-javadoc
BuildRequires:  jdom >= 0:1.0
BuildRequires:  jdom-javadoc >= 0:1.0
BuildRequires:  jdom2
BuildRequires:  dom4j
Requires:       bea-stax-api
Requires:       bea-stax
Requires: chkconfig update-alternatives
Provides:       jaxp_transform_impl = %{version}-%{release}

# Older versions were split into multile packages
Obsoletes:  %{name}-xpath < %{version}-%{release}
Provides:   %{name}-xpath = %{version}-%{release}
Obsoletes:  %{name}-xom < %{version}-%{release}
Provides:   %{name}-xom = %{version}-%{release}
Obsoletes:  %{name}-sql < %{version}-%{release}
Provides:   %{name}-sql = %{version}-%{release}
Obsoletes:  %{name}-jdom < %{version}-%{release}
Provides:   %{name}-jdom = %{version}-%{release}
Obsoletes:  %{name}-dom < %{version}-%{release}
Provides:   %{name}-dom = %{version}-%{release}

BuildArch:      noarch
Source44: import.info

%description
Saxon HE is Saxonica's non-schema-aware implementation of the XPath 2.0,
XSLT 2.0, and XQuery 1.0 specifications aligned with the W3C Candidate
Recommendation published on 3 November 2005. It is a complete and
conformant implementation, providing all the mandatory features of
those specifications and nearly all the optional features.

%package        manual
Group: Text tools
Summary:        Manual for %{name}
BuildArch: noarch

%description    manual
Manual for %{name}.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%package        demo
Group: Text tools
Summary:        Demos for %{name}
Requires:       %{name} = %{version}

%description    demo
Demonstrations and samples for %{name}.

%package        scripts
Group: Text tools
Summary:        Utility scripts for %{name}
Requires:       %{name} = %{version}

%description    scripts
Utility scripts for %{name}.


%prep
%setup -q -c

unzip -q %{SOURCE6}
cp -p %{SOURCE3} ./build.xml

# deadNET
rm -rf net/sf/saxon/dotnet samples/cs

# Depends on XQJ (javax.xml.xquery)
rm -rf net/sf/saxon/xqj

# This requires a EE edition feature (com.saxonica.xsltextn)
rm -rf net/sf/saxon/option/sql/SQLElementFactory.java

# cleanup unnecessary stuff we'll build ourselves
rm -rf docs/api
find . \( -name "*.jar" -name "*.pyc" \) -delete

cp %{SOURCE8} %{SOURCE9} .

cat >%{artifact_id}-%{version_maven}.pom <<POM_XML
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">

  <modelVersion>4.0.0</modelVersion>
  <groupId>net.sf.saxon</groupId>
  <artifactId>%{artifact_id}</artifactId>
  <version>%{version_maven}</version>
  <packaging>jar</packaging>
  <name>%{artifact_id}</name>
  <url>http://saxon.sf.net/</url>
  <description>The XSLT and XQuery Processor</description>
  <licenses>
    <license>
      <name>Mozilla Public License Version 2.0</name>
      <url>http://www.mozilla.org/MPL/2.0/</url>
      <distribution>repo</distribution>
    </license>
  </licenses>

  <scm>
    <connection>scm:svn:https://dev.saxonica.com/repos/archive/opensource/latest%{version_major_minor}/</connection>
    <developerConnection>scm:svn:https://dev.saxonica.com/repos/archive/opensource/latest%{version_major_minor}/</developerConnection>
    <url>https://saxon.svn.sourceforge.net/svnroot/saxon/latest%{version_major_minor}/</url>
  </scm>
</project> 
POM_XML

%build
mkdir -p build/classes
cat >build/classes/edition.properties <<EOF
config=net.sf.saxon.Configuration
platform=net.sf.saxon.java.JavaPlatform
EOF

export CLASSPATH=%(build-classpath axiom xml-commons-apis xml-commons-resolver jdom jdom2 xom bea-stax-api dom4j)
ant \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Djdom.javadoc=%{_javadocdir}/jdom

%mvn_artifact %{artifact_id}-%{version_maven}.pom build/lib/saxon.jar
%mvn_alias : :saxon
%mvn_alias : net.sf.saxon:saxon::dom:

%install
%mvn_install

# For compactability
ln -s %{artifact_id}.jar $RPM_BUILD_ROOT/%{_javadir}/saxon/saxon.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}

# scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}q
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -p -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}q.1

# jaxp_transform_impl ghost symlink
ln -s %{_sysconfdir}/alternatives \
  $RPM_BUILD_ROOT%{_javadir}/jaxp_transform_impl.jar
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_transform_impl_saxon<<EOF
%{_javadir}/jaxp_transform_impl.jar	%{_javadir}/saxon/%{artifact_id}.jar	25
EOF
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

%files -f .mfiles
%_altdir/jaxp_transform_impl_saxon
%doc mpl-1.0.txt mpl-1.1.txt
%{_javadir}/%{name}/saxon.jar

%files manual
%doc doc/*

%files javadoc
%doc mpl-1.0.txt mpl-1.1.txt
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%files scripts
%{_bindir}/%{name}
%{_bindir}/%{name}q
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}q.1*

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.4.0.9-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt3_16jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt2_16jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt2_8jpp7
- new release

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt1_5jpp7
- new version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt2_3jpp6
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt1_1jpp5
- converted from JPackage by jppimport script

* Thu Jul 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:6.5.3-alt2_5jpp1.7
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:6.5.3-alt1_5jpp1.7
- converted from JPackage by jppimport script

