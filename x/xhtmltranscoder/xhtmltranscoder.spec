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

Name:           xhtmltranscoder
Version:        1.0.007
Release:        alt1_1jpp6
Summary:        Convert broken HTML to XHTML

Group:          Development/Java
License:        LGPL
URL:            http://xhtmltranscoder.sourceforge.net

Source0:        xhtmltranscoder_1_0_007.zip
Source1:        xhtmltranscoder-build.xml
Source2:        xhtmltranscoder-1.0.007.pom

BuildRequires: ant >= 1.6.5
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: htmlentities
BuildRequires: htmlstrings
BuildRequires: xmlconfigreader


Requires: jpackage-utils >= 0:5.0.0
Requires: htmlentities
Requires: htmlstrings
Requires: xmlconfigreader

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
XHTMLTranscoder is an Open Source Java class that quickly 
converts broken HTML code to well-formed XHTML.
XHTMLTranscoder is a fast transcoder useful to convert HTML
code in real-time.
This class do not check headers, it checks only the general
rules for tags, attributes and nesting:
* tags (elements) names in lowercase (eg: <ACRONYM> become 
  <acronym>);
* attributes names in lowercase (eg: <acronym TITLE="example">
  become <acronym title="example">);
* unquoted attributes (eg: <acronym title=example> become 
  <acronym title="example">);
* elements nesting (eg: <b><i>hello</b></i> become 
  <b><i>hello</i></b>);
* elements termination (eg: <p>hello world ... become 
  <p>hello world ...</p>);
* unminimized attributes (eg: <input type="checkbox" checkedu/>s
   become <input type="checkbox" checked="checked" />);
* unterminated empty tags (eg: <br> become <br />);
* preserve other languages elements (php, asp, jsp, ...)
The HTML documents transcoded using the XHTMLTranscoder 
class are generally recognized as valid XHTML document by 
the W3C Markup Validation Service.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
cp %{SOURCE1} build.xml

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath \
xmlconfigreader \
htmlentities \
htmlstrings \
)
LANG=en_US.iso88591
%ant -Dbuild.sysclasspath=first -Djunit.jar=$(build-classpath junit) jar test javadoc

%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}
%__install -m 644 build/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

%__install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%__install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.tecnick.htmlutils %{name} %{version} JPP %{name}

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a build/javadoc %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%doc *.TXT
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.007-alt1_1jpp6
- new version

