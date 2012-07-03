BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define _without_gcj_support 1

%define gcj_support 0


%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/asm/1.5.3-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

Name:           asm
Version:        1.5.3
Release:        alt2_8jpp6
Epoch:          0
Summary:        Code manipulation tool to implement adaptable systems
License:        BSD
URL:            http://asm.objectweb.org/
Group:          Development/Java
Source0:        http://download.us.forge.objectweb.org/asm/asm-1.5.3.tar.gz
Source1:        http://asm.objectweb.org/current/asm-eng.pdf
Source2:        http://asm.objectweb.org/doc/faq.html
Source3:        http://repo1.maven.org/maven2/asm/asm/1.5.3/asm-1.5.3.pom
Source4:        http://repo1.maven.org/maven2/asm/asm-analysis/1.5.3/asm-analysis-1.5.3.pom
Source5:        http://repo1.maven.org/maven2/asm/asm-attrs/1.5.3/asm-attrs-1.5.3.pom
Source6:        http://repo1.maven.org/maven2/asm/asm-tree/1.5.3/asm-tree-1.5.3.pom
Source7:        http://repo1.maven.org/maven2/asm/asm-util/1.5.3/asm-util-1.5.3.pom
Source8:        http://repo1.maven.org/maven2/asm/asm-xml/1.5.3/asm-xml-1.5.3.pom
Source9:        http://repo1.maven.org/maven2/asm/kasm/1.5.3/kasm-1.5.3.pom
Source10:       asm-component-info.xml
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: objectweb-anttask
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
ASM is a code manipulation tool to implement adaptable systems.

%if %{with_repolib}
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
install -p -m 644 %{SOURCE1} .
install -p -m 644 %{SOURCE2} .

#Fix end of line encoding
sed -i 's/\r//g' README.txt
#Fix class path in manifest
sed -i '/Class\-path/d' archive/asm-xml.xml

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dobjectweb.ant.tasks.path=$(build-classpath objectweb-anttask) jar jdoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -p -m 644 output/dist/lib/asm-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.asm-asm.pom
%add_to_maven_depmap asm asm %{version} JPP/%{name} asm
%add_to_maven_depmap asm1 asm %{version} JPP/%{name} asm

install -p -m 644 output/dist/lib/asm-analysis-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.asm-asm-analysis.pom
%add_to_maven_depmap asm asm-analysis %{version} JPP/%{name} asm-analysis
%add_to_maven_depmap asm1 asm-analysis %{version} JPP/%{name} asm-analysis

install -p -m 644 output/dist/lib/asm-attrs-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.asm-asm-attrs.pom
%add_to_maven_depmap asm asm-attrs %{version} JPP/%{name} asm-attrs
%add_to_maven_depmap asm1 asm-attrs %{version} JPP/%{name} asm-attrs

install -p -m 644 output/dist/lib/asm-tree-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.asm-asm-tree.pom
%add_to_maven_depmap asm asm-tree %{version} JPP/%{name} asm-tree
%add_to_maven_depmap asm1 asm-tree %{version} JPP/%{name} asm-tree

install -p -m 644 output/dist/lib/asm-util-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.asm-asm-util.pom
%add_to_maven_depmap asm asm-util %{version} JPP/%{name} asm-util
%add_to_maven_depmap asm1 asm-util %{version} JPP/%{name} asm-util

install -p -m 644 output/dist/lib/asm-xml-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.asm-asm-xml.pom
%add_to_maven_depmap asm asm-xml %{version} JPP/%{name} asm-xml
%add_to_maven_depmap asm1 asm-xml %{version} JPP/%{name} asm-xml

install -p -m 644 output/dist/lib/kasm-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
install -p -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.asm-kasm.pom
%add_to_maven_depmap asm kasm %{version} JPP/%{name} kasm
%add_to_maven_depmap asm1 kasm %{version} JPP/%{name} kasm

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

# javadoc
install -p -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/doc/javadoc/user/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_repolib}
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/asm/asm.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/asm/asm-attrs.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%doc README.txt faq.html asm-eng.pdf
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{subname}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_8jpp6
- added versioned pom groupid asm1

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_8jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_7jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_5jpp5
- converted from JPackage by jppimport script

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_2jpp1.7
- converted from JPackage by jppimport script

