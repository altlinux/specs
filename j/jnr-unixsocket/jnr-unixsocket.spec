# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jnr-unixsocket
Version:        0.12
Release:        alt1_3jpp8
Summary:        Unix sockets for Java
Group:          Development/Other
License:        ASL 2.0
URL:            http://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  jnr-constants
BuildRequires:  jnr-enxio
BuildRequires:  jnr-ffi
BuildRequires:  jnr-posix

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  sonatype-oss-parent
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

# remove unnecessary wagon extension
%pom_xpath_remove pom:build/pom:extensions

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
* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_1jpp7
- new release

