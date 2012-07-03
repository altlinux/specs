Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-core
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


Name:           chainedoptions
Version:        0.9.0
Release:        alt2_1jpp5
Epoch:          0
Summary:        Chained Options

Group:          Development/Java
License:        LGPL
URL:            http://chainedoptions.sourceforge.net
Source0:        http://downloads.sourceforge.net/chainedoptions/chainedoptions-buildable-0.9.0.zip
Patch: chainedoptions-0.9.0-alt-kill-ivy.patch

BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant17 >= 0:1.6.5
BuildRequires: ant17-nodeps
BuildRequires: ant17-junit
BuildRequires: junit
BuildRequires: ivy
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: easymock-classextension
BuildRequires: easymock-java5
BuildRequires: gsbase
BuildRequires: servlet_2_4_api
BuildRequires: spring2-beans
BuildRequires: spring2-context
BuildRequires: spring2-core
BuildRequires: spring2-test
BuildRequires: spring2-web
BuildRequires: spring2-webmvc

Requires: jakarta-commons-lang
Requires: spring2-beans

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Java framework for chained options (listboxes, dropdowns 
etc). Provides functionality so that when the value is 
changed in one listbox, other listboxes change accordingly.
Handles special items like 'Any Value' or 'None Selected'.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.


%prep
%setup -q -c
for j in $(find modules/lib -name "*.jar"); do
    mv $j $j.no
done
%patch -p1

%build
cd build-chainedoptions
export OPT_JAR_LIST="junit ant17/ant17-junit ant17/ant17-nodeps ivy"
export CLASSPATH=$(build-classpath \
commons-lang \
commons-logging \
easymock-classextension \
easymock-java5 \
gsbase \
servlet_2_4_api \
spring2/beans \
spring2/context \
spring2/core \
spring2/test \
spring2/web \
spring2/webmvc \
)
CLASSPATH=$CLASSPATH:../chainedoptions/target/classes:../chainedoptions/target/test-classes
CLASSPATH=$CLASSPATH:../chainedoptions-samples/regioncountry/target/classes:../chainedoptions-samples/regioncountry/target/test-classes
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -v -Dbuild.sysclasspath=only release

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 chainedoptions/target/dist/jars/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap net.sf %{name} %{version} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr chainedoptions/target/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%doc %{name}/LICENSE.txt
#%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.0-alt2_1jpp5
- build with ant17

* Sat Mar 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9.0-alt1_1jpp5
- first build

