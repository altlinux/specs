BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           aether-ant-tasks
Version:        1.0
Release:        alt1_0.6.SNAPSHOTjpp7
Summary:        Ant tasks using Aether to resolve, install and deploy artifacts
Group:          Development/Java
BuildArch:      noarch

License:        EPL
URL:            https://github.com/sonatype/aether-ant-tasks
# git clone git://github.com/sonatype/aether-ant-tasks.git
# tar c --exclude-vcs aether-ant-tasks | lbzip2 >aether-ant-tasks.tar.bz2
Source0:        aether-ant-tasks.tar.bz2
Source1:        http://www.eclipse.org/legal/epl-v10.html

BuildRequires:  maven-local
BuildRequires:  aether
BuildRequires:  ant
BuildRequires:  maven-error-diagnostics
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  plexus-cipher
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-sec-dispatcher
Source44: import.info

%description
The Aether Ant Tasks enable build scripts for Apache Ant 1.7+ to use Sonatype
Aether to resolve dependencies and install and deploy locally built artifacts.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
cp -p %{SOURCE1} LICENSE

%build
# Tests are skipped because of missing dependency - mvn(junit:junit-dep)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.6.SNAPSHOTjpp7
- new release

