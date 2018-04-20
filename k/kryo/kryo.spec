Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          kryo
Version:       3.0.3
Release:       alt1_5jpp8
Summary:       Object graph serialization framework for Java
# ASL: src/com/esotericsoftware/kryo/util/IdentityMap.java src/com/esotericsoftware/kryo/util/IntMap.java
License:       ASL 2.0 and BSD
Url:           https://github.com/EsotericSoftware/kryo
Source0:       https://github.com/EsotericSoftware/kryo/archive/%{name}-parent-%{version}.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(com.esotericsoftware:minlog)
BuildRequires: mvn(com.esotericsoftware:reflectasm)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.objenesis:objenesis)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Kryo is a fast and efficient object graph serialization framework for Java.
The goals of the project are speed, efficiency, and an easy to use API.
The project is useful any time objects need to be persisted, whether to a
file, database, or over the network.

Kryo can also perform automatic deep and shallow copying/cloning.
This is direct copying from object to object, not object->bytes->object.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-parent-%{version}
find . -name "*.class" -delete
find . -name "*.jar" -delete

# Do not shaded reflectasm
%pom_disable_module pom-shaded.xml

%pom_remove_plugin :maven-assembly-plugin pom-main.xml
%pom_remove_plugin :clirr-maven-plugin pom-main.xml

%pom_remove_plugin :maven-bundle-plugin pom-main.xml
%pom_add_plugin org.apache.felix:maven-bundle-plugin pom-main.xml "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Import-Package>sun.reflect;resolution:=optional,*</Import-Package>
    <Export-Package>com.esotericsoftware.kryo.*</Export-Package>
  </instructions>
</configuration>"

# remove shaded deps
%pom_xpath_remove "pom:dependency[pom:classifier = 'shaded']"

cp -p %{SOURCE1} .
sed -i 's/\r//' license.txt LICENSE-2.0.txt

%mvn_file :%{name} %{name}
%mvn_alias :%{name} "com.esotericsoftware.%{name}:%{name}"

%build

# Test on arm builder fails, see RHBZ#991712
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md README.md
%doc --no-dereference license.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference license.txt LICENSE-2.0.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_5jpp8
- java update

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp8
- new version

