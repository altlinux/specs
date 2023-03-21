Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           java-diff-utils
Version:        4.12
Release:        alt1_1jpp11
Summary:        Java library to create and apply patches

License:        ASL 2.0
URL:            https://java-diff-utils.github.io/java-diff-utils/
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-parent-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)

BuildArch:      noarch

%global _desc \
The Java Diff Utils library is an open source library for performing\
comparison operations between texts: computing diffs, applying patches,\
generating or parsing unified diffs, generating diff output for easy\
display (e.g., side-by-side view), and so on.
Source44: import.info

%description 
%_desc

%package        parent
Group: Development/Java
Summary:        Java Diff Utils parent POM

%description    parent 
%_desc

This package contains the parent POM for Java Diff Utils.

%package        jgit
Group: Development/Java
Summary:        Java Diff Utils extension using jgit difference algorithms
Requires:       %{name} = %{version}-%{release}

%description    jgit 
%_desc

This package contains an extension to the main package that uses jgit's
difference algorithms.

%{?javadoc_package}

%prep
%setup -q -n %{name}-%{name}-parent-%{version}


# Unnecessary plugins for an RPM build
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-java-diff-utils
%doc --no-dereference LICENSE

%files parent -f .mfiles-java-diff-utils-parent
%doc --no-dereference LICENSE

%files jgit -f .mfiles-java-diff-utils-jgit

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 4.12-alt1_1jpp11
- new version

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 4.11-alt1_1jpp11
- new version

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 4.10-alt1_2jpp11
- new version

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 4.9-alt1_2jpp11
- new version

