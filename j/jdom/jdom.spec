AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

#def_with bootstrap
%bcond_with bootstrap
#def_with gcj_support
%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           jdom
Version:        1.1.1
Release:	alt3_2jpp6
Epoch:          0
Summary:        Java alternative to DOM and SAX
License:        Apache Software License-like
URL:            http://www.jdom.org/
Group:          Development/Java
Source0:        http://www.jdom.org/dist/source/jdom-1.1.1.tar.gz
Source1:        jdom-1.1.1.pom
Patch0:         %{name}-crosslink.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: xalan-j2 >= 0:2.2.0
%if %with bootstrap
Requires: jaxen-bootstrap
%else
Requires: jaxen
%endif
BuildRequires: ant >= 0:1.6
BuildRequires: xalan-j2 >= 0:2.2.0
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: java-javadoc
%if %with bootstrap
BuildRequires: jaxen-bootstrap
%else
BuildRequires: jaxen
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info
Source45: jdom-1.1.1.jar-OSGi-MANIFEST.MF

%description
JDOM is, quite simply, a Java representation of an XML document. JDOM
provides a way to represent that document for easy and efficient
reading, manipulation, and writing. It has a straightforward API, is a
lightweight and fast, and is optimized for the Java programmer. It's an
alternative to DOM and SAX, although it integrates well with both DOM
and SAX.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demos for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n jdom
%patch0 -p0
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{_bindir}/find -type f -name "*.class" | %{_bindir}/xargs -t %{__rm}
%if %with bootstrap
%{__rm} src/java/org/jdom/xpath/JaxenXPath.java
%endif

%{__sed} -i -e 's|<property name="build.compiler".*||' build.xml

%build
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath jaxen xalan-j2):$(pwd)/build/jdom.jar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Dj2se.apidoc=%{_javadocdir}/java package javadoc-link

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/jdom.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jdom jdom %{version} JPP %{name}
%add_to_maven_depmap jdom jdom %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# demo
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__cp} -pr samples %{buildroot}%{_datadir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

# inject OSGi manifest jdom-1.1.1.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
zip -u %buildroot/usr/share/java/jdom.jar META-INF/MANIFEST.MF
# end inject OSGi manifest jdom-1.1.1.jar-OSGi-MANIFEST.MF

%files
%doc CHANGES.txt COMMITTERS.txt LICENSE.txt README.txt TODO.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/jdom-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}

%changelog
* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_2jpp6
- added jdom:jdom jppmap

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_2jpp6
- added osgi manifest

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp6
- new jpp release

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5.5jpp5
- added OSGi manifest for eclipse

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp1.7
- converted from JPackage by jppimport script

* Thu Apr 07 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Initial build for ALTLinux Sisyphus

