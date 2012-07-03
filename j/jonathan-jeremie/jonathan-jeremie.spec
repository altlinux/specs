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


Name:           jonathan-jeremie
Version:        4.2.2
Release:        alt2_3jpp6
Epoch:          0
Summary:        Distributed Object Platform (DOP) written entirely in Java
License:        LGPL
URL:            http://jonathan.objectweb.org/
Group:          Development/Java
Source0:        %{name}-%{version}-src.tar.gz
Source1:        %{name}-%{version}.pom
# cvs -d:pserver:anonymous@cvs.forge.objectweb.org:/cvsroot/jonathan login
# cvs -z3 -d:pserver:anonymous@cvs.forge.objectweb.org:/cvsroot/jonathan export -r JEREMIE_4_2_2 jeremie
Patch0:         jonathan-jeremie-build.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  jonathan-core >= 0:4.1
BuildRequires:  kilim1
BuildRequires:  monolog
BuildRequires:  objectweb-anttask
Requires:       jonathan-core >= 0:4.1
Requires:       kilim1
Requires:       monolog
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
JEREMIE is an implementation of RMI provided by the Jonathan
Objectweb project. It provides local call (RMI calls within 
a same JVM) optimization.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -qq -n jeremie
find . -name "*.jar" -exec rm -f {} \;
%patch0 -b .sav0

%build
export CLASSPATH=

pushd config
    ln -sf $(build-classpath objectweb-anttask) ow_util_ant_tasks.jar
popd
pushd externals
    ln -sf $(build-classpath monolog/ow_util_log_api) .
    # jonathan-core needs kilim1 and nanoxml-lite
    ln -sf $(build-classpath nanoxml-lite) .
    ln -sf $(build-classpath kilim1) kilim.jar
    ln -sf $(build-classpath jonathan-core) .
popd

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar jdoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 output/dist/lib/jeremie.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/ && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.objectweb.jonathan jeremie %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/doc/javadoc/user/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%files
%{_javadir}/*
%doc README.txt
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.2-alt2_3jpp6
- new jpp relase

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.2-alt2_2jpp5
- build with ant17

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.2.2-alt1_2jpp5
- new jpp release

* Mon Jul 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.2.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

