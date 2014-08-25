Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             guacamole-common
Version:          0.8.0
Release:          alt1_4jpp7
Summary:          The core Java library used by the Guacamole web application
License:          MPLv1.1 or GPLv2+ or LGPLv2+
URL:              http://guac-dev.org/
Source0:          http://guac-dev.org/pub/dist/source/%{name}-%{version}.tar.gz
BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    servlet3
Source44: import.info

%description
Guacamole is an HTML5 web application that provides access to desktop
environments using remote desktop protocols such as VNC or RDP. A centralized
server acts as a tunnel and proxy, allowing access to multiple desktops through
a web browser. No plugins are needed: the client requires nothing more than a
web browser supporting HTML5 and AJAX.

%{name} is the core Java library used by the Guacamole web application.
%{name} provides abstract means of connecting to guacd, interfacing
with the JavaScript client and tunnel provided by guacamole-common-js, and
reading configuration from a standard location (guacamole.properties).

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%{_javadir}/%{name}
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_4jpp7
- update

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_3jpp7
- new version

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_2jpp7
- fc update

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_2jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_7jpp7
- new version

