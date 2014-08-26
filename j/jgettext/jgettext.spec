Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jgettext
Version:        0.13
Release:        alt1_2jpp7
Summary:        An ANTLR-based parser and generator for GNU Gettext PO/POT 

License:        LGPLv2
URL:            https://github.com/zanata/%{name}
Source0:        https://github.com/zanata/%{name}/archive/%{name}-%{version}.zip

BuildArch:      noarch

BuildRequires:  maven-local

BuildRequires:  maven-install-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  antlr-maven-plugin
BuildRequires:  junit
BuildRequires:  gettext

Requires:       antlr
Requires:       jpackage-utils
Source44: import.info

%description
JGettext includes an ANTLR-based parser for GNU Gettext PO/POT files and a 
PO/POT generator as well.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2jpp7
- new release

