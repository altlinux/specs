Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           jsoup
Version:        1.14.3
Release:        alt2_7jpp11
Summary:        Java library for working with real-world HTML
License:        MIT
URL:            http://jsoup.org/
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
# The sources contain non-free scraped web pages as test data
Source1:        generate-tarball.sh

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif
BuildRequires: jsr-305

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

%{?module_package}
%{?javadoc_package}

%prep
%setup -q -n %{name}-%{name}-%{version}

## Try common possible root names for upstream archive. If one fails, try next.
## This covers archives that unpack to jsoup-1.14.3 or jsoup (no version) or jsoup-jsoup-1.14.3.
#%define _try_setup(n) %{nil:%%{?__dummy:%%{expand:(%{?__dummy})}}}
#%{!?_setup_done:%global _setup_done 0}
#%{!?_setup_tried:%global _setup_tried 0}
#
## Try the most likely names; the first successful %setup will set _setup_done.
#%if %{?_setup_done:0} == 0
#%_setup_tried 0
#%__try1:
#%define _setup_name %{name}-%{version}
#%setup -q -n %{_setup_name} || %{nil}
#%if 0%{?rpmbuild_exit_status:0} == 0
#%global _setup_done 1
#%endif
#%endif
#
#%if %{?_setup_done:0} == 0
#%setup -q -n %{name} || %setup -q
#%endif

# Remove japicmp plugin safely (javapackages-tools macro).
# Use "|| true" so absence of the plugin won't abort %prep (pom_remove_plugin exits non-zero if nothing to remove).
%pom_remove_plugin -r :japicmp-maven-plugin || true
#%pom_remove_plugin com.github.siom79.japicmp:japicmp-maven-plugin || true

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :maven-javadoc-plugin

# Expose internal packages in the OSGi metadata, clearly marking them as such
# using the x-internal attribute
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions" \
  "<_exportcontents>*.internal;x-internal:=true,*</_exportcontents>"

%build
# skip japicmp mojo in offline builds (plugin tries to download from Maven Central)
%mvn_build -f -- -Djapicmp.skip=true -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -n %{?module_prefix}%{name} -f .mfiles
%doc README.md CHANGES
%doc --no-dereference LICENSE

%changelog
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

