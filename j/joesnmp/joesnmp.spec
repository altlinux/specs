Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/joesnmp/0.3.4-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           joesnmp
Version:        0.3.4
Release:	alt2_4jpp6
Epoch:          0
Summary:        Java SNMP class library 
Group:          Development/Java
License:        LGPLv2+
URL:            http://sourceforge.net/projects/joesnmp/
Source0:        joesnmp-0.3.4.zip
Source1:        http://repository.jboss.com/maven2/joesnmp/joesnmp/0.3.4/joesnmp-0.3.4.pom
Source2:        joesnmp-component-info.xml
Patch0:         joesnmp-0.3.3-build_xml.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: ant
BuildRequires: jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
joeSNMP is an open-source Java SNMP class library 
published under the LGPL.

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
%setup -q 
%patch0 -b .sav0
%{__perl} -pi -e 's/\r$//g' docs/FAQ.txt
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%build
export OPT_JAR_LIST=:
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dfilters.noload=true

%install

%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p output/lib/joesnmp.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap joesnmp joesnmp %{version} JPP %{name}

%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr output/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/joesnmp.jar
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/joesnmp.pom
%endif

%files
%doc docs/FAQ.txt
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
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.3.4-alt2_4jpp6
- added pom

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.3.4-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.3.4-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.3.4-alt1_1jpp1.7
- updated to new jpackage release

* Thu May 05 2005 Vladimir Lettiev <crux@altlinux.ru> 0.3.3-alt1
- Initial release for ALT Linux Sisyphus


