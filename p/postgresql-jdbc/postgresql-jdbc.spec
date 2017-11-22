Epoch: 0
Group: Databases
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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


# Configuration for rpmbuild, might be specified by options
# like e.g. 'rpmbuild --define "runselftest 0"'.

%{!?runselftest:%global runselftest 0}


%global section		devel
%global source_path	pgjdbc/src/main/java/org/postgresql
%global parent_ver	1.1.2
%global parent_poms_builddir	./pgjdbc-parent-poms

%global pgjdbc_mvn_options -DwaffleEnabled=false -DosgiEnabled=false \\\
	-DexcludePackageNames=org.postgresql.osgi:org.postgresql.sspi

Summary:	JDBC driver for PostgreSQL
Name:		postgresql-jdbc
Version:	42.1.4
Release:	alt1_1jpp8
License:	BSD
URL:		http://jdbc.postgresql.org/

Source0:	https://github.com/pgjdbc/pgjdbc/archive/REL%version.tar.gz

# Upstream moved parent pom.xml into separate project (even though there is only
# one dependant project on it?).  Let's try to not complicate packaging by
# having separate spec file for it, too.
Source1:	https://github.com/pgjdbc/pgjdbc-parent-poms/archive/REL%parent_ver.tar.gz

# disable test that makes unpredictable assumptions about non-routable IPs
# See https://github.com/pgjdbc/pgjdbc/issues/556
Patch0:         disable-ConnectTimeoutTest.patch

BuildArch:	noarch
BuildRequires:	java-devel >= 1.8
BuildRequires:	maven-local
BuildRequires:	java-comment-preprocessor
BuildRequires:	properties-maven-plugin
BuildRequires:	maven-enforcer-plugin
BuildRequires:	maven-plugin-bundle
BuildRequires:	maven-plugin-build-helper
BuildRequires:	classloader-leak-test-framework

%if %runselftest
BuildRequires:	postgresql10-contrib postgresql10-server
BuildRequires:	libecpg-devel libpq-devel postgresql-devel
BuildRequires:	postgresql10-contrib postgresql10-server
%endif
Source44: import.info

# gettext is only needed if we try to update translations
#BuildRequires:	gettext

%description
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-jdbc package includes the .jar files needed for
Java programs to access a PostgreSQL database.


%package	parent-poms
Group: Databases
Summary:	Build dependency management for PostgreSQL JDBC driver.

%description parent-poms
Pom files bringing dependencies required for successful PostgreSQL JDBC driver
build.


%package javadoc
Group: Development/Java
Summary:	API docs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API Documentation for %{name}.


%prep
%setup -c -q -a 1 -n pgjdbc-REL%version

mv pgjdbc-REL%version/* .
mv pgjdbc-parent-poms-REL%parent_ver pgjdbc-parent-poms

%patch0 -p1

# remove any binary libs
find -name "*.jar" -or -name "*.class" | xargs rm -f

%pom_disable_module ubenchmark

# Build parent POMs in the same Maven call.
%pom_xpath_inject pom:modules "<module>%parent_poms_builddir</module>"
%pom_xpath_inject pom:parent "<relativePath>pgjdbc-parent-poms/pgjdbc-versions</relativePath>"
%pom_xpath_set pom:relativePath ../pgjdbc-parent-poms/pgjdbc-core-parent pgjdbc

# compat symlink: requested by dtardon (libreoffice), reverts part of
# 0af97ce32de877 commit.
%mvn_file org.postgresql:postgresql %{name}/postgresql %{name}

# Parent POMs should be installed in a separate subpackage.
%mvn_package ":*{parent,versions,prevjre}*" parent-poms

# For compat reasons, make Maven artifact available under older coordinates.
%mvn_alias org.postgresql:postgresql postgresql:postgresql

# Hack #1!  This directory is missing for some reason, it is most probably some
# misunderstanding between maven, maven-compiler-plugin and
# java-comment-preprocessor?  Not solved yet.  See rhbz#1325060.
mkdir -p pgjdbc/target/generated-sources/annotations


%build
# Ideally we would run "sh update-translations.sh" here, but that results
# in inserting the build timestamp into the generated messages_*.class
# files, which makes rpmdiff complain about multilib conflicts if the
# different platforms don't build in the same minute.  For now, rely on
# upstream to have updated the translations files before packaging.

# Include PostgreSQL testing methods and variables.
%if %runselftest
%pgtests_init

PGTESTS_LOCALE=C.UTF-8

cat <<EOF > build.local.properties
server=localhost
port=$PGTESTS_PORT
database=test
username=test
password=test
privilegedUser=$PGTESTS_ADMIN
privilegedPassword=$PGTESTS_ADMINPASS
preparethreshold=5
loglevel=0
protocolVersion=0
EOF

# Start the local PG cluster.
%pgtests_start
%else
# -f is equal to -Dmaven.test.skip=true
opts="-f"
%endif

%mvn_build $opts -- %pgjdbc_mvn_options


%install
%mvn_install


%files -f .mfiles
%doc LICENSE
%doc README.md


%files parent-poms -f .mfiles-parent-poms
%doc LICENSE
%doc pgjdbc-parent-poms/CHANGELOG.md pgjdbc-parent-poms/README.md


%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:42.1.4-alt1_1jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:9.4.1212-alt1_4jpp8
- new version

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

