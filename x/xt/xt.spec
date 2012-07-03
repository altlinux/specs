Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

%define gcj_support        %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

Name:           xt
Version:        20051206
Release:        alt2_5jpp5
Epoch:          0
Summary:        Fast, free implementation of XSLT in Java
License:        BSD
Group:          Development/Java
Source0:        http://www.blnz.com/xt/xt-20051206-src.zip
Source1:        xt-build.xml
Patch0:         xt-20050823-build.patch
Patch1:         xt-java5-enum.patch
URL:            http://www.blnz.com/xt/index.html
Requires: servlet_2_3_api
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: servlet_2_3_api
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
%if 0
Obsoletes:      xt-dash < %{epoch}:%{version}-%{release}
Obsoletes:      xt-dash-demo <= %{epoch}:%{version}-%{release}
Provides:       xt-dash = %{epoch}:%{version}-%{release}
%endif

%description
XT is an implementation in Java of XSL Transformations.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
%if 0
Obsoletes:      xt-dash-javadoc < %{epoch}:%{version}-%{release}
Provides:       xt-dash-javadoc = %{epoch}:%{version}-%{release}
%endif
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%if 0
%package demo
Summary:        Demo for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Group:          Development/Java
%if 0
Obsoletes:      xt-dash-demo < %{epoch}:%{version}-%{release}
Provides:       xt-dash-demo = %{epoch}:%{version}-%{release}
%endif

%description demo
Demonstrations and samples for %{name}.
%endif

%prep
%setup -q
find . -name "*.jar" | xargs -t %{__rm}
%patch0 -p1
%patch1 -p1
%{__cp} -a %{SOURCE1} build.xml
%{__rm} -r docs thirdparty
%{__perl} -pi -e 's/\r$//g' *.txt *.html

%build
export CLASSPATH=$(build-classpath servlet_2_3_api xerces-j2 xml-commons-jaxp-1.3-apis)
export OPT_JAR_LIST=:
%{ant} jar javadoc

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -a build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%if 0
(cd %{buildroot}%{_javadir} && %{__ln_s} %{name}-%{version}.jar %{name}-dash-%{version}.jar)
%endif
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -a build/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if 0
# data
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__cp} -a demo %{buildroot}%{_datadir}/%{name}
%endif

%files
%doc *.txt *.html
%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if 0
%files demo
%{_datadir}/%{name}
%endif

%changelog
* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:20051206-alt2_5jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:20051206-alt1_5jpp5
- converted from JPackage by jppimport script

