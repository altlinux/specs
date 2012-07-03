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

%define cvsversion      20061207

Name:           rngom
Summary:        RELAX NG Object Model / Parser
Url:            https://rngom.dev.java.net/
Version:        0.1
Release:        alt3_0.20061207.1jpp5
Epoch:          0
License:        MIT-style
Group:          Development/Java
BuildArch:      noarch
Source0:        rngom-20061207.tar.gz
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs login
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r jaxb21_fcs rngom
Source1:        rngom-20061207.pom
Patch0:         rngom-build.patch
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-nodeps
BuildRequires: javacc
BuildRequires: javatools-package-rename-task
BuildRequires: junit
BuildRequires: msv-xsdlib
BuildRequires: relaxngDatatype
BuildRequires: retroweaver
BuildRequires: stax_1_0_api
BuildRequires: xmlunit

Requires: relaxngDatatype
Requires: stax_1_0_api

Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4
Patch33: rngom-20061207-alt-javadoc.patch

%description
RNGOM is an open-source Java library for parsing RELAX NG 
grammars. In particular, RNGOM can:
1. parse the XML syntax
2. parse the compact syntax
3. check all the semantic restrictions as specified in the 
   specification
4. parse RELAX NG into application-defined data structures
5. build a default data structure based around the binarized 
   simple syntax or another data structure that preserves 
   more of the parsed information.
6. parse foreign elements/attributes in a schema
7. parse comments in a schema 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0

#BUILD/rngom/rngom/lib/javacc/bin/lib/javacc.jar.no
ln -sf $(build-classpath javacc) rngom/lib/javacc/bin/lib/javacc.jar
#BUILD/rngom/rngom/lib/jsr173_1.0_api.jar.no
ln -sf $(build-classpath stax_1_0_api) rngom/lib/jsr173_1.0_api.jar
#BUILD/rngom/rngom/lib/junit.jar.no
ln -sf $(build-classpath junit) rngom/lib/junit.jar
#BUILD/rngom/rngom/lib/relaxngDatatype.jar.no
ln -sf $(build-classpath relaxngDatatype) rngom/lib/relaxngDatatype.jar

#BUILD/rngom/rngom/lib/retroweaver/bcel-5.1.jar.no
#BUILD/rngom/rngom/lib/retroweaver/jace.jar.no
#BUILD/rngom/rngom/lib/retroweaver/Regex.jar.no
#BUILD/rngom/rngom/lib/retroweaver/retroweaver.jar.no
ln -sf $(build-classpath retroweaver-all) rngom/lib/retroweaver/

#BUILD/rngom/rngom/lib/util/package-rename-task.jar.no
ln -sf $(build-classpath javatools-package-rename-task) rngom/lib/util/package-rename-task.jar

#BUILD/rngom/rngom/lib/xmlunit1.0.jar.no
ln -sf $(build-classpath xmlunit) rngom/lib/xmlunit1.0.jar
#BUILD/rngom/rngom/lib/xsdlib.jar.no
ln -sf $(build-classpath xsdlib) rngom/lib/xsdlib.jar
%patch33 -p0


%build
cd %{name}
ant -Dbuild.sysclasspath=first jar javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}/build/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 %{name}/build/%{name}-1.3.jar $RPM_BUILD_ROOT%{_javadir}/%{name}13-%{version}.jar
install -m 644 %{name}/build/jax-qname.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-jax-qname-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.kohsuke %{name} %{cvsversion} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr %{name}/build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 www/doc/LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/*
%{_datadir}/maven2
%{_mavendepmapfragdir}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt3_0.20061207.1jpp5
- fixes for java6 support

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt2_0.20061207.1jpp5
- fixed docdir ownership

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_0.20061207.1jpp5
- converted from JPackage by jppimport script

