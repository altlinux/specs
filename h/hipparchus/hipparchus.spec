%define _unpackaged_files_terminate_build 1

Name: hipparchus
Version: 4.0.3
Release: alt1

Summary: Mathematical and statistical libraries for Java
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and Minpack
Group: Development/Java
URL: https://www.hipparchus.org/
VCS: https://github.com/Hipparchus-Math/hipparchus.git

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit-pioneer:junit-pioneer)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)

%description
Hipparchus provides numerical analysis, statistics, geometry, optimization,
ordinary differential equations, fitting, FFT, clustering and filtering.
This package contains the parent POMs for its independently usable modules.

%package core
Summary: Hipparchus core library
Group: Development/Java

%description core
Hipparchus mathematical library: core module.

%package stat
Summary: Hipparchus stat library
Group: Development/Java

%description stat
Hipparchus mathematical library: stat module.

%package geometry
Summary: Hipparchus geometry library
Group: Development/Java

%description geometry
Hipparchus mathematical library: geometry module.

%package ode
Summary: Hipparchus ode library
Group: Development/Java

%description ode
Hipparchus mathematical library: ode module.

%package optim
Summary: Hipparchus optim library
Group: Development/Java

%description optim
Hipparchus mathematical library: optim module.

%package fitting
Summary: Hipparchus fitting library
Group: Development/Java

%description fitting
Hipparchus mathematical library: fitting module.

%package fft
Summary: Hipparchus fft library
Group: Development/Java

%description fft
Hipparchus mathematical library: fft module.

%package clustering
Summary: Hipparchus clustering library
Group: Development/Java

%description clustering
Hipparchus mathematical library: clustering module.

%package filtering
Summary: Hipparchus filtering library
Group: Development/Java

%description filtering
Hipparchus mathematical library: filtering module.

%package tests
Summary: Shared test fixtures for Hipparchus modules
Group: Development/Java

%description tests
Upstream shared tests and fixtures for the Hipparchus module reactor.

%package javadoc
Summary: API documentation for Hipparchus
Group: Development/Documentation

%description javadoc
API documentation for the Hipparchus mathematical libraries.

%prep
%setup -q
# The Swing demonstration applications are separate from the libraries.
%pom_disable_module hipparchus-samples
# RPMs replace the upstream source and binary distribution ZIPs.
%pom_remove_plugin :maven-assembly-plugin
# Documentation-site generators are not part of library builds or consumers.
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-site-plugin hipparchus-parent
%pom_remove_plugin :maven-project-info-reports-plugin hipparchus-parent
%pom_remove_plugin :plantuml-maven-plugin hipparchus-parent
for module in core stat geometry ode optim fitting fft clustering filtering; do
    %pom_remove_plugin :maven-checkstyle-plugin hipparchus-$module
done
# Classifier mappings precede broader module mappings.
%mvn_package :*::sources: __noinstall
%mvn_package :*::tests: tests
%pom_xpath_inject pom:properties \
    '<maven.compiler.release>8</maven.compiler.release>' hipparchus-parent
%mvn_package :hipparchus-core core
%mvn_file :hipparchus-core hipparchus/hipparchus-core
%mvn_package :hipparchus-stat stat
%mvn_file :hipparchus-stat hipparchus/hipparchus-stat
%mvn_package :hipparchus-geometry geometry
%mvn_file :hipparchus-geometry hipparchus/hipparchus-geometry
%mvn_package :hipparchus-ode ode
%mvn_file :hipparchus-ode hipparchus/hipparchus-ode
%mvn_package :hipparchus-optim optim
%mvn_file :hipparchus-optim hipparchus/hipparchus-optim
%mvn_package :hipparchus-fitting fitting
%mvn_file :hipparchus-fitting hipparchus/hipparchus-fitting
%mvn_package :hipparchus-fft fft
%mvn_file :hipparchus-fft hipparchus/hipparchus-fft
%mvn_package :hipparchus-clustering clustering
%mvn_file :hipparchus-clustering hipparchus/hipparchus-clustering
%mvn_package :hipparchus-filtering filtering
%mvn_file :hipparchus-filtering hipparchus/hipparchus-filtering

# Separate test classifiers from library runtime payloads.
# Keep the public parent POM, but omit internal aggregation POMs.
%mvn_package :hipparchus hipparchus
%mvn_package :hipparchus-aggregator __noinstall
%mvn_package :hipparchus-coverage __noinstall

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-hipparchus
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files core -f .mfiles-core

%files stat -f .mfiles-stat

%files geometry -f .mfiles-geometry

%files ode -f .mfiles-ode

%files optim -f .mfiles-optim

%files fitting -f .mfiles-fitting

%files fft -f .mfiles-fft

%files clustering -f .mfiles-clustering

%files filtering -f .mfiles-filtering

%files tests -f .mfiles-tests

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 4.0.3-alt1
- Initial build for ALT.
