BuildRequires: javapackages-local
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

%define gcj_support 0


Name:           jardiff
Version:        0.2
Release:	alt9_3jpp6
Epoch:          0
Summary:        Jar Diff Util
License:        BSD
Group:          Development/Java
URL:            http://www.osjava.org/jardiff/
Source0:        http://dist.osjava.org/releases/official/jardiff/jardiff-0.2-src.tar.gz
Source1:        %{name}-%{version}.pom

# debian patches from jardiff_0.2-4.debian
Patch1: 01_fix_build_with_asm3.diff
Patch2: 02_fix_build_with_asm4.diff

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif


%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils 
BuildRequires: ant 
BuildRequires: ant-junit
BuildRequires: objectweb-asm3
BuildRequires: apache-commons-cli

Requires: objectweb-asm3
Requires: apache-commons-cli

%description
A tool to help visualise API differences between two 
different versions of a project. Jardiff takes two jar 
files and outputs all the public API changes as xml, 
html or plain text. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q 
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%patch1 -p1
# TODO for objectweb-asm4
#patch2 -p1

%build
export CLASSPATH=$(build-classpath \
objectweb-asm3/asm \
objectweb-asm3/asm-commons \
commons-cli \
)
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6  -Dbuild.sysclasspath=only jar test javadoc


%install
# jars
install -d -m 755 %buildroot%{_javadir}
install -m 644 target/%{name}-%{version}.jar %buildroot%{_javadir}/%{name}.jar

# TODO maven support
install -d -m 755 %buildroot%{_mavenpomdir}
install -m 644 %{SOURCE1} %buildroot%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%jpackage_script org.osjava.jardiff.Main "" "" jardiff:commons-cli:objectweb-asm3/asm:objectweb-asm3/asm-commons %name true

# javadoc
install -d -m 755 %buildroot%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %buildroot%{_javadocdir}/%{name}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files -f .mfiles
%{_bindir}/%name
%{_javadir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt9_3jpp6
- added BR: javapackages-local for javapackages 5

* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt8_3jpp6
- added maven metadata and script

* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt7_3jpp6
- fixed build
- TODO: script
- TODO: properly install maven pom

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt6_3jpp5
- use junit 4

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt5_3jpp5
- fixed build

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt4_3jpp5
- explicitly use junit3

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt3_3jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt2_3jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_1jpp5
- converted from JPackage by jppimport script

