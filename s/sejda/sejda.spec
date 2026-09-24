%define milestone M6
%define upstream_version %version.%milestone

Name: sejda
Version: 6.0.0
Release: alt0.1

Summary: An extendible and configurable PDF manipulation layer library written in java

License: AGPL-3.0
Group: Development/Java
Url: https://sejda.org
Vcs: https://github.com/torakiki/sejda.git
BuildArch: noarch
ExcludeArch: %ix86

Source0: https://github.com/torakiki/%name/archive/v%upstream_version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: java-25-openjdk-devel

BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.sejda:sejda-io)
BuildRequires: mvn(jakarta.validation:jakarta.validation-api)
BuildRequires: mvn(org.glassfish:jakarta.el)
BuildRequires: mvn(com.ibm.icu:icu4j)
BuildRequires: mvn(com.twelvemonkeys.imageio:imageio-core)
BuildRequires: mvn(com.twelvemonkeys.imageio:imageio-metadata)
BuildRequires: mvn(com.twelvemonkeys.imageio:imageio-tiff)
BuildRequires: mvn(com.twelvemonkeys.imageio:imageio-jpeg)
BuildRequires: mvn(org.sejda:sambox)
BuildRequires: mvn(org.bouncycastle:bcmail-jdk18on)
BuildRequires: mvn(com.drewnoakes:metadata-extractor)
BuildRequires: mvn(net.coobird:thumbnailator)
BuildRequires: mvn(org.hibernate.validator:hibernate-validator)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(com.github.romankh3:image-comparison)

%description
An extendible and configurable PDF manipulation layer library written in java.

%javadoc_package

%prep
%setup -n %name-%upstream_version

%pom_remove_plugin :maven-toolchains-plugin
%pom_disable_module sejda-tests

# The system metadata-extractor uses its automatic JPMS module name.
subst 's/requires com.drew.metadata;/requires metadata.extractor;/' sejda-sambox/src/main/java/module-info.java

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Wed Sep 09 2026 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt0.1
- NMU: update to 6.0.0.M6.
- Fix attachment extraction path traversal and harden XML configuration parsing.

* Fri May 15 2026 Anton Meleshnikov <alton@altlinux.org> 5.0.11-alt1
- Initial build for Sisyphus.
