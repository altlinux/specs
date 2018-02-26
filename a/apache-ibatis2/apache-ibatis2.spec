BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2012, JPackage Project
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

%define oname    ibatis
%define sversion 2.3.4
%define aversion 1.2.1


Name:           apache-ibatis2
Summary:        iBATIS SQL Maps Framework
Url:            http://ibatis.apache.org/
Version:        2.3.4
Release:        alt2_2jpp6
Epoch:          0
License:        Apache Software License 2
Group:          Databases
BuildArch:      noarch
Source0:        ibatis-2.3.4.tar.gz
# svn export http://svn.apache.org/repos/asf/ibatis/tags/java_release_2.3.2-715/mapper/mapper2/ ibatis-2.3.4
Source1:        ibatis-sqlmap-2.3.4.pom
Source2:        http://ibatis.apache.org/docs/java/pdf/iBATIS-SqlMaps-2_en.pdf
Source3:        http://ibatis.apache.org/docs/java/pdf/iBATIS-SqlMaps-2-Tutorial_en.pdf
Source4:        ibator-1.2.1.tar.gz
# svn export http://svn.apache.org/repos/asf/ibatis/java/ibator/tags/ibator_release_1.2.1-681/ ibator-1.2.1
Patch0: apache-ibatis2-SimpleDataSource.patch
Patch1: apache-ibatis2-CallableStatementResultSet.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-trax
BuildRequires:  ant-nodeps
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  emma

BuildRequires:  cglib
BuildRequires:  derby
BuildRequires:  db-ojb
BuildRequires:  hsqldb
BuildRequires:  apache-commons-dbcp
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  jta_1_0_1B_api
BuildRequires:  log4j
BuildRequires:  spring2-beans
BuildRequires:  spring2-core
BuildRequires:  spring2-orm
BuildRequires:  spring2-jdbc
BuildRequires:  spring2-tx
BuildRequires:  xalan-j2

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info


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

%package sqlmap
Summary:        Ibatis SQL mapper
Group:          Databases
Version:        %{sversion}

%description sqlmap
%{summary}.

%package ibator-core
Summary:        Ibatis Core Code Generator
Group:          Databases
Version:        %{aversion}
Provides:       apache-ibatis-abator-core = %{aversion}-%{release}
Obsoletes:      apache-ibatis-abator-core < %{aversion}-%{release}

%description ibator-core
%{summary}.

%package sqlmap-javadoc
Summary:        Javadoc for Ibatis SQL mapper
Group:          Development/Documentation
Version:        %{sversion}

%description sqlmap-javadoc
%{summary}.

%package ibator-core-javadoc
Summary:        Javadoc for Ibatis Core Code Generator
Group:          Development/Documentation
Version:        %{aversion}
Provides:       apache-ibatis-abator-core-javadoc = %{aversion}-%{release}
Obsoletes:      apache-ibatis-abator-core-javadoc < %{aversion}-%{release}

%description ibator-core-javadoc
%{summary}.

%package ibator-core-manual
Summary:        Documents for Ibatis Core Code Generator
Group:          Development/Documentation
Version:        %{aversion}
Provides:       apache-ibatis-abator-core-manual = %{aversion}-%{release}
Obsoletes:      apache-ibatis-abator-core-manual < %{aversion}-%{release}

%description ibator-core-manual
%{summary}.

%package sqlmap-manual
Summary:        Documents for Ibatis SQL Mapper
Group:          Development/Documentation
Version:        %{sversion}

%description sqlmap-manual
%{summary}.

%prep
%setup -q -n %{oname}-%{version}
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
tar xzf %{SOURCE4}
ln -s ibator-1.2.1 ibator
%patch0 -b .sav0
%patch1 -b .sav1

%build
cd ibatis-2-core
pushd devlib
ln -sf $(build-classpath cglib-nodep)
ln -sf $(build-classpath commons-dbcp)
ln -sf $(build-classpath commons-lang)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath emma_ant)
ln -sf $(build-classpath emma)
ln -sf $(build-classpath db-ojb/db-ojb)
ln -sf $(build-classpath derby/derby)
ln -sf $(build-classpath hsqldb)
ln -sf $(build-classpath jta_1_0_1B_api)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath log4j)
ln -sf $(build-classpath xalan-j2-serializer)
ln -sf $(build-classpath xalan-j2)
popd
pushd ../ibator/core/devlib/
ln -sf $(build-classpath hsqldb)
popd
export OPT_JAR_LIST="ant/ant-trax ant/ant-nodeps ant/ant-junit junit"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f build/build.xml
cp build/exploded/lib/ibatis-2.3.4.727.jar ../ibator/core/devlib/ibatis.jar
pushd ../ibator/core
ln -sf $(build-classpath hsqldb) devlib/hsqldb.jar
export CLASSPATH=$(build-classpath hsqldb emma spring2/beans spring2/core spring2/orm spring2/jdbc spring2/tx)
CLASSPATH=$CLASSPATH:$(pwd)/devlib/ibatis.jar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f build/build.xml
popd

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 ibatis-2-core/build/exploded/lib/ibatis-%{version}*.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.ibatis ibatis-sqlmap %{version} JPP %{name}

install -m 644 ibator/core/build/deploy/files/ibator.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-ibator-core-%{aversion}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{aversion}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{aversion}||g"`; done)
# create legacy symlinks
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}.jar %{name}-common.jar
ln -s %{name}.jar %{name}-sqlmap.jar
popd

# sqlmap javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-sqlmap-%{version}
cp -pr ibatis-2-core/build/work/javadocs/dev $RPM_BUILD_ROOT%{_javadocdir}/%{name}-sqlmap-%{version}
cp -pr ibatis-2-core/build/work/javadocs/user $RPM_BUILD_ROOT%{_javadocdir}/%{name}-sqlmap-%{version}
ln -s %{name}-sqlmap-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-sqlmap # ghost symlink

# abator javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-ibator-core-%{aversion}
cp -pr ibator/core/build/work/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-ibator-core-%{aversion}
ln -s %{name}-ibator-core-%{aversion} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-ibator-core # ghost symlink

# sqlmap manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-sqlmap-%{version}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}-sqlmap-%{version}
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_docdir}/%{name}-sqlmap-%{version}

# ibator-core manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-ibator-core-%{aversion}
cp -pr ibator/core/htmldoc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-ibator-core-%{aversion}

%files sqlmap
%{_javadir}/%{name}-common.jar
%{_javadir}/%{name}-sqlmap.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%doc ibatis-2-core/doc/license.txt
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files ibator-core
%{_javadir}/%{name}-ibator-core*.jar

%files sqlmap-javadoc
%doc %{_javadocdir}/%{name}-sqlmap-%{version}
%doc %{_javadocdir}/%{name}-sqlmap

%files ibator-core-javadoc
%{_javadocdir}/%{name}-ibator-core-%{aversion}
%ghost %doc %{_javadocdir}/%{name}-ibator-core

%files sqlmap-manual
%{_docdir}/%{name}-sqlmap-%{version}

%files ibator-core-manual
%{_docdir}/%{name}-ibator-core-%{aversion}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.4-alt2_2jpp6
- built with java 6 due to abstract getParentLogger

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.4-alt1_2jpp6
- jpp6 release

