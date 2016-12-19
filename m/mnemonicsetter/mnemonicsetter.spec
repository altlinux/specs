Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           mnemonicsetter
Version:        0.5
Release:        alt1_1jpp8
Summary:        Menu and toolbar mnemonic library
License:        ASL 2.0
URL:            https://github.com/dpolivaev/%{name}
BuildArch:      noarch

Source0:        https://github.com/dpolivaev/%{name}/archive/%{name}_%{version}.tar.gz

# Remove Gradle bintray plugin (not available in Fedora)
Patch0:         %{name}-remove-bintray-plugin.patch

BuildRequires:  gradle-local
BuildRequires:  mvn(org.mockito:mockito-all)
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
%doc LICENSE

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1jpp8
- new version

