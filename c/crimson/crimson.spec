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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           crimson
Version:        1.1.3
Release:	alt1_19jpp6
Epoch:          0
Summary:        Java XML parser
Group:          Development/Java
License:        ASL 1.1
URL:            http://xml.apache.org/crimson/
Source0:        http://xml.apache.org/dist/%{name}/%{name}-%{version}-src.tar.gz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/crimson/crimson/1.1.3/crimson-1.1.3.pom
Patch0:         crimson-noapis.patch
Provides:       jaxp_parser_impl
Requires: xml-commons-jaxp-1.1-apis
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires(post): alternatives >= 0:0.4
Requires(preun): alternatives >= 0:0.4
Requires: jpackage-utils
BuildRequires: ant
BuildRequires: jpackage-utils
BuildRequires: xml-commons-jaxp-1.1-apis
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch: noarch
%endif
Source44: import.info

%description
Crimson is a Java XML parser which supports XML 1.0 via the following
APIs:
- Java API for XML Processing (JAXP) 1.1 minus the javax.xml.transform
package. JAXP is a pluggable API that allows applications to access XML
documents in a parser-independent manner. It endorses the industry
standard SAX and DOM APIs and also adds a few classes under the
javax.xml.parsers package to implement pluggability and utility methods
Note: the javax.xml.transform package hierarchy of JAXP is not
implemented by Crimson. One implementation of javax.xml.transform can be
found at Xalan Java 2.
- SAX 2.0
- SAX2 Extensions version 1.0
- DOM Level 2 Core Recommendation

%package manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q
%patch0 -p0

mkdir lib
%{__ln_s} $(build-classpath xml-commons-jaxp-1.1-apis) lib/xml-commons-jaxp-1.1-apis.jar

# -----------------------------------------------------------------------------

%build
export OPT_JAR_LIST=:
export CLASSPATH=
export ANT_OPTS="-Djava.endorsed.dirs=$(pwd)/lib"
%{ant} jar javadoc

# -----------------------------------------------------------------------------

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo $jar | %{__sed} "s|-%{version}||g"`; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# demo
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__cp} -pr examples %{buildroot}%{_datadir}/%{name}

# jaxp_parser_impl ghost symlink
%{__ln_s} %{_sysconfdir}/alternatives %{buildroot}%{_javadir}/jaxp_parser_impl.jar

# maven
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap crimson crimson %{version} JPP %{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_parser_impl_%{name}<<EOF
%{_javadir}/jaxp_parser_impl.jar	%{_javadir}/%{name}.jar	20
EOF

%post
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]; then
    %{_bindir}/rebuild-gcj-db
fi
%endif
:

%preun
if [ "$1" -eq 0 ]; then
    :
fi

%postun
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]; then
    %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%_altdir/jaxp_parser_impl_%{name}
%doc ChangeLog README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%exclude %{_javadir}/jaxp_parser_impl.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files manual
%doc docs/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
* Sat Nov 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_19jpp6
- full build

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt0.1jpp
- bootstrap for jetty6

