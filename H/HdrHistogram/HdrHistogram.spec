Name:          HdrHistogram
Version:       2.2.2
Release:       alt1

Summary:       A High Dynamic Range (HDR) Histogram
License:       BSD-2-Clause OR CC0-1.0
Group:         Development/Java
URL:           https://hdrhistogram.github.io/HdrHistogram/
VCS:           https://github.com/HdrHistogram/HdrHistogram

Source0:       %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:maven-replacer-plugin)

Requires:      javapackages-tools

BuildArch:     noarch

%description
HdrHistogram is a High Dynamic Range (HDR) Histogram implementation for Java.
It supports recording and analyzing sampled value distributions across a
configurable range with configurable precision.

HdrHistogram is designed for latency and performance-sensitive applications.
It provides a fixed memory footprint for a configured range and precision,
constant-time value recording, and supports analysis using percentiles,
linear and logarithmic buckets, mean, and standard deviation.

%javadoc_package

%prep
%setup

# Remove bundled JUnit
rm lib/test/junit-4.10.jar

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin

%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

%build
%mvn_build

%install
%mvn_install

%jpackage_script org.%name.HistogramLogProcessor "" "" %name HistogramLogProcessor true

%files -f .mfiles
%_bindir/HistogramLogProcessor
%doc README.md
%doc COPYING.txt LICENSE.txt

%changelog
* Mon Aug 31 2026 Evgeniy Serov <scala@altlinux.org> 2.2.2-alt1
- Updated to 2.2.2.
- Build with jpackage-default.

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.1.12-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.1.11-alt1_6jpp11
- update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 2.1.11-alt1_2jpp11
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.9-alt1_7jpp8
- new version

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.9-alt1_5jpp8
- java update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.9-alt1_4jpp8
- java update

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.9-alt1_3jpp8
- new version

