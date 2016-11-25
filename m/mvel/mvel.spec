Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mvel
%define version 2.2.7
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          mvel
Version:       2.2.7
Release:       alt1_1jpp8
Summary:       MVFLEX Expression Language
License:       ASL 2.0
Url:           https://github.com/mvel
Source0:       https://github.com/mvel/mvel/archive/%{name}2-%{namedversion}.tar.gz
Source1:       %{name}-script
Patch0:        %{name}-2.2.7.Final-use-system-asm.patch
# remove tests which require internal objectweb-asm libraries
Patch1:        %{name}-2.2.7.Final-tests.patch

BuildRequires: maven-local
BuildRequires: mvn(com.thoughtworks.xstream:xstream)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-report-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-util)

BuildArch:     noarch
Source44: import.info

%description
MVEL is a powerful expression language for Java-based applications. It
provides a plethora of features and is suited for everything from the
smallest property binding and extraction, to full blown scripts.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}2-%{namedversion}
find . -name "*.jar" -delete
find . -name "*.class" -delete

rm ASM-LICENSE.txt

%patch0 -p1
rm -rf src/main/java/org/mvel2/asm
%patch1 -p1

# See https://bugzilla.redhat.com/show_bug.cgi?id=1095339
sed -i '/Unsafe/d' src/main/java/org/mvel2/util/JITClassLoader.java

# Uwanted
%pom_remove_plugin :maven-source-plugin
# Remove org.apache.maven.wagon:wagon-webdav:1.0-beta-2
%pom_xpath_remove "pom:project/pom:build/pom:extensions"

sed -i 's/\r//' LICENSE.txt

# fix non ASCII chars
native2ascii -encoding UTF8 src/main/java/org/mvel2/sh/ShellSession.java src/main/java/org/mvel2/sh/ShellSession.java

%mvn_file :%{name}2 %{name}

%build

# Tests fails only on ARM builder
%mvn_build -f

%install
%mvn_install

mkdir -p %{buildroot}%{_bindir}
install -pm 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/mvel.conf`
touch $RPM_BUILD_ROOT/etc/mvel.conf

%files -f .mfiles
%{_bindir}/%{name}
%doc LICENSE.txt
%config(noreplace,missingok) /etc/mvel.conf

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_1jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1_3jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.6-alt1_1jpp7
- new release

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.19-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.19-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.19-alt1_2jpp7
- new version

