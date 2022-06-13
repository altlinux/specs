Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jol
Version:        0.16
Release:        alt1_1jpp11
Summary:        Java Object Layout

License:        GPLv2 with exceptions
URL:            https://openjdk.java.net/projects/code-tools/jol/
Source0:        https://github.com/openjdk/jol/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.jopt-simple:jopt-simple)
BuildRequires:  mvn(org.ow2.asm:asm)

BuildArch:      noarch

%global _desc \
JOL (Java Object Layout) is a tiny toolbox to analyze Java object\
layouts.  These tools use Unsafe, JVMTI, and Serviceability Agent (SA)\
heavily to decode the actual object layout, footprint, and references.\
This makes JOL much more accurate than other tools relying on heap dumps,\
specification assumptions, etc.
Source44: import.info

%description 

# Uncomment this once javadocs can be generated again
# See https://github.com/fedora-java/xmvn/issues/58
#%%{?javadoc_package}

%_desc
%package        parent
Group: Development/Java
Summary:        Java Object Layout parent POM

%description    parent 

This package contains the parent POM for JOL.

%_desc
%package        core
Group: Development/Java
Summary:        Java Object Layout core classes

%description    core 

This package contains the core classes for JOL.

%_desc
%package        cli
Group: Development/Java
Summary:        Java Object Layout command line interface
Requires:       %{name}-core = %{version}-%{release}

%description    cli 

This package contains a command line interface to JOL.

%_desc
%prep
%setup -q


# Unnecessary plugins for an RPM build
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-source-plugin

# We do not need benchmarks or samples
%pom_disable_module jol-benchmarks
%pom_disable_module jol-samples

# Build for JDK 1.8
sed -i 's/1\.7/1.8/' pom.xml

%build
# Skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -s -j -f

%install
%mvn_install

%files parent -f .mfiles-jol-parent
%doc --no-dereference LICENSE

%files core -f .mfiles-jol-core
%doc README.md
%doc --no-dereference LICENSE

%files cli -f .mfiles-jol-cli

%changelog
* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0.16-alt1_1jpp11
- java11 build

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 0.16-alt1_1jpp8
- new version

