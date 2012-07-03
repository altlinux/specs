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

%global parent plexus
%global subname container-default

Name:           plexus-container-default
Version:        1.0
Release:        alt5_0.8.a9jpp7
Epoch:          0
Summary:        Default Plexus Container
License:        ASL 2.0 and MIT
Group:          Development/Java
URL:            http://plexus.codehaus.org/
# git clone git://github.com/sonatype/plexus-containers.git
# git archive --format=tar --prefix=plexus-containers/ plexus-container-default-1.0-alpha-9-stable-1 | gzip > plexus-container-default-1.0-alpha-9-stable-1-src.tgz
Source0:        %{name}-1.0-alpha-9-stable-1-src.tgz
# test ClassicSingletonComponentManagerTest.testThreads10() fails in koji
# (dev says it fails randomly)
Patch0:         %{name}-fixed-test.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  junit
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven
BuildRequires:  classworlds >= 0:1.1
BuildRequires:  plexus-utils
Requires:  classworlds >= 0:1.1
Requires:  plexus-utils
Source44: import.info

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n plexus-containers
%patch0 -p1

%build
mvn-rpmbuild install javadoc:aggregate


%install
# jars
install -d -m 755 %{buildroot}%{_javadir}/%{parent}
install -pm 644 target/%{name}-%{version}-alpha-9-stable-1.jar \
  %{buildroot}%{_javadir}/%{parent}/%{subname}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{parent}-%{subname}.pom

# we don't provide depmap on purpose. If anyone wants to use this old
# code they should do extra work

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%{_javadir}/%{parent}
%{_mavenpomdir}/JPP.%{parent}-%{subname}.pom

%files javadoc
%{_javadocdir}/*


%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.8.a9jpp7
- fc build

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.a9s1.2jpp6
- added maven2-plugin-site dep

* Tue Sep 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a9s1.2jpp6
- update to a9.2

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a9s1.1jpp5
- fixed build

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a9s1.1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a8.3jpp1.7
- build with maven2

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a8.3jpp1.7
- converted from JPackage by jppimport script

* Sun Dec 04 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt0.1.alpha8
- Rebuild for ALTLinux Sisyphus
- spec cleanup

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a8.1jpp
- First JPackage build

