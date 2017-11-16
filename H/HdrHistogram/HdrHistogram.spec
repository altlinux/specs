Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          HdrHistogram
Version:       2.1.9
Release:       alt1_3jpp8
Summary:       A High Dynamic Range (HDR) Histogram
License:       BSD and CC0
URL:           http://hdrhistogram.github.io/%{name}/
Source0:       https://github.com/%{name}/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
# fedora 25
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:     noarch
Source44: import.info

%description
HdrHistogram supports the recording and analyzing sampled data value
counts across a configurable integer value range with configurable value
precision within the range. Value precision is expressed as the number of
significant digits in the value recording, and provides control over value
quantization behavior across the value range and the subsequent value
resolution at any given level.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find  -name "*.class"  -print -delete
find  -name "*.jar"  -print -delete

%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin

%pom_xpath_set "pom:plugin[pom:groupId = 'com.google.code.maven-replacer-plugin' ]/pom:artifactId" replacer

%mvn_file :%{name} %{name}

%build
%mvn_build

%install
%mvn_install

%jpackage_script org.%{name}.HistogramLogProcessor "" "" %{name} HistogramLogProcessor true

%files -f .mfiles
%{_bindir}/HistogramLogProcessor
%doc README.md
%doc COPYING.txt LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc COPYING.txt LICENSE.txt

%changelog
* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.9-alt1_3jpp8
- new version

