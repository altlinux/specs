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


Name:           de-java2html
Version:        5.0
Release:	alt2_1jpp6
Epoch:          0
Summary:        Java to Html converter
Group:          Development/Java
License:        GPL or CPL1.0
URL:            http://www.java2html.de
Source0:        http://www.java2html.de/java2html_50.zip

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant
BuildRequires: junit
BuildRequires: jdemo
BuildRequires: jspwiki
Requires: jdemo
Requires: jspwiki
BuildArch:      noarch
Source44: import.info

%description
Java2Html converts Java (and other) source code (complete
files or snippets) to HTML, RTF, TeX and XHTML with syntax
highlighting.
This open source Java project consists of an extendible 
library along with a Java application, a Java applet and
many plugins in order to integrate the library into other
programs.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep 
%setup -q -c
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
export LANG=en_US.ISO8859-1
mkdir src
pushd src
   unzip ../java2html_src.zip
popd
export CLASSPATH=$(build-classpath ant jdemo junit jspwiki)
mkdir classes
javac -d classes $(find src -name "*.java")
pushd classes
jar cf ../%{name}.jar *
popd
javadoc -d apidocs $(find src -name "*.java")

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}

install -m 644 %{name}.jar \
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
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt2_1jpp6
- fixed build with java 7

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_1jpp6
- new version

