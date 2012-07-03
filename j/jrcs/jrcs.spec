Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%bcond_without maven

%define gcj_support 0


Name:           jrcs
Version:        1.1
Release:        alt4_0.r72.1jpp6
Epoch:          0
Summary:        JRCS - A RCS Archive Parser in Java

Group:          Development/Java
License:        Open Source
URL:            http://jrcs.codehaus.org/
Source0:        jrcs-1.1.tgz
# svn export http://svn.codehaus.org/jrcs/trunk/jrcs 
# tar czf ../SOURCES/jrcs-1.1.tgz jrcs

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        jrcs-1.1-jpp-depmap.xml

Patch0:         jrcs-1.1-project_xml.patch
Patch1:         jrcs-1.1-xdocs-project_xml.patch

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: ant >= 0:1.7
%if %with maven
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
BuildRequires: junit
BuildRequires: jakarta-oro
Requires: jakarta-oro
Source44: import.info

%description
JRCS is a library for parsing and manipulation of RCS archive
files like the ones produced by the RCS (Revision Control
System) itself and by CVS (Concurrent Version System).

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%if %with maven
%package        manual
Summary:        Docs for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.
%endif

%prep
%setup -q -n %{name}
%patch0 -b .sav0
%patch1 -b .sav1
if [ ! -f %{SOURCE4} ]; then
export DEPCAT=$(pwd)/jrcs-1.0-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > jrcs-1.1-depmap.new.xml
fi

%build
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

%if %with maven
maven -Dmaven.compile.target=1.5 -Dmaven.compile.source=1.5 -Dmaven.javadoc.source=1.5  \
         -Dmaven.repo.remote=file:/usr/share/maven1/repository \
         -Dmaven.home.local=$(pwd)/.maven \
         jar javadoc 
%else
export CLASSPATH=target/classes:target/test-classes
export OPT_JAR_LIST=:
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
%endif

%install
install -Dpm 644 target/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadocs
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}


%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_0.r72.1jpp6
- fixed build with java 7

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_0.r72.1jpp6
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_0.r72.1jpp6
- use maven1

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.r72.1jpp6
- new version

