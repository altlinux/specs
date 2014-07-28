Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
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

Name:           relaxngDatatype
Version:        1.0
Release:        alt4_10.4jpp7
Summary:        RELAX NG Datatype API

Group:          Development/Java
License:        BSD
URL:            https://sourceforge.net/projects/relaxng
# wget http://netcologne.dl.sourceforge.net/project/relaxng/datatype%20%28java%29/Ver.%{version}/%{name}-%{version}.zip
Source0:        http://netcologne.dl.sourceforge.net/project/relaxng/datatype%%20%%28java%%29/Ver.%{version}/%{name}-%{version}.zip
Source1:        http://repo1.maven.org/maven2/%{name}/%{name}/20020414/%{name}-20020414.pom
Patch0:         %{name}-compressjar.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
Requires:       jpackage-utils
Provides:       msv <= %{version}
Obsoletes:      msv <= %{version}
Source44: import.info

%description
RELAX NG is a public space for test cases and other ancillary software
related to the construction of the RELAX NG language and its
implementations.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p0

%build
ant -Dbuild.sysclasspath=only
sed -i 's/\r//g' copying.txt

%install
install -Dpm 644 %{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
pushd $RPM_BUILD_ROOT%{_javadocdir}/%{name}
for f in `find -name \*.html -o -name \*.css`; do
    sed -i 's/\r//g' $f > /dev/null
done
popd

# POM and depmap
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

%files
%doc copying.txt
%{_javadir}/*.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}*

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_10.4jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_8.3jpp7
- rebuild to properly resolve msv conflict

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_8.3jpp7
- update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp5
- use default jpp profile

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_3jpp5
- converted from JPackage by jppimport script

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Sun Apr 24 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux Sisyphus

