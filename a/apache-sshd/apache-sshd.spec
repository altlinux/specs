Epoch:          1
Name:           apache-sshd
Version:        2.17.1
Release:        alt1.1

Summary:        Apache MINA sshd is a comprehensive Java library for client- and server-side SSH
License:        Apache-2.0 AND ISC
Group:          Development/Java
URL:            http://mina.apache.org/sshd-project
VCS:            https://github.com/apache/mina-sshd

Source0:        %name-%version.tar

Patch0:         0001-Avoid-optional-dependency-on-native-tomcat-APR-libra.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk18on)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk18on)
BuildRequires:  mvn(net.i2p.crypto:eddsa)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:      noarch

%description
Apache SSHD is a 100% pure java library to support the SSH protocols on both
the client and server side.

%javadoc_package

%prep
%setup
%autopatch -p1

sed -i 's/session\.rootDirectory/maven.multiModuleProjectDirectory/' .mvn/maven.config
rm -rv sshd-core/src/main/java/org/apache/sshd/agent/unix

%pom_remove_dep :spring-framework-bom
%pom_remove_dep :testcontainers-bom sshd-sftp sshd-core sshd-scp

%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :formatter-maven-plugin . sshd-core
%pom_remove_plugin :impsort-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-assembly-plugin

%pom_remove_plugin :maven-enforcer-plugin

%pom_disable_module sshd-spring-sftp
%pom_disable_module sshd-netty
%pom_disable_module sshd-benchmarks
%pom_disable_module sshd-openpgp
%pom_disable_module sshd-mina
%pom_disable_module assembly

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md LICENSE.txt NOTICE.txt assembly/src/main/legal/licenses/jbcrypt.txt

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 1:2.17.1-alt1.1
- Cosmetic fixes.

* Wed Feb 25 2026 Evgeniy Serov <scala@altlinux.org> 1:2.17.1-alt1
- Updated to 2.17.1.

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 1:2.6.0-alt1_2jpp11
- fc34 update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:2.6.0-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:2.4.0-alt1_5jpp11
- new version

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 1:2.2.0-alt1_4jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:2.2.0-alt1_2jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.0.0-alt1_4jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_8jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_5jpp8
- new jpp release

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_3jpp8
- new version

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_1jpp7
- new release

