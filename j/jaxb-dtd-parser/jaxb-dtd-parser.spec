Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
BuildRequires: /usr/bin/git
Name:           jaxb-dtd-parser
Version:        1.5.0
Release:        alt1_3jpp11
Summary:        SAX-like API for parsing XML DTDs
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-dtd-parser
BuildArch:      noarch
Source0:        https://github.com/eclipse-ee4j/jaxb-dtd-parser/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  git
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
Provides:       glassfish-dtd-parser = %{version}-%{release}
Source44: import.info

%description
SAX-like API for parsing XML DTDs.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch
%description javadoc
API documentation for %{name}.


%prep
# -S: enable usage of git repo
%setup -q
git init -q
git config user.name "rpmbuild"
git config user.email "<rpmbuild>"
git config gc.auto 0
git add --force .
git commit -q --allow-empty -a --author "rpmbuild <rpmbuild>" -m "%{NAME}-%{VERSION} base"

# delete precompiled jar and class files
find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

cd dtd-parser
# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent
# remove unnecessary plugins
%pom_remove_plugin :glassfish-copyright-maven-plugin
cd -

%build
cd dtd-parser
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
cd -

%install
cd dtd-parser
%mvn_install
cd -

%files -f dtd-parser/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md
%files javadoc -f dtd-parser/.mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1.5.0-alt1_3jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.4.5-alt1_3jpp11
- new version

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.4.3-alt1_4jpp11
- new version

