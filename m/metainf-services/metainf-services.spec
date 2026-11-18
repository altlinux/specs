%define _unpackaged_files_terminate_build 1

Name: metainf-services
Version: 1.11
Release: alt1

Summary: Annotation processor for META-INF/services registration
License: MIT
Group: Development/Java
URL: https://github.com/kohsuke/metainf-services
VCS: https://github.com/kohsuke/metainf-services.git

Source0: %name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.kohsuke:pom:pom:)
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

%description
Annotation processor that generates META-INF/services descriptors from
annotated Java provider classes.

%prep
%setup -q

sed -n '1,/^ \*\/$/p' src/main/java/org/kohsuke/MetaInfServices.java \
    > LICENSE

# Preserve the Java 8 API check with the compiler's platform signatures.
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_xpath_remove pom:build/pom:plugins/pom:plugin[1]/pom:configuration/pom:source
%pom_xpath_remove pom:build/pom:plugins/pom:plugin[1]/pom:configuration/pom:target
%pom_xpath_inject pom:build/pom:plugins/pom:plugin[1]/pom:configuration "<release>8</release>"

%build
%mvn_build -s

%install
%mvn_install
if [ -s .mfiles-javadoc ]; then
    cat .mfiles-javadoc >> .mfiles-%{name}
fi

%files -f .mfiles-%{name}
%doc LICENSE

%changelog
* Sat Nov 14 2026 Ivan Khanas <xeno@altlinux.org> 1.11-alt1
- Initial build for ALT.
