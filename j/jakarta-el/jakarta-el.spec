Name: jakarta-el
Version: 6.0.1
Release: alt1

Summary: Jakarta Expression Language
License: EPL-2.0 or GPLv2 with exceptions
Group: Development/Java
Url: https://github.com/eclipse-ee4j/el-ri
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.surefire:surefire-junit47)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-17-compat
Requires: %name-api = %EVR

Provides: glassfish-el = %EVR
Obsoletes: glassfish-el < 3.0.1-1

%description
Jakarta Expression Language provides a specification document, API,
reference implementation and TCK that describes an expression language
for Java applications.

This package contains the implementation.

%package api
Group: Development/Java
Summary: Jakarta Expression Language API

# package renamed in fedora 33, remove in fedora 35
Provides: glassfish-el-api = %EVR
Obsoletes: glassfish-el-api < 3.0.1-1

%description api
Jakarta Expression Language provides a specification document, API,
reference implementation and TCK that describes an expression language
for Java applications.

This package contains only the API.

%package javadoc
Group: Development/Java
Summary: Javadoc for %name

# package renamed in fedora 33, remove in fedora 35
Provides: glassfish-el-javadoc = %version-%release
Obsoletes: glassfish-el-javadoc < 3.0.1-1
BuildArch: noarch

%description javadoc
This package contains javadoc for %name.

%prep
%setup

# remove unnecessary dependency on parent POM
%pom_remove_parent . api spec

# do not build specification documentation
%pom_disable_module spec

# provide javax.el packages in addition to jakarta.el to ease transition
cp -pr api/src/main/java/jakarta api/src/main/java/javax
sed -i -e 's/jakarta\./javax./g' $(find api/src/main/java/javax -name *.java)
%pom_xpath_replace pom:instructions/pom:Export-Package \
  '<Export-Package>jakarta.el,javax.el;version="3.0.0"</Export-Package>' api

# do not install useless parent POM
%mvn_package jakarta.el:el-parent __noinstall

# remove maven plugins unnecessary for RPM builds
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

# add maven artifact coordinate aliases for backwards compatibility
%mvn_alias jakarta.el:jakarta.el-api jakarta.el:jakarta.el org.glassfish:jakarta.el org.glassfish:javax.el
%mvn_alias jakarta.el:jakarta.el-api javax.el:javax.el-api javax.el:el-api

# add compat symlinks for packages constructing the classpath manually
%mvn_file :jakarta.el     %name/jakarta.el     glassfish-el
%mvn_file :jakarta.el-api %name/jakarta.el-api glassfish-el-api

%build
%mvn_build -s

%install
%mvn_install

%files
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%files api -f .mfiles-jakarta.el-api
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md

%changelog
* Mon Mar 30 2026 Ivan Khanas <xeno@altlinux.org> 6.0.1-alt1
- New version.

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 4.0.0-alt1_5jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 4.0.0-alt1_3jpp11
- new version
