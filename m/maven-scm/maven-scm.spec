Name:           maven-scm
Version:        2.2.1
Release:        alt1.1

Summary:        Apache Maven SCM (Plugin)
License:        Apache-2.0
Group:          Development/Java
URL:            http://maven.apache.org/scm
VCS:            https://github.com/apache/maven-scm

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interactivity-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.commons:commons-text)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit.ssh.apache)

BuildArch:      noarch

%description
Maven SCM supports Maven plugins (for example maven-release-plugin) and other
tools by providing them with a common API for source code management operations.
You can look at the list of SCMs for more information on using Maven SCM with
your favorite SCM tool.

%javadoc_package

%prep
%setup

%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_remove_plugin :maven-assembly-plugin maven-scm-client

%pom_disable_module maven-scm-provider-gittest maven-scm-providers/maven-scm-providers-git

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc *.md LICENSE

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.2.1-alt1.1
- Cosmetic fixes.

* Mon Feb 23 2026 Evgeniy Serov <scala@altlinux.org> 2.2.1-alt1
- Updated to 2.2.1 (without tests).
- Fixed FTBFS.

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.10.0-alt1_9jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.10.0-alt1_6jpp8
- fc update

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.10.0-alt1_4jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.9.5-alt1_6jpp8
- java fc28+ update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.5-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.5-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4-alt1_3jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt1_2jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt4_6jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt3_6jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_3jpp7
- new release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_4jpp7
- applied repocop patches

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_4jpp7
- restored maven-scm-cvsjava (reverted to rel4)

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_5jpp7
- new version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp6
- new jpp relase

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp6
- fixed build

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_2jpp5
- fixed modello plugin dep

* Sat Oct 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_2jpp5
- added missing symlink in maven2/plugins

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp5
- selected java5 compiler explicitly

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- fixed build

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b3.2jpp1.7
- converted from JPackage by jppimport script

