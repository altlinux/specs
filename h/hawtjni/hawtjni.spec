Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             hawtjni
Version:          1.16
Release:          alt1_4jpp8
Summary:          Code generator that produces the JNI code
# Maven plugin is under ASL 2.0.
# stdint.h, shipped in JAR as resource, used only with M$ VC++, is under BSD.
# Everything else is under EPL-1.0
License:          ASL 2.0 and EPL-1.0 and BSD
URL:              http://hawtjni.fusesource.org/
BuildArch:        noarch

# That is the maven-release-plugin generated commit, but it's not tagged for some reason
# https://github.com/fusesource/hawtjni/issues/46
%global commit    fa1fd5dfdd0a1a5a67b61fa7d7ee7126b300c8f0
Source0:          https://github.com/fusesource/hawtjni/archive/%{commit}/hawtjni-%{commit}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(commons-cli:commons-cli)
BuildRequires:    mvn(org.apache.maven:maven-archiver)
BuildRequires:    mvn(org.apache.maven:maven-artifact)
BuildRequires:    mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:    mvn(org.apache.maven:maven-plugin-api)
BuildRequires:    mvn(org.apache.maven:maven-project)
BuildRequires:    mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:    mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:    mvn(org.apache.xbean:xbean-finder)
BuildRequires:    mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:    mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:    mvn(org.codehaus.plexus:plexus-io)
BuildRequires:    mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:    mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires:    mvn(org.ow2.asm:asm)
BuildRequires:    mvn(org.ow2.asm:asm-commons)

Requires:         autoconf
Requires:         automake
Requires:         libtool
Requires:         make
Source44: import.info

%description
HawtJNI is a code generator that produces the JNI code needed to
implement java native methods. It is based on the jnigen code generator
that is part of the SWT Tools project which is used to generate all the
JNI code which powers the eclipse platform.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package runtime
Group: Development/Java
Summary:          HawtJNI Runtime

%description runtime
This package provides API that projects using HawtJNI should build
against.

%package -n maven-hawtjni-plugin
Group: Development/Java
Summary:          Use HawtJNI from a maven plugin

%description -n maven-%{name}-plugin
This package allows to use HawtJNI from a maven plugin.

%prep
%setup -q -n hawtjni-%{commit}

%pom_disable_module hawtjni-example
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-eclipse-plugin

%mvn_package ":hawtjni-runtime" runtime
%mvn_package ":hawtjni-maven-plugin" maven-plugin

%mvn_alias :hawtjni-maven-plugin :maven-hawtjni-plugin

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin hawtjni-runtime

%build
%mvn_build

%install
%mvn_install

%files runtime -f .mfiles-runtime
%doc readme.md license.txt changelog.md

%files -f .mfiles

%files javadoc -f .mfiles-javadoc
%doc license.txt

%files -n maven-hawtjni-plugin -f .mfiles-maven-plugin

%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.16-alt1_4jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.16-alt1_1jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_6jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_5jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_1jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp7
- configure.ac template fixes for jansi-native

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt4_5jpp7
- fixed build

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_5jpp7
- fixed build with new junit

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_5jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_5jpp7
- fc update

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_4jpp7
- new fc release

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_3jpp7
- new version

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp6
- fixed build:
  + changed objectweb-asm version in hawtjni-asm.patch to 3.3.1
  + added hawtjni-pom-alt.patch to fix shading

* Fri Feb 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp6
- new version

