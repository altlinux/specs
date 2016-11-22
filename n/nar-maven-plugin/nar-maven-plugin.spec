Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             nar-maven-plugin
Version:          3.0.0
Release:          alt1_11jpp8
Summary:          Native ARchive plugin for Maven
License:          ASL 2.0 and LGPLv2
URL:              https://github.com/maven-nar/nar-maven-plugin/
Source0:          https://github.com/maven-nar/nar-maven-plugin/archive/nar-maven-plugin-%{version}.tar.gz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:           0001-Add-support-for-handling-the-RPM_OPT_FLAGS-variable-.patch
Patch1:           0002-Added-ARM-support.patch
Patch2:           0003-Added-PPC64LE-support.patch
# Patch adds support for rest sec archs not included in previous patches, 
# also fixes bad C defines on ppc64le
Patch3:           secarch.patch

BuildRequires:    maven-local
BuildRequires:    mvn(commons-io:commons-io)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.ant:ant)
BuildRequires:    mvn(org.apache.bcel:bcel)
BuildRequires:    mvn(org.apache.maven:maven-core)
BuildRequires:    mvn(org.apache.maven:maven-model)
BuildRequires:    mvn(org.apache.maven:maven-plugin-api)
BuildRequires:    mvn(org.apache.maven:maven-project)
BuildRequires:    mvn(org.apache.maven:maven-toolchain)
BuildRequires:    mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:    mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:    mvn(org.apache.maven.shared:maven-artifact-resolver)
BuildRequires:    mvn(org.apache.maven.surefire:surefire-booter)
BuildRequires:    mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:    mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:    mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:    mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:    mvn(xerces:xercesImpl)

Requires:         gcc-c++-common

BuildArch:        noarch
Source44: import.info

%description
The NAR plugin for Maven allows you to compile native code (C++, C and Fortran)
on a number of different architectures (Linux, Windows, MacOSX, Solaris, ...)
and with a number of different compilers/linkers (g++, Microsoft Visual C++,
CC, ...) The output produced is wrapped up in Native ARchive files (.nar) some
of which are machine independent (-noarch), while others are machine specific
and thus depend on a combination of machine architecture(A),
operating-system(O) and linker(L) identified as AOL. These nar files can be
installed in the local Maven repository and deployed to a standard Maven (web)
server, using the standard maven-install-plugin and maven-deploy-plugin.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n nar-maven-plugin-nar-maven-plugin-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .secarch

# Remove bundled stuff
rm -rf src/it/it0006-jni-3rdparty/src/nar/resources/aol

%pom_xpath_remove "pom:build/pom:extensions"
# Duplicate pom entry
#%% pom_add_dep "org.apache.maven.surefire:surefire-booter"
%pom_add_dep "org.apache.maven.shared:maven-artifact-resolver"

%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

cp %{SOURCE1} .

rm src/main/java/com/github/maven_nar/NarIntegrationTestMojo.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc README.md
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_11jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_8jpp8
- new version

