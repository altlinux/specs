Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
Name:          littleproxy
Version:       0.4
Release:       alt1_6jpp7
Summary:       High Performance HTTP Proxy
License:       ASL 2.0
URL:           http://www.littleshoot.org/littleproxy/
# git clone git://github.com/adamfisk/LittleProxy.git littleproxy-0.4
# cd littleproxy-0.4 &&  git archive --format=tar --prefix=littleproxy-0.4/ littleproxy-0.4 | xz > ../littleproxy-0.4-src-git.tar.xz
Source0:       %{name}-%{version}-src-git.tar.xz
# add netty 3.5.x support
Patch0:        %{name}-%{version}-netty35.patch
# remove: maven-assembly-plugin, maven-gpg-plugin
Patch1:        %{name}-%{version}-pom.patch

BuildRequires: sonatype-oss-parent

BuildRequires: apache-commons-codec
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: ehcache-core
BuildRequires: log4j
BuildRequires: netty
BuildRequires: slf4j

# test deps
BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-surefire-provider-junit4

BuildArch:     noarch
Source44: import.info

%description
LittleProxy is a high performance HTTP proxy written in Java and
using the Netty networking framework.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%if %{?fedora} > 17
%patch0 -p1
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%else
%patch1 -p0
%endif

%build

%mvn_file :%{name} %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc COPYRIGHT.txt LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc COPYRIGHT.txt LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_4jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp7
- new version

