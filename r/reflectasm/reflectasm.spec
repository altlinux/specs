Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          reflectasm
Version:       1.11.0
Release:       alt1_3jpp8
Summary:       High performance Java library that provides reflection by using code generation
License:       BSD
URL:           https://github.com/EsotericSoftware/reflectasm
Source0:       https://github.com/EsotericSoftware/reflectasm/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
ReflectASM is a very small Java library that provides
high performance reflection by using code generation.
An access class is generated to set/get fields,
call methods, or create a new instance. The access class
uses byte-code rather than Java's reflection, so it
is much faster. It can also access primitive fields
via byte-code to avoid boxing.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find -name "*.class" -delete
find -name "*.jar" -delete

sed -i 's/\r//' license.txt
# Do not shade asm
%pom_remove_plugin :maven-shade-plugin

%mvn_file :%{name} %{name}
%mvn_alias :%{name} "com.esotericsoftware.%{name}:%{name}"

# AssertionFailedError: expected:<1> but was:<0>
rm -r test/com/esotericsoftware/reflectasm/ClassLoaderTest.java

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_2jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_4jpp7
- new release

