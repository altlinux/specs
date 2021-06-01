Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           IPAddress
Version:        5.2.1
Release:        alt1_6jpp11
Summary:        Library for handling IP addresses and subnets, both IPv4 and IPv6
License:        ASL 2.0
URL:            https://github.com/seancfoley/IPAddress
Source0:        https://github.com/seancfoley/IPAddress/archive/v%{version}.tar.gz
Patch1:         removeNonAsciChars.patch
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  ant
# the package builds in jdk8 friendly, but in jdk9+ usable jar/module
BuildRequires:  java-11-openjdk-devel
Source44: import.info


%description
Library for handling IP addresses and subnets, both IPv4 and IPv6

%prep
%setup -q
%patch1 -p1

%build
pushd IPAddress
rm dist/IPAddress.jar
mkdir bin #for classes
#while jdk8 is main, we need both jdks, and prefer the upper one
#export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
# be aware, the build do not fail in compilation faiure, and you can end with empty, or full of sources jar, as I did first time!
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  "create dist jar" #yah, funny name, as the whole ant-maven-less-with-pom build system
mv dist/IPAddress*.jar dist/IPAddress.jar
#%%mvn_build it looks like pom is useles, and is enough as it is

%install
%mvn_artifact IPAddress/pom.xml IPAddress/dist/IPAddress.jar
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc README.md


%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 5.2.1-alt1_6jpp11
- new version

