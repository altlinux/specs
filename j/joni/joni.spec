Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             joni
Version:          2.1.3
Release:          alt2_3jpp8
Summary:          Java port of Oniguruma regexp library 
Group:            Development/Other
License:          MIT
URL:              http://github.com/jruby/%{name}
Source0:          https://github.com/jruby/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.zip
Patch1:           joni-remove-useless-wagon-dependency.patch

BuildRequires:    jcodings
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    junit
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-surefire-plugin

BuildRequires:    objectweb-asm

Requires:         jcodings
Requires: javapackages-tools rpm-build-java
Requires:         objectweb-asm

BuildArch:      noarch
Source44: import.info


%description
joni is a port of Oniguruma, a regular expressions library,
to java. It is used by jruby.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch1 -p0

# fixes rpmlint warning about wrong-file-end-of-line-encoding
sed -i -e 's|\r||' test/org/joni/test/TestC.java
sed -i -e 's|\r||' test/org/joni/test/TestU.java
sed -i -e 's|\r||' test/org/joni/test/TestA.java

%mvn_file : %{name}

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc MANIFEST.MF

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_3jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_2jpp8
- build with objectweb-asm

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.9-alt1_3jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.9-alt1_1jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_7jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_6jpp7
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_2jpp5
- fixes for java6 support

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- converted from JPackage by jppimport script

