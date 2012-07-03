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

Name:           jxhtmledit
Version:        4.0.005
Release:        alt2_1jpp6
Summary:        Browser-based HTML/XHTML content authoring tool

Group:          Development/Java
License:        LGPL
URL:            http://jxhtmledit.sourceforge.net

Source0:        jxhtmledit-4.0.005.tgz
Source1:        jxhtmledit-build.xml
Source2:        jxhtmledit-4.0.005.pom

BuildRequires: ant >= 1.6.5
BuildRequires: junit
BuildRequires: java-plugin
BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: htmlcolors
BuildRequires: htmlentities
BuildRequires: htmlstrings
BuildRequires: htmlurls
BuildRequires: tmxjavabridge
BuildRequires: xhtmltranscoder
BuildRequires: xmlconfigreader


Requires: jpackage-utils >= 0:5.0.0
Requires: htmlcolors
Requires: htmlentities
Requires: htmlstrings
Requires: htmlurls
Requires: tmxjavabridge
Requires: xhtmltranscoder
Requires: xmlconfigreader

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
JXHTMLEdit is a cross-platform WYSIWYG (What You See Is What
You Get) HTML/XHTML content authoring tool, a very small 
Java Applet based on the Java 2 Platform. JXHTMLEdit provides 
word processor-like user interface that allows users to edit
the XHTML document directly in the final form (as will be 
rendered). This empower non-technical users to become content 
contributors without any knowledge of HTML or XHTML.
Specifically designed and optimized to edit only the <body>
portion of HTML/XHTML page, JXHTMLEdit outputs to your choice
HTML or well-formed XHTML.
JXHTMLEDIT preloads the HTML/XHTML content during startup from 
a specified html form field (e.g.: <textarea>) where it also 
saves the generated code.
JXHTMLEdit has been designed to offer great flexibility and
could be used to easily integrate WYSIWYG authoring 
functionality into existing websites, CMS, WMS or any other 
Web-based software. The Applet JAR archive is less than 150 KB 
and it's cacheable, so it loads very quickly.

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
export CLASSPATH=$(build-classpath \
htmlcolors \
htmlentities \
htmlstrings \
htmlurls \
tmxjavabridge \
xhtmltranscoder \
xmlconfigreader \
):/usr/lib/jvm/java/jre/lib/plugin.jar:/usr/share/icedtea-web/plugin.jar
%ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
	-Dbuild.sysclasspath=first \
	-Djunit.jar=$(build-classpath junit) \
	-Dtmxjavabridge.jar=$(build-classpath tmxjavabridge) \
	-Dxhtmltranscoder.jar=$(build-classpath xhtmltranscoder) \
	-Dxmlconfigreader.jar=$(build-classpath xmlconfigreader) \
	-Dhtmlcolors.jar=$(build-classpath htmlcolors) \
	-Dhtmlentities.jar=$(build-classpath htmlentities) \
	-Dhtmlstrings.jar=$(build-classpath htmlstrings) \
	-Dhtmlurls.jar=$(build-classpath htmlurls) \
	jar test javadoc

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
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.005-alt2_1jpp6
- fixed build with java 7

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 4.0.005-alt1_1jpp6
- new version

