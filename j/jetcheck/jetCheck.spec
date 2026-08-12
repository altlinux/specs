%define _unpackaged_files_terminate_build 1
%define githash f3e7384

%def_with check

Name: jetcheck
Version: 0.2.1
Release: alt1.%githash

Summary: Property-based testing framework for Java
License: Apache-2.0
Group: Development/Java
Url: https://github.com/JetBrains/jetCheck
Vcs: https://github.com/JetBrains/jetCheck.git

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.jetbrains:annotations)

%if_with check
BuildRequires: mvn(junit:junit)
%endif

%description
jetCheck is a property-based testing library for Java,
developed by JetBrains. It generates random test data
according to specified generators and checks that properties hold.

%package javadoc
Summary: API documentation for jetCheck
Group: Development/Java

%description javadoc
API documentation for jetCheck.

%prep
%setup

for plugin in maven-release-plugin maven-gpg-plugin maven-source-plugin \
              jacoco-maven-plugin maven-checkstyle-plugin \
              maven-javadoc-plugin; do
    %pom_remove_plugin :$plugin || :
done

%build
%mvn_build %{?_without_check:-f}

%install
%mvn_install

%check
%mvn_build -s

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Aug 11 2026 Timofei Fedotov <sovtouch@altlinux.org> 0.2.1-alt1.f3e7384
- Initial build for ALT Sisyphus.
