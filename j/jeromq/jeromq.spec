Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jeromq
Version:        0.3.6
Release:        alt2_6jpp8
Summary:        Pure Java implementation of libzmq
License:        MPLv2.0
URL:            https://github.com/zeromq/jeromq
BuildArch:      noarch

Source0:        https://github.com/zeromq/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
Pure Java implementation of libzmq.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
# Tests require network access and fail on Koji.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md CHANGELOG.md AUTHORS
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.6-alt2_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.6-alt2_5jpp8
- fc29 update

* Wed May 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.6-alt2_3jpp8
- fixed build with maven-javadoc-plugin 3

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.6-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.6-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_5jpp8
- new fc release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_4jpp8
- new version

