Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: subversion
%define _without_maven 1
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 2.4.0
%define name xmlbeans
# Copyright (c) 2000-2009, JPackage Project
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%define gcj_support 0

%define source_top %{name}-%{cvs_version}

Name:           xmlbeans
Version:        2.4.0
Release:        alt1_3jpp6
Epoch:          0
Summary:        XML-Java binding tool
License:        ASL 2.0
Group:          Development/Java
URL:            http://xmlbeans.apache.org
# svn export http://svn.apache.org/repos/asf/xmlbeans/tags/2.4.0 xmlbeans-2.4.0
# tar czf xmlbeans-2.4.0-src.tgz xmlbeans-2.4.0
Source0:        xmlbeans-2.4.0-src.tgz
Source1:        http://repo1.maven.org/maven2/org/apache/xmlbeans/xmlbeans/2.4.0/xmlbeans-2.4.0.pom
Source2:        http://repo1.maven.org/maven2/org/apache/xmlbeans/xmlbeans-xpath/2.4.0/xmlbeans-xpath-2.4.0.pom
Source3:        http://repo1.maven.org/maven2/org/apache/xmlbeans/xmlbeans-xmlpublic/2.4.0/xmlbeans-xmlpublic-2.4.0.pom
Source4:        http://repo1.maven.org/maven2/org/apache/xmlbeans/xmlbeans-qname/2.4.0/xmlbeans-qname-2.4.0.pom
#FIXME, pre-built saxon9 jars, replace it with saxon9 package if saxon9 was built
#Source5:        saxon9-jars.tgz

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: ant-nodeps
#BuildRequires:  ant-contrib
BuildRequires: junit
BuildRequires: xml-commons-resolver11
BuildRequires: stax_1_0_api
BuildRequires: saxon9
BuildRequires: saxon9-dom
BuildRequires: saxon9-xpath
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: jpackage-utils >= 0:1.7.3
Requires: stax_1_0_api
Requires: saxon9
Requires: saxon9-dom
Requires: saxon9-xpath
Requires: xml-commons-resolver11
Source44: import.info

%description
XMLBeans is a tool that allows you to access the full power
of XML in a Java friendly way. It is an XML-Java binding tool.
The idea is that you can take advantage the richness and
features of XML and XML Schema and have these features mapped 
as naturally as possible to the equivalent Java language and
typing constructs. XMLBeans uses XML Schema to compile Java
interfaces and classes that you can then use to access and
modify XML instance data. Using XMLBeans is similar to using
any other Java interface/class, you will see things like
getFoo or setFoo just as you would expect when working with
Java. While a major use of XMLBeans is to access your XML
instance data with strongly typed Java classes there are also
API's that allow you access to the full XML infoset (XMLBeans
keeps full XML Infoset fidelity) as well as to allow you to
reflect into the XML schema itself through an XML Schema
Object model.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%package scripts
Summary:        Scripts for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description scripts
%{summary}.

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    jj=$(basename $j)
    m=$(expr $jj : '\(piccolo_apache_dist\).*') || :
    n=$(expr $jj : '\(jam-\).*') || :
    if [ "$m" != "piccolo_apache_dist" -a "$n" != "jam-" ]; then
       mv $j $j.no
    fi
done
mkdir -p build/lib

#tar zxf %{SOURCE5}

pushd build/lib
ln -sf $(build-classpath xml-commons-resolver) resolver.jar
ln -sf $(build-classpath stax_1_0_api) jsr173_1.0_api.jar
ln -sf $(build-classpath saxon9) saxon9.jar
ln -sf $(build-classpath saxon9/saxon9-dom) saxon9-dom.jar
ln -sf $(build-classpath saxon9/saxon9-xpath) saxon9-xpath.jar
popd

pushd external/lib
mv oldxbean.jar.no oldxbean.jar
ln -sf $(build-classpath stax_1_0_api) jsr173_1.0_api_bundle.jar
touch xcresolver.zip
popd

%build
export CLASSPATH="$(build-classpath-directory build/lib)"
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/{nodeps}`"
export XMLBEANS_EXTERNALS=/usr/share/java
export XMLBEANS_HOME=`pwd`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 default docs

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 0644 build/lib/xmlbeans-qname.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlbeans-qname-%{version}.jar
install -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-xmlbeans-qname.pom
%add_to_maven_depmap org.apache.xmlbeans xmlbeans-qname %{version} JPP/%{name} xmlbeans-qname

install -m 0644 build/lib/xmlpublic.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlpublic-%{version}.jar
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-xmlpublic.pom
%add_to_maven_depmap org.apache.xmlbeans xmlbeans-xmlpublic %{version} JPP/%{name} xmlpublic

install -m 0644 build/lib/xbean_xpath.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xbean_xpath-%{version}.jar
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-xbean_xpath.pom
%add_to_maven_depmap org.apache.xmlbeans xmlbeans-xpath %{version} JPP/%{name} xbean_xpath

install -m 0644 build/lib/xbean.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xbean-%{version}.jar
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-xbean.pom
%add_to_maven_depmap org.apache.xmlbeans xmlbeans %{version} JPP/%{name} xbean

ln -s xmlbeans-qname-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlbeans-qname.jar
ln -s xmlpublic-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlpublic.jar
ln -s xbean_xpath-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xbean_xpath.jar
ln -s xbean-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xbean.jar

# bin
install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/dumpxsb   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/inst2xsd  $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/scomp     $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/sdownload $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/sfactor   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/svalidate $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/validate  $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xpretty   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xsd2inst  $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xsdtree   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xstc      $RPM_BUILD_ROOT%{_bindir}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/reference/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf build/docs/reference

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr build/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/x*-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%files scripts
%attr(0755,root,root) %{_bindir}/*

%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_3jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt3_2jpp5
- new jpp release

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_1jpp5
- converted from JPackage by jppimport script

* Fri Jul 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_4jpp1.7
- converted from JPackage by jppimport script

