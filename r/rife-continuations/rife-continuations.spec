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

%define gcj_support 0


Name:           rife-continuations
Summary:        RIFE continuations
Url:            http://rifers.org/wiki/display/RIFECNT/Home
Version:        0.1
Release:        alt1_2jpp5
Epoch:          0
License:        LGPL
Group:          Development/Java
Source0:        rife-continuations-0.1.tar.gz
# svn export https://svn.rifers.org/rife-continuations/trunk/
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/rifers/rife-continuations/0.0.1/rife-continuations-0.0.1.pom
Patch0:         rife-continuations-0.1-build_xml.patch
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit >= 0:3.8.1
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
RIFE/continuations is a sub-project of RIFE that aims to 
make its support for continuations in pure Java available 
as a general-purpose library.
The current state is highly experimental and is basically 
an exact copy of the current RIFE continuations code with 
some minor changes.  We intend to improve this over time 
to make truly framework-agnostic.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
for f in $(find . -name "*.jar"); do
    mv $f $f.no
done
%patch0 -b .sav

%build
pushd lib
ln -sf $(build-classpath junit) .
popd
ant jar test javadocs

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/dist/%{name}-%{version}-snapshot.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap org.rifers %{name} 0.0.1 JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE_LGPL.txt
%doc LICENSE_CDDL.txt
%{_javadir}/*
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_2jpp5
- new jpackage release

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

