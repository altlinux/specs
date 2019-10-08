Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           java-mersenne-twister
Version:        22
Release:        alt1_9jpp8
Summary:        Mersenne Twister random number generator in Java

License:        BSD
URL:            http://www.cs.gmu.edu/~sean/research/
Source0:        http://www.cs.gmu.edu/~sean/research/mersenne/MersenneTwister.java
Source1:        http://www.cs.gmu.edu/~sean/research/mersenne/MersenneTwisterFast.java

BuildArch:      noarch

BuildRequires:  javapackages-tools

Requires:       jpackage-utils
Source44: import.info

%description
The Mersenne Twister is an exceptionally high-quality, fast random number
generator.  This package contains two versions of it in Java, written by Sean
Luke.  MersenneTwister is a complete drop-in subclass replacement for
java.util.Random.  MersenneTwisterFast is algorithmically identical, except
that it isn't synchronized, and it's not a subclass of Random.  This, plus
other speed improvements, makes it over twice the speed.

%package javadoc
Group: Development/Java
Summary:        Documentation for the Mersenne Twister in Java
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc documentation for the Mersenne Twister in Java.

%prep
%setup -c -T
mkdir -p ec/util
cp -p %{SOURCE0} ec/util
cp -p %{SOURCE1} ec/util

%build
# Build the JAR
javac -source 1.6 -target 1.6 ec/util/*.java
jar cf mersenne-twister.jar ec/util/*.class

# Build the documentation
mkdir doc
javadoc -d doc -source 1.6 ec/util/*.java

%install
# Install the JAR
mkdir -p %{buildroot}%{_javadir}
cp -p mersenne-twister.jar %{buildroot}%{_javadir}

# Install the documentation
mkdir -p %{buildroot}%{_javadocdir}
cp -a doc %{buildroot}%{_javadocdir}/mersenne-twister

%files
%{_javadir}/mersenne-twister.jar

%files javadoc
%{_javadocdir}/mersenne-twister

%changelog
* Tue Oct 08 2019 Igor Vlasenko <viy@altlinux.ru> 22-alt1_9jpp8
- new version

