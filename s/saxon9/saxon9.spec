Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

%bcond_without xom

%define resolverdir %{_sysconfdir}/java/resolver
%define stdname saxon9
%define gcj_support 0

Name:           saxon9
Version:        B.9.0.0.8
Release:        alt1_2jpp6
Epoch:          0
Summary:        Java  Basic XPath 2.0, XSLT 2.0, and XQuery 1.0 implementation
License:        MPL
Group:          Development/Java
URL:            http://saxon.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/saxon/Saxon-B/9.0.0.8/saxonb9-0-0-8source.zip
Source1:        %{name}.saxon.script
Source2:        %{name}.saxonq.script
Source3:        %{name}.build.script
#FIXME: not saxon9 man page
#Source4:        saxon8.1
#Source5:        saxon8q.1

#poms are updated based on 8.7 http://mirrors.ibiblio.org/pub/mirrors/maven/net.sf.saxon/poms/
Source6:        saxon-9.0.pom
Source7:        saxon-dom-9.0.pom
Source8:        saxon-jdom-9.0.pom
Source9:        saxon-sql-9.0.pom
Source10:       saxon-xom-9.0.pom
Source11:       saxon-xpath-9.0.pom

#meatinfo from saxon 8.7
Source12:       saxon9-metainf.tar.gz
Source13:       saxonb9-0-0-8j-doc.zip
Source14:       saxon-ant-9.0.pom
Source15:       saxon-dom4j-9.0.pom
Source16:       saxon-xqj-9.0.pom

Patch0:         configuration-no-dotnet.patch
Requires: bea-stax-api
Requires: bea-stax
Requires: jaxp_parser_impl
Requires(post): alternatives >= 0:0.4
Requires(preun): alternatives >= 0:0.4
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Provides:       jaxp_transform_impl
BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: bea-stax-api
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: dom4j
%if %with xom
BuildRequires: xom
%endif
BuildRequires: jdom >= 0:1.0-0.b7
BuildRequires: java-javadoc
BuildRequires: jdom-javadoc >= 0:1.0-0.b9.3jpp
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
Release 8.6 represents an important milestone in Saxonica's 
progressive implementation of the XPath 2.0, XSLT 2.0, and 
XQuery 1.0 specifications. Saxon 8.6 is aligned with the W3C 
Candidate Recommendation published on 3 November 2005. It is 
a complete and conformant implementation, providing all the 
mandatory features of those specifications and nearly all the 
optional features. 
Saxon is available in two versions. Saxon-B is a non-schema-aware 
processor, and is available as an open-source product, free of 
charge, from SourceForge. It is designed to conform to the basic 
conformance level of XSLT 2.0, and the equivalent level of 
functionality in XQuery 1.0. Saxon-SA is the schema-aware version 
of the package, and is available as a commercially supported 
product from Saxonica Limited. 

This package provides the Basic XSLT 2.0 and XQuery 1.0 processor.
Includes the command line interfaces and the JAVA APIs; also
includes a standalone XPath API that doesn't depend on JAXP 1.3. 

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Manual for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package sql
Summary:        SQL support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description sql
Supports XSLT extensions for accessing and updating a 
relational database from within a stylesheet. 

%package jdom
Summary:        JDOM support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jdom >= 0:1.0-0.b7

%description jdom
Provides additional classes enabling Saxon to be used with 
JDOM trees. Supports using a JDOM document as the input or 
output of transformations and queries. Requires jdom.jar on 
the classpath. 

%package dom
Summary:        DOM support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
#Requires:      jdom >= 0:1.0-0.b7

%description dom
Provides additional classes enabling Saxon to be used with 
the DOM Document Object Model. Supports using a DOM as the 
input or output of transformations and queries, and calling 
extension functions that use DOM interfaces to access a 
Saxon tree structure. Requires DOM level 3 (dom.jar, part 
of JAXP 1.3) to be on the classpath, if not running under 
JDK 1.5. 

%if %with xom
%package xom
Summary:        XOM support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: xom

%description xom
Provides additional classes enabling Saxon to be used with 
XOM trees. Supports using a XOM document as the input or 
output of transformations and queries. Requires xom.jar on 
the classpath. 
%endif

%package xpath
Summary:        XPATH support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description xpath
Provides support for the JAXP 1.3 XPath API. Requires the 
JAXP 1.3 version of jaxp-api.jar on the classpath, if not 
running under JDK 1.5. 

%package scripts
Summary:        Utility scripts for %{name}
Group:          Development/Java
Requires: jpackage-utils >= 0:1.5
Requires: %{name} = %{epoch}:%{version}-%{release}

%description scripts
Utility scripts for %{name}.

# saxon9 new sub-packages
%package ant
Summary:        Ant support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: ant

%description ant
%{summary}

%package dom4j
Summary:        DOM4J support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: dom4j

%description dom4j
%{summary}

%package xqj
Summary:        XQUERY support for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: dom4j

%description xqj
%{summary}


%prep
#fail to run unzip by %setup
###/usr/bin/unzip -qq /builddir/build/SOURCES/saxonb9-0-0-8source.zip
###replace net/sf/saxon/dotnet/DocumentWrapper.java? [y]es, [n]o, [A]ll, [N]one, [r]ename:  NULL
#%setup -q -u -c
cd %_builddir
rm -rf saxon9-B.9.0.0.8
/bin/mkdir -p saxon9-B.9.0.0.8
cd saxon9-B.9.0.0.8
unzip -qq -u %{SOURCE0} -d src
(cd src
tar zxf %{SOURCE12}
)
(cd ..
unzip -qq -u %{SOURCE13}
)

%patch0 -b .sav

(cd src
# Clean up .NET classes
%{__rm} -rf net/sf/saxon/dotnet/
# needs saxonica classes 
%{__rm} -rf net/sf/saxon/s9api/
)

#%{__mkdir_p} src
#(cd src
#%{__unzip} -qq ../source.zip

# Clean up .NET classes
#%{__rm} -r net/sf/saxon/dotnet/)

%{__cp} -p %{SOURCE3} ./build.xml
# cleanup unnecessary stuff we'll build ourselves
#%{_bindir}/find . -name '*.exe' -o -name  '*.jar' | %{_bindir}/xargs -t %{__rm}

%build
cd saxon9-B.9.0.0.8
export CLASSPATH=$(build-classpath xml-commons-apis jdom bea-stax-api)
%if %with xom
export  CLASSPATH=$CLASSPATH:$(build-classpath xom)
%endif
export  CLASSPATH=$CLASSPATH:$(build-classpath dom4j)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Djdom.javadoc=%{_javadocdir}/jdom

%install
cd saxon9-B.9.0.0.8
# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/lib/%{stdname}.jar %{buildroot}%{_javadir}/%{stdname}-%{version}.jar
%{__cp} -p build/lib/%{stdname}-xpath.jar %{buildroot}%{_javadir}/%{stdname}-xpath-%{version}.jar
%if %with xom
%{__cp} -p build/lib/%{stdname}-xom.jar %{buildroot}%{_javadir}/%{stdname}-xom-%{version}.jar
%endif
%{__cp} -p build/lib/%{stdname}-sql.jar %{buildroot}%{_javadir}/%{stdname}-sql-%{version}.jar
%{__cp} -p build/lib/%{stdname}-jdom.jar %{buildroot}%{_javadir}/%{stdname}-jdom-%{version}.jar
%{__cp} -p build/lib/%{stdname}-dom.jar %{buildroot}%{_javadir}/%{stdname}-dom-%{version}.jar

# saxon9 new jars
%{__cp} -p build/lib/%{stdname}-ant.jar %{buildroot}%{_javadir}/%{stdname}-ant-%{version}.jar
%{__cp} -p build/lib/%{stdname}-dom4j.jar %{buildroot}%{_javadir}/%{stdname}-dom4j-%{version}.jar
%{__cp} -p build/lib/%{stdname}-xqj.jar %{buildroot}%{_javadir}/%{stdname}-xqj-%{version}.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s}f ${jar} `/bin/echo $jar | %{__sed} "s|-%{version}||g"`; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# scripts
%{__mkdir_p} %{buildroot}%{_bindir}
%{__sed} 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE1} \
  > %{buildroot}%{_bindir}/%{stdname}
%{__sed} 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE2} \
  > %{buildroot}%{_bindir}/%{stdname}q
%{__mkdir_p} %{buildroot}%{_mandir}/man1
#%{__sed} 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE4} \
#  > %{buildroot}%{_mandir}/man1/%{stdname}.1
#%{__sed} 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE5} \
#  > %{buildroot}%{_mandir}/man1/%{stdname}q.1

# jaxp_transform_impl ghost symlink
%{__ln_s} %{_sysconfdir}/alternatives \
  %{buildroot}%{_javadir}/jaxp_transform_impl.jar
# jaxp_parser_impl ghost symlink
#%{__ln_s} %{_sysconfdir}/alternatives \
#  %{buildroot}%{_javadir}/jaxp_parser_impl.jar

# maven
%add_to_maven_depmap net.sf.saxon saxon %{version} JPP %{stdname}
%{__install} -D -p -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/maven2/poms/JPP-%{stdname}.pom
%add_to_maven_depmap net.sf.saxon saxon-dom %{version} JPP %{stdname}-dom
%{__install} -D -p -m 0644 %{SOURCE7} %{buildroot}%{_datadir}/maven2/poms/JPP-%{stdname}-dom.pom
%add_to_maven_depmap net.sf.saxon saxon-jdom %{version} JPP %{stdname}-jdom
%{__install} -D -p -m 0644 %{SOURCE8} %{buildroot}%{_datadir}/maven2/poms/JPP-%{stdname}-jdom.pom
%add_to_maven_depmap net.sf.saxon saxon-sql %{version} JPP %{stdname}-sql
%{__install} -D -p -m 0644 %{SOURCE9} %{buildroot}%{_datadir}/maven2/poms/JPP-%{stdname}-sql.pom
%if %with xom
%add_to_maven_depmap net.sf.saxon saxon-xom %{version} JPP %{stdname}-xom
%{__install} -D -p -m 0644 %{SOURCE10} %{buildroot}%{_datadir}/maven2/poms/JPP-%{stdname}-xom.pom
%endif
%add_to_maven_depmap net.sf.saxon saxon-xpath %{version} JPP %{stdname}-xpath
%{__install} -D -p -m 0644 %{SOURCE11} %{buildroot}%{_datadir}/maven2/poms/JPP-%{stdname}-xpath.pom

%add_to_maven_depmap net.sf.saxon saxon-ant %{version} JPP %{stdname}-ant
%{__install} -D -p -m 0644 %{SOURCE14} %{buildroot}%{_datadir}/maven2/poms/JPP-%{stdname}-ant.pom
%add_to_maven_depmap net.sf.saxon saxon-dom4j %{version} JPP %{stdname}-dom4j
%{__install} -D -p -m 0644 %{SOURCE15} %{buildroot}%{_datadir}/maven2/poms/JPP-%{stdname}-dom4j.pom
%add_to_maven_depmap net.sf.saxon saxon-xqj %{version} JPP %{stdname}-xqj
%{__install} -D -p -m 0644 %{SOURCE16} %{buildroot}%{_datadir}/maven2/poms/JPP-%{stdname}-xqj.pom

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_transform_impl_%{name}<<EOF
%{_javadir}/jaxp_transform_impl.jar	%{_javadir}/%{stdname}.jar	25
EOF
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

%files
%_altdir/jaxp_transform_impl_%{name}
%{_javadir}/%{stdname}.jar
%{_javadir}/%{stdname}-%{version}.jar
%{_datadir}/maven2/poms/JPP-%{stdname}.pom
%{_mavendepmapfragdir}/%{name}
%exclude %{_javadir}/jaxp_transform_impl.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%dir %{_libdir}/gcj/%{name}/java*
%{_libdir}/gcj/%{name}/%{stdname}-%{version}*
%endif

%files xpath
%{_javadir}/%{stdname}-xpath*
%{_datadir}/maven2/poms/JPP-%{stdname}-xpath.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{stdname}-xpath*
%endif

%if %with xom
%files xom
%{_javadir}/%{stdname}-xom*
%{_datadir}/maven2/poms/JPP-%{stdname}-xom.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{stdname}-xom*
%endif
%endif

%files sql
%{_javadir}/%{stdname}-sql*
%{_datadir}/maven2/poms/JPP-%{stdname}-sql.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{stdname}-sql*
%endif

%files jdom
%{_javadir}/%{stdname}-jdom*
%{_datadir}/maven2/poms/JPP-%{stdname}-jdom.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{stdname}-jdom*
%endif

%files dom
%{_javadir}/%{stdname}-dom*
%{_datadir}/maven2/poms/JPP-%{stdname}-dom.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{stdname}-dom*
%endif

%files ant
%{_javadir}/%{stdname}-ant*
%{_datadir}/maven2/poms/JPP-%{stdname}-ant.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{stdname}-ant*
%endif

%files dom4j
%{_javadir}/%{stdname}-dom4j*
%{_datadir}/maven2/poms/JPP-%{stdname}-dom4j.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{stdname}-dom4j*
%endif

%files xqj
%{_javadir}/%{stdname}-xqj*
%{_datadir}/maven2/poms/JPP-%{stdname}-xqj.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{stdname}-xqj*
%endif

%files manual
%doc doc/
%doc notices/

%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}

%files scripts
#%defattr(0755,root,root,0755)
%{_bindir}/%{stdname}
%{_bindir}/%{stdname}q
#%attr(0644,root,root) %{_mandir}/man1/%{stdname}.1*
#%attr(0644,root,root) %{_mandir}/man1/%{stdname}q.1*

%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:B.9.0.0.8-alt1_2jpp6
- new version

