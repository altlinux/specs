BuildRequires: felix-osgi-obr felix-framework
BuildRequires: /proc
BuildRequires: jpackage-compat
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

Name:           bindex
Version:        2.2
Release:        alt3_1jpp6
Summary:        BIndex

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://www.osgi.org/Repository/BIndex

Source0:        bindex.tgz
# svn export http://www.osgi.org/svn/public/trunk/org.osgi.impl.bundle.bindex/ bindex
# tar czf bindex.tgz bindex


BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 1.7
BuildRequires:  aqute-bndlib
BuildRequires:  junit
BuildRequires:  kxml2

Requires:  jpackage-utils >= 0:1.7.5

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
The BIndex program is a small Java progam that implements 
the manifest header to repository format mapping as 
described in RFC-0112 Bundle Repository. BIndex can recurse
over a directory structure and just creates a repository.xml
file. The URLs can be rewritten using a template. 

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath ant) jar/ant.jar
ln -sf $(build-classpath kxml2-min) jar/kxml2-min.jar
ln -sf $(build-classpath felix/org.osgi.service.obr) jar/org.osgi.service.obr.jar

%build
export CLASSPATH=$(build-classpath \
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
felix/org.apache.felix.framework \
felix/org.osgi.service.obr \
junit \
kxml2-min \
)
mkdir bin
javac -d bin $(find src -name "*.java")
java -jar /usr/share/java/aqute-bndlib.jar -exceptions build  bindex.bnd
mkdir apidocs
javadoc -source 1.4 -d apidocs -sourcepath src org org.osgi.impl.bundle.obr.resource org.osgi.impl.bundle.bindex org.osgi.impl.bundle.bindex.ant

%install
%__rm -rf %{buildroot}

# jar
%__install -d -m 755 %{buildroot}%{_javadir}
%__install -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

%__install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_1jpp6
- dropped felix dependency

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_1jpp6
- added felix-osgi-obr dep

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_1jpp6
- new version

