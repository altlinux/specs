Name:           apache-commons-logging
Version:        1.3.6
Release:        alt1

Summary:        Apache Commons Logging
License:        Apache-2.0
Group:          Development/Java
URL:            https://commons.apache.org/logging/
VCS:            https://github.com/apache/commons-logging

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(avalon-framework:avalon-framework-impl)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-1.2-api)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)

BuildArch:      noarch

%description
When writing a library it is very useful to log information. However there are
many logging implementations out there, and a library cannot impose the use of
a particular one on the overall application that the library is a part of.

The Logging package is an ultra-thin bridge between different logging
implementations. A library that uses the commons-logging API can be used with
any logging implementation at runtime. Commons Logging comes with support for
a number of popular logging implementations, and writing adapters for others is
a reasonably simple task.

Applications (rather than libraries) may also choose to use commons-logging.
While logging-implementation independence is not as important for applications
as it is for libraries, using commons-logging does allow the application to
change to a different logging implementation without recompiling code.

Note that commons-logging does not attempt to initialize or terminate the
underlying logging implementation that is used at runtime; that is the
responsibility of the application. However many popular logging implementations
do automatically initialize themselves; in this case an application may be
able to avoid containing any code that is specific to the logging implementation
used.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_change_dep :avalon-framework :avalon-framework-impl

%mvn_file  : commons-logging %name
%mvn_alias :commons-logging :commons-logging-api org.apache.commons:commons-logging apache:commons-logging

%build
# Tests disabled due missing deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Mon May 25 2026 Evgeniy Serov <scala@altlinux.org> 1.3.6-alt1
- Updated to 1.3.6.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_30jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_27jpp11
- update

* Fri Jun 11 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_25jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_23jpp11
- fixed build

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_20jpp11
- update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_17jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_14jpp8
- fc29 update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_13jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_11jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_2jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt8_20jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt7_20jpp7
- fixed build

* Tue Jul 15 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt6_20jpp7
- fixed build

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt5_20jpp7
- added jakarta cpmpat symlinks

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt4_20jpp7
- no not package repolib in main commons-logging

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_20jpp7
- new release

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_6jpp6
- fixed build

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_6jpp6
- synced osgi manifest

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_6jpp6
- new version

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_8jpp5
- updated OSGi manifest

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_7jpp5
- rebuild with osgi provides

* Mon May 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp1.7
- updated to new jpackage release

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_3jpp1.7
- added eclipse manifest

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp1.7
- updated to new jpackage release

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp1.7
- updated to new jpackage release

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt4
- added JPackage compatibility stuff

* Sun Aug 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt3
- Disabled check by default due to a circular build dependency

* Thu Jul 15 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt2
- Disabled avalon by default

* Thu Jun 17 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt1
- New upstream release
- Patch0 obsoleted

* Thu Feb 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3-alt1
- Adapted for Sisyphus from the JPackage project
