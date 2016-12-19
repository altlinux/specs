Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Summary:        Extension of the Java Collections Framework
Name:           apache-commons-collections4
Version:        4.0
Release:        alt1_6jpp8
License:        ASL 2.0
URL:            http://commons.apache.org/proper/commons-collections/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/collections/source/commons-collections4-4.0-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
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
%doc README.txt RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_6jpp8
- new version

