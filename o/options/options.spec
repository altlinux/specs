Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           options
Version:        1.2
Release:        alt1_6jpp8
Summary:        Library for managing sets of JVM properties to configure an app or library
License:        ASL 2.0
URL:            https://github.com/headius/%{name}
Source0:        https://github.com/headius/%{name}/archive/%{name}-%{version}.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
BuildRequires:  maven-local
Source44: import.info

%description
Provides a simple mechanism for defining JVM property-based
configuration for an application or library.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files  -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_6jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_5jpp8
- unbootsrap build

