Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          xmpcore
Version:       5.1.2
Release:       alt1_5jpp8
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
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_5jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_4jpp8
- new version

