Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           jcodings
Version:        1.0.55
Release:        alt1_0jpp11
Summary:        Java-based codings helper classes for Joni and JRuby

License:        MIT
URL:            https://github.com/jruby/%{name}
Source0:        https://github.com/jruby/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch: noarch
Source44: import.info

%description
Java-based codings helper classes for Joni and JRuby.

%package javadoc
Group: Development/Other
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find -name '*.class' -delete
find -name '*.jar' -delete

%mvn_file : %{name}

# Remove pointless parent pom
%pom_remove_parent

# Remove wagon extension
%pom_xpath_remove "pom:build/pom:extensions"

# Remove plugins not relevant for downstream RPM builds
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

# Generate OSGi metadata by using bundle packaging
%pom_xpath_inject pom:project "<packaging>bundle</packaging>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin "<extensions>true</extensions>"

%build
# the pom is already on 1.7, I had not found what builds by 6 deep in sources 
%mvn_build  -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 1.0.55-alt1_0jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.0.36-alt1_2jpp11
- new version; needs java9 api

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_17jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_15jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_14jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_13jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_12jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_8jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_5jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_1jpp7
- rebuild with maven-local

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_1jpp7
- new version

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_3jpp7
- new release

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp5
- new version

