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

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define base_name commons-latka

Name:           jakarta-commons-latka
Version:        1.0
Release:        alt5_0.r560660.1jpp5
Epoch:          0
Summary:        Functional (end-to-end) testing tool

Group:          Development/Java
License:        Apache Software License
URL:            http://jakarta.apache.org/commons/latka/
Source0:        commons-latka-1.0-r560660.tar.gz
# svn export -r 560660 http://svn.apache.org/repos/asf/commons/dormant/latka/trunk commons-latka-1.0-r560660
Source1:        pom-maven2jpp-mapdeps.xsl
Source2:        commons-latka-1.0-jpp-depmap.xml
Source3:        commons-build.tar.gz
Source4:        commons-latka-1.0.pom

Patch0:         commons-latka-build_xml.patch
Patch1:         commons-latka-project_xml.patch
Patch2:         commons-latka-project_properties.patch
Patch3:         commons-latka-maven_xml.patch
Patch4:         commons-latka-navigation_xml.patch

%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: junit
BuildRequires: ant >= 0:1.6
%if %{with_maven}
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-checkstyle
BuildRequires: maven1-plugin-developer-activity
BuildRequires: maven1-plugin-file-activity
BuildRequires: maven1-plugin-jdepend
BuildRequires: maven1-plugin-jellydoc
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-tasklist
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif

BuildRequires: dom4j >= 0:1.6
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-commons-jelly
BuildRequires: jakarta-commons-jelly-tags-junit
BuildRequires: jakarta-commons-jexl
BuildRequires: jakarta-commons-logging
BuildRequires: jaxen >= 0:1.1
BuildRequires: jdom >= 0:1.0
BuildRequires: log4j
BuildRequires: regexp
BuildRequires: servlet_2_3_api
Requires: dom4j >= 0:1.6
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jakarta-commons-httpclient
Requires: jakarta-commons-jelly
Requires: jakarta-commons-jelly-tags-junit
Requires: jakarta-commons-jexl
Requires: jakarta-commons-logging
Requires: jaxen >= 0:1.1
Requires: jdom >= 0:1.0
Requires: log4j
Requires: regexp
Requires: servlet_2_3_api
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: dos2unix

%description
Latka is a functional (end-to-end) testing tool. 
It is implemented in Java, and uses an XML syntax 
to define a series of HTTP (or HTTPS) requests and 
a set of validations used to verify that the request 
was processed correctly. 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%if %{with_maven}
%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description    manual
%{summary}.
%endif

%prep
%setup -q -n commons-latka-1.0-r560660
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
gzip -dc %{SOURCE3} | tar xf -

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav

%build
%if %{with_maven}
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE1} map=%{SOURCE2}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven
maven -Dmaven.compile.target=1.5 -Dmaven.compile.source=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        jar:install javadoc:generate xdoc:transform


%else
mkdir -p target/lib
pushd target/lib
    ln -sf $(build-classpath dom4j)
    ln -sf $(build-classpath commons-beanutils)
    ln -sf $(build-classpath commons-codec)
    ln -sf $(build-classpath commons-collections)
    ln -sf $(build-classpath commons-httpclient)
    ln -sf $(build-classpath commons-jelly)
    ln -sf $(build-classpath commons-jelly-tags-junit)
    ln -sf $(build-classpath commons-jexl)
    ln -sf $(build-classpath commons-logging)
    ln -sf $(build-classpath jaxen)
    ln -sf $(build-classpath jdom)
    ln -sf $(build-classpath log4j)
    ln -sf $(build-classpath regexp)
    ln -sf $(build-classpath servlet_2_3_api)
popd
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 test dist
%endif

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{base_name}-%{version}-SNAPSHOT.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}-%{version}.jar
ln -s %{base_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}.jar
%add_to_maven_depmap commons-latka commons-latka %{version} JPP commons-latka

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin
cp -p src/distribution/bin/*.sh $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf
cp -p src/distribution/conf/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/resources
cp -p src/resources/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/resources

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -p LICENSE.txt $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{with_maven}
# manual
rm -rf target/docs/apidocs
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
find $RPM_BUILD_ROOT -name *.sh -print0 | xargs -0 dos2unix

%files
%{_javadir}/*.jar
%doc %{_datadir}/%{name}-%{version}
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%if %{with_maven}
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.r560660.1jpp5
- fixed build with java 7

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.r560660.1jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.r560660.1jpp5
- use maven1

* Tue May 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.r560660.1jpp5
- new jpp release

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.r389670.3jpp1.7
- new jpp release

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.r389670.2jpp1.7
- rebuilt with maven1

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.r389670.2jpp1.7
- converted from JPackage by jppimport script

