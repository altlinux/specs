Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jsemver
Version:        0.9.0
Release:        alt1_3jpp8
Summary:        A Java implementation of the Semantic Versioning Specification

License:        MIT
URL:            https://github.com/zafarkhaja/jsemver
Source0:        https://github.com/zafarkhaja/jsemver/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin >= 3.2
BuildRequires:  maven-javadoc-plugin >= 2.10.2
BuildRequires:  junit >= 4.12
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
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_3jpp8
- new version

