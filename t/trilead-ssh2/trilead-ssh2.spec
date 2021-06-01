Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global buildver 217
%global patchlvl 21

Name:           trilead-ssh2
Version:        %{buildver}.%{patchlvl}
Release:        alt1_3jpp11
Summary:        SSH-2 protocol implementation in pure Java

# Project is under BSD, but some parts are MIT licensed
# see LICENSE.txt for more information
# One file is ISC licensed: The bundled implementation of BCrypt.java
# One file is RSA licensed: src/com/trilead/ssh2/crypto/digest/MD5.java
License:        BSD and MIT and ISC and RSA

# Jenkins fork is used because the original sources of this library,
# "ganymed" and then "trilead" are both defunct and the original
# project sites are unavailable. However Jenkins project continues
# to maintain it
URL:            https://github.com/jenkinsci/trilead-ssh2
Source0:        https://github.com/jenkinsci/trilead-ssh2/archive/%{name}-build-%{buildver}-jenkins-%{patchlvl}.tar.gz

# Source of bundled BCrypt implementation, taken from:
# https://mvnrepository.com/artifact/org.connectbot.jbcrypt/jbcrypt/1.0.0
Source1:  BCrypt.java
Provides: bundled(jbcrypt) = 1.0.0

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(net.i2p.crypto:eddsa)

BuildArch:      noarch
Source44: import.info

%description
Trilead SSH-2 for Java is a library which implements the SSH-2 protocol in pure
Java (tested on J2SE 1.4.2 and 5.0). It allows one to connect to SSH servers
from within Java programs. It supports SSH sessions (remote command execution
and shell access), local and remote port forwarding, local stream forwarding,
X11 forwarding and SCP. There are no dependencies on any JCE provider, as all
crypto functionality is included.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-build-%{buildver}-jenkins-%{patchlvl}

# jbcrypt is not available in Fedora, it is bundled instead
mkdir -p src/org/mindrot/jbcrypt
cp -p %{SOURCE1} src/org/mindrot/jbcrypt
%pom_remove_dep "org.connectbot.jbcrypt:jbcrypt"

# test dependency not available in Fedora
%pom_remove_dep "org.testcontainers:testcontainers"

# compat symlink/alias
%mvn_file  : %{name}/%{name} %{name}
%mvn_alias : "org.tmatesoft.svnkit:trilead-ssh2" "com.trilead:trilead-ssh2"

%build
# Skip tests due to unavailability of test deps
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%doc HISTORY.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:217.21-alt1_3jpp11
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:217-alt1_12.jenkins8jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:217-alt1_10.jenkins8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:217-alt1_9.jenkins8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:217-alt1_8.jenkins8jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:217-alt1_7.jenkins8jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:217-alt1_6.jenkins8jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:217-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:215-alt1_1jpp7
- update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:213-alt2_10_redhat_1jpp6
- new jpp relase

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:213-alt2_5jpp6
- added pom

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 213-alt1_6jpp6
- new version

