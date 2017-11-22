Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: A Java template engine
Name: stringtemplate
Version: 3.2.1
Release: alt2_15jpp8
URL: http://www.stringtemplate.org/
Source0: http://www.stringtemplate.org/download/stringtemplate-%{version}.tar.gz
# Build jUnit tests + make the antlr2 generated code before preparing sources
Patch0: stringtemplate-3.1-build-junit.patch
License: BSD
Group: Development/Other
BuildArch: noarch
BuildRequires: ant-antlr ant-junit
BuildRequires: antlr-tool
# Standard deps
BuildRequires: java-devel >= 1.6.0
BuildRequires: javapackages-local
Requires: antlr-tool
Source44: import.info

%description
StringTemplate is a java template engine (with ports for 
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       java-javadoc
BuildArch: noarch

%description    javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0

%build
rm -rf lib target
ant jar
ant javadocs -Dpackages= -Djavadocs.additionalparam="-Xdoclint:none"

%install
install -D build/stringtemplate.jar $RPM_BUILD_ROOT%{_datadir}/java/stringtemplate.jar
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pR docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -Dpm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom stringtemplate.jar

%files -f .mfiles
%doc LICENSE.txt README.txt

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
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

