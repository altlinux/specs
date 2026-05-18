Name:           jetty-alpn-agent
Version:        2.0.10
Release:        alt1

Summary:        Enables Jetty ALPN/NPN support via -javaagent JVM option
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/jetty-project/jetty-alpn-agent
VCS:            https://github.com/jetty-project/jetty-alpn-agent

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildArch:      noarch

%description
Jetty-alpn-agent is a JVM agent that enables TLS ALPN (or NPN) extension support
for Java 7 and 8 by transforming relevant Java classes using the correct Jetty
alpn-boot (or npn-boot) JAR file for the JVM version in use.

%javadoc_package

%prep
%setup

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Tue Apr 07 2026 Evgeniy Serov <scala@altlinux.org> 2.0.10-alt1
- Initial build for Sisyphus.
