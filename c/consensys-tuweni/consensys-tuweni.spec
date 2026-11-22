%define _unpackaged_files_terminate_build 1

Name: consensys-tuweni
Version: 2.8.0
Release: alt1

Summary: Consensys Tuweni TOML parser library
License: Apache-2.0
Group: Development/Java
URL: https://github.com/Consensys/tuweni
VCS: https://github.com/Consensys/tuweni.git

Source0: tuweni-%version.tar
Patch0: tuweni-toml-only.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.antlr:antlr4)
BuildRequires: mvn(org.antlr:antlr4-runtime)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)

BuildArch: noarch

%description
Tuweni TOML is a Java parser for Tom's Obvious, Minimal Language. This package
contains the standalone io.consensys.tuweni:tuweni-toml module.

%prep
%setup -q -n tuweni-%version
%autopatch -p1

%build
%gradle_publish

%check
%gradle_check

%install
%gradle_register --artifacts=tuweni-toml
%gradle_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 2.8.0-alt1
- Initial build for ALT.
