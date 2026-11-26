%define _unpackaged_files_terminate_build 1

Name: stately
Version: 2.1.0
Release: alt1
Summary: Kotlin Multiplatform state and concurrency utilities

License: Apache-2.0
Group: Development/Java
Url: https://github.com/touchlab/Stately
VCS: https://github.com/touchlab/Stately.git

# Source-url: https://github.com/touchlab/Stately/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: java-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-maven-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)

%description
Stately provides concurrency primitives and thread-safe collections for Kotlin
Multiplatform applications.

%package concurrency
Summary: Stately concurrency primitives for Kotlin
Group: Development/Java

%description concurrency
The JVM implementation of Stately concurrency primitives.

%package concurrent-collections
Summary: Stately thread-safe collections for Kotlin
Group: Development/Java

%description concurrent-collections
Thread-safe mutable collections for Kotlin Multiplatform applications.

%prep
%setup

%build
%mvn_package :stately-parent __noinstall
%mvn_package :stately-strict %name
%mvn_package :stately-concurrency concurrency
%mvn_package :stately-concurrent-collections concurrent-collections
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%name
%doc README.md LICENSE.txt

%files concurrency -f .mfiles-concurrency

%files concurrent-collections -f .mfiles-concurrent-collections

%changelog
* Wed Nov 25 2026 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- initial build for ALT.

