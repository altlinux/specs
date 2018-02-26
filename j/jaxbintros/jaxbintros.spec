BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define _with_repolib 1
# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define reltag GA
%define version_full %{version}.%{reltag}
%define repodir %{_javadir}/repository.jboss.com/jboss/jaxbintros/%{version_full}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


Name:           jaxbintros
Version:        1.0.0
Release:        alt2_1jpp6
Epoch:          0
Summary:        JAXB introduction
License:        LGPLv2+
Group:          Development/Java
URL:            http://wiki.jboss.org/wiki/JAXBIntroductions
# svn -q export http://anonsvn.jboss.org/repos/jbossws/projects/jaxbintros/tags/1.0.0.GA/ jaxbintros-1.0.0.GA && tar cjf jaxbintros-1.0.0.GA.tar.bz2 jaxbintros-1.0.0.GA
Source0:        %{name}-%{version_full}.tar.bz2
Source1:        http://repository.jboss.org/maven2/jboss/jaxbintros/jboss-jaxb-intros/1.0.0.GA/jboss-jaxb-intros-1.0.0.GA.pom
Source2:        %{name}-component-info.xml
Patch0:         jaxbintros-build.patch
Requires: codehaus-stax11-api
Requires: glassfish-jaf
Requires: glassfish-jaxb
Requires: jakarta-commons-logging-jboss
Requires: jbossws-spi
Requires: junit
Requires: log4j
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: codehaus-stax11-api
BuildRequires: glassfish-jaf
BuildRequires: glassfish-jaxb
BuildRequires: jakarta-commons-logging-jboss
BuildRequires: jbossws-spi
BuildRequires: junit
BuildRequires: log4j
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
JAXB introduction.

%if %{with_repolib}
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n jaxbintros-%{version_full}
%patch0 -p1

%{__mkdir_p} thirdparty
pushd thirdparty
%{__ln_s} $(build-classpath glassfish-jaf) activation.jar
%{__ln_s} $(build-classpath commons-logging-jboss) commons-logging.jar
%{__ln_s} $(build-classpath sun-jaxb/jaxb-api) jaxb-api.jar
%{__ln_s} $(build-classpath sun-jaxb/jaxb-impl) jaxb-impl.jar
%{__ln_s} $(build-classpath jbossws-spi) jbossws-spi.jar
%{__ln_s} $(build-classpath junit) junit.jar
%{__ln_s} $(build-classpath log4j) log4j.jar
%{__ln_s} $(build-classpath codehaus-stax11-api) stax-api.jar
popd

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}/jboss
%{__cp} -p output/lib/jboss-jaxb-intros.jar %{buildroot}%{_javadir}/jboss/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/jboss/jboss-jaxb-intros-%{version}.jar
(cd %{buildroot}%{_javadir}/jboss && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%add_to_maven_depmap jboss.jaxbintros jboss-jaxb-intros %{version_full} JPP/jboss %{name}
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.pom

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_repolib}
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -a %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version_full}-brew/g" %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -a %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -a %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/jboss/%{name}-%{version}.jar %{buildroot}%{repodirlib}/jboss-jaxb-intros.jar
%endif

%files
%{_javadir}/jboss
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/jboss-xml-binding-1.0.0.jar.db
%{_libdir}/gcj/%{name}/jboss-xml-binding-1.0.0.jar.so
%endif

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt2_1jpp6
- cleaned up comoonents-info

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_1jpp6
- new jpp release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_0.beta2.1jpp5
- new jpp release

