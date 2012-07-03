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


Name:           carol
Summary:        CAROL: Common Architecture for RMI ObjectWeb Layer
Url:            http://carol.objectweb.org/
Version:        2.2.7
Release:        alt2_3jpp6
Epoch:          0
License:        LGPL
Group:          Development/Java
BuildArch:      noarch
Source0:        carol-%{version}-src.tar.gz
Source1:        carol-%{version}.pom

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  %{_bindir}/perl
BuildRequires:  carol-irmi >= 1.0
BuildRequires:  carol-cmi >= 1.2.7
BuildRequires:  objectweb-anttask
BuildRequires:  apache-commons-logging >= 1.0.4
# Commons-collections is required by irmi
BuildRequires:  apache-commons-collections >= 3.1
# FIXME Using private version of JacORB
# JONAS_JACORB_1_0_3
#BuildRequires:  jacorb >= 2.2.1
BuildRequires:  jgroups >= 2.2.7
BuildRequires:  jonathan-core >= 4.1
BuildRequires:  jonathan-jeremie >= 4.2.1
BuildRequires:  junit >= 3.8.1
BuildRequires:  monolog >= 1.9.2
BuildRequires:  mx4j >= 3.0.1
BuildRequires:  kilim1 >= 1.1.3
BuildRequires:  nanoxml-lite >= 2.2.1
BuildRequires:  velocity >= 1.4
Requires:  carol-irmi >= 1.0
Requires:  carol-cmi >= 1.2.7
Requires:  apache-commons-logging >= 1.0.4
# Commons-collections is required by irmi
Requires:  apache-commons-collections >= 3.1
# FIXME Using private version of JacORB
# JONAS_JACORB_1_0_3
#Requires:  jacorb >= 2.2.1
Requires:  jgroups >= 2.2.7
Requires:  jonathan-core >= 4.1
Requires:  jonathan-jeremie >= 4.2.1
Requires:  junit >= 3.8.1
Requires:  monolog >= 1.9
Requires:  mx4j >= 3.0.1
Requires:  kilim1 >= 1.1.3
Requires:  nanoxml-lite >= 2.2.1
Requires:  velocity >= 1.4
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
CAROL is a library allowing to use different RMI implementations. 
Thanks to CAROL, a Java server application can be independent of 
RMI implementations and accessible simultaneously by RMI clients 
using different RMI implementations. CAROL allows to design, 
implement, compile, package, deploy, and execute distributed 
applications compliant with the RMI model.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Documents for %{name}.

%prep
%setup -q -n %{name}
chmod -R go=u-w *

# FIXME Using private version of JacORB
# JONAS_JACORB_1_0_3
find . -name "*.jar" \
       -not -name "jacorb.jar" \
       -exec rm -f {} \;

%build
pushd externals

ln -sf $(build-classpath ow_carol_cmi) cmi.jar
ln -sf $(build-classpath ow_carol_irmi) irmi.jar
ln -sf $(build-classpath commons-logging-api) .
ln -sf $(build-classpath commons-collections) .
ln -sf $(build-classpath mx4j/mx4j) .
ln -sf $(build-classpath jgroups) .
# FIXME Using private version of JacORB
# JONAS_JACORB_1_0_3
#ln -sf $(build-classpath jacorb/jacorb) .
ln -sf $(build-classpath junit) .
ln -sf $(build-classpath velocity) .

cd jeremie
ln -sf $(build-classpath jonathan-core) .
ln -sf $(build-classpath jonathan-jeremie) .
ln -sf $(build-classpath nanoxml-lite) .
ln -sf $(build-classpath kilim1) .
ln -sf $(build-classpath monolog/ow_util_log_api) .
popd

export OPT_JAR_LIST="objectweb-anttask ant/ant-junit junit"
#ant dist jdoc run.tests
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist jdoc 

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 archive/output/dist/lib/ow_%{name}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/ow_%{name}-%{version}.jar
install -m 644 archive/output/dist/lib/ow_%{name}_iiop_delegate.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/ow_%{name}-%{version}_iiop_delegate.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-ow_%{name}.pom
%add_to_maven_depmap org.objectweb.carol carol %{version} JPP ow_%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -m 644 output/dist/config/carol.properties \
                  $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/jdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr output/dist/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/ow_carol.jar
%{_javadir}/%{name}/ow_carol-%{version}.jar
%{_javadir}/%{name}/ow_carol_iiop_delegate.jar
%{_javadir}/%{name}/ow_carol-%{version}_iiop_delegate.jar
%{_datadir}/%{name}-%{version}
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.7-alt2_3jpp6
- new jpp relase

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.7-alt2_2jpp5
- build with ant17

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.7-alt1_2jpp5
- new jpp release

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2.7-alt1_1jpp5
- fixed build with java 5

* Mon Jul 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.7-alt1_1jpp1.7
- converted from JPackage by jppimport script

