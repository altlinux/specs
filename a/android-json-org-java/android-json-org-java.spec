Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name android-json-org-java
%define version 6.0.1
%global namedreltag _r22
%global namedversion %{version}%{?namedreltag}
%global oname json
Name:          android-json-org-java
Version:       6.0.1
Release:       alt1_0.1.r22jpp8
Summary:       Androids rewrite of the evil licensed Json.org
License:       ASL 2.0
URL:           https://android.googlesource.com/platform/libcore/+/master/json
# git clone https://android.googlesource.com/platform/libcore/ android-json-org-java
# (cd android-json-org-java/json/ && git archive --format=tar --prefix=android-json-org-java-6.0.1_r22/ android-6.0.1_r22 | xz > ../../android-json-org-java-6.0.1_r22.tar.xz)
Source0:       %{name}-%{namedversion}.tar.xz
Source1:       %{name}-template.pom
# android-json-org-java package don't include the license file
Source2:       http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:        %{name}-20130122-ignore_failing_junit_test.patch
BuildRequires: geronimo-parent-poms
BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
Json.org is a popular java library to parse and
create json string from the author of the json
standard Douglas Crockford. His implementation
however is not free software.
Therefor the Android team did a clean-room
re-implementation of a json library to
be used in-place of the original one.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p0

sed -i '/java.nio.channels.Selector.open/d' \
 src/test/java/org/json/JSONObjectTest.java

cp -p %{SOURCE1} pom.xml
sed -i "s|<version>@version@|<version>%{namedversion}|" pom.xml
cp -p %{SOURCE2} .
sed -i 's/\r//' LICENSE-2.0.txt

# empty file
rm -rf MODULE_LICENSE_BSD_LIKE

%mvn_file :%{oname} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_0.1.r22jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_0.3.r1jpp8
- new version

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.2-alt1_0.2.r1jpp8
- new version

