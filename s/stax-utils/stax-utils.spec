BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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

%define tstamp  20070216

Name:           stax-utils
Version:        0.0
Release:        alt1_0.20070216.3jpp6
Epoch:          0
Summary:        STAX Utilities
Group:          Development/Java
License:        BSD
URL:            https://stax-utils.dev.java.net/
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs login
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -D 20070216 stax-utils && tar cjf stax-utils-0.0-cvs20070216.tar.bz2 stax-utils/
Source0:        %{name}-%{version}-cvs%{tstamp}.tar.bz2
Patch0:         stax-utils-build_xml.patch
Patch1:         stax-utils-XMLEventConsumerDelegate.patch
Requires:  bea-stax-api
Requires:  bea-stax
BuildRequires:  ant >= 0:1.7
BuildRequires:  ant-junit
BuildRequires:  ant-trax
BuildRequires:  bea-stax-api
BuildRequires:  bea-stax
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  junit
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info
Patch33: stax-utils-0.0-javadoc-exclude.patch

%description
The purpose of this project is to help facilitate the adoption 
of JSR-173: Streaming API for XML (StAX) by providing a set of 
utility classes that make it easy for developers to integrate 
StAX into their existing XML processing applications.

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

%prep
%setup -q -n %{name}
find . -type f -name "*.jar" | xargs -t rm
%patch0 -p0
%patch1 -p0

pushd lib
#jsr173_1.0_api.jar.no
ln -s $(build-classpath bea-stax-api)
#jsr173_1.0_ri.jar.no
ln -s $(build-classpath bea-stax-ri)
#junit.jar.no
ln -s $(build-classpath junit)
popd
%patch33 -p1

%build
export CLASSPATH=
export OPT_JAR_LIST="`cat %{_sysconfdir}/ant.d/{junit,trax}`"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all test

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 build/stax-utils.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadocs
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/sax/ $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc docs/COPYRIGHT.TXT
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.20070216.3jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.20070216.1jpp5
- new jpackage release

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.20060502.1jpp1.7
- new version

* Wed Oct 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.20050302.3jpp1.7
- converted from JPackage by jppimport script

