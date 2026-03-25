Name: metadata-extractor
Version: 2.18.0
Release: alt1

Summary: Java library for extracting EXIF, IPTC, XMP, ICC and other metadata from image and video files.
License: Apache-2.0
Group: Development/Java
Url: https://github.com/drewnoakes/metadata-extractor.git
Vcs: https://github.com/drewnoakes/metadata-extractor.git.git
BuildArch: noarch

Source0: https://github.com/drewnoakes/metadata-extractor/archive/%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default

BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(com.adobe.xmp:xmpcore)

%description
Java library for extracting EXIF, IPTC, XMP, ICC and other metadata from image and video files.

%javadoc_package

%prep
%setup

%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Wed Mar 25 2026 Anton Meleshnikov <alton@altlinux.org> 2.18.0-alt1
- Initial build for Sisyphus.
