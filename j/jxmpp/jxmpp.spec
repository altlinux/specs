Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jxmpp
Version:       0.4.1
Release:       alt1_3jpp8
Summary:       An Open Source XMPP Java base-library
License:       ASL 2.0
URL:           https://github.com/igniterealtime/jxmpp
Source0:       https://github.com/igniterealtime/jxmpp/archive/%{version}.tar.gz
Source1:       jxmpp-core-template.pom
Source2:       jxmpp-jid-template.pom
Source4:       jxmpp-util-cache-template.pom
Source5:       jxmpp-stringprep-libidn-template.pom
Source6:       jxmpp-pom.xml

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.gnu.inet:libidn)

BuildArch:     noarch
Source44: import.info

%description
JXMPP is an Open Source Java base library for XMPP. It
provides often used functionality needed to build a XMPP stack.

%package core
Group: Development/Java
Summary:       JXMPP Core

%description core
JXMPP core components.

%package jid
Group: Development/Java
Summary:       JXMPP JID

%description jid
JID classes from JXMPP.

%package stringprep-libidn
Group: Development/Java
Summary:       JXMPP Stringprep Libidn

%description stringprep-libidn
JXMPP Stringprep with libidn.

%package util-cache
Group: Development/Java
Summary:       JXMPP Util Cache

%description util-cache
A minimalistic and efficient bounded LRU Cache
with optional expiration.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# cleanup
find . -name "*.class" -print -delete
find . -name "*.dll" -print -delete
find . -name "*.jar" -print  -delete

cp -p %{SOURCE1} %{name}-core/pom.xml
cp -p %{SOURCE2} %{name}-jid/pom.xml
cp -p %{SOURCE4} %{name}-util-cache/pom.xml
cp -p %{SOURCE5} %{name}-stringprep-libidn/pom.xml

for p in core jid stringprep-libidn util-cache;do
sed -i "s|@VERSION@|%{version}|" %{name}-${p}/pom.xml
done
cp -p %{SOURCE6} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml

%mvn_package :%{name}-parent __noinstall

%mvn_alias : org.jxmpp:

%build

%mvn_build -s -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files core -f .mfiles-%{name}-core
%doc LICENSE

%files jid -f .mfiles-%{name}-jid
%doc LICENSE

%files stringprep-libidn -f .mfiles-%{name}-stringprep-libidn
%doc LICENSE

%files util-cache -f .mfiles-%{name}-util-cache
%dir %{_javadir}/%{name}
%doc README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_3jpp8
- new version

