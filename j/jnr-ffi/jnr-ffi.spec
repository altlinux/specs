Group: System/Libraries
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:     jnr-ffi
Version:  2.1.8
Release:  alt1_12jpp11
Summary:  Java Abstracted Foreign Function Layer
License:  ASL 2.0
URL:      http://github.com/jnr/%{name}/
Source0:  https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz

# Taken from https://github.com/jnr/jnr-ffi/commit/edda8cfe60b77ceeba301d20db0f5c996b958f5a
Patch1:   0001-Convert-int-to-boolean-like-C-does-nonzero-is-true.patch

BuildRequires:  gcc

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jffi)
BuildRequires:  mvn(com.github.jnr:jffi::native:)
BuildRequires:  mvn(com.github.jnr:jnr-x86asm)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)

BuildArch:     noarch
Source44: import.info

%description
An abstracted interface to invoking native functions from java

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch1 -p1

# remove all builtin jars
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

# Unnecessary for RPM builds
%pom_remove_parent
%pom_remove_plugin ":maven-javadoc-plugin"

# Port to maven-antrun-plugin 3.0.0
sed -i s/tasks/target/ pom.xml

# don't fail on unused parameters... (TODO: send patch upstream)
sed -i 's|-Werror||' libtest/GNUmakefile

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dasm.version=7.0

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.1.8-alt1_12jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.1.8-alt1_9jpp11
- update

* Sat Jul 20 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.8-alt1_3jpp8
- fc update & java 8 build

* Wed May 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.6-alt1_4jpp8
- java update

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.6-alt1_2jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1_4jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.10-alt1_3jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.10-alt1_2jpp7
- new version

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.10-alt3_3jpp7
- fixed build

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.10-alt2_3jpp7
- gcc47 build

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.10-alt1_3jpp7
- new version

