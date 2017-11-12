Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global patchlvl 8

Name:           trilead-ssh2
Version:        217
Release:        alt1_9.jenkins8jpp8
Summary:        SSH-2 protocol implementation in pure Java

# project is under BSD, but some parts are MIT licensed
# see LICENSE.txt for more information
License:        BSD and MIT
URL:            https://github.com/jenkinsci/trilead-ssh2
Source0:        https://github.com/jenkinsci/%{name}/archive/%{name}-build%{version}-jenkins-%{patchlvl}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)

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
%setup -q -n %{name}-%{name}-build%{version}-jenkins-%{patchlvl}

# compat symlink/alias
%mvn_file  : %{name}/%{name} %{name}
%mvn_alias : "org.tmatesoft.svnkit:trilead-ssh2" "com.trilead:trilead-ssh2"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt HISTORY.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
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

