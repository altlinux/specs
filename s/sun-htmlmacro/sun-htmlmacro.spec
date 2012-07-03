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

%define bname   htmlmacro
%define svnrel  r27

Name:           sun-htmlmacro
Summary:        Macro engine for generating HTML documents
Url:            https://htmlmacro.dev.java.net/
Version:        1.0
Release:        alt4_0.r27.2jpp6
Epoch:          0
License:        CDDL
Group:          Development/Java
BuildArch:      noarch
Source0:        sun-htmlmacro-1.0-%{svnrel}.tar.gz
# svn export -r 27 https://htmlmacro.dev.java.net/svn/htmlmacro/trunk sun-htmlmacro-1.0-r27 --username guest
Patch0:         sun-htmlmacro-build.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7
BuildRequires:  dom4j
BuildRequires:  jakarta-commons-beanutils
BuildRequires:  jakarta-commons-jelly
BuildRequires:  jakarta-commons-jelly-tags-define
BuildRequires:  jakarta-commons-jelly-tags-xml
BuildRequires:  jakarta-commons-jexl
BuildRequires:  jakarta-commons-logging
BuildRequires:  jaxen
BuildRequires:  nekohtml
Requires:       ant >= 0:1.7
Requires:       dom4j
Requires:       jakarta-commons-beanutils
Requires:       jakarta-commons-jelly
Requires:       jakarta-commons-jelly-tags-define
Requires:       jakarta-commons-jelly-tags-xml
Requires:       jakarta-commons-jexl
Requires:       jakarta-commons-logging
Requires:       jaxen
Requires:       nekohtml
Source44: import.info

%description
Writing a serious, consistent, nice-looking documents in HTML
is hard. CSS improves the situation a bit, but it's still 
very painful. For example, suppose if you are writing a 
release note like this, and you want to do:
1. Generate the navigation bar in multiple pages
2. Have the same footer for all documents 
This project believes that a part of the problem is the lack
of "programmability" in HTML. For example, if you can define
your own <footer/> tag (just like you define a JSP tag), then
it becomes very easy to guarantee the consistent footer.
HTMLMacro lets you do just that. When you write HTML, 
it lets you define and use macros. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
%{summary}.

%prep
%setup -q -n %{name}-%{version}-%{svnrel}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0

#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/ant.jar.no
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/args4j-2.0.1.jar.no
### ln -sf $(build-classpath args4j) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/commons-beanutils-1.6.jar.no
ln -sf $(build-classpath commons-beanutils) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/commons-collections-2.1.jar.no
### ln -sf $(build-classpath commons-collections) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/commons-jelly-1.0.jar.no
ln -sf $(build-classpath commons-jelly) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/commons-jelly-tags-define-1.0.jar.no
ln -sf $(build-classpath jelly-tags/commons-jelly-tags-define) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/commons-jelly-tags-xml-1.1.jar.no
ln -sf $(build-classpath jelly-tags/commons-jelly-tags-xml) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/commons-jexl-1.0.jar.no
ln -sf $(build-classpath commons-jexl) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/commons-lang-2.0.jar.no
### ln -sf $(build-classpath commons-lang) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/commons-logging-1.0.3.jar.no
ln -sf $(build-classpath commons-logging) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/dom4j.jar.no
ln -sf $(build-classpath dom4j) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/jaxen-1.1-beta-4.jar.no
ln -sf $(build-classpath jaxen) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/nekohtml.jar.no
ln -sf $(build-classpath nekohtml) htmlmacro/lib/
#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/soimp-1.0.jar.no

#BUILD/sun-htmlmacro-1.0-r27/htmlmacro/lib/xercesImpl.jar.no
### ln -sf $(build-classpath xerces-j2) htmlmacro/lib/


%build
cd %{bname}
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first dist doc javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{bname}/build/%{bname}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr %{bname}/build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr %{bname}/build/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr %{bname}/examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%files
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.r27.2jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.r27.1jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.r27.1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.r27.1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.r27.1jpp5
- converted from JPackage by jppimport script

