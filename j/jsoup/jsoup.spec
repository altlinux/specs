Name:           jsoup
Version:        1.22.2
Release:        alt1

Summary:        Java HTML parser, built for HTML editing, cleaning, scraping, and XSS safety
License:        MIT
Group:          Development/Java
URL:            http://jsoup.org/
VCS:            https://github.com/jhy/jsoup

Source0:        %name-%version.tar

Patch0:         remove-re2j.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(io.netty:netty-bom:pom:)

BuildArch:      noarch

%description
jsoup is a Java library that makes it easy to work with real-world HTML and XML.
It offers an easy-to-use API for URL fetching, data parsing, extraction, and
manipulation using DOM API methods, CSS, and xpath selectors.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :japicmp-maven-plugin

%pom_remove_dep com.google.re2j:re2j

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE *.md

%changelog
* Fri Jul 10 2026 Evgeniy Serov <scala@altlinux.org> 1.22.2-alt1
- Updated to 1.22.2.

* Mon Apr 20 2026 Pavel Vasenkov <pav@altlinux.org> 1.14.3-alt2_7jpp11
- NMU: Fixed FTBFS with jsr305

* Tue Oct 28 2025 Pavel Vasenkov <pav@altlinux.org> 1.14.3-alt1_7jpp11
- new version

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 1.13.1-alt1_7jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.13.1-alt1_4jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 1.12.1-alt1_3jpp11
- fixed build

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.12.1-alt1_2jpp11
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.11.3-alt1_4jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.11.3-alt1_1jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.11.2-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.11.1-alt1_1jpp8
- new version

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.10.3-alt1_2jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_2jpp8
- new version

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.2-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_7jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_5jpp7
- new fc release

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_3jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

