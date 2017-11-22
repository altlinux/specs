Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jsoup
Version:        1.11.1
Release:        alt1_1jpp8
Summary:        Java library for working with real-world HTML
License:        MIT
URL:            http://jsoup.org/
BuildArch:      noarch

Source0:        https://github.com/jhy/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
jsoup is a Java library for working with real-world HTML.
It provides a very convenient API for extracting and manipulating data,
using the best of DOM, CSS, and jquery-like methods.

jsoup implements the WHATWG HTML5 specification,
and parses HTML to the same DOM as modern browsers do.

 - scrape and parse HTML from a URL, file, or string
 - find and extract data, using DOM traversal or CSS selectors
 - manipulate the HTML elements, attributes, and text
 - clean user-submitted content against a safe white-list,
   to prevent XSS attacks
 - output tidy HTML

jsoup is designed to deal with all varieties of HTML found in the wild;
from pristine and validating, to invalid tag-soup;
jsoup will create a sensible parse tree.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md CHANGES
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
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

