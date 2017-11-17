Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jnr-posix
Version:        3.0.41
Release:        alt1_2jpp8
Summary:        Java Posix layer
License:        CPL or GPLv2+ or LGPLv2+
URL:            http://github.com/jnr/jnr-posix
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-constants) >= 0.9.9
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:      noarch
Source44: import.info

%description
jnr-posix is a lightweight cross-platform POSIX emulation layer for Java, 
written in Java and is part of the JNR project 

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# fix test which assumes that there is a group named "nogroup"
sed -i 's|"nogroup"|"root"|' src/test/java/jnr/posix/GroupTest.java

# Remove useless wagon extension.
%pom_xpath_remove "pom:build/pom:extensions"

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"

%build
%mvn_build -f

%install
%mvn_install
ln -s %name/%name.jar %buildroot%_javadir/%name.jar

%files -f .mfiles
%doc README.md
%doc LICENSE.txt
%_javadir/%name.jar

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.41-alt1_2jpp8
- new version

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.33-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.29-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.27-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.17-alt1_1jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_2jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_1jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_3jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_2jpp7
- new version

