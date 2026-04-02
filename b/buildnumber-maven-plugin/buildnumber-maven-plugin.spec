Name:           buildnumber-maven-plugin
Version:        3.3.0
Release:        alt1.1

Summary:        BuildNumber Maven Plugin
License:        MIT
Group:          Development/Java
URL:            https://www.mojohaus.org/buildnumber-maven-plugin/
VCS:            https://github.com/mojohaus/buildnumber-maven-plugin

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-api)
BuildRequires:  mvn(com.google.code.maven-scm-provider-svnjava:maven-scm-provider-svnjava)
BuildRequires:  mvn(org.tmatesoft.svnkit:svnkit)

BuildArch:      noarch

%description
This mojo is designed to get a unique build number for each time you build
your project. So while your version may remain constant at 1.0-SNAPSHOT
for many iterations until release, you will have a build number that can
uniquely identify each build during that time. The build number is obtained
from scm, and in particular, at this time, from svn. You can then place that
build number in metadata, which can be accessed from your app, if desired.

The mojo also has a couple of extra functions to ensure you get the proper
build number. First, your local repository is checked to make sure it is
up to date. Second, your local repository is automatically updated, so that
you get the latest build number. Both these functions can be suppressed,
if desired.

Optionally, you can configure this mojo to produce a revision based on a
timestamp, or on a sequence, without requiring any interaction with an
SCM system. Note that currently, the only supported SCM is subversion.

%javadoc_package

%prep
%setup

%pom_remove_plugin :takari-lifecycle-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-dependency-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt *.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 3.3.0-alt1.1
- Cosmetic fixes.

* Tue Feb 24 2026 Evgeniy Serov <scala@altlinux.org> 3.3.0-alt1
- Updated to 3.3.0.

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.3-alt1_17jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_14jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_12jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_11jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_10jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_5jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4jpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_6jpp7
- new release

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3jpp7
- patched out dependency on maven2 (patch33)

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp7
- new version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- complete build

* Tue Mar 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

