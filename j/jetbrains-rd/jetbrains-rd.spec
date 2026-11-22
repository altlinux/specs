%define _unpackaged_files_terminate_build 1

Name: jetbrains-rd
Version: 2026.3.2
Release: alt1

Summary: JetBrains Reactive Distributed communication framework
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/rd
VCS: https://github.com/JetBrains/rd.git

Source0: %name-%version.tar
Patch0: %name-system.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib-jdk8)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit5)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-core)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(org.jetbrains.intellij.deps:trove4j)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(com.squareup.okhttp3:okhttp)

BuildArch: noarch

%description
JetBrains RD is a reactive distributed communication framework. This package
provides its Kotlin artifacts: core, framework, generator, Swing integration,
and text utilities.

%package core
Summary: JetBrains RD core module
Group: Development/Java

%description core
JetBrains RD core module.

%package framework
Summary: JetBrains RD framework module
Group: Development/Java

%description framework
JetBrains RD framework module.

%package gen
Summary: JetBrains RD gen module
Group: Development/Java

%description gen
JetBrains RD gen module.

%package swing
Summary: JetBrains RD swing module
Group: Development/Java

%description swing
JetBrains RD swing module.

%package text
Summary: JetBrains RD text module
Group: Development/Java

%description text
JetBrains RD text module.

%prep
%setup -q -n jetbrains-rd-%version
%patch0 -p1

%build
# Validate the build logic against the system Gradle before product publication.
TEAMCITY_VERSION=1 %__gradle -p buildSrc compileKotlin --offline
TEAMCITY_VERSION=1 %gradle_publish

%install
%mvn_package com.jetbrains.rd:rd-core core
%mvn_package com.jetbrains.rd:rd-framework framework
%mvn_package com.jetbrains.rd:rd-gen gen
%mvn_package com.jetbrains.rd:rd-swing swing
%mvn_package com.jetbrains.rd:rd-text text
%gradle_register --artifacts=rd-core-,rd-framework-,rd-gen-,rd-swing-,rd-text-
%gradle_install

%check
TEAMCITY_VERSION=1 %gradle_check

%files core -f .mfiles-core
%doc LICENSE

%files framework -f .mfiles-framework

%files gen -f .mfiles-gen

%files swing -f .mfiles-swing

%files text -f .mfiles-text

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 2026.3.2-alt1
- Initial build for ALT.
