Name:		jai-imageio-core
Version:	1.4.0
Release:	alt2

Summary:	JAI ImageIO Core
License:	BSD-3-Clause
Group:          Development/Java
URL:		https://github.com/jai-imageio/jai-imageio-core
VCS:            https://github.com/jai-imageio/jai-imageio-core

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:	noarch

%description
This package contains the core Java Advanced Imaging Image I/O Tools API,
minus JPEG 2000, JAI Image I/O operations, and the C-based codecLib.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt COPYRIGHT.txt README.md

%changelog
* Mon Jun 29 2026 Evgeniy Serov <scala@altlinux.org> 1.4.0-alt2
- Fixed FTBFS: fix build with JDK 17.

* Mon Mar 16 2026 Evgeniy Serov <scala@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.
- Returned to Sisyphus.

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.24.20100217cvsjpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.22.20100217cvsjpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.21.20100217cvsjpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.19.20100217cvsjpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.18.20100217cvsjpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.16.20100217cvsjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.13.20100217cvsjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.12.20100217cvsjpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.11.20100217cvsjpp7
- fc update

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.10.20100217cvsjpp7
- new release

