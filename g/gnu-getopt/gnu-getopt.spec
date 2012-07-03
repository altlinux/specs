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

%define repodir %{_javadir}/repository.jboss.com/gnu-getopt/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           gnu-getopt
Version:        1.0.13
Release:        alt1_4jpp6
Epoch:          0
Summary:        Java getopt implementation
License:        LGPLv2+
URL:            http://www.urbanophile.com/arenn/hacking/download.html
Source0:        http://www.urbanophile.com/arenn/hacking/getopt/java-getopt-%{version}.tar.gz
Source1:        gnu-getopt-component-info.xml
Source2:        gnu-getopt-%{version}.pom
Group:          Development/Java
Provides:       gnu.getopt = %{epoch}:%{version}-%{release}
Obsoletes:      gnu.getopt < %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: ant
BuildRequires: jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
The GNU Java getopt classes support short and long argument parsing in
a manner 100%% compatible with the version of GNU getopt in glibc 2.0.6
with a mostly compatible programmer's interface as well. Note that this
is a port, not a new implementation. I am currently unaware of any bugs
in this software, but there certainly could be some lying about. I would
appreciate bug reports as well as hearing about positive experiences.

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       gnu.getopt-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      gnu.getopt-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c
%{__mv} gnu/getopt/buildx.xml build.xml

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar javadoc

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/lib/gnu.getopt.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/gnu.getopt-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/gnu.getopt-%{version}
%{__ln_s} gnu.getopt-%{version} %{buildroot}%{_javadocdir}/gnu.getopt

# poms
%add_to_maven_depmap gnu-getopt getopt %{version} JPP %{name}
%add_to_maven_depmap urbanophile java-getopt %{version} JPP %{name}
%{__install} -D -p -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/gnu-getopt.jar $RPM_BUILD_ROOT%{repodirlib}/getopt.jar
%endif

%files
%doc gnu/getopt/COPYING.LIB gnu/getopt/README
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/gnu.getopt-%{version}.jar
%{_javadir}/gnu.getopt.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/gnu.getopt-%{version}
%{_javadocdir}/gnu.getopt

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt1_4jpp6
- new jpp release

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt1_3jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.12-alt2_6jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.12-alt1_6jpp5
- converted from JPackage by jppimport script

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.12-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0.11-alt1
- Initial build for ALT Linux Sisyphus

