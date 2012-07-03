Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: apache-jdo-1.1-impl
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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


Summary:        Triactive JDO
Name:           tjdo
Version:        2.2
Release:        alt1_1jpp5
Epoch:          0
License:        Apache Software License
URL:            http://tjdo.sourceforge.net/
Group:          Development/Java
Source0:        TJDO_2_2-src.zip
Source1:        tjdo-2.2.pom
Patch0:         tjdo-2.2-NoOracleAdapter.patch
Patch1:         tjdo-2.2-exclude-SoftValueMapTest.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-nodeps
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: junit
BuildRequires: derby
BuildRequires: jakarta-commons-logging
BuildRequires: apache-jdo-1.1-api
BuildRequires: apache-jdo-1.1-impl
BuildRequires: jta_1_0_1B_api
BuildRequires: log4j
Requires: jakarta-commons-logging
Requires: jdo < 0:2.0
Requires: jta_1_0_1B_api
Requires: log4j
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
TriActive JDO (TJDO) is an open source implementation 
of Sun's JDO specification (JSR 12), designed to support 
transparent persistence using any JDBC-compliant database. 
Although the project is formally in beta release, TJDO is 
currently deployed and running successfully in a number of 
commercial installations. 
The current version has been tested successfully using 
Cloudscape, DB2, Firebird, MySQL, Oracle 8i, PostgreSQL, 
SAP DB, and MS SQL Server.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Docs for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.


%prep
%setup -q -n %{name}-src
for j in $(find . -name "*.jar"); do
     mv $j $j.no
done
(cd lib
ln -s $(build-classpath commons-logging)
ln -s $(build-classpath apache-jdo-1.1-api) jdo.jar
ln -s $(build-classpath apache-jdo-1.1-impl) jdori.jar
ln -s $(build-classpath apache-jdo-1.1-impl) jdori-enhancer.jar
ln -s $(build-classpath junit)
ln -s $(build-classpath log4j)
ln -s $(build-classpath jta_1_0_1B_api)
ln -s $(build-classpath derby/derby) test/derby
ln -s $(build-classpath derby/derbytools) test/derby
)
rm src/com/triactive/jdo/store/mapping/Oracle*.java
rm src/com/triactive/jdo/store/adapter/Oracle*.java
%patch0 -b .sav0
%patch1 -b .sav1

%build
export LANG=C
ant jar javadoc unit-tests -Ddb=derby
#ant jar javadoc


%install

# jars
install -Dpm 644 build/jars/%{name}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_javadir}/*.jar
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_1jpp5
- selected java5 compiler explicitly

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_2jpp5
- fixed repocop warnings

* Sun Oct 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

