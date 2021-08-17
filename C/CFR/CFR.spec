Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           CFR
Version:        0.151
Release:        alt1_4jpp11
Summary:        CFR - Another Java Decompiler

License:        MIT
URL:            https://github.com/leibnitz27/cfr
Source0:        https://github.com/leibnitz27/cfr/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin

Requires:       javapackages-tools

Provides:       cfr
Provides:       Cfr

%global lowercase_name cfr
%global build_folder %{lowercase_name}-%{version}
Source44: import.info

%description
CFR will decompile modern Java features - including much of Java 9, 12 & 14,
but is written entirely in Java 6, so will work anywhere!
It'll even make a decent go of turning class files from other JVM languages back into java!

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{build_folder}

%pom_remove_plugin :git-commit-id-plugin
%pom_remove_plugin :templating-maven-plugin
%pom_remove_plugin :maven-jar-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-gpg-plugin

# workaround for template-maven-plugin
sed -i 's/${project.version}/%{version}/' %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java
sed -i 's/${git.commit.id.abbrev}/%{version}/' %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java
sed -i 's/${git.dirty}/false/' %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java
cp %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java %{_builddir}/%{build_folder}/src/org/benf/cfr/reader/util/CfrVersionInfo.java


%build
%mvn_build


%install
%mvn_install
%jpackage_script org.benf.cfr.reader.Main "" "" %{name}/%{name} %{lowercase_name}


%files -f .mfiles
%doc --no-dereference LICENSE
%doc README.md
%{_bindir}/%{lowercase_name}


%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE


%changelog
* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0.151-alt1_4jpp11
- new version

