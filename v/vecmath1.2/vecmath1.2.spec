# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           vecmath1.2
Version:        1.14
Release:        alt1_15jpp8
Summary:        Free version of vecmath from the Java3D 1.2 specification
Group:          System/Libraries
License:        MIT
URL:            http://www.objectclub.jp/download/vecmath_e
Source0:        http://www.objectclub.jp/download/files/vecmath//%{name}-%{version}.tar.gz
Patch0:         vecmath1.2-1.14-javadoc-fixes.patch
BuildArch:      noarch
BuildRequires: javapackages-tools rpm-build-java
Requires: javapackages-tools rpm-build-java
# Necessary due to architecture change to noarch
Obsoletes:      %{name} < %{version}-%{release}
Source44: import.info

%description
This is an unofficial implementation (java source code) of the javax.vecmath
package specified in the Java(TM) 3D API 1.2 . The package includes classes
for 3-space vector/point, 4-space vector, 4x4, 3x3 matrix, quaternion,
axis-angle combination and etc. which are often utilized for computer graphics
mathematics. Most of the classes have single and double precision versions.
Generic matrices' LU and SV decomposition are also there.


%package javadoc
Group:          Development/Other
Summary:        Javadoc for %{name}
Requires:       %{name} = %{version}
# Necessary due to architecture change to noarch
Obsoletes:      %{name}-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
find -name *.jar -delete
find -name *.class -delete


%build
make -f Makefile.unix all docs
pushd classes
jar cf ../%{name}.jar .
popd


%install
# jar
install -D -m 644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/
cp -r docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/


%files
%doc README CHANGES
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}/


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_9jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_8jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_7jpp7
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_6jpp6
- update to new release by jppimport

