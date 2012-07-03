AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2010, JPackage Project
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

Name:           h2database
Version:        1.2.145
Release:        alt3_2jpp6
Epoch:          0
Summary:        Java SQL database
Group:          Development/Java
License:        MPL/EPL
URL:            http://www.h2database.com/html/main.html
# svn export http://h2database.googlecode.com/svn/tags/version-1.2.145/h2/ h2database-1.2.145
# tar cjf h2database-1.2.145.tar.bz2 h2database-1.2.145/
# Exported revision 3108.
Source0:        h2database-1.2.145.tar.bz2
Patch0:         h2database-build.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: felix-osgi-core
Requires: jpackage-utils >= 0:1.7.3
Requires: lucene
Requires: servlet_2_5_api
Requires: slf4j
BuildRequires: ant >= 1.7
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: servlet_2_5_api
BuildRequires: lucene
BuildRequires: slf4j >= 0:1.6.1
BuildRequires: felix-osgi-core >= 0:1.2.0
BuildArch:      noarch
Source44: import.info
Source45: h2.jar-OSGi-MANIFEST.MF

%description
Welcome to H2, the Java SQL database. The main features of 
H2 are:
* Very fast, open source, JDBC API
* Embedded and server modes; in-memory databases
* Browser based Console application
* Small footprint: around 1 MB jar file size 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
%patch0 -p0 -b .sav0
# XXX: allows easy servlet upgrade
rm src/test/org/h2/test/unit/TestServlet.java
%{__perl} -p -e 's/\@version\@/%{version}/g;' src/installer/pom-template.xml > %{name}-%{version}.pom

%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

mkdir ext
%{__ln_s} $(build-classpath servlet_2_5_api) ext/servlet-api-2.4.jar
%{__ln_s} $(build-classpath lucene) ext/lucene-core-2.2.0.jar
%{__ln_s} $(build-classpath slf4j/slf4j-api) ext/slf4j-api-1.5.0.jar
%{__ln_s} $(build-classpath felix/org.osgi.core) ext/org.osgi.core-1.2.0.jar

%build
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all javadoc

%install
%__rm -rf %{buildroot}

# jar
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p bin/h2.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# pom
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%{__cp} -p %{name}-%{version}.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.h2database h2 %{version} JPP %{name}

%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# inject OSGi manifest h2.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/h2database.jar META-INF/MANIFEST.MF
# end inject OSGi manifest h2.jar-OSGi-MANIFEST.MF

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.145-alt3_2jpp6
- built with java 6 due to abstract getParentLogger

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.145-alt2_2jpp6
- added OSGi manifest

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.145-alt1_2jpp6
- new version

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.119-alt1_1jpp6
- new version

