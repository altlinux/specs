BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define gcj_support 0


Summary:        Java code generation framework
Name:           vdoclet
Version:        0.2
Release:        alt1_0.20070127.8jpp6
Epoch:          0
License:        BSD-style
URL:            http://vdoclet.sourceforge.net/
Group:          Development/Java
Source0:        http://downloads.sourceforge.net/vdoclet/vdoclet-20070127.tar.gz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/vdoclet/vdoclet/20070127/vdoclet-20070127.pom
Patch0:         vdoclet-QDoxBuilder.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-nodeps
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  jaxp_transform_impl
BuildRequires:  ant-trax
BuildRequires:  jakarta-commons-collections
BuildRequires:  qdox >= 0:1.10
BuildRequires:  velocity
Requires:  jakarta-commons-collections
Requires:  qdox >= 0:1.10
Requires:  velocity
%if %{gcj_support}
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
vDoclet is a Java code-generation framework. It takes 
Java source-code, annotated with custom Javadoc tags, and 
uses Velocity templates to produce a number of output files.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{name}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
mkdir -p lib/downloads
(cd lib/downloads
ln -s $(find-jar velocity) velocity-dep-1.3.1.jar
ln -s $(find-jar qdox) qdox-1.6.1.jar
)

%patch0

%build
export OPT_JAR_LIST="ant/ant-junit junit ant/ant-nodeps jaxp_transform_impl ant/ant-trax"
export CLASSPATH=$(build-classpath \
commons-collections \
qdox \
velocity)
CLASSPATH=build/main/classes:$CLASSPATH
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only test dist

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/lib/%{name}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap %{name} %{name} 20070127 JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf dist/doc/apidist/doc/api

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr dist/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p dist/LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_0.20070127.8jpp6
- new version

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_0.20070127.1jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_0.20030717.6jpp5
- fixed repocop warnings

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_0.20030717.6jpp1.7
- converted from JPackage by jppimport script

