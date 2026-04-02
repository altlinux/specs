Name:           jaxb-istack-commons
Version:        4.2.0
Release:        alt1.1

Summary:        iStack Common Utility Code
License:        BSD-3-Clause
Group:          Development/Java
URL:            https://github.com/eclipse-ee4j/jaxb-istack-commons
VCS:            https://github.com/eclipse-ee4j/jaxb-istack-commons

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.glassfish.jaxb:codemodel)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(args4j:args4j)

BuildArch:      noarch

%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.

%package -n istack-commons-maven-plugin
Group:          Development/Java
Summary:        istack-commons Maven Mojo
%description -n istack-commons-maven-plugin
This package contains the istack-commons Maven Mojo.

%package -n import-properties-plugin
Group:          Development/Java
Summary:        istack-commons import properties plugin
%description -n import-properties-plugin
This package contains the istack-commons import properties Maven Mojo.

%package -n istack-commons-runtime
Group:          Development/Java
Summary:        istack-commons runtime
%description -n istack-commons-runtime
This package contains istack-commons runtime.

%package -n istack-commons-tools
Group:          Development/Java
Summary:        istack-commons tools
%description -n istack-commons-tools
This package contains istack-commons tools.

%package -n istack-commons-buildtools
Group:          Development/Java
Summary:        istack-commons buildtools
%description -n istack-commons-buildtools
This package contains istack-commons buildtools.

%package -n istack-commons-soimp
Group:          Development/Java
Summary:        istack-commons soimp
%description -n istack-commons-soimp
This package contains istack-commons soimp.

%package -n istack-commons-test
Group:          Development/Java
Summary:        istack-commons test
%description -n istack-commons-test
This package contains istack-commons test.

%prep
%setup -n %name-%version/istack-commons

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%mvn_package :istack-commons __noinstall

%build
%mvn_build -j -s

%install
%mvn_install

%files -n istack-commons-maven-plugin -f .mfiles-istack-commons-maven-plugin
%doc ../LICENSE.md ../NOTICE.md

%files -n import-properties-plugin -f .mfiles-import-properties-plugin
%doc ../LICENSE.md ../NOTICE.md

%files -n istack-commons-runtime -f .mfiles-istack-commons-runtime
%doc ../LICENSE.md ../NOTICE.md

%files -n istack-commons-tools -f .mfiles-istack-commons-tools
%doc ../LICENSE.md ../NOTICE.md

%files -n istack-commons-buildtools -f .mfiles-istack-commons-buildtools
%doc ../LICENSE.md ../NOTICE.md

%files -n istack-commons-test -f .mfiles-istack-commons-test
%doc ../LICENSE.md ../NOTICE.md

%files -n istack-commons-soimp -f .mfiles-istack-commons-soimp
%doc ../LICENSE.md ../NOTICE.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 4.2.0-alt1.1
- Cosmetic fixes.

* Thu Jan 15 2026 Evgeniy Serov <scala@altlinux.org> 4.2.0-alt1
- Updated to 4.2.0.
- Removed import.info.

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 3.0.12-alt1_3jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 3.0.11-alt1_4jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 3.0.11-alt1_3jpp11
- new version

