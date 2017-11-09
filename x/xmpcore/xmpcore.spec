Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          xmpcore
Version:       5.1.2
Release:       alt1_8jpp8
Summary:       Java XMP Library
License:       BSD
URL:           http://www.adobe.com/devnet/xmp.html
Source0:       http://repo1.maven.org/maven2/com/adobe/xmp/%{name}/%{version}/%{name}-%{version}-sources.jar
# from http://repo1.maven.org/maven2/com/adobe/xmp/xmpcore/5.1.2/xmpcore-5.1.2.pom
# customized:
# fix compiler,javadoc-plugin configuration
# fix manifest entries
Source1:       %{name}-%{version}.pom
# from http://download.macromedia.com/pub/developer/xmp/sdk/XMP-Toolkit-SDK-5.1.2.zip
Source2:       %{name}-BSD-License.txt
BuildRequires: buildnumber-maven-plugin
BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
The XMP Library for Java is based on the
C++ XMPCore library and the API is similar.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c

mkdir java
mv com java/
rm -r META-INF

cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE2} BSD-License.txt
sed -i 's/\r//' BSD-License.txt

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc BSD-License.txt

%files javadoc -f .mfiles-javadoc
%doc BSD-License.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_5jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_4jpp8
- new version

