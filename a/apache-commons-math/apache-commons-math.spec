Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global short_name commons-math3

Name:             apache-commons-math
Version:          3.6.1
Release:          alt1_8jpp11
Summary:          Java library of lightweight mathematics and statistics components
License:          ASL 1.1 and ASL 2.0 and BSD
URL:              http://commons.apache.org/math/
Source0:          http://www.apache.org/dist/commons/math/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.commons:commons-parent:pom:)
BuildArch:        noarch
Source44: import.info

%description
Commons Math is a library of lightweight, self-contained mathematics and
statistics components addressing the most common problems not available in the
Java programming language or Commons Lang.


%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src


# Skip test that fails on Java 11
sed -i -e '/checkMissingFastMathClasses/i@Ignore' \
src/test/java/org/apache/commons/math3/util/FastMathTest.java

# Compatibility links
%mvn_alias "org.apache.commons:%{short_name}" "%{short_name}:%{short_name}"
%mvn_file :%{short_name} %{short_name} %{name}

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc NOTICE.txt RELEASE-NOTES.txt
%doc --no-dereference LICENSE.txt


%files javadoc -f .mfiles-javadoc
%doc NOTICE.txt
%doc --no-dereference LICENSE.txt


%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:3.6.1-alt1_8jpp11
- update

* Mon Oct 12 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.6.1-alt1_5jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt2_10jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt2_9jpp8
- fc29 update

* Tue Jun 05 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt2_8jpp8
- fixed build

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_7jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_6jpp8
- new jpp release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_3jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_1jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_1jpp7
- new version

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_1jpp7
- fc update

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt2_2jpp7
- added jpp compat symlink

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_2jpp7
- new version

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_5jpp6
- build without mojo-* plugins

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_5jpp6
- fixed build with maven3

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_5jpp6
- fixed jakarta symlink

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_5jpp6
- build with maven2-plugin-shade

