%define _unpackaged_files_terminate_build 1

Name: apache-tapestry
Version: 5.9.2
Release: alt1

Summary: Apache Tapestry annotations module
Group: Development/Java
License: Apache-2.0 AND BSD-3-Clause
URL: https://tapestry.apache.org/
VCS: https://github.com/apache/tapestry-5.git

Source: %name-%version.tar
Patch0: 0001-Build-the-JSON-modules-with-system-Gradle.patch
Patch1: 0002-Run-Plastic-tests-with-system-Groovy.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-nop)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(org.spockframework:spock-core)
BuildRequires: mvn(org.jacoco:org.jacoco.agent)
BuildRequires: mvn(commons-lang:commons-lang)

%description
Apache Tapestry annotations used by the selected Tapestry JSON provider and
its production project dependency closure.

%package func
Summary: Apache Tapestry functional programming library
Group: Development/Java
License: Apache-2.0

%description func
Apache Tapestry's lightweight functional programming library.

%package plastic
Summary: Apache Tapestry Plastic bytecode transformation library
Group: Development/Java
License: Apache-2.0 AND BSD-3-Clause

%description plastic
Apache Tapestry's Plastic runtime transformation library.

%package commons
Summary: Apache Tapestry common library
Group: Development/Java
License: Apache-2.0

%description commons
Common classes used by Apache Tapestry framework modules.

%package json
Summary: Apache Tapestry JSON library
Group: Development/Java
License: Apache-2.0

%description json
Apache Tapestry JSON module, published with its upstream Maven coordinates.

%prep
%setup -q
%autopatch -p1
%mvn_package org.apache.tapestry:tapestry5-annotations %name
%mvn_package org.apache.tapestry:tapestry-func func
%mvn_package org.apache.tapestry:plastic plastic
%mvn_package org.apache.tapestry:commons commons
%mvn_package org.apache.tapestry:tapestry-json json
%mvn_package :::sources: __noinstall

%build
%gradle_publish

%install
%gradle_register --artifacts=tapestry5-annotations,tapestry-func,plastic,commons,tapestry-json
%gradle_install

%check
%gradle_check

%files -f .mfiles-%name
%doc LICENSE.txt NOTICE.txt

%files func -f .mfiles-func

%files plastic -f .mfiles-plastic
%doc plastic/src/external/java/LICENSE-ASM.txt

%files commons -f .mfiles-commons

%files json -f .mfiles-json

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 5.9.2-alt1
- Initial build for ALT.
