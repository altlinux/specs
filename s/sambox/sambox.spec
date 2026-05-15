Name: sambox
Version: 3.0.6
Release: alt1

Summary: A PDFBox fork intended to be used as PDF processor for Sejda and PDFsam
License: Apache-2.0
Group: Development/Java
Url: https://github.com/torakiki/sambox
Vcs: https://github.com/torakiki/sambox.git
BuildArch: noarch

Source0: https://github.com/torakiki/sambox/archive/v%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: java-17-openjdk-devel

BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.sejda:sejda-io)
BuildRequires: mvn(org.bouncycastle:bcmail-jdk18on)
BuildRequires: fontbox2

%description
An Apache PDFBox fork intended to be used as PDF processor
for Sejda and PDFsam related projects.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-toolchains-plugin
%pom_remove_plugin :download-maven-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE NOTICE.txt

%changelog
* Fri May 15 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.6-alt1
- Initial build for Sisyphus.
