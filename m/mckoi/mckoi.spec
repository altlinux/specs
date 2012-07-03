Packager: Igor Vlasenko <viy@altlinux.ru>
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


Name:		mckoi
Version:	1.0.3
Release:	alt2_1jpp5
Epoch:		0
Summary:	An Open Source Java SQL Database System
License:	GPL
Url:		http://www.mckoi.com/database/
Group:		Development/Java
Source0:	http://www.mckoi.com/database/ver/mckoi1.0.3.zip
Source1:	mckoi-build.xml
Source2:	%{name}-%{version}.pom

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 1.6.5
BuildRequires: junit >= 3.8.1
BuildRequires: gnu-regexp
BuildRequires: jakarta-commons-logging
BuildRequires: jboss4-common
BuildRequires: jboss4-jmx
BuildRequires: jboss4-system
Requires: gnu-regexp
Requires: jakarta-commons-logging
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

BuildArch:	noarch

%description
Mckoi SQL Database is an SQL (Structured Query Language) 
Database management system written for the JavaTM platform.
Mckoi SQL Database is optimized to run as a client/server 
database server for multiple clients, however it can also 
be embedded in an application as a stand-alone database. 
It is highly multi-threaded and features an extendable 
object-oriented engine.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}%{version}
cp %{SOURCE1} build.xml
unzip -q src.zip
for f in $(find . -name "*.jar" -o -name "*.zip"); do
    mv $f $f.no
done
mkdir lib
ln -sf $(build-classpath commons-logging) lib
ln -sf $(build-classpath gnu-regexp) lib
ln -sf $(build-classpath jboss4/jboss-common) lib
ln -sf $(build-classpath jboss4/jboss-jmx) lib
ln -sf $(build-classpath jboss4/jboss-system) lib


%build
ant jar jdoc

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 output/dist/lib/mckoidb-%{version}.jar \
		$RPM_BUILD_ROOT%{_javadir}/mckoidb-%{version}.jar
install -m 644 output/dist/lib/mkjdbc-%{version}.jar \
		$RPM_BUILD_ROOT%{_javadir}/mkjdbc-%{version}.jar

# create unprefixed and unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done
)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr contrib $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr test $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
find $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version} -name "*.bat" -exec rm {} \;

%files
%doc %{_docdir}/%{name}-%{version}/*
%dir %{_docdir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt2_1jpp5
- selected java5 compiler explicitly

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt1_1jpp5
- new version

