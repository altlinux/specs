# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
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

%global base_name oro

Name:           jakarta-oro
Version:        2.0.8
Release:        alt2_13jpp7
Epoch:          0
Summary:        Full regular expressions API
License:        ASL 1.1
Group:          Development/Java
Source0:        http://archive.apache.org/dist/jakarta/oro/%{name}-%{version}.tar.gz
Source1:        MANIFEST.MF
Source2:        http://repo1.maven.org/maven2/%{base_name}/%{base_name}/%{version}/%{base_name}-%{version}.pom
Patch1:         %{name}-build-xml.patch
URL:            http://jakarta.apache.org/oro
BuildRequires:  jpackage-utils > 1.6
BuildRequires:  ant
BuildArch:      noarch
Requires:       jpackage-utils
Source44: import.info
Provides: oro = %epoch:%version-%release
Source45: oro-2.0.8.pom

%description
The Jakarta-ORO Java classes are a set of text-processing Java classes
that provide Perl5 compatible regular expressions, AWK-like regular
expressions, glob expressions, and utility classes for performing
substitutions, splits, filtering filenames, etc. This library is the
successor to the OROMatcher, AwkTools, PerlTools, and TextTools
libraries from ORO, Inc. (www.oroinc.com). 

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
# remove all CVS files
for dir in `find . -type d -name CVS`; do rm -rf $dir; done
for file in `find . -type f -name .cvsignore`; do rm -rf $file; done

%patch1
cp %{SOURCE1} .

%build
ant -Dfinal.name=%{base_name} jar javadocs

%install
#jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{base_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}.jar %{base_name}.jar)
#javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf docs/api

# POM and depmap
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap
# pom
mkdir -p %{buildroot}%{_mavenpomdir}
cp -p %{SOURCE45} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap oro oro %{version} JPP %{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc COMPILE ISSUES README TODO CHANGES CONTRIBUTORS LICENSE STYLE
%{_javadir}/*.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%_mavendepmapfragdir/*
%_mavenpomdir/*.pom

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt2_13jpp7
- new release

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt2_11jpp7
- fc update

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt2_6jpp6
- added osgi manifest

* Thu Feb 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt1_6.3jpp5
- build for new eclipse version

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Thu Feb 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.8-alt1
- New upstream release

* Tue Sep 16 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.7-alt1
- Adapted for Sisyphus from JPackage project.
