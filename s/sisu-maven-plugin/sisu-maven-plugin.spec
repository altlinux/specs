BuildRequires: /proc
BuildRequires: jpackage-compat
%global tag d63011e

Name:           sisu-maven-plugin
Version:        1.1
Release:        alt1_5jpp7
Summary:        Sisu plugin for Apache Maven
BuildArch:      noarch
Group:          Development/Java
License:        ASL 2.0 and EPL
URL:            http://sonatype.github.com/%{name}/
Source:         https://github.com/sonatype/%{name}/tarball/%{name}-%{version}#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  maven-common-artifact-filters
BuildRequires:  plexus-utils
BuildRequires:  sisu
BuildRequires:  sonatype-plugins-parent
# test deps
BuildRequires:  junit
BuildRequires:  maven-surefire-provider-junit4
Source44: import.info


%description
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n sonatype-%{name}-%{tag}

%build
%mvn_file  : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-ASL.txt LICENSE-EPL.txt README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE-ASL.txt LICENSE-EPL.txt


%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5jpp7
- new release

