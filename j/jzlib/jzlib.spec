Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jzlib
Version:        1.1.3
Release:        alt1_10jpp8
Epoch:          0
Summary:        Re-implementation of zlib in pure Java
License:        BSD
URL:            http://www.jcraft.com/jzlib/
BuildArch:      noarch
Source0:        https://github.com/ymnk/jzlib/archive/%{version}.tar.gz

# This patch is sent upstream: https://github.com/ymnk/jzlib/pull/15
Patch0:         jzlib-javadoc-fixes.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
The zlib is designed to be a free, general-purpose, legally unencumbered 
-- that is, not covered by any patents -- loss-less data-compression 
library for use on virtually any computer hardware and operating system. 
The zlib was written by Jean-loup Gailly (compression) and Mark Adler 
(decompression). 

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%package        demo
Group: Development/Java
Summary:        Examples for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    demo
%{summary}.

%prep
%setup -q
%patch0

# Make into OSGi bundle
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin "org.apache.felix:maven-bundle-plugin" . "<extensions>true</extensions>"

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

# examples
install -dm 755 %{buildroot}%{_datadir}/%{name}
cp -pr example/* %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%files demo
%doc %{_datadir}/%{name}

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_10jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_2jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_3jpp7
- new version

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt2_3jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_3jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_2jpp7
- new release

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt1_5jpp6
- jpp 6 release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt1_4jpp5
- new jpackage release

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt1_4jpp1.7
- converted from JPackage by jppimport script

