%define _unpackaged_files_terminate_build 1

Name: reflectasm
Version: 1.11.9
Release: alt2

Summary: Fast Java reflection using generated access classes
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/EsotericSoftware/reflectasm
VCS: https://github.com/EsotericSoftware/reflectasm.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

%description
ReflectASM is a very small Java library that provides
high performance reflection by using code generation.
An access class is generated to set/get fields,
call methods, or create a new instance. The access class
uses byte-code rather than Java's reflection, so it
is much faster. It can also access primitive fields
via byte-code to avoid boxing.

%package javadoc
Summary: Javadoc for %name
Group: Development/Java

%description javadoc
This package contains javadoc for %name.

%prep
%setup -q
%autopatch -p1
find -name "*.class" -delete
find -name "*.jar" -delete

sed -i 's/\r//' license.txt
# Do not shade asm
%pom_remove_plugin :maven-shade-plugin

%mvn_file :%name %name
%mvn_alias :%name "com.esotericsoftware.%name:%name"

# The system ASM dependency must remain visible to OSGi consumers.
bundle_instructions="pom:build/pom:plugins/pom:plugin"
bundle_instructions="$bundle_instructions[pom:artifactId='maven-bundle-plugin']"
bundle_instructions="$bundle_instructions/pom:configuration/pom:instructions"
reflectasm_module=com.esotericsoftware.reflectasm
%pom_xpath_set "$bundle_instructions/pom:Import-Package" '*'
%pom_xpath_inject "$bundle_instructions" \
    "<Automatic-Module-Name>$reflectasm_module</Automatic-Module-Name>"
compiler_config="pom:build/pom:plugins/pom:plugin"
compiler_config="$compiler_config[pom:artifactId='maven-compiler-plugin']"
compiler_config="$compiler_config/pom:configuration"
%pom_xpath_set "$compiler_config/pom:source" 8
%pom_xpath_set "$compiler_config/pom:target" 8
%pom_xpath_inject "$compiler_config" '<release>8</release>'

%build
%mvn_build -- -Dmaven.javadoc.source=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference license.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 1.11.9-alt2
- New version.
- Support accessors on modern JDKs.

* Fri Aug 27 2021 Igor Vlasenko <viy@altlinux.org> 1.11.0-alt3_8jpp11
- rebuild with jpackage-default

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.11.0-alt2_8jpp11
- fixed build

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_8jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_2jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_4jpp7
- new release

