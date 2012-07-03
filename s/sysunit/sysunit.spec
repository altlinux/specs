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


Name:           sysunit
Summary:        SysUnit
Url:            http://sourceforge.net/projects/sysunit
Version:        1.0
Release:        alt5_1jpp5
Epoch:          0
License:        Apache Software License 2
Group:          Development/Java
Source0:        sysunit.tar.gz
#  cvs -d:pserver:anonymous@sysunit.cvs.sourceforge.net:/cvsroot/sysunit login
#  cvs -z3 -d:pserver:anonymous@sysunit.cvs.sourceforge.net:/cvsroot/sysunit export -r HEAD sysunit

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        sysunit-1.0-jpp-depmap.xml
Source5:        sysunit-1.0.pom

Patch0:         sysunit-project.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant
BuildRequires: junit
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-changelog
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-checkstyle
BuildRequires: maven1-plugin-developer-activity
BuildRequires: maven1-plugin-file-activity
BuildRequires: maven1-plugin-html2xdoc
BuildRequires: maven1-plugin-jdepend
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-linkcheck
BuildRequires: maven1-plugin-multiproject
BuildRequires: maven1-plugin-pmd
BuildRequires: maven1-plugin-tasklist
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-war
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
#
BuildRequires: jakarta-commons-logging
BuildRequires: jbossas

#BuildRequires:  mx4j

#
Requires: jakarta-commons-logging
#Requires:  jbossas
#Requires:  mx4j

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
SysUnit is a JUnit framework for distributed testing, system
testing and integration testing. SysUnit is ideal for testing
highly distributed software such as clusters of web
applications, web services or MOM based software.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

export DEPCAT=$(pwd)/sysunit-1.0-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > sysunit-1.0-depmap.new.xml

%patch0 -b .sav0

%build
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven

maven -e \
	-Dmaven.compile.target=1.5 -Dmaven.compile.source=1.5 -Dmaven.javadoc.source=1.5 \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        sar 
	#doc javadoc


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 \
        target/%{name}-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}

# sar
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/sar
install -m 644 \
        target/%{name}-%{version}.sar \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/sar/%{name}-%{version}.sar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

#cp -pr target/docs/apidocs/* \
#                $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
#ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
#install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#rm -rf target/docs/apidocs
#cp -pr target/docs/* \
#   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm \
    --exclude /usr/share/%{name}/sar/%{name}-5{version}.sar
%endif

%files
%{_javadir}/*.jar
%{_datadir}/%{name}
#%doc %{_docdir}/%{name}-%{version}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*-%{version}.jar.*
%endif

#%files javadoc
#%doc %{_javadocdir}/%{name}-%{version}
#%doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_1jpp5
- fixed build with java 7

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_1jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1jpp5
- use maven1

* Sat Dec 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- fixed build: dropped javadocs due to dying maven1

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- new version

