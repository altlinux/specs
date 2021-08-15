Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jakarta-activation
Version:        1.2.2
Release:        alt1_4jpp11
Summary:        Jakarta Activation Specification and Implementation
License:        BSD
URL:            https://eclipse-ee4j.github.io/jaf/
BuildArch:      noarch

Source0:        https://github.com/eclipse-ee4j/jaf/archive/%{version}/jaf-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Source44: import.info

%description
Jakarta Activation lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to
it; discover the operations available on it; and instantiate the
appropriate bean to perform the operation(s).

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jaf-%{version}

%pom_remove_parent
%pom_disable_module demo

%pom_remove_plugin :directory-maven-plugin
sed -i 's/${main.basedir}/${basedir}/' pom.xml

# remove custom doclet configuration
%pom_remove_plugin :maven-javadoc-plugin activation

# set bundle version manually instead of with osgiversion-maven-plugin
# (the plugin is only used to strip off -SNAPSHOT or -Mx qualifiers)
%pom_remove_plugin :osgiversion-maven-plugin
sed -i "s/\${activation.osgiversion}/%{version}/g" activation/pom.xml

%build
# javadoc temporairly disabled due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.md NOTICE.md

# javadoc temporairly disabled due to https://github.com/fedora-java/xmvn/issues/58
#%files javadoc -f .mfiles-javadoc
%files javadoc
%doc --no-dereference LICENSE.md NOTICE.md

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.2.2-alt1_4jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.2.2-alt1_1jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 1.2.1-alt2_5jpp11
- fixed build

* Thu May 13 2021 Igor Vlasenko <viy@altlinux.org> 1.2.1-alt1_5jpp11
- new version

