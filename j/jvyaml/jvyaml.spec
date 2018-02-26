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


Name:           jvyaml
Version:        0.2.1
Release:        alt1_1jpp6
Epoch:          0
Summary:        Java YAML 1.1 parser and emitter
Group:          Development/Java
License:        MIT
URL:            https://jvyaml.dev.java.net/
Source0:        https://jvyaml.dev.java.net/files/documents/5215/41455/jvyaml-src-0.2.1.tar.gz

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
BuildRequires: junit
BuildArch:      noarch
Source44: import.info

%description
JvYAML originated in the JRuby project
(http://jruby.sourceforge.net), from the base of RbYAML
(http://rbyaml.rubyforge.org). For a long time Java have
lacked a good YAML loader and dumper with all the features
that the SYCK using scripting communities have gotten used
to. JvYAML aims to rectify this.
JvYAML is a complete YAML processor with support for both
loading and dumping YAML.
Of major importance is that JvYAML works the same way as
SYCK, so that JRuby can rely on YAML parsing and emitting
that mirrors C Ruby.
JvYAML is a quite clean port of RbYAML, which was a port
from Python code written by Kirill Simonov
<xi@resolvent.net> for PyYAML3000.
The JvYAML project is created and maintained by
Ola Bini <ola@ologix.com>

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep 
%setup -q 

%build
ant 
javadoc -d apidocs $(find src -name "*.java")

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}

install -m 644 lib/%{name}.jar \
           %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
ln -s ${jar} ${jar/-%{version}/}; done)

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.2.1-alt1_1jpp6
- new version

