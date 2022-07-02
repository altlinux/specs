Epoch: 1
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
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.0.0
%bcond_with bootstrap

%global upstream_version %(echo %{version} | tr '~' '-')

Name:           qdox
Version:        2.0.0
Release:        alt1_9jpp11
Summary:        Extract class/interface/method definitions from sources
License:        ASL 2.0
URL:            https://github.com/paul-hammant/qdox
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        qdox-MANIFEST.MF
# Remove bundled binaries which are possibly proprietary
Source2:        generate-tarball.sh

Patch0:         0001-Port-to-JFlex-1.7.0.patch

BuildRequires:  maven-local
BuildRequires:  byaccj
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  jflex
%endif
Source44: import.info
Obsoletes: qdox16-poms < 1.1

%description
QDox is a high speed, small footprint parser
for extracting class/interface/method definitions
from source files complete with JavaDoc @tags.
It is designed to be used by active code
generators or documentation tools.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API docs for %{name}.

%prep
%setup -q -n %{name}-%{upstream_version}
%patch0 -p1

# remove unnecessary dependency on parent POM
%pom_remove_parent

# We don't need these plugins
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :maven-invoker-plugin
%pom_remove_plugin :maven-jflex-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :exec-maven-plugin

%mvn_file : %{name}
%mvn_alias : qdox:qdox

%build
%{?jpb_env}

# Generate scanners (upstream does this with maven-jflex-plugin)
jflex -d src/main/java/com/thoughtworks/qdox/parser/impl src/grammar/lexer.flex
jflex -d src/main/java/com/thoughtworks/qdox/parser/impl src/grammar/commentlexer.flex

# Generate parsers (upstream does this with exec-maven-plugin)
(cd ./src/main/java/com/thoughtworks/qdox/parser/impl
 byaccj -v -Jnorun -Jnoconstruct -Jclass=DefaultJavaCommentParser -Jpackage=com.thoughtworks.qdox.parser.impl ../../../../../../../grammar/commentparser.y
 byaccj -v -Jnorun -Jnoconstruct -Jclass=Parser -Jimplements=CommentHandler -Jsemantic=Value -Jpackage=com.thoughtworks.qdox.parser.impl -Jstack=500 ../../../../../../../grammar/parser.y
)

# Build artifact
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.source=1.7 -Dmaven.compiler.target=1.7

# Inject OSGi manifests
jar ufm target/%{name}-%{upstream_version}.jar %{SOURCE1}

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1:2.0.0-alt1_9jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1:2.0-alt1_8.M9jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_6.M9jpp8
- update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_4.M9jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_0.12.M7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_0.11.M7jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_0.8.M5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_0.5.M3jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_0.4.M3jpp8
- unbootstrap build

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt2_7jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt2_5jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt1_5jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt1_2jpp7
- fc update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt3_2jpp6
- fixed build

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt2_2jpp6
- fixed build with java 7

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt1_2jpp6
- new version

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt2_5jpp6
- rebuild with target=5

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_5jpp6
- new version

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_5jpp5
- reverted to version 1.6.1

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp5
- fixed build with jpackage 5

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp1.7
- rebuilt with maven1

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_4jpp1.7
- converted from JPackage by jppimport script

