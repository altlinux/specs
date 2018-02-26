Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
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

%define _with_gcj_support 0

%define gcj_support 0

%define snapshot	20001002


Name:		cryptix
Version:	3.2.0
Release:	alt1.11_9jpp5
Epoch:		0
Summary:	Java crypto package
License:	BSD
Url:		http://www.cryptix.org
Group:		Development/Java
Source0:	%{name}32-%{snapshot}-r%{version}-RHCLEAN.zip
Source1:	%{name}.build.script
Patch0:          cryptix-jdk15-compatibility.patch
BuildRequires: ant
%if ! %{gcj_support}
BuildArch:	noarch
%endif

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
Cryptix 3 is a cleanroom implementation of Sun's Java Cryptography
Extensions (JCE) version 1.1. In addition to that it contains the
Cryptix Provider which delivers a wide range of algorithms and support
for PGP 2.x. Cryptix 3 runs on both JDK 1.1 and JDK 1.2 (Java 2).

%package javadoc
Group:		Development/Documentation
Summary:	Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -c
cp %{SOURCE1} build.xml
# remove all binary libs
rm -fr $(find . -name "*.jar")
# correct silly permissions
chmod -R go=u-w *

%patch0 -b .sav

%build
export CLASSPATH=

ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 clean jar javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%post
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc LICENCE.TXT README.TXT
%{_javadir}/*

%if %{gcj_support}
%{_libdir}/gcj/%{name}/cryptix-3.2.0.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1.11_9jpp5
- build fixed; from fedora 9

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_9jpp1.7
- converted from JPackage by jppimport script

