Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname jaf

Name:           jakarta-activation
Version:        1.2.1
Release:        alt2_5jpp11
Summary:        Jakarta Activation Specification and Implementation
License:        BSD

URL:            https://eclipse-ee4j.github.io/jaf/
Source0:        https://github.com/eclipse-ee4j/jaf/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

Provides:       jaf = %{version}-%{release}
Obsoletes:      jaf < 1.2.1-5
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
%setup -q -n %{srcname}-%{version}

# remove unnecessary dependency on "org.eclipse.ee4j:project" (not packaged)
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :build-helper-maven-plugin
%pom_remove_plugin :directory-maven-plugin
%pom_remove_plugin :osgiversion-maven-plugin

# remove custom doclet configuration
%pom_remove_plugin :maven-javadoc-plugin activation

# disable demo submodule
%pom_disable_module demo

# set bundle version manually instead of with osgiversion-maven-plugin
# (the plugin is only used to strip off -SNAPSHOT or -Mx qualifiers)
sed -i "s/\${activation.osgiversion}/%{version}/g" activation/pom.xml


%build
%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md


%changelog
* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 1.2.1-alt2_5jpp11
- fixed build

* Thu May 13 2021 Igor Vlasenko <viy@altlinux.org> 1.2.1-alt1_5jpp11
- new version

