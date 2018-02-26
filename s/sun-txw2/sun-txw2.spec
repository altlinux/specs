Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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

%define bname   txw2
%define cvsdate 20070624

Name:           sun-txw2
Summary:        Typed XML writer
Url:            https://txw.dev.java.net/
Version:        0.1
Release:	alt2_0.20070624.2jpp5
Epoch:          0
License:        CDDL
Group:          Development/Java
BuildArch:      noarch
Source0:        txw2-20070624.tar.gz
# cvs -d:pserver:guest@cvs.dev.java.net:/cvs export -D 2007-06-24 -d txw2 jaxb2-sources/txw2
Source1:        http://download.java.net/maven/2/com/sun/xml/txw2/txw2/20070624/txw2-20070624.pom
Source2:        txwc2-20070624.pom
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: args4j10
BuildRequires: javatools-package-rename-task
BuildRequires: msv-xsdlib
BuildRequires: relaxngDatatype
BuildRequires: rngom
BuildRequires: stax_1_0_api
BuildRequires: sun-codemodel
BuildRequires: sun-xsom
Requires: stax_1_0_api

Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
TXW is a library that allows you to write XML documents. 
TXW has the following benefits compared to the other XML 
writer libraries:
1. TXW gets rid of string constants for element/attribute 
   names. Those constant names become method names.
2. TXW manages the namespace binding for you. It automatically 
   declares the necessary URIs.
3. TXW allows you to use typed values (such as ints, booleans, 
   or QNames), eliminating cumbersome String.valueOf or the
   use of toString methods.
4. TXW allows you to stream the writing process (IOW, it starts 
   generating pieces as soon as data is available), while at
   the same time allowing you to work out-of-order when you need to.
5. TXW is very small (<50KB)
6. TXW allows you to control various low-level aspects of XML
   writing, such as comments, PIs, and prefix assignments. 

%package compiler
Summary:        Compiler from %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: ant
Requires: args4j10
Requires: relaxngDatatype
Requires: rngom
Requires: sun-codemodel
Requires: sun-xsom

%description compiler
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{bname}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

#BUILD/txw2/lib/compiler/ant.jar.no
#BUILD/txw2/lib/compiler/args4j-1.0-RC.jar.no
ln -sf $(build-classpath args4j10) lib/compiler/args4j-1.0-RC.jar
#BUILD/txw2/lib/compiler/codemodel.jar.no
ln -sf $(build-classpath sun-codemodel) lib/compiler/codemodel.jar
#BUILD/txw2/lib/compiler/relaxngDatatype.jar.no
ln -sf $(build-classpath relaxngDatatype) lib/compiler/relaxngDatatype.jar
#BUILD/txw2/lib/compiler/rngom.jar.no
ln -sf $(build-classpath rngom) lib/compiler/rngom.jar
#BUILD/txw2/lib/compiler/xsdlib.jar.no
ln -sf $(build-classpath xsdlib) lib/compiler/xsdlib.jar
#BUILD/txw2/lib/compiler/xsom.jar.no
ln -sf $(build-classpath sun-xsom/xsom) lib/compiler/xsom.jar
#BUILD/txw2/lib/package-rename-task.jar.no
ln -sf $(build-classpath javatools-package-rename-task) lib/package-rename-task.jar
#BUILD/txw2/lib/runtime/jsr173_1.0_api.jar.no
ln -sf $(build-classpath stax_1_0_api) lib/runtime/jsr173_1.0_api.jar

%build
ant -Dbuild.sysclasspath=first dist test javadoc
pushd wsdl11/
ant
popd
pushd xmlschema/
ant
popd

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/txw2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 build/txwc2.jar $RPM_BUILD_ROOT%{_javadir}/sun-txwc2-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.sun.xml.txw2 txw2 %{cvsdate} JPP %{name}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-sun-txwc2.pom
%add_to_maven_depmap com.sun.xml.txw2 txwc2 %{cvsdate} JPP sun-txwc2


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 doc/license.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/%{name}*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}
%doc %{_docdir}/%{name}-%{version}

%files compiler
%{_javadir}/sun-txwc2*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt2_0.20070624.2jpp5
- selected java5 compiler explicitly

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_0.20070624.2jpp5
- new jpp release

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_0.20070624.1jpp5
- converted from JPackage by jppimport script

