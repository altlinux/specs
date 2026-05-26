Name:           apache-commons-jexl
Version:        3.6.2
Release:        alt1

Summary:        Apache Commons JEXL
License:        Apache-2.0
Group:          Development/Java
URL:            https://commons.apache.org/jexl/
VCS:            https://github.com/apache/commons-jexl

Source0:        %name-%version.tar

Patch0:         0001-switch-to-javacc-maven-plugin.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)

BuildArch:      noarch

%description
JEXL is a library intended to facilitate the implementation of dynamic and
scripting features in applications and frameworks written in Java.

JEXL implements an Expression Language based on some extensions to the JSTL
Expression Language supporting most of the constructs seen in shell-script or
ECMAScript.
Its goal is to expose scripting features usable by technical operatives or
consultants working with enterprise platforms. In many use cases, JEXL allows
end-users of an application to code their own scripts or expressions and ensure
their execution within controlled functional constraints.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-antrun-plugin

%pom_xpath_remove //pom:argLine
%pom_xpath_remove //pom:reporting

%build
# Tests disabled due missing dep
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Fri May 15 2026 Evgeniy Serov <scala@altlinux.org> 3.6.2-alt1
- Updated to 3.6.2.
- Returned to Sisyphus.

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 0:2.1.1-alt2_25jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_22jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_21jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_20jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_19jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_18jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_16jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_14jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_3jpp7
- new version

* Tue Feb 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_5jpp6
- fixed obsoletes (closes: #25046)

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_5jpp6
- new version

