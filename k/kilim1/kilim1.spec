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


Name:           kilim1
Version:        1.1.3
Release:        alt1_5jpp6
Epoch:          0
Summary:        A generic configuration framework for Java
License:        BSD
URL:            http://kilim.objectweb.org/
Group:          Development/Java
Source0:        http://download.us.forge.objectweb.org/kilim/Kilim_1_1_3-src.tar.gz
Source1:        kilim-1.1.3.pom
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  nanoxml-lite
Requires:       nanoxml-lite
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
Kilim is a generic configuration framework for Java, which can be used
easily with existing applications, frameworks, and systems. It was
originally built into Jonathan in order to allow fine configuration of
its various frameworks (protocols, resource management policies, etc.)
without requiring specific code, and has since grown independently of
Jonathan.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
Documents for %{name}.

%prep
%setup -q -n kilim
find . -name "*.jar" -exec rm -f {} \;
find . -type d -name "CVS" | xargs rm -rf

%build
export CLASSPATH=$(build-classpath nanoxml-lite)
pushd externals
for jar in $(echo $CLASSPATH | sed 's/:/ /g'); do
ln -sf ${jar} .
done
popd
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 distrib javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 distrib/kilim.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 distrib/kilim-tools.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tools-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap kilim kilim %{version} JPP %{name}

install -p -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -m 644 Readme.txt $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/apis/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/GettingStarted $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_javadir}/*.jar
%doc %{_datadir}/%{name}-%{version}/Readme.txt
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%dir %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_5jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_4jpp5
- new jpp release

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_3jpp1.7
- converted from JPackage by jppimport script

