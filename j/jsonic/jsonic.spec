Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 29
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jsonic
Version:       1.3.0
Release:       alt1_12jpp8
Summary:       Simple JSON encoder/decoder for Java
License:       ASL 2.0
URL:           http://jsonic.sourceforge.jp/
Source0:       http://jaist.dl.sourceforge.jp/%{name}/56583/%{name}-%{version}.zip
# fix maven compiler-plugin configuration
# fix encoding
# fix build deps
# disable unavailable org.seasar.container:s2-framework support
# https://www.seasar.org/svn/s2container/
Patch0:        %{name}-%{version}-pom.patch
# Use servlet 3.1 api
Patch1:        %{name}-%{version}-servlet.patch

BuildRequires: maven-local
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(org.apache.commons:commons-logging)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-web)
BuildRequires: mvn(org.sonatype.sisu:sisu-guice)
%if %{?fedora} <= 20
BuildRequires: mvn(org.sonatype.sisu.inject:guice-extensions)
%endif
BuildRequires: mvn(org.sonatype.sisu.inject:guice-servlet)

BuildArch:     noarch
Source44: import.info

%description
Jsonic is a JSON encoding/decoding library for Java implementing RFC 4627
(The application/JSON Media Type for JavaScript Object Notation).
Encoding/decoding of primitive types and full Java objects is supported.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# cleanup
find -name "*.class" -print -delete
find -name "*.jar" -print -delete
rm -r docs/*

%patch0 -p0
%patch1 -p1

sed -i 's/\r//' LICENSE.txt

# Remove javadoc warning
# rm -r src/java/net/arnx/jsonic/web/extension/S2Container.java

%mvn_file : %{name}

%build

# No tests to run
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_12jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_11jpp8
- fc29 update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_10jpp8
- new version

