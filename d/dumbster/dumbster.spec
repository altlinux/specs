# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Copyright (c) 2000-2007, JPackage Project
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

Summary:        Fake SMTP Server
Name:           dumbster
Version:        1.6
Release:        alt4_20jpp8
Epoch:          0
License:        ASL 2.0
URL:            http://quintanasoft.com/dumbster/
Group:          Development/Java
# cvs -z3 -d:pserver:anonymous@dumbster.cvs.sourceforge.net:/cvsroot/dumbster export -r RELEASE_1_6 dumbster
# tar czf dumbster-1.6-src.tgz dumbster
Source0:        %{name}-%{version}-src.tgz
Source1:        %{name}-1.6.pom
Patch0:         %{name}-SimpleSmtpServer.patch
BuildRequires:  ant
BuildRequires: javapackages-local rpm-build-java
BuildRequires:  javamail
BuildRequires:  junit
Requires:       java-sasl
Requires:       javamail

BuildArch:      noarch
Source44: import.info

%description
The Dumbster is a very simple fake SMTP server designed for
unit and system testing applications that send email messages.
It responds to all standard SMTP commands but does not deliver
messages to the user. The messages are stored within the
Dumbster for later extraction and verification.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%patch0
rm -f src/com/dumbster/smtp/SimpleSmtpServer.java.orig

%build
pushd lib
ln -sf $(build-classpath javamail)
ln -sf $(build-classpath junit)
popd

ant jar javadoc

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

install -p -m 644 build/%{name}.jar %{buildroot}%{_javadir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%doc license.txt

%files javadoc
%doc license.txt
%{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt4_20jpp8
- fixed build

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt3_20jpp8
- cleaned up dependencies

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_20jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_19jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_14jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_12jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_12jpp7
- fc update

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_6jpp6
- added pom

* Wed Jun 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_3jpp5
- smtp test was too long idle

* Tue Oct 23 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp1.7
- converted from JPackage by jppimport script

