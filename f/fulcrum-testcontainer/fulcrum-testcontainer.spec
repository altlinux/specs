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

%define gcj_support 0


Name:           fulcrum-testcontainer
Version:        1.0.5
Release:        alt3_1jpp5
Epoch:          0
Summary:        Fulcrum Test Container
License:        Apache Software License 2.0
Group:          Development/Java
#Vendor: %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:%{_vendor}}
#Distribution: %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}
URL:            http://turbine.apache.org/fulcrum/fulcrum-testcontainer/
Source0:        http://www.apache.org/dist/turbine/fulcrum/fulcrum-testcontainer/source/fulcrum-testcontainer-1.0.5-src.tar.gz

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        %{name}-%{version}-jpp-depmap.xml
Source5:        fulcrum-testcontainer-1.0.5.pom
Source6:        fulcrum-parent-project.xml
Source7:        fulcrum-parent-project.properties

Patch0:         fulcrum-testcontainer-project_xml.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: excalibur-avalon-framework-api
BuildRequires: excalibur-avalon-framework-impl
BuildRequires: excalibur-component
BuildRequires: excalibur-instrument-api
BuildRequires: excalibur-logger
BuildRequires: excalibur-pool-api
BuildRequires: fulcrum-yaafi
BuildRequires: jakarta-commons-logging

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
This component is really just a test container for testing 
the other components. This container is not meant to be 
used in a production environment.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
#Requires(post):   /bin/rm,/bin/ln
#Requires(postun): /bin/rm

%description    javadoc
%{summary}.


%prep
%setup -q -n %{name}-%{version}
%patch0 -b .sav0
mkdir parent
cp %{SOURCE6} parent/project.xml
cp %{SOURCE7} parent/project.properties

%build
if [ ! -f %{SOURCE4} ]; then
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
fi
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
        jar:install javadoc:generate

%install

# jars
install -dm 0755 $RPM_BUILD_ROOT%{_javadir}
install -m 0644 target/%{name}-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap fulcrum %{name} %{version} JPP %{name}

# javadoc
install -dm 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt3_1jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt2_1jpp5
- use maven1

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt1_1jpp5
- converted from JPackage by jppimport script

