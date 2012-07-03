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


Name:           jzlib
Version:        1.0.7
Release:        alt1_5jpp6
Epoch:          0
Summary:        JZlib re-implementation of zlib in pure Java

Group:          Development/Java
License:        BSD-style
URL:            http://www.jcraft.com/jzlib/
Source0:        http://www.jcraft.com/jzlib/jzlib-1.0.7.tar.gz
Source1:        %{name}_build.xml
Source2:        http://repo1.maven.org/maven2/com/jcraft/jzlib/1.0.7/jzlib-1.0.7.pom

%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
The zlib is designed to be a free, general-purpose, legally unencumbered 
-- that is, not covered by any patents -- lossless data-compression 
library for use on virtually any computer hardware and operating system. 
The zlib was written by Jean-loup Gailly (compression) and Mark Adler 
(decompression). 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%package        demo
Summary:        Examples for %{name}
Group:          Development/Java

%description    demo
%{summary}.


%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} build.xml
mkdir src
mv com src

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  dist javadoc 

%install
# jars
install -Dm 644 dist/lib/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# pom
install -Dm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.jcraft %{name} %{version} JPP %{name}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# examples
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr example/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}


%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%doc LICENSE.txt
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*


%if %{gcj_support}
%{_libdir}/gcj/%{name}/jzlib-1.0.7.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}*

%files demo
%doc %{_datadir}/%{name}-%{version}

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt1_5jpp6
- jpp 6 release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt1_4jpp5
- new jpackage release

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt1_4jpp1.7
- converted from JPackage by jppimport script

