%define _unpackaged_files_terminate_build 1

Name: asn-one
Version: 0.7.0
Release: alt1

Summary: ASN.1 encoding and decoding library for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/hierynomus/asn-one
VCS: https://github.com/hierynomus/asn-one

Source0: %name-%version.tar
Patch0: %name-%version.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.spockframework:spock-core)
BuildRequires: mvn(org.apache.groovy:groovy)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(ch.qos.logback:logback-classic)

BuildArch: noarch

%description
asn-one is a standalone Java library for encoding and decoding ASN.1 data
using the BER and DER encoding rules.

%prep
%setup -q
%patch0 -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=asn-one-
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
