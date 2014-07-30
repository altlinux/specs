# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: oro plexus-resources
BuildRequires: /proc
BuildRequires: jpackage-compat
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
Name:           pmd
Version:        4.2.5
Release:        alt5_15jpp7
Epoch:          0
Summary:        Scans Java source code and looks for potential problems
License:        BSD

Source0:        http://downloads.sourceforge.net/pmd/pmd-src-%{version}.zip
# This patch has not been sent upstream.  It causes the build to use installed
# jars for dependencies rather than use those distributed with the source.  It
# also kills retroweaver dead, dead, dead so it won't interfere with the build.
Patch0:         pmd-4.2.5-build.patch
# This patch was sent upstream on 11 Feb 2009.  It fixes a null pointer
# exception when using the nicerhtml output format.
Patch1:         pmd-4.2.4-nicerhtml.patch
# This patch has not been sent upstream.  It updates an ant dep in a pom file
# to use the latest groupId for ant.
Patch2:         pmd-4.2.5-antdep.patch
URL:            http://pmd.sourceforge.net/

BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  jaxen >= 0:1.1.1
BuildRequires:  objectweb-asm >= 0:3.1
BuildRequires:  objectweb-asm-javadoc >= 0:3.1
BuildRequires:  xml-commons-apis >= 1.3.02
Requires:       jpackage-utils >= 0:1.6
Requires:       jaxen >= 0:1.1.1
Requires:       objectweb-asm >= 0:3.1
Requires:       xerces-j2
Requires:       xml-commons-apis >= 1.3.02
Group:          Development/Java
BuildArch:      noarch

Provides:       %{name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-manual < 0:4.0.0-1
Source44: import.info

%description
PMD scans Java source code and looks for potential problems like:
* Possible bugs: empty try/catch/finally/switch statements
+ Dead code: unused local variables, parameters and private methods
+ Suboptimal code: wasteful String/StringBuffer usage
+ Overcomplicated expressions: unnecessary if statements, for loops
  that could be while loops
+ Duplicate code: copied/pasted code means copied/pasted bugs

PMD has plugins for JDeveloper, Eclipse, JEdit, JBuilder, BlueJ,
CodeGuide, NetBeans/Sun Java Studio Enterprise/Creator, IntelliJ IDEA,
TextPad, Maven, Ant, Gel, JCreator, and Emacs.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       objectweb-asm-javadoc
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1
%patch2

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

# remove an unneeded script in an otherwise documentation directory
rm -f etc/fr_docs/copy_up.sh

%build
ant
ant -f bin/build.xml -Ddir.lib=%{_javadir} javadoc

%install
# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 lib/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}
cp -p etc/pmd-nicerhtml.xsl $RPM_BUILD_ROOT%{_sysconfdir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr etc/xslt $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/rulesets
cp -pr rulesets/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/rulesets

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt etc/changelog.txt etc/fr_docs etc/readme.txt
%doc etc/pmdProperties.rtf
%{_javadir}/*.jar
%{_datadir}/%{name}-%{version}
%config(noreplace) %{_sysconfdir}/pmd-nicerhtml.xsl
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/*

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt5_15jpp7
- new release

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt5_14jpp7
- merged junit-junit4

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt4_14jpp7
- fixed build with new junit

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt3_14jpp7
- fc update

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt3_2jpp6
- dropped velocity14

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt2_2jpp6
- fixed build with java 7

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt1_2jpp6
- new jpp release

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt1_1jpp5
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.2.4-alt1_2jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.9-alt1_2jpp5
- converted from JPackage by jppimport script

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_1jpp1.7
- converted from JPackage by jppimport script

