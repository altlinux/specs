Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global short_name      commons-cli

Name:             apache-%{short_name}
Version:          1.2
Release:          alt2_11jpp7
Summary:          Command Line Interface Library for Java
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/cli/
Source0:          http://www.apache.org/dist/commons/cli/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local

Requires:         jpackage-utils
Source44: import.info
Provides: jakarta-%{short_name} = 1:%{version}-%{release}
Obsoletes: jakarta-%{short_name} < 1:%{version}-%{release}
Conflicts: jakarta-%{short_name} < 1:%{version}-%{release}

%description
The CLI library provides a simple and easy to use API for working with the 
command line arguments and options.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :commons-cli %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_9jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_7jpp7
- fc update

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_6jpp6
- add obsoletes

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_6jpp6
- fixed repolib

