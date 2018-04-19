Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        Extension of the Java Collections Framework
Name:           apache-commons-collections4
Version:        4.1
Release:        alt1_2jpp8
License:        ASL 2.0
URL:            http://commons.apache.org/proper/commons-collections/
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/commons/collections/source/commons-collections4-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.easymock:easymock)
Source44: import.info

%description
Commons-Collections seek to build upon the JDK classes by providing
new interfaces, implementations and utilities.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n commons-collections4-%{version}-src
%mvn_file : %{name} commons-collections4

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_2jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_1jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_7jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_6jpp8
- new version

