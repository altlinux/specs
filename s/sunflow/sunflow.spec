Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit aa1930a

Summary: A rendering system for photo-realistic image synthesis
Name: sunflow
Version: 0.07.4
Release: alt2_13jpp11
URL: https://github.com/sparkoo/sunflow
Source0: https://github.com/sparkoo/sunflow/archive/v%{version}/%{name}-%{version}.tar.gz
# based on sunflow_logo.png from http://sunflow.sourceforge.net/logo2007.zip
Source1: sunflow_icon_128.png
Source2: sunflow.desktop
License: MIT
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: maven-local
BuildRequires: janino
# Explicit requires for javapackages-tools since sunflow script
# uses /usr/share/java-utils/java-functions
Requires:      javapackages-tools
Source44: import.info

%description
Sunflow is an open source rendering system for photo-realistic image synthesis.
It is written in Java and built around a flexible ray tracing core and an
extensible object-oriented design.

%package javadoc
Group: Development/Java
Summary: Javadoc for sunflow
BuildArch: noarch

%description javadoc
API documentation for sunflow.

%prep
%setup -q -n %{name}-%{version}
dos2unix -k CHANGELOG LICENSE README
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%jpackage_script org.sunflow.SunflowGUI "" "" "janino:sunflow" sunflow true

install -Dpm644 %{SOURCE1} \
                %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/sunflow.png

desktop-file-install \
 --dir=%{buildroot}%{_datadir}/applications \
 --mode=644 \
 --vendor="" \
 %{SOURCE2}

%check
java -server -Xmx1g -classpath $(build-classpath janino):target/%{name}-%{version}.jar org.sunflow.Benchmark -bench 0 128

%files -f .mfiles
%doc CHANGELOG README
%doc --no-dereference LICENSE
%{_bindir}/sunflow
%{_datadir}/icons/hicolor/128x128/apps/sunflow.png
%{_datadir}/applications/sunflow.desktop

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 0.07.4-alt2_13jpp11
- new version

* Sat Apr 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.07.4-alt1_3
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.07.4-alt1_2
- update by mgaimport

* Mon Sep 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.07.4-alt1_1
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.07.3-alt1_6
- new version

