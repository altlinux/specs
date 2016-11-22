Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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

%global cvstag  release-20050331

Name:           isorelax
Summary:        Public interfaces for RELAX Core
URL:            http://iso-relax.sourceforge.net/
Epoch:          2
Version:        0
# I can't use %%{cvstag} as dashes aren't allowed in Release tags
Release:        alt1_0.19.release20050331jpp8
License:        MIT and ASL 1.1
BuildArch:      noarch

# mkdir isorelax-release-20050331-src
# cd isorelax-release-20050331-src
# cvs -d:pserver:anonymous@iso-relax.cvs.sourceforge.net:/cvsroot/iso-relax \
#   export -r release-20050331 src lib
# cvs -d:pserver:anonymous@iso-relax.cvs.sourceforge.net:/cvsroot/iso-relax \
#   co -r release-20050331 build.xml
# rm -rf CVS
# cd ..
# tar cjf isorelax-release-20050331-src.tar.bz2 isorelax-release-20050331-src
Source0:        %{name}-%{cvstag}-src.tar.bz2
# There's no license in the upstream tarball so include it here
Source1:        license.txt
Source2:        http://repo2.maven.org/maven2/%{name}/%{name}/20030108/%{name}-20030108.pom
Patch0:         %{name}-apidocsandcompressedjar.patch

BuildRequires:  javapackages-local
BuildRequires:  ant
Source44: import.info

%description
The ISO RELAX project was started to host public interfaces 
useful for applications to support RELAX Core. Now, however,
some of the hosted material is schema language-neutral.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{cvstag}-src
find -name "*.jar" -delete
ln -s %{_javadir}/ant.jar lib/
%patch0 -p0
cp %{SOURCE1} .

%build
ant release

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

# POM and depmap
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

%files -f .mfiles
%doc license.txt

%files javadoc
%doc license.txt
%{_javadocdir}/*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2:0-alt1_0.19.release20050331jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2:0-alt1_0.18.release20050331jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2:0-alt1_0.14.release20050331jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2:0-alt1_0.12.release20050331jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 2:0-alt1_0.10.release20050331jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt4_0.20041111.7jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt4_0.20041111.6jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt3_0.20041111.6jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt2_0.20041111.6jpp5
- converted from JPackage by jppimport script

