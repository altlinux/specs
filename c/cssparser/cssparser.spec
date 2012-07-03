BuildRequires: maven-surefire-provider-junit maven-surefire-provider-junit4

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

%define gcj_support 0


Name:           cssparser
Version:        0.9.5
Release:        alt3_1jpp5
Epoch:          0
Summary:        CSS Parser
License:        LGPL
Url:            http://cssparser.sourceforge.net/
Group:          Development/Java
Source0:        %{name}-%{version}.tar.gz
# cvs -d:pserver:anonymous@cssparser.cvs.sourceforge.net:/cvsroot/cssparser login 
# cvs -z3 -d:pserver:anonymous@cssparser.cvs.sourceforge.net:/cvsroot/cssparser export -r CSSPARSER_0_9_5 cssparser

Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-changes
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven2-default-skin
BuildRequires: maven-surefire-plugin
BuildRequires: mojo-maven2-plugin-javacc

BuildRequires: sac

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

Requires: sac

BuildArch:      noarch
Source44: import.info
Patch33: cssparser-javacc.patch

%description
The CSS Parser is implemented as a package of Java classes,
that inputs Cascading Style Sheets Level 2 source text and
outputs a Document Object Model Level 2 Style tree.
Alternatively, applications can use SAC: The Simple API for
CSS. Its purpose is to allow developers working with Java to
incorporate Cascading Style Sheet information, primarily in
conjunction with XML application developments.

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
%setup -q -n %{name}
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

cp %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
%patch33 -p0

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2_SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Daggregate=true \
        install javadoc:javadoc site

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap net.sourceforge.cssparser %{name} %{version} JPP %{name}
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 target/%{name}-%{version}.jar \
           $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf target/site/apidocs
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

## manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp target/site/license.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/site $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_docdir}/%{name}-%{version}/license.html
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt3_1jpp5
- fixed build with javacc 5

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt2_1jpp5
- fixed build with javacc 5

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt2_1jpp5
- fixed build with new maven 2.0.8

* Mon Feb 09 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_1jpp5
- new version

