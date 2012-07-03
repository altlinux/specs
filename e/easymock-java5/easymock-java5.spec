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

%define oname   easymock

Name:           easymock-java5
Version:        1.2
Release:	alt1_6jpp6
Epoch:          0
Summary:        Easy mock objects

Group:          Development/Java
License:        MIT
URL:            http://www.easymock.org/
Source0:        EasyMock1_2_Java1_5.tar.gz
# cvs -d:pserver:anonymous@easymock.cvs.sourceforge.net:/cvsroot/easymock login
# cvs -z3 -d:pserver:anonymous@easymock.cvs.sourceforge.net:/cvsroot/easymock export -r EasyMock1_2_Java1_5 easymock
Source1:        http://repo1.maven.org/maven2/easymock/easymock/1.2_Java1.5/easymock-1.2_Java1.5.pom

Patch0:         easymock-1.2-java5-build_xml.patch


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: junit >= 0:3.8.1

Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Source44: import.info

%description
EasyMock provides Mock Objects for interfaces in JUnit tests by generating 
them on the fly using Java's proxy mechanism. Due to EasyMock's unique style 
of recording expectations, most refactorings will not affect the Mock Objects. 
So EasyMock is a perfect fit for Test-Driven Development.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}


%prep
%setup -q -n %{oname}
mkdir lib
pushd lib
ln -sf $(build-classpath junit) .
popd
echo "java\ 1.4=%{java}" >> easymockbuild.properties
echo "java\ 1.5=%{java}" >> easymockbuild.properties
echo "java\ compiler=%{javac}" >> easymockbuild.properties

%patch0 -b .sav

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first


%install
unzip %{oname}%{version}_Java1.5.zip

install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 %{oname}%{version}_Java1.5/%{oname}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap easymock easymock 1.2_Java1.5 JPP %{name}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr %{oname}%{version}_Java1.5/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar
%doc %{oname}%{version}_Java1.5/{Documentation,License}.html
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_6jpp6
- jpp 6 release

* Thu May 13 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_6jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp5
- converted from JPackage by jppimport script

