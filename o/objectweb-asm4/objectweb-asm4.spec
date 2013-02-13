# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
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

Name:           objectweb-asm4
Version:        4.1
Release:        alt1_2jpp7
Epoch:          0
Summary:        A code manipulation tool to implement adaptable systems
License:        BSD
URL:            http://asm.objectweb.org/
Group:          Development/Java
Source0:        http://download.forge.objectweb.org/asm/asm-%{version}.tar.gz
# remove classpath from asm-xml manifest
# and fix Import-Package value
Patch0:         asm4-%{version}-fix-xml-manifest.patch
# Needed by asm-xml.jar
Requires:       xml-commons-jaxp-1.3-apis
Requires:       jpackage-utils >= 0:1.7.4
BuildRequires:  jpackage-utils >= 0:1.7.4
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  aqute-bnd
BuildRequires:  objectweb-anttask
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  zip
BuildArch:      noarch
Source44: import.info

%description
ASM is a code manipulation tool to implement adaptable systems.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %%{name}.

%prep
%setup -q -n asm-%{version}
sed -i 's/\r//' LICENSE.txt README.txt

%patch0 -p0

# remove ow2-1.3.pom, master pom, references
sed -ie '/<parent>/,/<\/parent/ {d}' archive/asm-parent.pom

# update asm gId
sed -i "s|<groupId>asm</groupId>|<groupId>org.ow2.asm</groupId>|" archive/*.pom
# fix system bndlib location. disable eclipse support ... unavailable deps
sed -i 's,${config}/biz.aQute.bnd.jar,%{_javadir}/aqute-bnd.jar,;s,eclipse="true",eclipse="false",' archive/*.xml

# eclipse plugin manifest headers
sed -i "s,Bundle-Vendor: France Telecom R&D,Bundle-Vendor: %providerName,;s,Bundle-Name: ASM all classes with debug info,Bundle-Name: %pluginName," archive/asm-all.bnd

%build

ant -Dobjectweb.ant.tasks.path=$(build-classpath objectweb-anttask) jar jdoc

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}
for jar in output/dist/lib/*.jar; do
  install -m 644 ${jar} %{buildroot}%{_javadir}/%{name}/`basename ${jar/-%{version}/}`
done

install -m 644 output/dist/lib/all/asm-all-%{version}.jar %{buildroot}%{_javadir}/%{name}/asm-all.jar
install -pm 644 output/dist/lib/all/asm-all-%{version}.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-asm-all.pom

# pom
for pom in output/dist/lib/*.pom; do
  install -pm 644 ${pom} %{buildroot}%{_mavenpomdir}/JPP.%{name}-`basename ${pom/-%{version}/}`
done

%add_maven_depmap JPP.%{name}-asm.pom %{name}/asm.jar
%add_maven_depmap JPP.%{name}-asm-analysis.pom %{name}/asm-analysis.jar
%add_maven_depmap JPP.%{name}-asm-commons.pom %{name}/asm-commons.jar
%add_maven_depmap JPP.%{name}-asm-tree.pom %{name}/asm-tree.jar
%add_maven_depmap JPP.%{name}-asm-util.pom %{name}/asm-util.jar
%add_maven_depmap JPP.%{name}-asm-xml.pom %{name}/asm-xml.jar
%add_maven_depmap JPP.%{name}-asm-all.pom %{name}/asm-all.jar
%add_maven_depmap JPP.%{name}-asm-parent.pom

# javadoc
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr output/dist/doc/javadoc/user/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt README.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt1_2jpp7
- fc update

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_2jpp7
- complete build

