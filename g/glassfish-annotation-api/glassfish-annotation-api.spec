Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.3.2
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global oname javax.annotation-api
%global sname javax.annotation

Name:          glassfish-annotation-api
Version:       1.3.2
Release:       alt1_2jpp11
Summary:       Common Annotations API Specification (JSR 250)
License:       CDDL-1.1 or GPLv2 with exceptions

# NOTE: The new upstream repository under the Eclipse EE4J umbrella is here:
# https://github.com/eclipse-ee4j/common-annotations-api
# However, the new package provides a different groupId:artifactId.
URL:           https://github.com/javaee/%{sname}
Source0:       %{url}/archive/%{version}/%{sname}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.glassfish.build:spec-version-maven-plugin)
# xmvn-builddep misses this one
BuildRequires: mvn(org.glassfish:legal)

BuildArch:     noarch
Source44: import.info

%description
Common Annotations APIs for the Java Platform (JSR 250).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{sname}-%{namedversion}

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-gpg-plugin

%mvn_file :%{oname} %{name}

%build
%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.3.2-alt1_2jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_15jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_14jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_13jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_12jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_9jpp8
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_5jpp7
- new release

