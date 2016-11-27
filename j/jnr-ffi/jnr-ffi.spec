Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:     jnr-ffi
Version:  2.0.6
Release:  alt1_1jpp8
Summary:  Java Abstracted Foreign Function Layer
License:  ASL 2.0
URL:      http://github.com/jnr/%{name}/
Source0:  https://github.com/jnr/%{name}/archive/%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jffi)
BuildRequires:  mvn(com.github.jnr:jffi::native:)
BuildRequires:  mvn(com.github.jnr:jnr-x86asm)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)
BuildRequires:  sonatype-oss-parent


BuildArch:     noarch
Source44: import.info

# don't obsolete/provide jaffl, gradle is using both jaffl and jnr-ffi...

%description
An abstracted interface to invoking native functions from java

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# remove all builtin jars
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

# don't fail on unused parameters... (TODO: send patch upstream)
sed -i 's|-Werror||' libtest/GNUmakefile

%mvn_file :{*} %{name}/@1 @1

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1_4jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.10-alt1_3jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.10-alt1_2jpp7
- new version

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.10-alt3_3jpp7
- fixed build

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.10-alt2_3jpp7
- gcc47 build

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.10-alt1_3jpp7
- new version

