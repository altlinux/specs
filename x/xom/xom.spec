BuildRequires: dom4j
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# Copyright (c) 2000-2010, JPackage Project
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

#def_with bootstrap
%bcond_with bootstrap
#def_with gcj_support
%bcond_with gcj_support
#def_with test
%bcond_with test

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           xom
Version:        1.2.6
Release:        alt1_2jpp6
Epoch:          0
Summary:        XML Pull Parser
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.xom.nu/
Source0:        http://www.cafeconleche.org/XOM/xom-1.2.6-src.tar.gz
Source1:        http://repo1.maven.org/maven2/xom/xom/1.2.6/xom-1.2.6.pom
Patch0:         xom-1.2.6-remove-jaxen.patch
Patch1:         xom-1.1-clean-dist.patch
Patch3:         xom-1.1-remove_sun_import.patch
Patch4:         xom-1.2.6-crosslink.patch
Patch5:         xom-1.1-sinjdoc.patch
Patch6:         xom-1.2b2-javadoc-stack-size.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit
BuildRequires:  jarjar
BuildRequires:  java-javadoc
BuildRequires:  jaxen
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  junit-javadoc
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-jaxp-1.3-apis
%if %without bootstrap
BuildRequires:  tagsoup
BuildRequires:  saxon
BuildRequires:  jaxp_parser_impl
BuildRequires:  xml-commons-resolver12
BuildRequires:  servlet
%endif
%if !%{gcj_support}
BuildArch:      noarch
%else
BuildRequires:  java-gcj-compat-devel
%endif
Source44: import.info

%description
XOM is a new XML object model. It is an open source (LGPL), 
tree-based API for processing XML with Java that strives 
for correctness, simplicity, and performance, in that order. 
XOM is designed to be easy to learn and easy to use. It 
works very straight-forwardly, and has a very shallow 
learning curve. Assuming you're already familiar with XML, 
you should be able to get up and running with XOM very quickly.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %without bootstrap
%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
%{summary}.
%endif

%prep
%setup -q -n XOM
# remove all binary libs
%{_bindir}/find -type f -name "*.jar" -o -type f -name "*.class" | %{_bindir}/xargs -t %{__rm}
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch3 -p0 -b .sav3
%patch4 -p0 -b .sav4
# XXX: (dwalluck): Required only for sinjdoc
%if 0
%patch5 -p0 -b .sav5
%endif
%patch6 -p0 -b .sav6
%{__perl} -pi -e 's/\r$//g' *.html *.txt
%{__perl} -pi -e 's/compress="no"/compress="yes"/g' build.xml

pushd lib
ln -s $(build-classpath junit) junit.jar
ln -s $(build-classpath xerces-j2) xercesImpl.jar
ln -s $(build-classpath xalan-j2) xalan.jar
ln -s $(build-classpath xml-commons-jaxp-1.3-apis) xmlParserAPIs.jar
popd
mkdir lib2
%if %without bootstrap
pushd lib2
ln -s $(build-classpath tagsoup) tagsoup-1.0rc1.jar
ln -s $(build-classpath saxon) saxon.jar
ln -s $(build-classpath jaxp_parser_impl) gnujaxp.jar
ln -s $(build-classpath xml-commons-resolver12) resolver.jar
DOM4J_PRESENT=$(build-classpath dom4j 2>/dev/null || :)
if [ -n "$DOM4J_PRESENT" ]; then
ln -s $(build-classpath dom4j) dom4j-1.5.1.jar
fi
ln -s $(build-classpath servlet) servlet.jar
popd
%endif

%build
export CLASSPATH=$(build-classpath jarjar jaxen)
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
export ANT_OPTS="-Xss1m"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Dj2se.api=%{_javadocdir}/java -Djunit.api=%{_javadocdir}/junit compile15 jar javadoc
%if %without bootstrap
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first samples
%if %with test
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first test
%endif
%endif

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 build/xom-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -s ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -a build/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %without bootstrap
# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -p -m 644 build/xom-samples.jar %{buildroot}%{_datadir}/%{name}
install -p -m 644 xom.graffle %{buildroot}%{_datadir}/%{name}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc overview.html README.txt LICENSE.txt Todo.txt lgpl.txt
%if %without bootstrap
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/xom.graffle
%endif
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %without bootstrap
%files demo
%{_datadir}/%{name}/xom-samples.jar
%endif

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.6-alt1_2jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp5
- new version

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.b2.4jpp5
- jpp5 build

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_6jpp1.7
- updated to new jpackage release

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp1.7
fixes jvm 5.0 poisoning

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp1.7
- full-fledged build

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp1.7
- imported with jppimport script; note: bootstrapped version

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp1.7
- imported with jppimport script; note: bootstrapped version

