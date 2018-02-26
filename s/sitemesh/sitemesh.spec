Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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

%define gcj_support 0


Name:           sitemesh
Version:        2.4.1
Release:        alt2_1jpp5
Epoch:          0
Summary:        A web-page layout and decoration framework
License:        OpenSymphony Software License
Url:            http://www.opensymphony.com/sitemesh/
Group:          Development/Java
Source0: %{name}-%{version}.zip
Source1: %{name}-%{version}.pom
Patch0:  sitemesh-2.4.1-build.patch
Patch1:  sitemesh-2.4.1-lexer_flex.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
BuildRequires: java-cup
BuildRequires: jflex
BuildRequires: freemarker
BuildRequires: hivemind
BuildRequires: jakarta-commons-collections
BuildRequires: jsp_api >= 0:1.2
BuildRequires: servlet_api >= 0:2.3
BuildRequires: tapestry
BuildRequires: velocity
BuildRequires: velocity-tools
#BuildRequires:  xerces-j2
#BuildRequires:  xml-commons-apis
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires: freemarker
Requires: hivemind
Requires: jsp_api >= 0:1.2
Requires: servlet_api >= 0:2.3
Requires: tapestry
Requires: velocity
Requires: velocity-tools
#Requires:       jaxp_parser_impl
#Requires:       xml-commons-apis
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description 
SiteMesh is a web-page layout and decoration framework and web-
application integration framework to aid in creating large sites
consisting of many pages for which a consistent look/feel, navigation
and layout scheme is required.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Documents for %{name}.

%prep
%setup -q -c -n %{name}
# Remove the jars that shipped with it to replace with jpackage jars
for j in $(find . -name "*.jar"); do
       mv $j $j.no
done
%patch0 -b .sav0
%patch1 -b .sav1

build-jar-repository -p lib/ \
commons-collections \
freemarker \
hivemind \
java-cup \
jflex \
junit \
jsp_api \
servlet_api \
tapestry/tapestry \
velocity \
velocity-tools \
#xerces-j2 \
#xml-commons-apis

%build
export LANG=en_US.ISO8859-1

ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar test javadocs

%install

# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/sitemesh-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%add_to_maven_depmap opensymphony %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 README.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/README.txt
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_1jpp5
- fixed build with java 7

* Sun Mar 07 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_1jpp5
- new version

* Mon Feb 23 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_1jpp5
- fixed build

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_1jpp5
- fixed build w/jflex

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1jpp5.0
- converted from JPackage by jppimport script

