%define _unpackaged_files_terminate_build 1

Name: glassfish-hk2-extra
Version: 3.0.0
Release: alt3

Summary: HK2 OSGi resource locator
License: EPL-2.0
Group: Development/Java
Url: https://github.com/eclipse-ee4j/glassfish-hk2-extra
Vcs: https://github.com/eclipse-ee4j/glassfish-hk2-extra.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-build-helper
BuildRequires: osgi-core
BuildRequires: osgi-compendium
BuildRequires: glassfish-hk2-core
BuildRequires: glassfish-hk2-osgi-adapter
BuildRequires: args4j
BuildRequires: apache-commons-bcel
BuildRequires: junit5
BuildRequires: ee4j-parent

%description
%summary

%package osgi-resource-locator
Summary: HK2 OSGi resource locator
Group: Development/Java
Provides: glassfish-hk2-extra = %EVR
Obsoletes: glassfish-hk2-extra < %EVR

%description osgi-resource-locator
HK2 OSGi resource locator module.

%package bundle-viewer
Summary: HK2 OSGi bundle viewer
Group: Development/Java

%description bundle-viewer
HK2 OSGi bundle viewer module.

%package dependency-verifier
Summary: HK2 dependency verifier
Group: Development/Java
%description dependency-verifier
HK2 dependency verifier module.

%package dependency-visualizer
Summary: HK2 dependency visualizer
Group: Development/Java

%description dependency-visualizer
HK2 dependency visualizer module.

%prep
%setup
%autopatch -p1
%pom_remove_plugin :maven-javadoc-plugin osgi-resource-locator
%pom_remove_plugin :osgiversion-maven-plugin osgi-resource-locator
sed -i 's/${project.osgi.version}/%{version}/' osgi-resource-locator/osgi.bundle

%build
%mvn_build -s -j -f

%install
%mvn_install

%files -f .mfiles-hk2-extra-parent
%doc --no-dereference LICENSE.md NOTICE.md README.md

%files osgi-resource-locator -f .mfiles-osgi-resource-locator
%files bundle-viewer -f .mfiles-bundle-viewer
%files dependency-verifier -f .mfiles-hk2-dependency-verifier
%files dependency-visualizer -f .mfiles-hk2-dependency-visualizer

%changelog
* Thu Jun 18 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.0-alt3
- FTBFS fix.

* Wed Apr 01 2026 Ivan Khanas <xeno@altlinux.org> 3.0.0-alt2
- Augmented packaging.

* Tue Mar 24 2026 Ivan Khanas <xeno@altlinux.org> 3.0.0-alt1
- First build for ALT.
