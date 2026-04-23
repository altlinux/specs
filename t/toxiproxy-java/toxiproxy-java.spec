Name:           toxiproxy-java
Version: 	2.1.11
Release:        alt1

Summary:        Java API client for the Toxiproxy
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/trekawek/toxiproxy-java
VCS:            https://github.com/trekawek/toxiproxy-java

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)

BuildArch:      noarch

%description
This is a client library for the Toxiproxy - a proxy that simulates network and
system conditions. With toxiproxy-java you may use a convenient Java API to
create and manage proxies.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%build
# tests disabled cause missing dep testcontainers
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Wed Apr 15 2026 Evgeniy Serov <scala@altlinux.org> 2.1.11-alt1
- Initial build for Sisyphus.
