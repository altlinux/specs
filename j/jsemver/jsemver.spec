Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jsemver
Version:        0.9.0
Release:        alt1_7jpp8
Summary:        A Java implementation of the Semantic Versioning Specification

License:        MIT
URL:            https://github.com/zafarkhaja/jsemver
Source0:        https://github.com/zafarkhaja/jsemver/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin >= 3.2
BuildRequires:  maven-javadoc-plugin >= 2.10.2
BuildRequires:  junit >= 4.12
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
JSemVer (formerly Java SemVer) is a Java implementation of
version 2.0.0 of the Semantic Versioning Specification

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q
find -name \*.jar -delete
find -name \*.class -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}
%doc CHANGELOG.md
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_5jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_3jpp8
- new version

