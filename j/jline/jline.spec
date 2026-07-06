Name:           jline
Version:        3.23.0
Release:        alt1

Summary:        Java library for handling console input
License:        BSD-3-Clause
Group:          Development/Java
URL:            https://jline.org/
VCS:            https://github.com/jline/jline3

Source0:        %name-%version.tar

Patch0:         0001-load-native-library-fix.patch

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.github.albfernandez:juniversalchardet)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

%description 
JLine is a Java library for handling console input. It is similar in
functionality to BSD editline and GNU readline but with additional features
that bring it in par with ZSH line editor. People familiar with the
readline/editline capabilities for modern shells (such as bash and tcsh) will
find most of the command editing features of JLine to be familiar.

JLine 3.x is an evolution of JLine 2.x.

%javadoc_package

%package        core
Summary:        JLine core
Group:          Development/Java
BuildArch:      noarch

%description    core
%summary.

%package        builtins
Summary:        JLine builtins
Group:          Development/Java
BuildArch:      noarch

%description    builtins 
%summary.

%package        console
Summary:        JLine console
Group:          Development/Java
BuildArch:      noarch

%description    console 
%summary.

%package        native
Summary:        JLine Native Library
Group:          Development/Java

%description    native
%summary.

%package        reader
Summary:        JLine reader
Group:          Development/Java
BuildArch:      noarch

%description    reader 
%summary.

%package        remote-ssh
Summary:        JLine remote SSH
Group:          Development/Java
BuildArch:      noarch

%description    remote-ssh
%summary.

%package        remote-telnet
Summary:        JLine remote telnet
Group:          Development/Java
BuildArch:      noarch

%description    remote-telnet
%summary.

%package        style
Summary:        JLine style
Group:          Development/Java
BuildArch:      noarch

%description    style 
%summary.

%package        terminal
Summary:        JLine terminal
Group:          Development/Java
BuildArch:      noarch

%description    terminal
%summary.

%package        terminal-jansi
Summary:        JLine terminal with JANSI
Group:          Development/Java
BuildArch:      noarch

%description    terminal-jansi 
%summary.

%package        terminal-jna
Summary:        JLine terminal with JNA
Group:          Development/Java
BuildArch:      noarch

%description    terminal-jna 
%summary.

%prep
%setup
%autopatch -p1

rm -r native/src/main/resources/org/jline/nativ/*/

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :spotless-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_plugin :exec-maven-plugin native
%pom_remove_dep :picocli-codegen native

# fails
rm terminal-jna/src/test/java/org/jline/terminal/impl/jna/JnaNativePtyTest.java

%pom_disable_module groovy
%pom_disable_module demo
%pom_disable_module graal

%mvn_package :%name-parent __noinstall

%build
# Build a native object
%add_optflags -Wall -fPIC -fvisibility=hidden -shared 
%add_optflags -I native/src/main/native 
%add_optflags -I %_jvmdir/jre/include
%add_optflags -I %_jvmdir/jre/include/linux %{?__global_ldflags}

gcc %optflags -o libjlinenative.so native/src/main/native/jlinenative.c

%mvn_build -s -- -Dlibrary.jline.path=$PWD

%install
%mvn_install
install -d -m 755 %buildroot%_libdir/%name
install -p -m 755 libjlinenative.so %buildroot%_libdir/%name/

%files core -f .mfiles-jline
%doc LICENSE.txt *.md

%files builtins -f .mfiles-jline-builtins
%files console -f .mfiles-jline-console
%files native -f .mfiles-jline-native
%_libdir/%name/libjlinenative.so

%files reader -f .mfiles-jline-reader
%files remote-ssh -f .mfiles-jline-remote-ssh
%files remote-telnet -f .mfiles-jline-remote-telnet
%files style -f .mfiles-jline-style
%files terminal -f .mfiles-jline-terminal
%files terminal-jansi -f .mfiles-jline-terminal-jansi
%files terminal-jna -f .mfiles-jline-terminal-jna

%changelog
* Thu Jul 02 2026 Evgeniy Serov <scala@altlinux.org> 3.23.0-alt1
- Updated to 3.23.0 (ty nash@).

* Mon Apr 20 2026 Anton Meleshnikov <alton@altlinux.org> 0:3.21.0-alt3
- fixed FTBFS: add necessary BuildRequires

* Wed Mar 04 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0:3.21.0-alt2
- fixed FTBFS: uncomment patch which rename classes

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:3.21.0-alt1_4jpp11
- update

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 0:3.21.0-alt1_3jpp11
- new version

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
