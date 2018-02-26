BuildRequires: apache-commons-pool apache-commons-dbcp
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define gcj_support 0

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define base_name jcs

Summary:        Java Caching System
Name:           jakarta-jcs
Version:        1.3.2.8
Release:        alt4_1jpp5
Epoch:          0
License:        Apache Software License
URL:            http://jakarta.apache.org/jcs/
Group:          Development/Java
Source0:        jcs-1.3.2.8-src.tar.gz
# svn export http://svn.apache.org/repos/asf/jakarta/jcs/tags/JCS_1_3_2_8/

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        jakarta-jcs-1.3.2.8-jpp-depmap.xml
Source5:        jakarta-jcs-build.xml
Patch0:         jakarta-jcs-project.patch
%if %{with_maven}
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-checkstyle
BuildRequires: maven1-plugin-ear
BuildRequires: maven1-plugin-faq
BuildRequires: maven1-plugin-jcoverage
BuildRequires: maven1-plugin-jdepend
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-pmd
BuildRequires: maven1-plugin-tasklist
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-war
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: sf-cobertura-maven-plugin
%endif
BuildRequires: junit
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5

BuildRequires: berkeleydb
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-configuration
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: concurrent
BuildRequires: hsqldb
BuildRequires: jgroups
BuildRequires: jisp2
BuildRequires: log4j
BuildRequires: mysql-connector-java
BuildRequires: servlet_2_3_api
BuildRequires: struts
BuildRequires: tomcat5-server-lib
BuildRequires: velocity
BuildRequires: xmlrpc2
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis

Requires: alternatives >= 0:0.4
Requires: berkeleydb
Requires: jakarta-commons-collections
Requires: jakarta-commons-configuration
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: concurrent
Requires: hsqldb
Requires: jgroups
Requires: jisp2
Requires: log4j
Requires: servlet_2_3_api
Requires: struts
Requires: tomcat5-server-lib
Requires: velocity
Requires: xmlrpc2
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
Provides:  hibernate_in_process_cache
Provides:  jakarta-turbine-jcs
Obsoletes:  jakarta-turbine-jcs
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
JCS is a distributed caching system written in java 
for server-side java applications. It is intended to 
speed up dynamic web applications by providing a means 
to manage cached data of various dynamic natures. 
Like any caching system, the JCS is most useful for 
high read, low put applications. Dynamic content and 
reporting systems can benefit most. 
However, any site that repeatedly constructs pages, 
dropdowns, or common search results form a database 
that is updated at intervals (rather than across 
categories continuously) can improve performance and 
scalability by implementing caching. Latency times drop 
sharply and bottlenecks move away from the database in 
an effectively cached system. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:  jakarta-turbine-jcs-javadoc
Obsoletes:  jakarta-turbine-jcs-javadoc
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%if %{with_maven}
%package manual
Summary:        Docs for %{name}
Group:          Development/Documentation
Provides:  jakarta-turbine-jcs-manual
Obsoletes:  jakarta-turbine-jcs-manual
BuildArch: noarch

%description manual
Docs for %{name}.
%endif

%prep
%setup -q -n jcs-%{version}-src
# remove all binary libs
## find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
cp %{SOURCE5} build.xml
%patch0 -b .sav0

# NOTE:
# org.apache.jcs.auxiliary.lateral.socket.tcp.discovery.UDPDiscoveryUnitTest
# must enable UDP port 6789 in firewall for this test to succeed

%build
%if %{with_maven}
export DEPCAT=$(pwd)/%{name}-%{version}-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > %{name}-%{version}-depmap.new.xml
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven

maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        -Dmaven.test.skip=true \
        jar javadoc xdoc:transform ear war
%else
export CLASSPATH=$(build-classpath concurrent servletapi4 velocity xmlrpc2 hsqldb):target/classes:target/test-classes:src/test-conf
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
%endif

%install
# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -m 0644 target/%{base_name}-%{version}-RC.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/ && ln -s %{name}-%{version}.jar %{base_name}-%{version}.jar)
(cd $RPM_BUILD_ROOT%{_javadir}/ && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
# ear, war
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
%if %{with_maven}
install -m 0644 target/%{base_name}-%{version}-RC.ear \
                $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -m 0644 target/%{base_name}.war \
                $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
%endif

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf target/docs/apidocs

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

# hibernate_in_process_cache ghost symlink
ln -s %{_sysconfdir}/alternatives \
  $RPM_BUILD_ROOT%{_javadir}/hibernate_in_process_cache.jar

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm \
%if %{with_maven}
--exclude /usr/share/%{name}-%{version}/jcs.war
%endif

%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/hibernate_in_process_cache_%{name}<<EOF
%{_javadir}/hibernate_in_process_cache.jar	%{_javadir}/%{name}.jar	10
EOF

%files
%_altdir/hibernate_in_process_cache_%{name}
%{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/*jcs*.jar
%exclude %{_javadir}/hibernate_in_process_cache.jar
%{_datadir}/%{name}-%{version}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%if %{with_maven}
%files manual
%{_docdir}/%{name}-%{version}
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2.8-alt4_1jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2.8-alt3_1jpp5
- use maven1

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2.8-alt2_1jpp5
- fixed build

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2.8-alt1_1jpp5
- new version

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7.0-alt1_7jpp5
- fixed repocop warnings

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7.0-alt1_7jpp1.7
- updated to new jpackage release

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7.0-alt1_6jpp1.7
- converted from JPackage by jppimport script

