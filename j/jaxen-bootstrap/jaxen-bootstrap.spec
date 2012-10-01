BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define real       jaxen
%define dom4jver   1.6.1

Name:           %{real}-bootstrap
Version:        1.1
Release:        alt1_6.2jpp7
Epoch:          0
Summary:        A convenience package for build of dom4j
License:        BSD
Url:            http://jaxen.codehaus.org/
Group:          Development/Java
Source0:        http://dist.codehaus.org/jaxen/distributions/jaxen-1.1-src.tar.gz
# dom4j is needed for bootstrapping; we build a subset of it below.
Source1:        http://prdownloads.sourceforge.net/dom4j/dom4j-%{dom4jver}.tar.gz

# Don't build or run the tests.  This limits dependencies.
Patch0:         %{name}-notest.patch

Requires:       jdom >= 0:1.0-0.rc1.1jpp
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       xom
BuildRequires:  ant >= 0:1.6 jpackage-utils >= 0:1.6 junit
BuildRequires:  jdom >= 0:1.0-0.rc1.1jpp
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xom
BuildArch:      noarch
Source44: import.info

%description
Dom4j depends on a jaxen build with dom4j support.
This package must only be installed in the rare
event of having to rebuild dom4j.

%prep
%setup -q -n %{real}-%{version}
%patch0
gzip -dc %{SOURCE1} | tar -xf -
find . -name "*.jar" -exec rm -f {} \;

%build
export CLASSPATH=$(build-classpath \
jdom \
xalan-j2 \
xerces-j2 \
xom \
)
pushd dom4j-%{dom4jver}/src/java
javac -sourcepath ../../../src/java/main:. \
        org/dom4j/Attribute.java \
        org/dom4j/Branch.java \
        org/dom4j/CDATA.java \
        org/dom4j/Comment.java \
        org/dom4j/Document.java \
        org/dom4j/DocumentException.java \
        org/dom4j/Element.java \
        org/dom4j/Namespace.java \
        org/dom4j/Node.java \
        org/dom4j/ProcessingInstruction.java \
        org/dom4j/Text.java \
        org/dom4j/io/SAXReader.java

jar cf ../../dom4j.jar $(find . -name "*.class")
popd

export CLASSPATH=$(build-classpath \
jdom \
xalan-j2 \
xerces-j2 \
xom \
):`pwd`/dom4j-%{dom4jver}/dom4j.jar

ant -Dnoget=true

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{real}-%{version}.jar \
$RPM_BUILD_ROOT%{_javadir}

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in %{real}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

%files
%doc LICENSE.txt
%{_javadir}/*

%changelog
* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_6.2jpp7
- new version

