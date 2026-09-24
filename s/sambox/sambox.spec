%define milestone M7
%define upstream_version %version.%milestone

Name: sambox
Version: 4.0.0
Release: alt0.1

Summary: A PDFBox fork intended to be used as PDF processor for Sejda and PDFsam

License: Apache-2.0
Group: Development/Java
Url: https://github.com/torakiki/sambox
Vcs: https://github.com/torakiki/sambox.git
BuildArch: noarch
ExcludeArch: %ix86

Source0: https://github.com/torakiki/sambox/archive/v%upstream_version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: java-25-openjdk-devel

BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.sejda:sejda-io)
BuildRequires: mvn(org.bouncycastle:bcmail-jdk18on)
BuildRequires: fontbox2
BuildRequires: mvn(org.apache.pdfbox:xmpbox)

%description
An Apache PDFBox fork intended to be used as PDF processor
for Sejda and PDFsam related projects.

%javadoc_package

%prep
%setup -n %name-%upstream_version

%pom_remove_plugin :maven-toolchains-plugin
%pom_remove_plugin :download-maven-plugin

# Resolve the parallel-installable FontBox 2 compatibility artifact.
%pom_change_dep org.apache.pdfbox:fontbox org.apache.pdfbox:fontbox:2

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE NOTICE.txt

%changelog
* Wed Sep 09 2026 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt0.1
- NMU: update to 4.0.0.M7.

* Fri May 15 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.6-alt1
- Initial build for Sisyphus.
