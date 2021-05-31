Epoch: 0
Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: A Java template engine
Name: stringtemplate
Version: 3.2.1
Release: alt2_24jpp11
URL: http://www.stringtemplate.org/
Source0: http://www.stringtemplate.org/download/stringtemplate-%{version}.tar.gz
# Build jUnit tests + make the antlr2 generated code before preparing sources
Patch0: stringtemplate-3.1-build-junit.patch
License: BSD

BuildRequires: ant
BuildRequires: ant-antlr
BuildRequires: ant-junit
BuildRequires: javapackages-local

BuildArch: noarch
Source44: import.info

%description
StringTemplate is a java template engine (with ports for 
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
Requires:       java-javadoc
BuildArch: noarch

%description    javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0
sed -i -e 's/source="1.4"/source="1.8"/g' build.xml
sed -i -e 's/target="1.4"/target="1.8"/g' build.xml

%build
rm -rf lib target
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  jar
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  javadocs -Dpackages= -Djavadocs.additionalparam="-Xdoclint:none"

%install
%mvn_artifact pom.xml build/%{name}.jar
%mvn_file : %{name}
%mvn_install -J docs/api/

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%doc README.txt

%files javadoc
%doc --no-dereference LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:3.2.1-alt2_24jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_21jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_19jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_17jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_15jpp8
- new fc release

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_12jpp8
- added BR: javapackages-local for javapackages 5

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_7jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_5jpp7
- fc update

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_3jpp6
- new jpp release

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt4_2jpp5
- fixes for java6 support

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt3_2jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_1jpp5
- converted from JPackage by jppimport script

