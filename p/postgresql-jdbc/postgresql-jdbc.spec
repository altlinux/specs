Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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

%global section		devel
%global upstreamrel	1200
%global upstreamver	9.4-%{upstreamrel}

Summary:	JDBC driver for PostgreSQL
Name:		postgresql-jdbc
Version:	9.4.%{upstreamrel}
Release:	alt1_3jpp8
# ASL 2.0 applies only to postgresql-jdbc.pom file, the rest is BSD
License:	BSD and ASL 2.0
Group:		Databases
URL:		http://jdbc.postgresql.org/

Source0:	http://jdbc.postgresql.org/download/%{name}-%{upstreamver}.src.tar.gz
# originally http://repo2.maven.org/maven2/postgresql/postgresql/8.4-701.jdbc4/postgresql-8.4-701.jdbc4.pom:
Source1:	%{name}.pom

# Revert back fix for travis build which breaks our ant-build for version 1.9.2
# & 1.9.4.
# ~> downstream
# ~> 1118667
Patch0:		postgresql-jdbc-9.3-1102-revert-88b9a034.patch

BuildArch:	noarch
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:	ant
BuildRequires:	ant-junit
BuildRequires:	junit
# gettext is only needed if we try to update translations
#BuildRequires:	gettext
Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-jdbc package includes the .jar files needed for
Java programs to access a PostgreSQL database.

%package javadoc
Summary:        API docs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API Documentation for %{name}.

%prep
%setup -c -q
mv -f %{name}-%{upstreamver}.src/* .
rm -f %{name}-%{upstreamver}.src/.gitignore
rm -f %{name}-%{upstreamver}.src/.travis.yml
rmdir %{name}-%{upstreamver}.src

# remove any binary libs
find -name "*.jar" -or -name "*.class" | xargs rm -f

%patch0 -p1 -b .revert-travis-fix

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=

# Ideally we would run "sh update-translations.sh" here, but that results
# in inserting the build timestamp into the generated messages_*.class
# files, which makes rpmdiff complain about multilib conflicts if the
# different platforms don't build in the same minute.  For now, rely on
# upstream to have updated the translations files before packaging.

ant jar publicapi

%install
install -d $RPM_BUILD_ROOT%{_javadir}
# Per jpp conventions, jars have version-numbered names and we add
# versionless symlinks.
install -m 644 jars/postgresql-%{upstreamver}.jdbc41.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


pushd $RPM_BUILD_ROOT%{_javadir}
# Also, for backwards compatibility with our old postgresql-jdbc packages,
# add these symlinks.  (Probably only the jdbc3 symlink really makes sense?)
ln -s postgresql-jdbc.jar postgresql-jdbc2.jar
ln -s postgresql-jdbc.jar postgresql-jdbc2ee.jar
ln -s postgresql-jdbc.jar postgresql-jdbc3.jar
popd

# Install the pom after inserting the correct version number
sed 's/UPSTREAM_VERSION/%{upstreamver}/g' %{SOURCE1} >JPP-%{name}.pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}/
install -m 644 JPP-%{name}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
cp -ra build/publicapi $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d build/publicapi docs/%{name}


%check
%if 0%{?runselftest}
# Note that this requires to have PostgreSQL properly configured;  for this
# reason the testsuite is turned off by default (see org/postgresql/test/README)
test_log=test.log
# TODO: more reliable testing
ant test 2>&1 | tee "$test_log" || :
( test -f "$test_log" && ! grep FAILED "$test_log" )

%endif


%files -f .mfiles
%doc LICENSE README.md doc/*
%{_javadir}/%{name}2.jar
%{_javadir}/%{name}2ee.jar
%{_javadir}/%{name}3.jar

%files javadoc
%doc LICENSE
%doc %{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.4.1200-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.4.1200-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.2.1002-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.2.1002-alt1_2jpp7
- new release

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:9.2.1002-alt1_1jpp7
- fc update

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:9.1.902-alt1_1jpp7
- new version

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:9.1.901-alt1_1jpp6
- update to new release by jppimport

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:9.0.801-alt1_1jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:8.3.604-alt1_1jpp5
- new jpackage release

* Fri Nov 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:8.1.407-alt1_2jpp1.7
- converted from JPackage by jppimport script

