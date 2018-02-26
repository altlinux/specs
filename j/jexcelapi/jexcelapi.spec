BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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

%define archivever 2_6_12

Name:           jexcelapi
Version:        2.6.12
Release:        alt3_1jpp6
Epoch:          0
Summary:        A Java API to read, write and modify Excel spreadsheets
License:        LGPL
Group:          Development/Java
URL:            http://www.andykhan.com/%{name}
Source0:        %{url}/%{name}_%{archivever}.tar.gz
Source1:        http://repo1.maven.org/maven2/net/sourceforge/jexcelapi/jxl/2.6.12/jxl-2.6.12.pom
Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires:	log4j >= 0:1.2.8

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  jflex
BuildRequires:  findutils
BuildRequires:  sed
BuildRequires:	log4j
BuildArch:      noarch
Source44: import.info

%description
Jexcelapi allows Java developers to read Excel spreadsheets and generate Excel
spreadsheets dynamically. In addition, it contains a mechanism which allows
Java applications to read a spreadsheet, modify some cells and write the
modified spreadsheet.

Thanks to jexcelapi non Windows operating systems can run pure Java applications
which process and deliver Excel spreadsheets. Because it is Java, this API may
be invoked from within a servlet, thus giving access to Excel functionality
over internet and intranet web applications.

Features:
- Reads data from Excel 95, 97, 2000 workbooks
- Reads and writes formulas (Excel 97 and later only)
- Generates spreadsheets in Excel 97 format
- Supports font, number and date formatting
- Supports shading and colouring of cells
- Modifies existing worksheets


%package        javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -n %{name} -q

# Clean up binary leftovers
%{_bindir}/find . -name "*.jar" -exec rm -f {} \;
%{_bindir}/find . -name "*.class" -exec rm -f {} \;

# Clean up temp files (confuses javadoc 1.3.1)
%{_bindir}/find . -name ".#*" -exec rm -f {} \;

mkdir -p build/out

%build
export LANG=en_US.ISO8859-1
cd build
cat > build.properties <<EOBP
logger=Log4jLogger
loggerClasspath=$(build-classpath log4j)
EOBP

[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
ln -sf $(build-classpath jflex) JFlex.jar

%{_bindir}/ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 clean
%{_bindir}/ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jxlall

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 0644 jxl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar

pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
        for jar in %{name}*.jar ; do
                ln -sf ${jar} $(echo $jar| sed "s|%{name}|jxl|g")
        done
        for jar in *-%{version}.jar ; do
                ln -sf ${jar} $(echo $jar| sed "s|-%{version}\.jar|.jar|g")
        done
popd

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
%add_to_maven_depmap %{name} jxl %{version} JPP/%{name} %{name}

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -r docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -sf %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%name
install -m 0644 *.dtd *.xls $RPM_BUILD_ROOT%{_datadir}/%name/

%files
%doc *.html
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.dtd
%{_datadir}/%{name}/*.xls

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt3_1jpp6
- target 5 build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt2_1jpp6
- fixed build with java 7

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt1_1jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.4.3-alt1_5jpp5
- new jpp release

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.3-alt1_4jpp1.7
- converted from JPackage by jppimport script

