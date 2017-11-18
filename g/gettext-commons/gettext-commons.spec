BuildRequires: maven-assembly-plugin
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           gettext-commons
Version:        0.9.6
Release:        alt4_14jpp8
Summary:        Java internationalization (i18n) library

Group:          Development/Other
License:        LGPLv2+
URL:            http://code.google.com/p/gettext-commons/
Source0:        http://gettext-commons.googlecode.com/files/%{name}-%{version}-src.tar.gz
Patch0:         %{name}-0.9.6-javadoc.patch

BuildArch:      noarch
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  maven-local
Source44: import.info

%description
The Gettext Commons project provides Java classes for internationalization 
(i18n) through GNU gettext.

The lightweight library combines the power of the unix-style gettext tools 
with the widely used Java ResourceBundles. This makes it possible to use the 
original text instead of arbitrary property keys, which is less cumbersome 
and makes programs easier to read.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt4_14jpp8
- added BR: maven-assembly-plugin for javapackages 5

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt3_14jpp8
- removed requires: from javadoc 

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt2_14jpp8
- updated dependencies

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1_8jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1_7jpp7
- new version

