%define _unpackaged_files_terminate_build 1

# Copyright (c) 2000-2012, JPackage Project
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

Name: aspectj
Version: 1.9.26
Release: alt1

Summary: AspectJ pointcut matching libraries
License: EPL-2.0 AND Apache-1.1 AND BSD-3-Clause
Group: Development/Java
Url: https://www.eclipse.org/aspectj
VCS: https://github.com/eclipse-aspectj/aspectj.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-11-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)

%description
AspectJ is an aspect-oriented extension for Java. This package contains its
pointcut matcher. Runtime support and bytecode weaving are packaged separately.
The compiler requires a separate AspectJ-patched Eclipse JDT build.

%package -n aspectjrt
Summary: AspectJ runtime library
License: EPL-2.0
Group: Development/Java

%description -n aspectjrt
AspectJ runtime classes and annotations used by applications compiled or
instrumented with AspectJ.

%package -n aspectjweaver
Summary: AspectJ bytecode weaving library
Group: Development/Java

%description -n aspectjweaver
The AspectJ weaver library for load-time and post-compile bytecode weaving.

%prep
%setup -q
%patch0 -p1
# This module only provisions legacy test libraries from the network. It is
# pulled in through test-scoped edges; those tests are not run in the RPM build.
%pom_remove_dep -r :lib
%pom_xpath_set pom:properties/pom:commons.logging.version 1.3.6
%pom_xpath_set pom:properties/pom:asm.version 9.11.1

# These plugins produce website documentation, release checksums and upload
# POMs. XMvn registers the actual consumer artifacts below.
for module in aspectjrt aspectjweaver aspectjmatcher; do
    %pom_remove_plugin :truezip-maven-plugin "$module"
    %pom_remove_plugin :flatten-maven-plugin "$module"
    %pom_remove_plugin :checksum-maven-plugin "$module"
    %pom_remove_plugin :maven-javadoc-plugin "$module"
    %pom_remove_plugin :maven-antrun-plugin "$module"
done
%pom_remove_plugin :maven-dependency-plugin aspectjweaver
# Retain the ALT system-ASM policy instead of embedding and relocating ASM.
%pom_remove_plugin :maven-shade-plugin aspectjweaver

%mvn_package :aspectjrt aspectjrt
%mvn_package :aspectjweaver aspectjweaver
%mvn_package :aspectjmatcher aspectj

%build
# Java 8 is the upstream target; Java 11 is the oldest packaged build JDK.
%mvn_build -s -f -j -- \
  -pl aspectjrt,aspectjweaver,aspectjmatcher -am \
  -Dmaven.source.skip=true \
  -Dmaven.javadoc.skip=true

# The upstream release POM flattener removes dependencies from assembled JARs.
# Keep upstream descriptive/license metadata and register only external deps.
mv .xmvn-reactor .xmvn-reactor-build
for module in aspectjrt aspectjweaver aspectjmatcher; do
    %pom_remove_dep 'org.aspectj:*' "$module"
    %pom_remove_parent "$module"
    %pom_xpath_inject pom:project \
      '<groupId>org.aspectj</groupId><version>%version</version>' "$module"
    %pom_xpath_remove pom:build "$module"
done
%pom_change_dep org.ow2.asm:asm org.ow2.asm:asm:9.11.1 aspectjweaver
%pom_change_dep org.ow2.asm:asm-commons \
  org.ow2.asm:asm-commons:9.11.1 aspectjweaver
%pom_add_dep commons-logging:commons-logging:1.3.6 aspectjweaver
%pom_add_dep commons-logging:commons-logging:1.3.6 aspectjmatcher
%mvn_artifact aspectjrt/pom.xml \
  aspectjrt/target/aspectjrt-%version.jar
%mvn_artifact aspectjweaver/pom.xml \
  aspectjweaver/target/aspectjweaver-%version.jar
%mvn_artifact aspectjmatcher/pom.xml \
  aspectjmatcher/target/aspectjmatcher-%version.jar

%install
%mvn_install

%files -f .mfiles-aspectj
%doc LICENSE docs/LICENSE-AspectJ.adoc docs/licenses/LICENSE-BSD-3-CLAUSE.txt
%doc README.md

%files -n aspectjrt -f .mfiles-aspectjrt
%doc LICENSE

%files -n aspectjweaver -f .mfiles-aspectjweaver
%doc LICENSE docs/LICENSE-AspectJ.adoc
%doc docs/licenses/LICENSE-Apache-1.1.txt
%doc docs/licenses/LICENSE-BSD-3-CLAUSE.txt

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 1.9.26-alt1
- New version.

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt4_1jpp6
- applied repocop patches

* Thu Oct 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt3_1jpp6
- merged aspectjweaver back

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt1_1jpp6
- new version

* Sat Oct 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.11-alt1_1jpp6
- new version

* Fri Oct 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.5-alt1_1jpp6
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt1_1jpp6
- new version

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt3_1jpp6
- build with saxon6

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt2_1jpp6
- fixed build

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt1_1jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt3_2jpp5
- fixed build with eclipse 3.5

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_2jpp5
- rebuild with eclipse 3.4

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_2jpp5
- new version
