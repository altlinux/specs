BuildRequires: geronimo-jta-1.0.1B-api
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

%define oname   ibatis


Name:           apache-ibatis-dao
Summary:        iBATIS DAO Frameworks
Url:            http://ibatis.apache.org/
Version:        2.2.0
Release:        alt3_2jpp5
Epoch:          0
License:        Apache Software License 2
Group:          Databases
BuildArch:      noarch
Source0:        ibatis-2.2.0.tar.gz
# svn export http://svn.apache.org/repos/asf/ibatis/tags/java_release_2.2.0-638/mapper/mapper2/ ibatis-2.2.0
Source1:        ibatis-dao-2.2.0.pom
Source2:        http://ibatis.apache.org/docs/java/pdf/iBATIS-DAO-2_en.pdf

Patch0:         ibatis-2.2.0-build_xml.patch

BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-trax
BuildRequires: ant-nodeps
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: emma

BuildRequires: apache-ibatis2-sqlmap
BuildRequires: db-ojb
BuildRequires: hsqldb
BuildRequires: jakarta-commons-lang
BuildRequires: jta_1_0_1B_api
Requires: apache-ibatis2-sqlmap
Requires: db-ojb
Requires: jakarta-commons-lang
Requires: jta_1_0_1B_api


%description
The iBATIS Data Mapper framework makes it easier to use a 
database with Java and .NET applications. iBATIS couples 
objects with stored procedures or SQL statements using a 
XML descriptor. Simplicity is the biggest advantage of the 
iBATIS Data Mapper over object relational mapping tools.

To use the iBATIS Data Mapper, you rely on your own objects, 
XML, and SQL. There is little to learn that you don't already 
know. With the iBATIS Data Mapper, you have the full power of 
both SQL and stored procedures at your fingertips.

%package javadoc
Summary:        Javadoc for Ibatis DAO Framework
Group:          Development/Documentation

%description javadoc
%{summary}.

%package manual
Summary:        Documents for Ibatis DAO Framework
Group:          Development/Documentation

%description manual
%{summary}.

%prep
%setup -q -n %{oname}-%{version}
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
rm -rf src/com/ibatis/common/
rm -rf src/com/ibatis/sqlmap/
rm -rf test/com/ibatis/common/
rm -rf test/com/ibatis/sqlmap/
%patch0 -b .sav0

%build
pushd devlib
ln -sf $(build-classpath apache-ibatis2) apache-ibatis.jar
ln -sf $(build-classpath commons-lang)
ln -sf $(build-classpath emma_ant)
ln -sf $(build-classpath emma)
ln -sf $(build-classpath db-ojb/db-ojb)
ln -sf $(build-classpath hsqldb)
ln -sf $(build-classpath jta_1_0_1B_api)
popd
export OPT_JAR_LIST="ant/ant-trax ant/ant-nodeps ant/ant-junit junit"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f build/build.xml

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/exploded/lib/ibatis-dao-2.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/work/javadocs/dev $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/work/javadocs/user $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# sqlmap manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_javadir}/%{name}*.jar
%doc doc/license.txt

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_2jpp5
- built with apache-ibatis2

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt2_2jpp5
- fixed build

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt1_2jpp5
- new jpp release

