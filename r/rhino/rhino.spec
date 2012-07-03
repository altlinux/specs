AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# one of the sources is a zip file
BuildRequires: unzip
%define version 1.7
%define name rhino
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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/rhino/%{version}%{rel}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


%define rel R2
%define cvs_version     1_7%{rel}
%define archive_version 1_7%{rel}

Name:           rhino
Version:        1.7
Release:        alt2_1.r2.8jpp6
Epoch:          0
Summary:        JavaScript for Java
License:        MPL
Source0:        ftp://ftp.mozilla.org/pub/mozilla.org/js/rhino%{archive_version}.zip
Source1:        http://java.sun.com/products/jfc/tsc/articles/treetable2/downloads/src.zip
Source2:        rhino.script
Source3:        rhino-debugger.script
Source4:        rhino-idswitch.script
Source5:        rhino-jsc.script
Source6:        rhino-js.pom
Source7:        rhino.pom
Source8:        rhino-component-info.xml
Patch0:         rhino-build.patch
Patch1:         rhino-dojo.patch
Patch2:         rhino-class-loader.patch
Patch3:         rhino-288467.patch
URL:            http://www.mozilla.org/rhino/
Group:          Development/Java
Requires:       jline
Requires:       stax_1_0_api
Requires:       xmlbeans
BuildRequires:  ant
BuildRequires:  jpackage-utils
BuildRequires:  jline
BuildRequires:  stax_1_0_api
BuildRequires:  xmlbeans
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info
Source45: js-1.7.jar-OSGi-MANIFEST.MF

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

This version contains Dojo's JavaScript compression patch.

%package demo
Summary:        Examples for %{name}
Group:          Development/Java

%description demo
Examples for %{name}.

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

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{name}%{cvs_version}
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3

# Fix build
%{__perl} -pi -e 's|.*<get.*src=.*>\n||' build.xml testsrc/build.xml toolsrc/org/mozilla/javascript/tools/debugger/build.xml xmlimplsrc/build.xml
%{__install} -D -p -m 644 %{SOURCE1} toolsrc/org/mozilla/javascript/tools/debugger/downloaded/swingExSrc.zip

# Fix manifest
%{__perl} -pi -e 's|^Class-Path:.*\n||g' src/manifest

# Add jpp release info to version
%{__perl} -pi -e 's|^implementation.version: Rhino .* release .* \${implementation.date}|implementation.version: Rhino %{version} release %{release} \${implementation.date}|' build.properties

%build
export CLASSPATH=$(build-classpath jline)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dxbean.jar=$(build-classpath xmlbeans/xbean) -Djsr173.jar=$(build-classpath stax_1_0_api) deepclean jar copy-all javadoc

export CLASSPATH=`pwd`/build/%{name}%{cvs_version}/js.jar
pushd examples
%{javac}  -target 1.5 -source 1.5 *.java
%{jar} cvf ../build/%{name}%{cvs_version}/%{name}-examples-%{version}.jar *.class
popd

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -a build/%{name}%{cvs_version}/js.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -a build/%{name}%{cvs_version}/%{name}-examples-%{version}.jar %{buildroot}%{_javadir}/%{name}-examples-%{version}.jar
(cd %{buildroot}%{_javadir} && %{__ln_s} %{name}-%{version}.jar js-%{version}.jar)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `echo $jar| %{__sed} "s|-%{version}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -a %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-js.pom
%{__cp} -a %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap %{name} js %{version} JPP js

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -a build/%{name}%{cvs_version}/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{_bindir}/find %{buildroot}%{_javadocdir}/%{name}-%{version} -type f -name '*.html' | %{_bindir}/xargs %{__perl} -pi -e 's/\r$//g'

# scripts
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}
%{__install} -p -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}-debugger
%{__install} -p -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}-idswitch
%{__install} -p -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/%{name}-jsc

# examples
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__cp} -a examples/* %{buildroot}%{_datadir}/%{name}

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE7} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE3} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE4} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE5} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE6} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH2} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/js.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

# inject OSGi manifest js-1.7.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/js.jar META-INF/MANIFEST.MF

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf
# end inject OSGi manifest js-1.7.jar-OSGi-MANIFEST.MF

%files
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}-debugger
%attr(0755,root,root) %{_bindir}/%{name}-idswitch
%attr(0755,root,root) %{_bindir}/%{name}-jsc
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/js-%{version}.jar
%{_javadir}/js.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_datadir}/maven2/poms/JPP-js.pom
%{_mavendepmapfragdir}/%{name}
%config(noreplace,missingok) /etc/%{name}.conf

%files demo
%{_javadir}/%{name}-examples-%{version}.jar
%{_javadir}/%{name}-examples.jar
%{_datadir}/%{name}

%files manual
%if 0
%doc build/%{name}%{cvs_version}/docs/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_1.r2.8jpp6
- updated OSGi manifest

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_1.r2.8jpp6
- added repolib

* Sun Feb 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_1.r2.6jpp5
- rev. 2.6

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_1.r2.3jpp5
- converted from JPackage by jppimport script

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_0.r2.2jpp1.7
- converted from JPackage by jppimport script

