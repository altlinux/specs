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

%define	jarname		carol_cmi


Name:		carol-cmi
Summary:	CMI: "Cluster aware" distribution protocol
Url:		http://carol.objectweb.org/
Version:	1.2.7
Release:	alt3_3jpp6
Epoch:		0
License:	LGPL
Group:		Development/Java
BuildArch:	noarch
Source0:	carol-cmi-%{version}-src.tar.gz
Source1:	cmi-%{version}.pom
Patch0:         carol-cmi-DistributedEquivSystem.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:	ant >= 0:1.7.1
BuildRequires:	junit >= 0:3.8.1
BuildRequires:	asm >= 0:1.5.3

BuildRequires:  geronimo-ejb-2.1-api
BuildRequires:  geronimo-servlet-2.4-api

BuildRequires:  apache-commons-collections >= 3.1
BuildRequires:  apache-commons-logging >= 1.0.4
BuildRequires:  jgroups
BuildRequires:  mx4j
BuildRequires:  velocity
Requires:  asm >= 0:1.5.3
Requires:  apache-commons-collections >= 3.1
Requires:  apache-commons-logging >= 1.0.4
Requires:  jgroups
Requires:  mx4j
Requires:  velocity
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
CMI: "Cluster aware" distribution protocol.


%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:	Documents for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description manual
Documents for %{name}.

%prep
%setup -qq -n cmi
chmod -R go=u-w *
%patch0 -b .sav0
find . -name "*.jar" \
       -exec rm -f {} \;

%build
build-jar-repository externals \
geronimo-ejb-2.1-api \
geronimo-servlet-2.4-api \
asm/asm \
commons-collections \
commons-logging \
jgroups \
mx4j/mx4j \
velocity \

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar jdoc doc 

%install
                                                                                
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 archive/output/dist/lib/ow_cmi.jar \
        $RPM_BUILD_ROOT%{_javadir}/ow_%{jarname}-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
ln -sf ow_%{jarname}-%{version}.jar ow_%{jarname}.jar
popd

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -m 644 config/configure.properties \
		$RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-ow_%{jarname}.pom
%add_to_maven_depmap org.objectweb.carol cmi %{version} JPP ow_%{jarname}


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/jdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

#manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr output/dist/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_javadir}/ow_%{jarname}.jar
%{_javadir}/ow_%{jarname}-%{version}.jar
%{_datadir}/%{name}-%{version}
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7-alt3_3jpp6
- new jpp relase

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7-alt3_2jpp5
- build with ant17

* Thu Apr 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7-alt2_2jpp5
- new jpp release

* Fri Oct 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7-alt2_1jpp5
- fixed build with new jgroups

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7-alt1_1jpp1.7
- converted from JPackage by jppimport script

