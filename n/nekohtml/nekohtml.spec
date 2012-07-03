BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 1.9.14
%define name nekohtml
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

%bcond_without repolib

%global repodir %{_javadir}/repository.jboss.com/nekohtml/%{version}-brew
%global repodirlib %{repodir}/lib
%global repodirsrc %{repodir}/src

%define xerces_version 2.9.1


Name:           nekohtml
Version:        1.9.14
Release:        alt2_4jpp6
Epoch:          0
Summary:        HTML scanner and tag balancer
License:        ASL 2.0
Group:          Development/Java
URL:            http://nekohtml.sourceforge.net/
Source0:        http://downloads.sourceforge.net/nekohtml/nekohtml-1.9.14.tar.gz
# http://www.jpackage.org/cgi-bin/viewvc.cgi/*checkout*/rpms/devel/nekohtml/nekohtml-filter.sh?root=jpackage&content-type=text%2Fplain
Source1:        %{name}-filter.sh
Source2:        nekohtml-component-info.xml
Source3:        http://nekohtml.sourceforge.net/m2-repo/net/sourceforge/nekohtml/nekohtml/1.9.14/nekohtml-1.9.14.pom
Patch0:         %{name}-crosslink.patch
Patch1:         %{name}-jars.patch
Patch2:         %{name}-skip-tests.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       bcel
Requires:       jpackage-utils
Requires:       xerces-j2 >= 0:%{xerces_version}
Requires:       xml-commons-jaxp-1.3-apis
BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  ant-trax
BuildRequires:  java-javadoc
BuildRequires:  bcel
BuildRequires:  bcel-javadoc
BuildRequires:  xerces-j2 = 0:%{xerces_version}
BuildRequires:  xerces-j2-javadoc-xni
BuildRequires:  xerces-j2-javadoc-impl
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildArch:      noarch
Source44: import.info

%description
NekoHTML is a simple HTML scanner and tag balancer that enables
application programmers to parse HTML documents and access the
information using standard XML interfaces. The parser can scan HTML
files and "fix up" many common mistakes that human (and computer)
authors make in writing HTML documents.  NekoHTML adds missing parent
elements; automatically closes elements with optional end tags; and
can handle mismatched inline element tags.
NekoHTML is written using the Xerces Native Interface (XNI) that is
the foundation of the Xerces2 implementation. This enables you to use
the NekoHTML parser with existing XNI tools without modification or
rewriting code.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

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
%setup -q
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%{_bindir}/find . -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__perl} -pi -e 's/\r$//g' *.txt doc/*.html
%{__rm} -r doc/javadoc

%build
export CLASSPATH=$(%{_bindir}/build-classpath bcel xerces-j2)
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/junit` ant/ant-trax xalan-j2"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    -Dbuild.sysclasspath=first \
    -Dlib.dir=%{_javadir} \
    -Djar.file=%{name}-%{version}.jar \
    -Djar.xni.file=%{name}-xni-%{version}.jar \
    -Djar.samples.file=%{name}-samples-%{version}.jar \
    -Dxerces.version=%{xerces_version} \
    -Dbcel.javadoc=%{_javadocdir}/bcel \
    -Dj2se.javadoc=%{_javadocdir}/java \
    -Dxni.javadoc=%{_javadocdir}/xerces-j2-xni \
    -Dxerces.javadoc=%{_javadocdir}/xerces-j2-impl \
    clean jar jar-xni doc test

%install

# Jars
mkdir -p %{buildroot}%{_javadir}
cp -p %{name}{,-samples,-xni}-%{version}.jar %{buildroot}%{_javadir}/
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}-samples-%{version}.jar %{buildroot}%{_javadir}/%{name}-samples.jar
ln -s %{name}-xni-%{version}.jar %{buildroot}%{_javadir}/%{name}-xni.jar

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap net.sourceforge.nekohtml nekohtml %{version} JPP %{name}

# Scripts
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}-filter

# Javadocs
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
mkdir -p %{buildroot}%{repodir}
mkdir -p %{buildroot}%{repodirlib}
cp -p %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
mkdir -p %{buildroot}%{repodirsrc}
cp -p %{SOURCE0} %{buildroot}%{repodirsrc}
cp -p %{SOURCE1} %{buildroot}%{repodirsrc}
cp -p %{PATCH0} %{buildroot}%{repodirsrc}
cp -p %{PATCH1} %{buildroot}%{repodirsrc}
cp -p %{PATCH2} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/nekohtml.pom
%{__cp} -p %{buildroot}%{_javadir}/%{name}.jar %{buildroot}%{repodirlib}/nekohtml.jar
%endif

%files
%doc --no-dereference LICENSE.txt README.txt doc/*.html
%attr(755,root,root) %{_bindir}/%{name}-filter
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_javadir}*/%{name}-xni-%{version}.jar
%{_javadir}*/%{name}-xni.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_javadir}*/%{name}-samples-%{version}.jar
%{_javadir}*/%{name}-samples.jar

%if %with repolib
%files repolib
%dir %{_javadir}*
%exclude %dir %{_javadocdir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.14-alt2_4jpp6
- new jpp relase

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.9.14-alt2_1jpp6
- new version

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.9.14-alt1_1jpp6
- added osgi manifest

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_5jpp5
- new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_4jpp1.7
- converted from JPackage by jppimport script

