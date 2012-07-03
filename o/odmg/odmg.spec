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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/odmg/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           odmg
Version:        3.0
Release:	alt1_7jpp6
Epoch:          0
Summary:        ODMG 3.0 Java Binding 
Group:          Development/Java
License:        LGPLv2+
URL:            http://www.ozone-db.org/
# cvs -d :pserver:anonymous@cvs.ozone.sourceforge.net:/cvsroot/ozone login
# cvs -d :pserver:anonymous@cvs.ozone.sourceforge.net:/cvsroot/ozone -z3 export -r HEAD ozone/modules/odmg
Source0:        odmg-src.tar.gz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/odmg/odmg/3.0/odmg-3.0.pom
Source2:        odmg-component-info.xml
Patch0:         odmg-build_xml.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: ant
BuildRequires: jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
Interfaces and Exceptions for ODMG 3.0

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

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
%{summary}.

%prep
%setup -q -n odmg
%patch0 -p0 -b .sav0

%{__mkdir_p} server/lib
%{__rm} -r src/org/ozoneDB

%{__cat} > build.properties << EOF
name=ozone
version.separator=-
EOF

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist.bin

%install

# jar
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/dist/ozoneODMG-0.1.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap odmg odmg %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/odmg.jar
cp -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/odmg.pom
%endif

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_7jpp6
- added pom

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_5jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_4jpp5
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

