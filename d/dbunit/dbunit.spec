BuildRequires: maven-plugin-cobertura velocity14
BuildRequires: /proc
BuildRequires: jpackage-compat
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

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'


Name:           dbunit
Summary:        DBUnit extension for JUnit
Url:            http://dbunit.sourceforge.net/
Version:        2.4.2
Release:        alt1_1jpp6
Epoch:          0
License:        LGPL
Group:          Development/Java
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz
# svn export http://dbunit.svn.sourceforge.net/svnroot/dbunit/tags/release-2.4.2/ dbunit-2.4.2

Source1:        dbunit-settings.xml
Source2:        dbunit-2.4.2-jpp-depmap.xml
Patch0:         dbunit-pom.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  junit-addons
BuildRequires:  derby
BuildRequires:  gsbase
BuildRequires:  hsqldb
BuildRequires:  mockmaker
BuildRequires:  mockobjects >= 0:0.09-17
BuildRequires:  mockobjects-jdk1.4 >= 0:0.09-17
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-skins
BuildRequires:  maven2-plugin-ant
BuildRequires:  maven2-plugin-changelog
BuildRequires:  maven2-plugin-changes
BuildRequires:  maven2-plugin-checkstyle
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-project-info-reports
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-site
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-surefire-report-plugin
BuildRequires:  maven-release
BuildRequires:  maven-jxr
BuildRequires:  maven-plugin-cobertura
BuildRequires:  mojo-maven2-plugin-jdepend
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-lang
BuildRequires:  apache-poi
BuildRequires:  slf4j
Requires:  ant
Requires:  junit
Requires:  junit-addons
Requires:  apache-commons-collections
Requires:  apache-commons-lang
Requires:  apache-poi
Requires:  slf4j
Source44: import.info

%description
DbUnit is a JUnit extension (also usable with Ant) targeted 
for database-driven projects that, among other things, puts 
your database into a known state between test runs. This is 
an excellent way to avoid the myriad of problems that can 
occur when one test case corrupts the database and causes 
subsequent tests to fail or exacerbate the damage. 
DbUnit has the ability to export and import your database 
data to and from XML datasets. Since version 2.0, DbUnit can 
works with very large dataset when use in streaming mode. 
DbUnit can also helps you to verify that your database data 
match expected set of values. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q 
chmod -R go=u-w *

cp %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml

%patch0 -b .sav0
#%patch1 -b .sav1

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2_SETTINGS=$(pwd)/settings.xml

mvn-jpp \
        -e \
        -s $M2_SETTINGS \
        -Dmaven.test.failure.ignore=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc #site


%install
%__rm -rf %{buildroot}

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.dbunit %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# manual
rm -rf target/site/apidocs
#cp -pr target/site $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

#files manual
#%{_docdir}/%{name}-%{version}/site
## hack; explicitly added docdir if not owned
#%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4.2-alt1_1jpp6
- new jpp6 release

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt4_2jpp5
- fixed build; built w/o maven

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt3_2jpp5
- explicit selection of java5 compiler

* Wed May 20 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt2_2jpp5
- fixed build

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt1_2jpp5
- new version

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_4jpp1.7
- build with maven

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

