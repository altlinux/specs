BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jnr-unixsocket
Version:        0.2
Release:        alt1_1jpp7
Summary:        Unix sockets for Java
Group:          Development/Java
License:        ASL 2.0
URL:            http://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  jnr-constants
BuildRequires:  jnr-enxio
BuildRequires:  jnr-ffi

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
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
%setup -q

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
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_1jpp7
- new release

