Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global cli_tool cplc

Name:           classpathless-compiler
Version:        2.1.1
Release:        alt1_3jpp11
Summary:        Tool for recompiling java sources with customizable class providers
License:        ASL 2.0
URL:            https://github.com/mkoncek/classpathless-compiler
BuildArch:      noarch

Source0:        https://github.com/mkoncek/classpathless-compiler/archive/refs/tags/%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.ow2.asm:asm-tree)

Requires:       beust-jcommander
Requires:       javapackages-tools
Source44: import.info

%description
Classpathless compiler (CPLC) is a compiler wrapper used for compiling java
sources with customizable class providers. This tool works differently from the
traditional java compiler in that it doesn't use provided classpath but instead
pulls dependencies using an API.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n classpathless-compiler-%{version}

find -name '*.java' -exec sed -i '/@SuppressFBWarnings\|import edu\.umd\.cs\.findbugs/d' {} +

%pom_remove_dep :spotbugs-annotations

%pom_remove_plugin :maven-assembly-plugin impl
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%jpackage_script io.github.mkoncek.classpathless.Tool "" "" classpathless-compiler/classpathless-compiler:classpathless-compiler/classpathless-compiler-api:classpathless-compiler/classpathless-compiler-util:beust-jcommander %{cli_tool}

%files -f .mfiles
%{_bindir}/%{cli_tool}

%doc --no-dereference LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 2.1.1-alt1_3jpp11
- new version

* Mon Aug 16 2021 Igor Vlasenko <viy@altlinux.org> 1.4-alt1_1jpp11
- new version

