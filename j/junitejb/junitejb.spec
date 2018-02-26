Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: jta geronimo-ejb-2.1-api
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
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

%define section   devel

Name:           junitejb
Version:        1.0
Release:        alt1_0.b2.2jpp5
Epoch:          0
Summary:        JUnitEJB extension to JUnit

Group:          Development/Java
License:        LGPL
URL:            http://sourceforge.net/projects/junitejb/
Source0:        junitejb-1.0.b2.tar.gz
Patch0:         junitejb-build_xml.patch

BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant
BuildRequires: junit >= 0:3.8.1
BuildRequires: ejb
BuildRequires: jta
Requires: junit >= 0:3.8.1
Requires: ejb
Requires: jta

%description
JUnitEJB is an extension to JUnit which runs test on a 
remote EJB server. Tests can be executes via a simple 
session bean. This allows the testing of a EJBLocalObject.


%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}

%patch0

%build
export OPT_JAR_LIST="ant-launcher"
export CLASSPATH=$(build-classpath \
ejb \
jta \
junit)
#export CLASSPATH=$(build-classpath \
#ant \
#ant-launcher \
#ejb \
#jta \
#junit)
ant -f build/build.xml -Dbuild.sysclasspath=only \
	-Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 \
	build javadoc


%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{name}.jar \
			$RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -pm 644 %{name}-full.jar \
			$RPM_BUILD_ROOT%{_javadir}/%{name}-full-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-full-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-full.jar
#
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
#
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr %{name}.ear $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}


%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}


%files
%{_javadir}/*.jar
%{_datadir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b2.2jpp5
- fixed build w/java5 

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b2.2jpp1.7
- converted from JPackage by jppimport script

