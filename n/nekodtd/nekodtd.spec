Packager: Igor Vlasenko <viy@altlinux.ru>
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


Name:           nekodtd
Version:        0.1.11
Release:        alt3_2jpp5
Epoch:          0
Summary:        CyberNeko DTD Converter
License:        Apache-style
URL:            http://people.apache.org/~andyc/neko/doc/dtd/
Group:          Development/Java
Source0:        nekodtd-0.1.11.tar.gz
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: xerces-j2-demo
BuildRequires: xml-commons-apis

Requires: xerces-j2
Requires: xml-commons-apis
BuildArch:      noarch

%description
NekoDTD is a configuration that parses Document Type Definition 
(DTD) files and converts the information into an XML document. 
This representation can then be processed using standard XML 
processors and applications to perform grammar analysis, convert 
the DTD into other grammar formats, etc. For example, using an 
XSLT stylesheet, the XML representation of the DTD can be 
converted to an equivalent XML Schema or Relax NG grammar. 
The NekoDTD parser configuration is written using the Xerces 
Native Interface (XNI) that is the foundation of the Xerces2 
implementation. This enables you to use NekoDTD with existing 
XNI tools without modification or rewriting code. 



%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description manual
%{summary}.

%prep
%setup -q -n %{name}-%{version}
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
mkdir lib
(cd lib
ln -sf $(build-classpath ant)
ln -sf /usr/share/xerces-j2/xerces-j2-samples.jar
)

ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -f build-dtd.xml package

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 %{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/dtd/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}


rm -rf doc/dtd/javadoc

# docs
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/dtd/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 LICENSE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_docdir}/%{name}-%{version}/LICENSE
%{_javadir}/*.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.1.11-alt3_2jpp5
- fixed repocop warnings

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.11-alt2_2jpp5
- fixed build with java 5

* Wed Feb 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.11-alt1_2jpp1.7
- converted from JPackage by jppimport script

