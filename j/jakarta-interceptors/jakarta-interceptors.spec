Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname interceptor-api

Name:           jakarta-interceptors
Version:        2.0.0
Release:        alt1_3jpp11
Summary:        Jakarta Interceptors
License:        EPL-2.0 or GPLv2 with exceptions

%global upstream_version %{version}-RELEASE

URL:            https://github.com/eclipse-ee4j/interceptor-api
Source0:        %{url}/archive/%{upstream_version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-interceptor = %{version}-%{release}
Obsoletes:      geronimo-interceptor < 1.0.1-25
Source44: import.info
Conflicts: geronimo-interceptor < 1.0.1-alt3

%description
Jakarta Interceptors defines a means of interposing on business method
invocations and specific eventsa..such as lifecycle events and timeout
eventsa..that occur on instances of Jakarta EE components and other
managed classes.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-interceptor-javadoc = %{version}-%{release}
Obsoletes:      geronimo-interceptor-javadoc < 1.0.1-25
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{upstream_version}


# remove unnecessary dependencies on parent POM
%pom_remove_parent . api

# do not install useless parent POM
%mvn_package :interceptor-api-parent __noinstall

# do not build specification documentation
%pom_disable_module spec

# remove unnecessary maven plugins
%pom_remove_plugin :maven-enforcer-plugin api .
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api

# disable spec verification (fails because spec-version-maven-plugin is too old)
%pom_xpath_remove 'pom:goal[text()="check-module"]' api

# provide javax.interceptor packages in addition to jakarta.interceptor
cp -pr api/src/main/java/jakarta api/src/main/java/javax
sed -i -e 's/jakarta\./javax./g' $(find api/src/main/java/javax -name *.java)

# add compatibility alias for old maven artifact coordinates
%mvn_alias :jakarta.interceptor-api \
    org.apache.geronimo.specs:geronimo-interceptor_1.1_spec \
    org.apache.geronimo.specs:geronimo-interceptor_3.0_spec

# add compatibility symlink for old classpath
%mvn_file : %{name}/jakarta.interceptor-api geronimo-interceptor


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md


%changelog
* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt1_3jpp11
- added conflict with jakarta-interceptors (closes: #40740)

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt1_2jpp11
- new version

