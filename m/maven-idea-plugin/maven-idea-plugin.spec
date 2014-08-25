# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-idea-plugin
Version:        2.2
Release:        alt3_12jpp7
Summary:        Maven IDEA Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-idea-plugin-2.2
# tar caf maven-idea-plugin-2.2.tar.xz maven-idea-plugin-2.2
Source0:        %{name}-%{version}.tar.xz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt
Patch0:         add_compat.patch

BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven-local
BuildRequires: maven-wagon
BuildRequires: plexus-container-default
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-testing-harness
BuildRequires: dom4j

Obsoletes: maven2-plugin-idea <= 0:2.0.8
Provides: maven2-plugin-idea = 1:%{version}-%{release}
Source44: import.info

%description
The IDEA Plugin is used to generate files (ipr, iml, and iws) for a
project so you can work on it using the IDE, IntelliJ IDEA.


%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.


%prep
%setup -q 
%patch0

cp %{SOURCE1} .

%build
# we skip test because even with binary mvn release these fail for
# various reasons.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_12jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_8jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_8jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_8jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_7jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

