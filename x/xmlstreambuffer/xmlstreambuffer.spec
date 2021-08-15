Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname metro-xmlstreambuffer

Name:           xmlstreambuffer
Version:        1.5.9
Release:        alt1_5jpp11
Summary:        Stream Based Representation for XML Infoset
License:        BSD

URL:            https://github.com/eclipse-ee4j/metro-xmlstreambuffer
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)

# javadoc subpackage is currently not built
Obsoletes:      xmlstreambuffer-javadoc < 1.5.9-1
Source44: import.info

%description
Stream based representation for XML infoset.


%prep
%setup -q -n %{srcname}-%{version}

pushd streambuffer
# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_dep "com.fasterxml.woodstox:woodstox-core"
%pom_remove_dep "junit:junit"
popd


%build
pushd streambuffer
# skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -f -j -- -DbuildNumber=unknown
popd


%install
pushd streambuffer
%mvn_install
popd


%files -f streambuffer/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md


%changelog
* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 1.5.9-alt1_5jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.5.9-alt1_1jpp11
- new version; needs java9+

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_11jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_9jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_2jpp8
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_3jpp7
- new release

