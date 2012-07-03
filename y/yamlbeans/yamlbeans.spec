Packager: Igor Vlasenko <viy@altlinux.ru>
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

Name:           yamlbeans
Version:        1.0
Release:        alt1_1jpp6
Summary:        yamlBeans

Group:          Development/Java
License:        BSD
URL:            http://code.google.com/p/yamlbeans/

Source0:        yamlbeans.tgz
# svn export http://yamlbeans.svn.sourceforge.net/svnroot/yamlbeans
# tar czf yamlbeans.tgz yamlbeans/


BuildRequires: jpackage-utils >= 0:1.7.5

Requires: jpackage-utils >= 0:1.7.5

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
YamlBeans makes it easy to serialize and deserialize Java 
object graphs to and from YAML, a human-friendly data format.
Replace XML and properties files with YAML for more 
expressive power (lists, maps, anchors, etc) and easier 
hand-editing. 

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

%build
mkdir bin
%{java_home}/bin/javac -d bin $(find src -name "*.java")
pushd bin
%{java_home}/bin/jar cf ../%{name}.jar *
popd
mkdir apidocs
%{java_home}/bin/javadoc -d apidocs -sourcepath src net.sourceforge.yamlbeans net.sourceforge.yamlbeans.emitter net.sourceforge.yamlbeans.parser net.sourceforge.yamlbeans.scalar net.sourceforge.yamlbeans.tokenizer

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
* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1jpp6
- new version

