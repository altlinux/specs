Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oname base64
Name:          java-base64
Version:       2.3.8
Release:       alt1_10jpp8
Summary:       Java class for encoding and decoding Base64 notation
# pom file license comment
# I have released this software into the Public Domain. That
# means you can do whatever you want with it. Really. You don't
# have to match it up with any other open source license -
# just use it. You can rename the files, move the Java packages,
# whatever you want. If your lawyers say you have to have a
# license, contact me, and I'll make a special release to you
# under whatever reasonable license you desire: MIT, BSD, GPL,
# whatever.
License:       Public Domain
URL:           http://iharder.net/base64/
Source0:       https://github.com/omalley/base64/archive/release-%{version}.tar.gz
Patch0:        %{name}-2.3.8-elasticsearch.patch

# test deps
BuildRequires: junit
BuildRequires: maven-local
Provides:      %{oname} = %{version}-%{release}
BuildArch:     noarch
Source44: import.info

%description
Base64 is a Public Domain Java class for encoding and
decoding Base64 notation. There are one-liner convenience
methods as well as Input and Output Streams.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-release-%{version}
%patch0 -p0

sed -i "s|<version>2.3.9-SNAPSHOT</version>|<version>%{version}</version>|" pom.xml

# Unwanted
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-scm-plugin
# Unwanted - disable javadoc source jar
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%mvn_file :%{oname} %{name}
%mvn_file :%{oname} %{oname}

%build

%mvn_build

%install
%mvn_install

(
 cd %{buildroot}%{_javadocdir}
 ln -sf %{name} %{oname}
)

%files -f .mfiles

%files javadoc -f .mfiles-javadoc
%{_javadocdir}/%{oname}

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.8-alt1_10jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.8-alt1_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.8-alt1_8jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.8-alt1_2jpp7
- new release

