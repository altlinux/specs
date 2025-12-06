%define _unpackaged_files_terminate_build 1

Name: java-websocket
Version: 1.6.0
Release: alt1

Summary: A barebones WebSocket client and server implementation written in 100%% Java 
License: MIT
Group: Development/Java
Url: https://tootallnate.github.io/Java-WebSocket
Vcs: https://github.com/TooTallNate/Java-WebSocket.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: bnd-maven-plugin

%description
This repository contains a barebones WebSocket server and client implementation
written in 100%% Java. The underlying classes are implemented java.nio, which
allows for a non-blocking event-driven model (similar to the WebSocket API for
web browsers).

%prep
%setup

%pom_remove_plugin :maven-checkstyle-plugin

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles

%changelog
* Fri Dec 05 2025 Ivan Khanas <xeno@altlinux.org> 1.6.0-alt1
- First build for ALT.
