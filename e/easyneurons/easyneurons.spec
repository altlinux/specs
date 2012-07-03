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

%define gcj_support 0


Name:           easyneurons
Version:        2.4
Release:        alt1_1jpp6
Epoch:          0
Summary:        Neuroph Neural Network Editor

Group:          Development/Java
License:        LGPL
URL:            http://neuroph.sourceforge.net
Source0:        easyneurons-2.4.tgz
# svn export http://neuroph.svn.sourceforge.net/svnroot/neuroph/trunk/easyneurons easyneurons-2.4
#Patch0:         neuroph-build-xml.patch
Source1:        AbsoluteLayout.jar
Source2:        %{name}-run.sh

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7.1
BuildRequires: jakarta-commons-io
BuildRequires: appframework
BuildRequires: colt
BuildRequires: javahelp2
BuildRequires: jung2
BuildRequires: neuroph = %{epoch}:%{version}
BuildRequires: sf-collections-generic
BuildRequires: swing-layout
BuildRequires: xstream
#Requires(post):    jpackage-utils >= 0:5.0.0
#Requires(postun):  jpackage-utils >= 0:5.0.0
Requires: jakarta-commons-io
Requires: appframework
Requires: colt
Requires: javahelp2
Requires: jung2
Requires: neuroph = %{epoch}:%{version}
Requires: sf-collections-generic
Requires: swing-layout
Requires: xstream
Source44: import.info

%description
Neuroph also has  nice GUI neural network editor to quickly 
create Java neural network components. 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q
#%patch0 -b .sav0
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done


%build
export CLASSPATH=$(build-classpath xstream neuroph jung2 sf-collections-generic appframework javahelp2):%{SOURCE1}
ant -Dbuild.sysclasspath=first -Dno.dependencies=true

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 dist/easyNeurons.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadocs
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# home
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/run.sh

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*
#%{_mavendepmapfragdir}/*
#%{_datadir}/maven2/poms/*
%dir %{_datadir}/%{name}/bin
%attr(755, root, root) %{_datadir}/%{name}/bin/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_1jpp6
- new version

