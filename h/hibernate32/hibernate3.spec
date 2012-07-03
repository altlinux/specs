%define oldname hibernate3
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: docbook-xml docbook-dtds
BuildRequires: /proc
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

%bcond_with bootstrap
%bcond_with jdk6
%bcond_without manual
%if %with jdk6
BuildRequires: jpackage-compat
# but classes will be java6 :(
%else
BuildRequires: jpackage-1.5.0-compat
%endif

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/hibernate/3.2.4.SP1_CP01-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define base_version 3.2
%define hname Hibernate3

%define reltag  SP1_CP01

Name:           hibernate32
Version:        3.2.4
Release:        alt5_1.SP1_CP01.9jpp5
Epoch:          0
Summary:        Relational persistence and query service
License:        LGPLv2+
URL:            http://www.hibernate.org/
Group:          Databases
# svn export https://svn.jboss.org/repos/hibernate/tags/JBOSS_EAP_3_2_4_SP1_CP01
# Exported revision 11676.
# tar czf hibernate-3.2.4.sp1_cp01-src.tar.gz Hibernate3
Source0:        hibernate-3.2.4.sp1_cp01-src.tar.gz
Source1:	hibernate3-component-info.xml
Patch0:		hibernate-3.2-EhCache.patch
Patch1:		hibernate3-javadoc.patch
Patch2:		hibernate3-build.patch
Patch3:		hibernate3-branch_3_2_jdbc4.patch
Patch4:		hibernate3-build-1.6.patch
Patch5:         hibernate3-xmlgraphics-fop.patch
Patch6:         hibernate3-doc.patch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-antlr
BuildRequires: ant-junit
BuildRequires: ant-swing
BuildRequires: junit >= 0:3.8.1
BuildRequires: checkstyle
#BuildRequires: cleanimports
#BuildRequires: versioncheck >= 0:1.0
#BuildRequires: syndiag2 >= 0:2.0
BuildRequires: javassist >= 0:3.4
BuildRequires: cglib21 >= 0:2.1.3
BuildRequires: asm
BuildRequires: jakarta-commons-collections >= 0:2.1.1
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: antlr >= 0:2.7.6
## xml/xstl handling
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: jaxen >= 0:1.1
BuildRequires: xerces-j2 >= 0:2.6.2
BuildRequires: xml-commons-apis
## j2ee related
BuildRequires: jdbc-stdext
BuildRequires: jta
BuildRequires: log4j >= 0:1.2.11
# JCA no longer supported
#BuildRequires:  j2ee-connector
#BuildRequires:  jaas
## Treecache
BuildRequires: jboss-cache >= 0:1.2.2
BuildRequires: concurrent >= 0:1.3.2
BuildRequires: jboss-common
# FIXME Some circular dependencies here...
%if %with bootstrap
BuildRequires: jboss4-jmx >= 0:4.0.2
BuildRequires: jboss4-system >= 0:4.0.2
%endif
## Replication
BuildRequires: jgroups >= 0:2.2.8
## cache providers
BuildRequires: ehcache >= 0:1.2.3
%if %without bootstrap
BuildRequires: oscache >= 0:2.1
BuildRequires: swarmcache
%endif
## connection pool
# FIXME BuildRequires:  c3p0 >= 0:0.9.1
BuildRequires: c3p0
BuildRequires: proxool >= 0:0.8.3
BuildRequires: jacc_1_0_api

# The bytecode provides can be either javassist or cglib (default)
# cglib requires asm
Requires: cglib21 >= 0:2.1.3
Requires: asm
#Optional:      javassist >= 0:3.4
# Always required:
Requires: jakarta-commons-collections >= 0:2.1.1
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: antlr >= 0:2.7.6
Requires: dom4j >= 0:1.6.1
# Required if one wants to deserialize a Configuration in order to improve
# startup performance
#Optional:      jaxen >= 0:1.1
# Some SAX parser is required
Requires: xml-commons-apis
# Required for standalone operation (outside an AppServer)
Requires: jdbc-stdext
Requires: jta
# Required by replicated caches
#Optional:      jgroups >= 0:2.2.8
# Cache providers (default none)
#Optional:      hibernate_in_process_cache	
# hibernate_in_process_cache is one of ehcache, oscache, swarmcache or
# jboss-cache (default none)
#Optional:      ehcache >= 0:1.2.3
#Optional:      oscache >= 0:2.1
#Optional:      swarmcache
# JDBC connection pool
# hibernate_jdbc_cache is for instance c3p0 or proxool
# note that jakarta-commons-dbcp is not supported
#Optional:      hibernate_jdbc_cache
BuildRequires: docbook-style-xsl
BuildRequires: docbook-xsl-saxon
BuildRequires: saxon
BuildRequires: xmlgraphics-batik
BuildRequires: xmlgraphics-fop
BuildArch:      noarch

%description
Hibernate is a powerful, ultra-high performance 
object/relational persistence and query service 
for Java. Hibernate lets you develop persistent 
objects following common Java idiom - including 
association, inheritance, polymorphism, composition 
and the Java collections framework. Extremely 
fine-grained, richly typed object models are 
possible. The Hibernate Query Language, designed 
as a "minimal" object-oriented extension to SQL, 
provides an elegant bridge between the object and 
relational worlds. Hibernate is now the most 
popular ORM solution for Java.

%if %{with_repolib}
%package repolib
Summary:	Artifacts to be uploaded to a repository library
Group:	        Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{oldname}.

%if %with manual
%package manual
Summary:        Documents for %{oldname}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Javadoc for %{oldname}.
%endif

%prep
%setup -q -n %{hname}
# remove all binary libs
find . -name "*.jar" | xargs -t rm
rm -r doc/reference/support/docbook-dtd doc/reference/support/docbook-xsl

# Uncomment if you want to build without EHCache
#%%patch0
# Refer to J2SE 1.5 documentation, not 1.3
%patch1
%patch2
%patch5 -p1
%patch6 -p1
%if %with jdk6
%patch3
%patch4
%endif
DOCBOOKX_DTD=`%{_bindir}/xmlcatalog %{_datadir}/sgml/docbook/xmlcatalog "-//OASIS//DTD DocBook XML V4.3//EN" 2>/dev/null`
%{__perl} -pi -e 's|@DOCBOOKX_DTD@|$DOCBOOKX_DTD|' doc/reference/en/master.xml doc/reference/fr/master.xml

%if %with bootstrap
rm src/org/hibernate/cache/OSCache.java src/org/hibernate/cache/OSCacheProvider.java
%endif

%build
export OPT_JAR_LIST="ant/ant-swing ant/ant-antlr antlr ant/ant-junit junit ant-launcher"
export CLASSPATH=

# FIXME We don't have those.  Optional build time dependencies it seems
##mv lib/cleanimports.jar.no lib/cleanimports.jar
##mv lib/syndiag2.jar.no lib/syndiag2.jar
# Don't do versioncheck as our JARs have different filenames than the ones
# specified in version.properties
#mv lib/versioncheck.jar.no lib/versioncheck.jar

%if %without bootstrap
# FIXME Circular dependencies on jbossas
ln -s $(build-classpath jbossas/jboss-jmx) lib/jboss-jmx.jar
ln -s $(build-classpath jbossas/jboss-system) lib/jboss-system.jar
%else
ln -s $(build-classpath jboss4/jboss-jmx) lib/jboss-jmx.jar
ln -s $(build-classpath jboss4/jboss-system) lib/jboss-system.jar
%endif

build-jar-repository -s -p lib \
ant \
ant/ant-antlr \
ant/ant-junit \
ant/ant-swing \
ant-launcher \
antlr \
asm/asm \
asm/asm-attrs \
c3p0 \
cglib21 \
commons-collections \
commons-logging \
concurrent \
dom4j \
ehcache \
jaas \
jacc_1_0_api \
javassist \
jaxen \
jboss-cache \
jboss-common \
jdbc-stdext \
jgroups \
jta \
junit \
log4j \
%if %without bootstrap
oscache \
%endif
proxool \
swarmcache \
xerces-j2 \
xml-commons-apis

build-jar-repository -s -p doc/reference/support/lib \
docbook-xsl-saxon \
excalibur/avalon-framework-api \
saxon \
xmlgraphics-batik \
xmlgraphics-fop 

#Check if we were successiful in cleaning up binary files
# ------------------------------------------------------
find . -name '*.?ar' -not -type l -print > BINARYFILES
echo "WARNING: Binary files not replaced by links!"
cat BINARYFILES
echo "---"
# ------------------------------------------------------
#

export CLASSPATH=${CLASSPATH}:build/classes:build/testclasses:etc
#ant dist.complete
# Do not run versioncheck
# Also, the BNF creation is failing, it wants a DISPLAY (do we need a "headless" setting?)
#ant init jar javadoc refdoc antlr.bnf
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dnosplash init jar javadoc \
%if %with manual
refdoc
%endif

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p build/%{oldname}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/etc
cp -p etc/* $RPM_BUILD_ROOT%{_datadir}/%{name}/etc

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf build/doc/api

# manual
%if %with manual
	mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
	cp -pr doc/reference/build/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        tag=`echo %{oldname}-%{version}-%{release} | sed 's|\.|_|g'`
        sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
        sed -i "s/@VERSION@/%{version}.%{reltag}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
#	install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
	install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/hibernate32.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate3.jar
%endif

%files
%doc lgpl.txt
%{_javadir}/*.jar
%{_datadir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with manual
%files manual
%{_docdir}/%{name}-%{version}
%endif

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Jan 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt5_1.SP1_CP01.9jpp5
- support for antlr 2.7.7

* Sun Feb 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt4_1.SP1_CP01.9jpp5
- compat build

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt3_1.SP1_CP01.9jpp5
- fixed build; use cglib21

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt2_1.SP1_CP01.9jpp5
- selected java5 compiler explicitly

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_1.SP1_CP01.9jpp5
- new jpp release

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_1.SP1_CP01.1jpp5
- new version

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt2_0.cr2.1jpp5
- fixed build

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_0.cr2.1jpp5
- fixed build with java 5

* Tue Jan 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_0.cr2.1jpp1.7
- nobootstrap build

