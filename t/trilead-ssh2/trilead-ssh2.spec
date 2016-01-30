Name: trilead-ssh2
Version: 217
Summary: SSH-2 protocol implementation in pure Java
License: BSD and MIT
Url: https://github.com/jenkinsci/trilead-ssh2
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(com.trilead:trilead-ssh2) = build217.jenkins.8
Provides: mvn(com.trilead:trilead-ssh2:pom:) = build217.jenkins.8
Provides: mvn(org.jenkins-ci:trilead-ssh2) = build217.jenkins.8
Provides: mvn(org.jenkins-ci:trilead-ssh2:pom:) = build217.jenkins.8
Provides: mvn(org.tmatesoft.svnkit:trilead-ssh2) = build217.jenkins.8
Provides: mvn(org.tmatesoft.svnkit:trilead-ssh2:pom:) = build217.jenkins.8
Provides: trilead-ssh2 = 217-6.jenkins8.fc23
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: trilead-ssh2-217-6.jenkins8.fc23.cpio

%description
Trilead SSH-2 for Java is a library which implements the SSH-2 protocol in pure
Java (tested on J2SE 1.4.2 and 5.0). It allows one to connect to SSH servers
from within Java programs. It supports SSH sessions (remote command execution
and shell access), local and remote port forwarding, local stream forwarding,
X11 forwarding and SCP. There are no dependencies on any JCE provider, as all
crypto functionality is included.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
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

