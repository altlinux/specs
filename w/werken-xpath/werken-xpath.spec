BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

%global dotname werken.xpath


Name:           werken-xpath
Version:        0.9.4
Release:        alt1_0.beta.15jpp6
Epoch:          0
Summary:        XPath implementation using JDOM
License:        ASL-like
Group:          Development/Java
URL:            http://sourceforge.net/projects/werken-xpath/
Source0:        %{dotname}-%{version}-beta-src.tar.gz
Source1:        %{name}-%{version}.pom
Patch0:         %{name}-ElementNamespaceContext.patch
Patch1:         %{name}-Partition.patch
Patch2:         %{name}-ParentStep.patch
Patch3:         %{name}-NodeTypeStep.patch
Patch4:         %{name}-UnAbbrStep.patch
Patch5:         %{name}-StringFunction.patch
Patch6:         %{name}-Test.patch
Patch7:         %{name}-Driver.patch
Patch8:         %{name}-runtests_sh.patch
Obsoletes:      werken.xpath < %{epoch}:%{version}-%{release}
Provides:       werken.xpath = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
Requires:       jdom
Requires:       jpackage-utils
BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  jdom
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-jaxp-1.3-apis
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
werken.xpath is an implementation of the W3C XPath Recommendation, on
top of the JDOM library.  It takes as input a XPath expression, and a
JDOM tree, and returns a NodeSet (java.util.List) of selected
elements.  Is is being used in the development of the
as-yet-unreleased werken.xslt (eXtensible Stylesheet Language) and the
werken.canonical (XML canonicalization) packages.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       werken.xpath-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      werken.xpath-javadoc < %{epoch}:%{version}-%{release}
Requires:       jpackage-utils
BuildRequires:  java-javadoc
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{dotname}
find -type f -name "*.jar" | xargs -t rm
%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
%patch5 -b .sav
%patch6 -b .sav
%patch7 -b .sav
%patch8 -b .sav

%if 0
pushd lib
ln -s $(build-classpath antlr) antlr-runtime.jar
ln -s $(build-classpath jdom) jdom.jar
ln -s $(build-classpath xerces-j2) xerces.jar
popd
%endif

%build
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath jdom antlr xerces-j2 xml-commons-jaxp-1.3-apis)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.compiler=modern package javadoc compile-test
# Note that you'll have to java in PATH for this to work, it is by default
# when using a JPackage JVM.
CLASSPATH=${CLASSPATH}:build/werken.xpath.jar:build/test/classes
sh ./runtests.sh

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/%{dotname}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{dotname}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -s ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap werken-xpath werken-xpath %{version} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc INSTALL LICENSE LIMITATIONS README TODO
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{dotname}-%{version}.jar
%{_javadir}/%{dotname}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/werken-xpath-0.9.4.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_0.beta.15jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_0.beta.13jpp5
- new jpp release

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_0.beta.13jpp1.7
- updated to new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_0.beta.12jpp1.7
- converted from JPackage by jppimport script

* Sun Jul 03 2005 Vladimir Lettiev <crux@altlinux.ru> 0.9.4-alt0.2beta
- added xml-commons-apis to classpath
- changed rpmgroup of javadoc package

* Fri May 06 2005 Vladimir Lettiev <crux@altlinux.ru> 0.9.4-alt0.1beta
- Initial build for ALT Linux Sisyphus

