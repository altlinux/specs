# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jnr-enxio
Version:        0.12
Release:        alt1_1jpp8
Summary:        Unix sockets for Java
Group:          Development/Other
# src/main/java/jnr/enxio/channels/PollSelectionKey.java is LGPLv3
# rest of the source code is ASL 2.0
License:        ASL 2.0 and LGPLv3
URL:            http://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  jnr-constants
BuildRequires:  jnr-ffi

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit

Requires:       jnr-constants
Requires:       jnr-ffi
Source44: import.info

%description
Unix sockets for Java.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_3jpp8
- java 8 mass update

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_3jpp7
- new version

