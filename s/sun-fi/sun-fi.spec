BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 1.2.2
%define name sun-fi
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define repodir %{_javadir}/repository.jboss.com/sun-fi/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           sun-fi
Version:        1.2.2
Release:        alt1_4jpp6
Epoch:          0
Summary:        Fast Infoset
License:        ASL 2.0
URL:            https://fi.dev.java.net/
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r jaxws211-fcs -d sun-fi-1.2.2 fi/FastInfoset
# mkdir sun-fi-1.2.2/FastInfosetUtilities
# cd sun-fi-1.2.2
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -D 20061004 -d FastInfosetUtilities fi/FastInfosetUtilities
# cd ..
# tar czf sun-fi-1.2.2.tar.gz sun-fi-1.2.2
Source0:        sun-fi-1.2.2.tar.gz
Source1:        FastInfoset-1.2.2.pom
Source2:        FastInfosetUtilities-1.2.2.pom
Source3:        sun-fi-component-info.xml
Patch0:         sun-fi-1.2.2-build-without-nb.patch
Group:          Development/Java
Provides:       FastInfoset = %{epoch}:%{version}-%{release}
Provides:       FastInfosetUtilities = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       stax_1_0_api
Requires:       stax-ex
Requires:       sun-xmlstreambuffer
Requires:       sun-xsom
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-junit
BuildRequires:  javatools-package-rename-task
BuildRequires:  jpackage-utils >= 0:1.7.4
BuildRequires:  junit
BuildRequires:  relaxngDatatype
BuildRequires:  stax_1_0_api
BuildRequires:  stax-ex
BuildRequires:  sun-xmlstreambuffer
BuildRequires:  sun-xsom
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
Fast Infoset Project, an Open Source implementation of the 
Fast Infoset Standard for Binary XML.
Fast Infoset specifies a standardized binary encoding for 
the XML Information Set. An XML infoset (such as a DOM tree, 
StAX events or SAX events in programmatic representations) 
may be serialized to an XML 1.x document or, as specified by 
the Fast Infoset standard, may be serialized to a fast 
infoset document. Fast infoset documents are generally 
smaller in size and faster to parse and serialize than 
equivalent XML documents.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q 
# remove all binary libs
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%patch0 -p0 -b .sav0

%build
export CLASSPATH=
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`

%{__ln_s} $(%{_bindir}/build-classpath junit) lib/junit.jar
%{__ln_s} $(%{_bindir}/build-classpath stax_1_0_api) lib/jsr173_api.jar
%{__ln_s} $(%{_bindir}/build-classpath javatools-package-rename-task) tools/lib/package-rename-task.jar

# Run to create java2 sources (need java5)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f j2se-integration.xml
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f build-without-nb.xml dist test doc

export CLASSPATH=`pwd`/dist/FastInfoset.jar
pushd FastInfosetUtilities
%{__ln_s} $(%{_bindir}/build-classpath stax_1_0_api) lib/jsr173_api.jar
%{__ln_s} $(%{_bindir}/build-classpath relaxngDatatype) lib/relaxngDatatype.jar
%{__ln_s} $(%{_bindir}/build-classpath stax-ex) lib/stax-ex.jar
%{__ln_s} $(%{_bindir}/build-classpath sun-xmlstreambuffer) lib/streambuffer.jar
%{__ln_s} $(%{_bindir}/build-classpath sun-xsom/xsom) lib/xsom.jar

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f build-without-nb.xml dist doc
popd

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p dist/FastInfoset.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/FastInfoset-%{version}.jar

pushd FastInfosetUtilities
%{__cp} -p dist/FastInfosetUtilities.jar %{buildroot}%{_javadir}/%{name}-utilities-%{version}.jar
%{__ln_s} %{name}-utilities-%{version}.jar %{buildroot}%{_javadir}/FastInfosetUtilities-%{version}.jar
popd

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.sun.xml.fastinfoset FastInfoset %{version} JPP %{name}

%{__cp} -p %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-utilities.pom
%add_to_maven_depmap com.sun.xml.fastinfoset FastInfosetUtilities %{version} JPP %{name}-utilities

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/FastInfoset-%{version}
%{__ln_s} FastInfoset-%{version} %{buildroot}%{_javadocdir}/FastInfoset

%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-utilities-%{version}
pushd FastInfosetUtilities
%{__cp} -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}-utilities-%{version}
popd
%{__ln_s} %{name}-utilities-%{version} %{buildroot}%{_javadocdir}/%{name}-utilities
%{__ln_s} %{name}-utilities-%{version} %{buildroot}%{_javadocdir}/FastInfosetUtilities-%{version}
%{__ln_s} FastInfosetUtilities-%{version} %{buildroot}%{_javadocdir}/FastInfosetUtilities

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/FastInfoset.jar %{buildroot}%{repodirlib}/FastInfoset.jar
%{__cp} -p %{buildroot}%{_javadir}/FastInfosetUtilities.jar %{buildroot}%{repodirlib}/FastInfosetUtilities.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/FastInfoset-%{version}.jar
%{_javadir}/FastInfoset.jar
%{_javadir}/%{name}-utilities-%{version}.jar
%{_javadir}/%{name}-utilities.jar
%{_javadir}/FastInfosetUtilities-%{version}.jar
%{_javadir}/FastInfosetUtilities.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_datadir}/maven2/poms/JPP-%{name}-utilities.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-utilities-%{version}
%{_javadocdir}/%{name}-utilities
%{_javadocdir}/FastInfoset-%{version}
%{_javadocdir}/FastInfoset
%{_javadocdir}/FastInfosetUtilities-%{version}
%{_javadocdir}/FastInfosetUtilities

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_4jpp6
- new jpp relase

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_3jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_2jpp5
- converted from JPackage by jppimport script

* Sat Dec 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

