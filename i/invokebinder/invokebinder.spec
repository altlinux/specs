# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           invokebinder
Version:        1.2
Release:        alt1_4jpp8
Summary:        A Java DSL for binding method handles forward, rather than backward
Group:          Development/Other
License:        ASL 2.0
URL:            http://github.com/headius/%{name}/
Source0:        https://github.com/headius/%{name}/archive/%{name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit

Requires:       jpackage-utils
Source44: import.info

%description
This library hopes to provide a more friendly DSL for binding method handles.
Unlike the normal MethodHandle API, handles are bound forward from a source
MethodType and eventually adapted to a final target MethodHandle. Along the
way the transformations are pushed onto a stack and eventually applied in
reverse order, as the standard API demands.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_8jpp7
- new release

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp7
- new release

