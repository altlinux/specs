Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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

Name:           jarjar
Version:        1.4
Release:        alt1_18jpp8
Summary:        Jar Jar Links
License:        ASL 2.0
URL:            http://code.google.com/p/jarjar/
Source0:        http://jarjar.googlecode.com/files/jarjar-src-1.4.zip
Source1:        jarjar.pom
Source2:        jarjar-util.pom
Patch0:         fix-maven-plugin.patch
Patch1:         do-not-embed-asm.patch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  objectweb-asm
BuildRequires:  javapackages-local
BuildRequires:  maven
Requires:       objectweb-asm

BuildArch:      noarch
Source44: import.info

%description
Jar Jar Links is a utility that makes it easy to repackage Java 
libraries and embed them into your own distribution. This is 
useful for two reasons:
You can easily ship a single jar file with no external dependencies. 
You can avoid problems where your library depends on a specific 
version of a library, which may conflict with the dependencies of 
another library.

%package maven-plugin
Group: Development/Java
Summary:        Maven plugin for %{name}
Requires:       maven
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description maven-plugin
%{summary}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch0
%patch1

# remove all binary libs
rm -f lib/*.jar

%mvn_package :jarjar-plugin %{name}-maven-plugin

# create ant config
echo "jarjar/jarjar objectweb-asm/asm objectweb-asm/asm-commons" > jarjar.ant

%build
pushd lib
ln -sf $(build-classpath objectweb-asm/asm) asm-4.0.jar
ln -sf $(build-classpath objectweb-asm/asm-commons) asm-commons-4.0.jar
ln -sf $(build-classpath maven/maven-plugin-api) maven-plugin-api.jar
popd
export CLASSPATH=$(build-classpath ant)
ant jar jar-util javadoc mojo test

sed -i -e s/@VERSION@/%{version}/g maven/pom.xml

# request maven artifact installation
%mvn_artifact %{SOURCE1} dist/jarjar-%{version}.jar
%mvn_artifact %{SOURCE2} dist/jarjar-util-%{version}.jar
%mvn_artifact maven/pom.xml dist/jarjar-plugin-%{version}.jar
%mvn_alias tonic:jarjar jarjar:jarjar com.tonicsystems:jarjar com.googlecode.jarjar:jarjar org.gradle.jarjar:jarjar
%mvn_alias tonic:jarjar-util jarjar:jarjar-util com.tonicsystems:jarjar-util
%mvn_alias com.tonicsystems.jarjar:jarjar-plugin jarjar:jarjar-plugin tonic:jarjar-plugin com.tonicsystems:jarjar-plugin

%install
%mvn_install -J dist/javadoc

%jpackage_script com.tonicsystems.jarjar.Main "" "" jarjar/jarjar:objectweb-asm/asm:objectweb-asm/asm-commons %{name} true

# install ant config
install -m 644 -D jarjar.ant %{buildroot}%{_sysconfdir}/ant.d/jarjar

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc COPYING
%{_bindir}/%{name}
%{_sysconfdir}/ant.d/jarjar
%dir %{_javadir}/%{name}
%config(noreplace,missingok) /etc/java/%{name}.conf

%files maven-plugin -f .mfiles-%{name}-maven-plugin
%doc COPYING

%files javadoc -f .mfiles-javadoc
%doc COPYING

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_18jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_17jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_16jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_15jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_4jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_6jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_6jpp7
- new release

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp7
- fc version

* Tue Jan 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp6
- fixed build of portals-bridges

* Tue Jan 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_3jpp6
- added compat depmap

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_2jpp5
- converted from JPackage by jppimport script

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_1jpp1.7
- updated to new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_2jpp1.7
- converted from JPackage by jppimport script

