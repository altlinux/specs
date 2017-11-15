Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           apache-logging-parent
Version:        1
Release:        alt1_2jpp8
License:        ASL 2.0
Summary:        Parent pom for Apache Logging Services projects
URL:            https://logging.apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/logging/logging-parent/%{version}/logging-parent-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
Source44: import.info

%description
Parent pom for Apache Logging Services projects.


%prep
%setup -q -n logging-parent-%{version}

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 1-alt1_2jpp8
- new version

