Name:           htmlunit-neko
Version:        4.21.0
Release:        alt1

Summary:        HtmlUnit adaptation of NekoHtml
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/HtmlUnit/htmlunit-neko
VCS:            https://github.com/HtmlUnit/htmlunit-neko

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildArch:     noarch

%description
The Htmlunit-NekoHtml Parser is a HTML scanner and tag balancer that enables
application programmers to parse HTML documents and access the information
using standard XML interfaces.
The parser can scan HTML files and "fix up" many common mistakes that human
(and computer) authors make in writing HTML documents.
NekoHTML adds missing parent elements; automatically closes elements with
optional end tags; and can handle mismatched inline element tags.

%javadoc_package

%prep
%setup

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md

%changelog
* Wed Apr 22 2026 Evgeniy Serov <scala@altlinux.org> 4.21.0-alt1
- Updated to 4.21.0.
- Renamed package.
- Returned to Sisyphus.

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1_6jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1_4jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1_3jpp8
- new version

