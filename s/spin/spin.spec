# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           spin
Version:        1.5
Release:        alt2_16jpp8
Summary:        A transparent threading solution for non-freezing Swing applications
License:        LGPLv2
Group:          Development/Java
Url:            http://spin.sourceforge.net/
BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-all.zip
Patch0:         %{name}-pom_xml.patch

BuildRequires:  maven-local
BuildRequires:  jpackage-utils
BuildRequires:  java-devel >= 1.6.0

BuildRequires:  cglib
BuildRequires:  objectweb-asm
Source44: import.info

%description
Spin is a small library that concentrates on offering a powerful solution
to build non-freezing Swing applications. Spin enforces good application
design by separating the GUI and non-visual components through interfaces.
If it is used wisely in an application framework, the GUI programmers will
never have to think about threads again.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Documentation for the spin Java library.

%prep
%setup -q
# Remove pre-build jar files
rm -rf lib
# Compile against the correct version of cglib
%patch0 -p1

%mvn_file : %{name}

%build
# One of the tests tries to access the X display
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_16jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_7jpp7
- new version

