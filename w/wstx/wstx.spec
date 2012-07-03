Packager: Igor Vlasenko <viy@altlinux.ru>
%define with_repolib 1
%define _with_repolib 1
BuildRequires: bcel ant-bcel
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

%define stax2_version 2.1

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%define repodir %{_javadir}/repository.jboss.com/woodstox/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

Name:           wstx
Version:        3.2.8
Release:	alt1_3jpp6
Epoch:          0
Summary:        Woodstox Stax Implementation
License:        ASL 2.0
Group:          Development/Java
URL:            http://woodstox.codehaus.org/
Source0:        http://woodstox.codehaus.org/3.2.8/wstx-src-3.2.8.tar.gz
Source1:        http://repository.codehaus.org/org/codehaus/woodstox/wstx-asl/3.2.8/wstx-asl-3.2.8.pom
Source2:        http://repository.codehaus.org/org/codehaus/woodstox/wstx-lgpl/3.2.8/wstx-lgpl-3.2.8.pom
Source3:        wstx-component-info.xml
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
Requires: jpackage-utils
Requires: msv-msv
Requires: msv-xsdlib
Requires: stax_1_0_api
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-nodeps
BuildRequires: ant-apache-bcel
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: stax_1_0_api
BuildRequires: emma
BuildRequires: msv-msv
BuildRequires: msv-xsdlib
BuildArch:      noarch
Source44: import.info

%description
Woodstox is a high-performance validating namespace-aware 
StAX-compliant (JSR-173) Open Source XML-processor written 
in Java.

XML processor means that it handles both input (== parsing) 
and output (== writing, serialization)), as well as 
supporting tasks such as validation.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package j2me
Group:          Development/Java
Summary:        J2ME libraries for %{name}

%description j2me
%{summary}.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -c -n wstx

sed -i 's|<import file="build-maven-deploy.xml" />||g' build.xml

find -type f -name '*.?ar' | xargs -t %{__rm}

pushd release-notes
mv CREDITS{,.orig}
mv VERSION{,.orig}
%{_bindir}/iconv -f iso-8859-1 -t utf8 -o CREDITS CREDITS.orig
%{_bindir}/iconv -f iso-8859-1 -t utf8 -o VERSION VERSION.orig
rm CREDITS.orig
rm VERSION.orig
popd

pushd lib
ln -s $(build-classpath emma) .
ln -s $(build-classpath emma_ant) .
ln -s $(build-classpath stax_1_0_api) stax-api-1.0.jar
pushd msv
ln -s $(build-classpath msv-msv) msv.jar
ln -s $(build-classpath msv-xsdlib) xsdlib.jar
ln -s $(build-classpath relaxngDatatype) .
popd
popd

%build
export CLASSPATH=
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/{nodeps,apache-bcel,junit,trax}`"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars jars.j2me javadoc test staxtest

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -p -m 644 build/stax2-%{stax2_version}.jar %{buildroot}%{_javadir}/%{name}/stax2-%{version}.jar
install -p -m 644 build/%{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}/wstx-api-%{version}.jar
install -p -m 644 build/%{name}-asl-%{version}.jar %{buildroot}%{_javadir}/%{name}/wstx-asl-%{version}.jar
install -p -m 644 build/%{name}-lgpl-%{version}.jar %{buildroot}%{_javadir}/%{name}/wstx-lgpl-%{version}.jar
install -p -m 644 build/%{name}-j2me-min-both.jar %{buildroot}%{_javadir}/%{name}/wstx-j2me-min-both-%{version}.jar
install -p -m 644 build/%{name}-j2me-min-input.jar %{buildroot}%{_javadir}/%{name}/wstx-j2me-min-input-%{version}.jar
install -p -m 644 build/%{name}-j2me-min-output.jar %{buildroot}%{_javadir}/%{name}/wstx-j2me-min-output-%{version}.jar
# create unversioned symlinks
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

%add_to_maven_depmap org.codehaus.woodstox stax2 %{version} JPP/%{name} stax2
%add_to_maven_depmap org.codehaus.woodstox wstx-api %{version} JPP/%{name} wstx-api
%add_to_maven_depmap org.codehaus.woodstox wstx-asl %{version} JPP/%{name} wstx-asl
%add_to_maven_depmap org.codehaus.woodstox wstx-lgpl %{version} JPP/%{name} wstx-lgpl
%add_to_maven_depmap org.codehaus.woodstox wstx-j2me-min-both %{version} JPP/%{name} wstx-j2me-min-both
%add_to_maven_depmap org.codehaus.woodstox wstx-j2me-min-input %{version} JPP/%{name} wstx-j2me-min-input
%add_to_maven_depmap org.codehaus.woodstox wstx-j2me-min-output %{version} JPP/%{name} wstx-j2me-min-output

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-wstx-asl.pom
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-wstx-lgpl.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr release-notes/* %{buildroot}%{_docdir}/%{name}-%{version}

%if %with repolib
install -d -m 0755 %{buildroot}%{repodir}
install -d -m 0755 %{buildroot}%{repodirlib}
install -p -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
install -d -m 0755 %{buildroot}%{repodirsrc}
install -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}/wstx-lgpl.jar %{buildroot}%{repodirlib}/wstx.jar
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/stax2-%{version}.jar
%{_javadir}/%{name}/stax2.jar
%{_javadir}/%{name}/wstx-api-%{version}.jar
%{_javadir}/%{name}/wstx-api.jar
%{_javadir}/%{name}/wstx-asl-%{version}.jar
%{_javadir}/%{name}/wstx-asl.jar
%{_javadir}/%{name}/wstx-lgpl-%{version}.jar
%{_javadir}/%{name}/wstx-lgpl.jar
%{_datadir}/maven2/poms/JPP.%{name}-wstx-asl.pom
%{_datadir}/maven2/poms/JPP.%{name}-wstx-lgpl.pom
%{_mavendepmapfragdir}/%{name}

%files j2me
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/wstx-j2me-min-both*.jar
%{_javadir}/%{name}/wstx-j2me-min-input*.jar
%{_javadir}/%{name}/wstx-j2me-min-output*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Mon Nov 01 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.8-alt1_3jpp6
- new version

* Tue Oct 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_1jpp1.7
- updated to new jpackage release

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.9.3-alt1_1jpp1.7
- converted from JPackage by jppimport script

