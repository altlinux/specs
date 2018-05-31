Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jnr-enxio
Version:        0.16
Release:        alt1_4jpp8
Summary:        Unix sockets for Java
# src/main/java/jnr/enxio/channels/PollSelectionKey.java is LGPLv3
# rest of the source code is ASL 2.0
License:        ASL 2.0 and LGPLv3
URL:            https://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz

# Avoid split-package situation, this patch submitted upstream here: https://github.com/jnr/jnr-enxio/pull/26
Patch0: add-abstract-impls-from-unixsocket.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-constants)
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
Unix sockets for Java.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_4jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_2jpp8
- new version

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_3jpp8
- java 8 mass update

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_3jpp7
- new version

