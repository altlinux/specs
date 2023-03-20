Epoch: 0
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

Name:           xmlunit
Version:        2.8.2
Release:        alt1_8jpp11
Summary:        Provides classes to do asserts on xml
# The whole package is ASL 2.0 except for xmlunit-legacy which is BSD
License:        ASL 2.0 and BSD
URL:            https://www.xmlunit.org/
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
# Remove bundled binaries which cannot be easily verified for licensing
Source1:        generate-tarball.sh

Patch1:         0001-Disable-tests-requiring-network-access.patch
Patch2:         0002-Port-to-hamcrest-2.1.patch
Patch3:         0003-Drop-support-for-JAXB.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
Source44: import.info

%description
XMLUnit provides you with the tools to verify the XML you emit is the one you
want to create. It provides helpers to validate against an XML Schema, assert
the values of XPath queries or compare XML documents against expected outcomes.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}

%package        assertj
Group: Development/Java
Summary:        Assertj for %{name}

%description    assertj
This package provides %{summary}.

%package        core
Group: Development/Java
Summary:        Core package for %{name}

%description    core
This package provides %{summary}.

%package        legacy
Group: Development/Java
Summary:        Legacy package for %{name}

%description    legacy
This package provides %{summary}.

%package        matchers
Group: Development/Java
Summary:        Matchers for %{name}

%description    matchers
This package provides %{summary}.

%package        placeholders
Group: Development/Java
Summary:        Placeholders for %{name}

%description    placeholders
This package provides %{summary}.

%prep
%setup -q -n %{name}-%{version}-src

%patch1 -p1
%patch2 -p1
%patch3 -p1

# Tests compare the string constent of thrown exceptions
# and we use a different version of assertj
find xmlunit-assertj3/src/test -name '*.java' -exec sed -i 's/\(Expecting not blank but was:\)<\(.*\)>/\1 \2/' {} +
sed -i 's/\(expected:\)<\\"\[\(something\)\]\\"> but was:<\\"\[\(abc\)\]\\">/\1 \\"\2\\"\\nbut was : \\"\3\\"/' xmlunit-assertj3/src/test/java/org/xmlunit/assertj3/ValueAssertTest.java

%pom_disable_module xmlunit-assertj

%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin -r :maven-shade-plugin

%mvn_alias org.xmlunit:xmlunit-legacy xmlunit:xmlunit
%mvn_alias org.xmlunit:xmlunit-assertj3 org.xmlunit:xmlunit-assertj

# JAXB and JAF are not available in JDK11
%pom_remove_dep org.glassfish.jaxb: xmlunit-core
%pom_remove_dep jakarta.xml.bind: xmlunit-core
rm -rf xmlunit-core/src/{main,test}/java/org/xmlunit/builder/{jaxb/,JaxbBuilder.java,JaxbBuilderTest.java}

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-xmlunit-parent
%doc README.md CONTRIBUTING.md RELEASE_NOTES.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%files assertj -f .mfiles-xmlunit-assertj3
%files core -f .mfiles-xmlunit-core
%files legacy -f .mfiles-xmlunit-legacy
%files matchers -f .mfiles-xmlunit-matchers
%files placeholders -f .mfiles-xmlunit-placeholders

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:2.8.2-alt1_8jpp11
- update

* Thu Jun 09 2022 Igor Vlasenko <viy@altlinux.org> 0:2.8.2-alt1_4jpp11
- new version

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 0:2.7.0-alt1_6jpp11
- fixed build

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.7.0-alt1_4jpp11
- new version

* Sun May 09 2021 Igor Vlasenko <viy@altlinux.ru> 0:2.6.3-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_9jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_6jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_1jpp7
- bugfixes

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_6jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_6jpp7
- new version

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_4jpp6
- fixed build

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp6
- build with ant17

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_6jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_6jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp1.7
- updated to new jpackage release

* Wed May 23 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_4jpp1.7
- converted from JPackage by jppimport script

* Thu Mar 23 2006 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt2
- Fix build with j2se-1.5

* Sat Apr 30 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Rebuilt for ALTLinux Sisyphus
- spec cleanup

* Thu Aug 26 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-3jpp
- Build with ant-1.6.2

* Wed Dec 17 2003 Paul Nasrat <pauln at truemesh.com> - 0:1.0-2jpp
- Fix license and improved description
- Thanks to Ralph Apel who produced a spec - merged version info

* Wed Dec 17 2003 Paul Nasrat <pauln at truemesh.com> - 0:1.0-1jpp
- Initial Version
