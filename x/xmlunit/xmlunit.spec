# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: docbook-simple
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

Name:           xmlunit
Version:        1.3
Release:        alt2_6jpp7
Epoch:          0
Summary:        Provides classes to do asserts on xml
License:        BSD
Source0:        http://downloads.sourceforge.net/project/xmlunit/xmlunit%%20for%%20Java/XMLUnit%%20for%%20Java%%201.3/xmlunit-1.3-src.zip
Source1:        http://repo1.maven.org/maven2/xmlunit/xmlunit/1.0/xmlunit-1.0.pom
URL:            http://xmlunit.sourceforge.net/
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-junit
BuildRequires:  ant-trax
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
BuildRequires:  dblatex
BuildRequires:  docbook5-style-xsl
Requires:       junit >= 0:3.8
Requires:       xalan-j2
Requires:       xml-commons-apis
Requires:       jpackage-utils
Group:          Development/Java
BuildArch:      noarch
Source44: import.info

%description
XMLUnit extends JUnit to simplify unit testing of XML. It compares a control
XML document to a test document or the result of a transformation, validates
documents against a DTD, and (from v0.5) compares the results of XPath
expressions.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
Javadoc for %{name}

%prep
%setup -q 
# remove all binary libs and javadocs
find . -name "*.jar" -exec rm -f {} \;
rm -rf doc

cat >build.properties <<EOF
junit.lib=$(build-classpath junit)
xmlxsl.lib=$(build-classpath xalan-j2 xalan-j2-serializer xerces-j2)
test.report.dir=test
EOF

cat >docbook.properties <<EOF
db5.xsl=%{_datadir}/sgml/docbook/xsl-ns-stylesheets
EOF

#Fix wrong-file-end-of-line-encoding
sed -i 's/\r//g' README.txt LICENSE.txt
# damn the net
# TODO: why catalog does not work? it is ant xslt task
sed -i 's,http://docbook.org/xml/simple/1.1b1/sdocbook.dtd,http://www.oasis-open.org/docbook/xml/simple/1.1/sdocbook.dtd,g' `grep -rl 'http://docbook.org/xml/simple/1.1b1/sdocbook.dtd' .`


%build
export CLASSPATH=$(build-classpath xalan-j2-serializer)
ant -Dbuild.compiler=modern -Dfailonerror=false jar javadocs

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -m 0644 build/lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom


# Javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc README.txt LICENSE.txt userguide/XMLUnit-Java.pdf 
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_6jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_6jpp7
- new version

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_4jpp6
- fixed build

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp6
- build with ant17

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_6jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_6jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp1.7
- updated to new jpackage release

* Wed May 23 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_4jpp1.7
- converted from JPackage by jppimport script

* Thu Mar 23 2006 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt2
- Fix build with j2se-1.5

* Sat Apr 30 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Rebuilt for ALTLinux Sisyphus
- spec cleanup

* Thu Aug 26 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-3jpp
- Build with ant-1.6.2

* Wed Dec 17 2003 Paul Nasrat <pauln at truemesh.com> - 0:1.0-2jpp
- Fix license and improved description
- Thanks to Ralph Apel who produced a spec - merged version info

* Wed Dec 17 2003 Paul Nasrat <pauln at truemesh.com> - 0:1.0-1jpp
- Initial Version
