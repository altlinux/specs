Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           mnemonicsetter
Version:        0.5
Release:        alt2_5jpp8
Summary:        Menu and toolbar mnemonic library
License:        ASL 2.0
URL:            https://github.com/dpolivaev/%{name}
BuildArch:      noarch

Source0:        https://github.com/dpolivaev/%{name}/archive/%{name}_%{version}.tar.gz

# Remove Gradle bintray plugin (not available in Fedora)
Patch0:         %{name}-remove-bintray-plugin.patch

BuildRequires:  gradle-local
BuildRequires:  mvn(org.mockito:mockito-all:1)
Source44: import.info

%description
Java library, which automatically assigns mnemonics to menu items and
toolbar elements.

%prep
%setup -q -n %{name}-%{name}_%{version}
%patch0
echo 'rootProject.name="%{name}"' >settings.gradle

%build
%gradle_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Thu Jul 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_5jpp8
- fc update & java 8 build

* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_4jpp8
 -build with mockito1

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_3jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_2jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1jpp8
- new version

