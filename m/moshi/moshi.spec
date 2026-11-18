%define _unpackaged_files_terminate_build 1

Name: moshi
Version: 1.15.2
Release: alt1

Summary: JSON library for Android and Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/square/moshi
VCS: https://github.com/square/moshi.git

Source0: %name-%version.tar
Patch0: 0001-system-gradle-kotlin.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: kotlin
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-symbol-processing
BuildRequires: shadow-gradle-plugin
BuildRequires: kotlinpoet
BuildRequires: kotlin-compile-testing
BuildRequires: okio
BuildRequires: kotlin-reflect
BuildRequires: auto-service
BuildRequires: guava
BuildRequires: objectweb-asm
BuildRequires: junit
BuildRequires: truth
BuildRequires: assertj-core
BuildRequires: jsr-305

%description
Moshi is a modern JSON library for Android and Java. This package publishes
its runtime, adapter, Kotlin reflection, and Kotlin code-generation modules.


%package adapters
Summary: Additional JSON adapters for Moshi
Group: Development/Java

%description adapters
Additional JSON adapters for Moshi.

%package kotlin
Summary: Kotlin reflection integration for Moshi
Group: Development/Java

%description kotlin
Kotlin reflection integration for Moshi.

%package kotlin-codegen
Summary: Kotlin code generator for Moshi
Group: Development/Java

%description kotlin-codegen
Kotlin code generator for Moshi.

%prep
%setup
%mvn_package com.squareup.moshi:moshi
%mvn_package com.squareup.moshi:moshi-adapters adapters
%mvn_package com.squareup.moshi:moshi-kotlin kotlin
%mvn_package com.squareup.moshi:moshi-kotlin-codegen kotlin-codegen
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=moshi-1.15.2,moshi-adapters-1.15.2,moshi-kotlin-1.15.2,moshi-kotlin-codegen-1.15.2
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE.txt

%files adapters -f .mfiles-adapters

%files kotlin -f .mfiles-kotlin

%files kotlin-codegen -f .mfiles-kotlin-codegen

%changelog
* Sat Nov 14 2026 Ivan Khanas <xeno@altlinux.org> 1.15.2-alt1
- Initial build for ALT.
