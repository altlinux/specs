%define _unpackaged_files_terminate_build 1

Name: jakarta-cdi-api
Version: 5.0.0
Release: alt1

Summary: Contexts and Dependency Injection APIs
License: Apache-2.0
Group: Development/Java
URL: https://jakarta.ee/specifications/cdi/
VCS: https://github.com/jakartaee/cdi.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: ee4j-parent
BuildRequires: atinject
BuildRequires: jakarta-annotations
BuildRequires: jakarta-interceptors
BuildRequires: jakarta-el-api
BuildRequires: maven-plugin-bundle
BuildRequires: testng
BuildRequires: asciidoctor

%description
The Contexts and Dependency Injection APIs, language model, EL integration
and IDE configuration. CDI 5 uses the genuine jakarta.cdi coordinates.

%package -n cdi-api-compat4
Summary: CDI 4.1 APIs for the Jakarta Enterprise coordinates
Group: Development/Java

%description -n cdi-api-compat4
The original CDI 4.1 API, language model and EL integration from the
official 4.1.0 release, with the genuine Jakarta Enterprise coordinates.


%package lang-model
Summary: Jakarta CDI language model API
Group: Development/Java

%description lang-model
Jakarta CDI language model API.

%package el
Summary: Jakarta CDI expression language integration
Group: Development/Java

%description el
Jakarta CDI expression language integration.

%package ide-config
Summary: Jakarta CDI IDE configuration
Group: Development/Java

%description ide-config
Jakarta CDI IDE configuration.

%package -n cdi-api-compat4-lang-model
Summary: CDI 4.1 language model API
Group: Development/Java

%description -n cdi-api-compat4-lang-model
CDI 4.1 language model API.

%package -n cdi-api-compat4-el
Summary: CDI 4.1 expression language integration
Group: Development/Java

%description -n cdi-api-compat4-el
CDI 4.1 expression language integration.

%package -n cdi-api-compat4-ide-config
Summary: CDI 4.1 IDE configuration
Group: Development/Java

%description -n cdi-api-compat4-ide-config
CDI 4.1 IDE configuration.

%package javadoc
Summary: API documentation for CDI
Group: Documentation

%description javadoc
Independent API documentation for CDI 5 and CDI 4.1.

%package manual
Summary: CDI specifications
Group: Documentation

%description manual
The complete HTML specifications from the selected CDI releases.

%prep
%setup -q
for module in . cdi4; do
    # Formatting is not part of RPM compilation or test qualification.
    %pom_xpath_remove "pom:profiles/pom:profile[pom:id='format']" "$module"
    %pom_xpath_remove "pom:profiles/pom:profile[pom:id='validate']" "$module"
    %pom_xpath_remove "pom:build/pom:pluginManagement" "$module"
    # Upstream RAT scans a release archive, not the combined Gear tree.
    # Original license files and notices are retained and installed.
    %pom_remove_plugin org.apache.rat:apache-rat-plugin "$module"
    %pom_remove_plugin -r :maven-source-plugin "$module"
    # XMvn generates independent Javadoc for each API.
    %pom_remove_plugin -r :maven-javadoc-plugin "$module"
    # Retain the spec POM; native Asciidoctor produces complete HTML below.
    %pom_remove_plugin org.asciidoctor:asciidoctor-maven-plugin "$module/spec"
done
%mvn_compat_version 'jakarta.enterprise:*' %version
%mvn_file jakarta.cdi:jakarta.cdi-api %name/jakarta.cdi-api
%mvn_file jakarta.cdi:jakarta.cdi-lang-model-api %name/jakarta.cdi-lang-model-api
%mvn_file jakarta.cdi:jakarta.cdi-el-api %name/jakarta.cdi-el-api
%mvn_file jakarta.cdi:jakarta.cdi-ide-config %name/jakarta.cdi-ide-config
%mvn_package jakarta.cdi:jakarta.cdi-parent
%mvn_package jakarta.cdi:jakarta.cdi-api
%mvn_package jakarta.cdi:jakarta.cdi-lang-model-api lang-model
%mvn_package jakarta.cdi:jakarta.cdi-el-api el
%mvn_package jakarta.cdi:jakarta.cdi-ide-config ide-config
%mvn_package jakarta.cdi:jakarta.cdi-spec-doc
%mvn_package jakarta.enterprise:jakarta.enterprise.cdi-parent
%mvn_package jakarta.enterprise:jakarta.enterprise.cdi-api
%mvn_package jakarta.enterprise:jakarta.enterprise.lang-model lang-model
%mvn_package jakarta.enterprise:jakarta.enterprise.cdi-el-api el
%mvn_package jakarta.enterprise:jakarta.enterprise.cdi-spec-doc

pushd cdi4
%mvn_compat_version 'jakarta.enterprise:*' 4.1.0
%mvn_file :jakarta.enterprise.cdi-api %name-compat4/jakarta.enterprise.cdi-api
%mvn_file :jakarta.enterprise.lang-model \
    %name-compat4/jakarta.enterprise.lang-model
%mvn_file :jakarta.enterprise.cdi-el-api \
    %name-compat4/jakarta.enterprise.cdi-el-api
%mvn_file :cdi-ide-config %name-compat4/cdi-ide-config
%mvn_package :jakarta.enterprise.lang-model compat4-lang-model
%mvn_package :jakarta.enterprise.cdi-el-api compat4-el
%mvn_package :cdi-ide-config compat4-ide-config
%mvn_package :jakarta.enterprise.cdi-api compat4
%mvn_package :jakarta.enterprise.cdi-parent compat4
%mvn_package :jakarta.enterprise.cdi-spec-doc compat4
popd

%build
java -version
%mvn_build -s
pushd cdi4
%mvn_build -s
popd
asciidoctor -b html5 -d book -a data-uri -a imagesdir=images \
    -a revnumber=5.0 -a revdate=2026-08-20 -a 'revremark=Draft(M1)' \
    -D target/manual spec/src/main/asciidoc/cdi-spec.asciidoc
asciidoctor -b html5 -d book -a data-uri -a imagesdir=images \
    -a revnumber=4.1 -a revdate=2024-03-07 -a revremark=Final \
    -D cdi4/target/manual cdi4/spec/src/main/asciidoc/cdi-spec.asciidoc

%install
# Generated module-source-path links and Javadoc arguments are build inputs.
rm -rf target/xmvn-apidocs/module-source-path \
    cdi4/target/xmvn-apidocs/module-source-path
rm -f target/xmvn-apidocs/args cdi4/target/xmvn-apidocs/args
%mvn_install
pushd cdi4
%mvn_install -J __compat_documentation_is_installed_below
install -d %buildroot%_javadocdir/%name/compat4
cp -a .xmvn/apidocs/. %buildroot%_javadocdir/%name/compat4/
popd
install -d %buildroot%_docdir/%name-manual-%version/manual/{5,4.1}
cp target/manual/cdi-spec.html \
    %buildroot%_docdir/%name-manual-%version/manual/5/
cp cdi4/target/manual/cdi-spec.html \
    %buildroot%_docdir/%name-manual-%version/manual/4.1/

%files -f .mfiles
%doc LICENSE.txt NOTICE.md

%files -n cdi-api-compat4 -f cdi4/.mfiles-compat4

%files lang-model -f .mfiles-lang-model

%files el -f .mfiles-el

%files ide-config -f .mfiles-ide-config

%files -n cdi-api-compat4-lang-model -f cdi4/.mfiles-compat4-lang-model

%files -n cdi-api-compat4-el -f cdi4/.mfiles-compat4-el

%files -n cdi-api-compat4-ide-config -f cdi4/.mfiles-compat4-ide-config

%files javadoc -f .mfiles-javadoc

%files manual
%dir %_docdir/%name-manual-%version
%_docdir/%name-manual-%version/manual

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 5.0.0-alt1
- Initial build for ALT.
