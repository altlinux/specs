Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jzlib
Version:        1.1.2
Release:        alt1_2jpp7
Epoch:          0
Summary:        Re-implementation of zlib in pure Java
License:        BSD
URL:            http://www.jcraft.com/jzlib/
BuildArch:      noarch
Source0:        https://github.com/ymnk/jzlib/archive/%{version}.tar.gz

BuildRequires:  maven-local
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

