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

#def_with maven
%bcond_with maven


Name:           joda-time
Version:        1.5.2
Release:        alt4_2jpp6
Epoch:          0
Summary:        Java date and time API
Group:          Development/Java
License:        ASL 2.0
URL:            http://www.joda.org/
Source0:        http://prdownloads.sourceforge.net/joda-time/joda-time-1.5.2-src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        %{name}-%{version}-jpp-depmap.xml
Source5:        http://mirrors.ibiblio.org/pub/mirrors/maven2/joda-time/joda-time/1.5.2/joda-time-1.5.2.pom
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
Requires: jpackage-utils
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: jpackage-utils >= 0:1.7.3
%if %with maven
BuildRequires: maven >= 0:1.1
BuildRequires: maven-plugins-base
BuildRequires: maven-plugin-changes
BuildRequires: maven-plugin-changelog
BuildRequires: maven-plugin-checkstyle
BuildRequires: maven-plugin-developer-activity
BuildRequires: maven-plugin-file-activity
BuildRequires: maven-plugin-jcoverage
BuildRequires: maven-plugin-jdiff
BuildRequires: maven-plugin-jxr
BuildRequires: maven-plugin-license
BuildRequires: maven-plugin-linkcheck
BuildRequires: maven-plugin-scm
BuildRequires: maven-plugin-tasklist
BuildRequires: maven-plugin-test
BuildRequires: maven-plugin-xdoc
BuildRequires: emma-maven-plugin
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
BuildArch:      noarch
Source44: import.info


%description
Joda-Time provides a quality replacement for the Java date 
and time classes. The design allows for multiple calendar 
systems, while still providing a simple API. The 'default' 
calendar is the ISO8601 standard which is used by XML. The 
Gregorian, Julian, Buddhist, Coptic and Ethiopic systems 
are also included, and we welcome further additions. 
Supporting classes include time zone, duration, format 
and parsing. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %with maven
%package manual
Summary:        Docs for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif


%prep
%setup -q -n joda-time-%{version}-src
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%if %with maven
export DEPCAT=$(pwd)/%{name}-%{version}-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    %{_bindir}/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
%{_bindir}/saxon $DEPCAT %{SOURCE2} > %{name}-%{version}-depmap.new.xml

for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    %{_bindir}/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done
%else
mkdir lib
pushd lib
ln -s $(build-classpath junit) junit-3.8.1.jar
popd
%endif

%build
%if %with maven
export MAVEN_HOME_LOCAL=$(pwd)/.maven
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=${MAVEN_HOME_LOCAL} \
        jar:jar javadoc:generate xdoc:transform
%else
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/junit`
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc 
%endif

%install

install -dm 755 %{buildroot}%{_javadir}

# jars
%if %with maven
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%else
install -pm 644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%endif
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE5} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap joda-time joda-time %{version} JPP %{name}

install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/docs/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%else
cp -pr build/docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
#
install -dm 755 %{buildroot}%{_docdir}/%{name}-%{version}
%if %with maven
cp -pr target/docs/* %{buildroot}%{_docdir}/%{name}-%{version}
rm -r %{buildroot}%{_docdir}/%{name}-%{version}/apidocs
%endif
cp -p LICENSE.txt %{buildroot}%{_docdir}/%{name}-%{version}

%files
%doc %dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with maven
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt4_2jpp6
- fixed build with moved maven1

* Sun Dec 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt3_2jpp6
- jpp 6.0 build

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_1jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_2jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

