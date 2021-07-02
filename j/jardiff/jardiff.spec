%def_without asm3
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: javapackages-local
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


Name:           jardiff
Version:        0.2
Release:	alt11_3jpp6
Epoch:          0
Summary:        Jar Diff Util
License:        BSD
Group:          Development/Java
URL:            http://www.osjava.org/jardiff/
Source0:        http://dist.osjava.org/releases/official/jardiff/jardiff-0.2-src.tar.gz
Source1:        %{name}-%{version}.pom

#see https://packages.debian.org/ru/sid/jardiff
# debian patches from jardiff_0.2-5.debian
Patch1: 01_fix_build_with_asm3.diff
Patch2: 02_fix_build_with_asm4.diff

BuildArch:      noarch

BuildRequires: ant ant-junit
BuildRequires: apache-commons-cli
%if_with asm3
BuildRequires: objectweb-asm3
Requires: objectweb-asm3
%else
BuildRequires: objectweb-asm
%endif

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
# for objectweb-asm4,5
%if_without asm3
%patch2 -p1
%endif

%build
export CLASSPATH=$(build-classpath \
commons-cli \
%if_with asm3
objectweb-asm3/asm \
objectweb-asm3/asm-commons \
%else
objectweb-asm/asm \
objectweb-asm/asm-commons \
%endif
)
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6  -Dbuild.sysclasspath=only jar test javadoc

%if_with asm3
%pom_change_dep org.ow2.asm: asm:
%endif

%mvn_artifact %{SOURCE1} target/%{name}-%{version}.jar

%install
%mvn_install -J dist/docs

%if_with asm3
%jpackage_script org.osjava.jardiff.Main "" "" jardiff:commons-cli:objectweb-asm3/asm:objectweb-asm3/asm-commons %name true
%else
%jpackage_script org.osjava.jardiff.Main "" "" jardiff:commons-cli:objectweb-asm/asm:objectweb-asm/asm-commons %name true
%endif

%files -f .mfiles
%{_bindir}/%name

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Jul 02 2021 Igor Vlasenko <viy@altlinux.org> 0:0.2-alt11_3jpp6
- java11 build
- build with objectweb-asm 8

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 0:0.2-alt10_3jpp6
- use jvm_run

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

