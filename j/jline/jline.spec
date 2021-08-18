Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             jline
Version:          3.20.0
Release:          alt1_2jpp11
Summary:          Java library for handling console input
License:          BSD
URL:              https://github.com/jline/jline3
BuildArch:        noarch

Source0:          %{url}/archive/jline-parent-%{version}.tar.gz
# Adapt to newer versions of apache-sshd
Patch0:           %{name}-apache-sshd.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.googlecode.juniversalchardet:juniversalchardet)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.sshd:sshd-core) >= 2.6.0
BuildRequires:  mvn(org.apache.sshd:sshd-scp) >= 2.6.0
BuildRequires:  mvn(org.apache.sshd:sshd-sftp) >= 2.6.0
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.fusesource.jansi:jansi)

%global _desc \
JLine is a Java library for handling console input.  It is similar in\
functionality to BSD editline and GNU readline but with additional\
features that bring it in par with the ZSH line editor.  Those familiar\
with the readline/editline capabilities for modern shells (such as bash\
and tcsh) will find most of the command editing features of JLine to be\
familiar.
Source44: import.info

%description 
%_desc

This package contains the parent POM for the jline project

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc 
%_desc

This package contains the API documentation for %{name}.

%package        terminal
Group: Development/Java
Summary:        JLine terminal

%description    terminal 
%_desc

This package contains the basic terminal support for JLine.

%package        terminal-jansi
Group: Development/Java
Summary:        JLine terminal with JANSI
Requires:       %{name}-terminal = %{?epoch:%epoch:}%{version}-%{release}

%description    terminal-jansi 
%_desc

This package contains a functioning terminal based on JANSI.

%package        terminal-jna
Group: Development/Java
Summary:        JLine terminal with JNA
Requires:       %{name}-terminal = %{?epoch:%epoch:}%{version}-%{release}

%description    terminal-jna 
%_desc

This package contains a functioning terminal based on JNA.

%package        reader
Group: Development/Java
Summary:        JLine reader
Requires:       %{name}-terminal = %{?epoch:%epoch:}%{version}-%{release}

%description    reader 
%_desc

This package supports reading lines from a console with customizable key
bindings and input editing.

%package        style
Group: Development/Java
Summary:        JLine style
Requires:       %{name}-terminal = %{?epoch:%epoch:}%{version}-%{release}

%description    style 
%_desc

This package contains a style processor for JLine, which can apply
colors to strings, for example.

%package        builtins
Group: Development/Java
Summary:        JLine builtins
Requires:       %{name}-reader = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-style = %{?epoch:%epoch:}%{version}-%{release}
Requires:     mvn(com.googlecode.juniversalchardet:juniversalchardet)

%description    builtins 
%_desc

This package contains keybindings to emulate popular tools such as nano
and less.

%package        console
Group: Development/Java
Summary:        JLine console
Requires:       %{name}-builtins = %{?epoch:%epoch:}%{version}-%{release}

%description    console 
%_desc

This package contains a console with command and script execution
support, and tab completion.

%package        remote-ssh
Group: Development/Java
Summary:        JLine remote SSH
Requires:       %{name}-builtins = %{?epoch:%epoch:}%{version}-%{release}
Requires:     mvn(org.apache.sshd:sshd-core) >= 2.6.0
Requires:     mvn(org.apache.sshd:sshd-scp) >= 2.6.0
Requires:     mvn(org.apache.sshd:sshd-sftp) >= 2.6.0

%description    remote-ssh 
%_desc

This package contains an ssh client.

%package        remote-telnet
Group: Development/Java
Summary:        JLine remote telnet
Requires:       %{name}-builtins = %{?epoch:%epoch:}%{version}-%{release}
Requires:     mvn(org.apache.sshd:sshd-core) >= 2.6.0

%description    remote-telnet 
%_desc

This package contains a telnet client.

%prep
%setup -q -n jline3-jline-parent-%{version}
%patch0


# remove unnecessary dependency on parent POM
%pom_remove_parent

# We don't need the bundle
%pom_disable_module jline

# Missing dependencies in Fedora
%pom_disable_module demo
%pom_disable_module groovy
%pom_disable_module graal
%pom_remove_plugin :gmavenplus-plugin
%pom_remove_dep :graal-sdk

# Unnecessary plugins for an rpm build
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :native-image-maven-plugin

# Apache SSHD package names where refactored in 2.6.0
# See https://github.com/apache/mina-sshd/commit/5cbae28a42c478c052ade11d0fc3b84d4ee2f720
sed -i -e 's/org.apache.sshd.server.scp/org.apache.sshd.scp.server/' \
  remote-ssh/src/main/java/org/jline/builtins/ssh/Ssh.java
sed -i -e 's/org.apache.sshd.server.subsystem.sftp/org.apache.sshd.sftp.server/' \
  remote-ssh/src/main/java/org/jline/builtins/ssh/Ssh.java


%build
%mvn_build -s -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-jline-parent
%doc changelog.md README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc changelog.md README.md
%doc --no-dereference LICENSE.txt

%files terminal -f .mfiles-jline-terminal
%doc changelog.md README.md
%doc --no-dereference LICENSE.txt

%files terminal-jansi -f .mfiles-jline-terminal-jansi

%files terminal-jna -f .mfiles-jline-terminal-jna

%files reader -f .mfiles-jline-reader

%files style -f .mfiles-jline-style

%files builtins -f .mfiles-jline-builtins

%files console -f .mfiles-jline-console

%files remote-ssh -f .mfiles-jline-remote-ssh

%files remote-telnet -f .mfiles-jline-remote-telnet

%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0:3.20.0-alt1_2jpp11
- new version

* Mon Jun 14 2021 Igor Vlasenko <viy@altlinux.org> 0:3.19.0-alt1_1jpp11
- new version

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 0:2.14.6-alt2_10jpp11
- fixed obsoletes on jline2

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.14.6-alt1_10jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.14.6-alt1_6jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.14.6-alt1_4jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.14.6-alt1_1jpp8
- new version

* Wed May 09 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.13-alt1_11jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.13-alt1_10jpp8
- fixed build

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.13-alt1_2jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.12.1-alt1_2jpp8
- unbootstrap build

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.12.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1jpp7
- applied repocop patches

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp7
- fc version

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.94-alt1_1jpp5
- new version

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt2_1jpp5
- fixed build w/java5

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt2_1jpp1.7
- build with maven

* Wed Aug 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_1jpp1.7
- updated to new jpackage release

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9-alt2_2jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2
- fixed build using elinks-utf8-hack

* Sun Dec 04 2005 Vladimir Lettiev <crux@altlinux.ru> 0.9.1-alt1
- Rebuild for ALTLinux Sisyphus
- spec cleanup
