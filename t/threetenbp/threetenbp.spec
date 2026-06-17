Name:           threetenbp
Version:        1.7.3
Release:        alt1

Summary:        Backport of functionality based on JSR-310 to Java SE 6 and 7
License:        BSD-3-Clause
Group:          Development/Java
URL:            https://www.threeten.org/threetenbp/
VCS:            https://github.com/ThreeTen/threetenbp

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.testng:testng)

BuildArch:      noarch

%description
The backport is NOT an implementation of JSR-310, as that would require jumping
through lots of unnecessary hoops. Instead, this is a simple backport intended
to allow users to quickly use the JSR-310 API on Java SE 6 and 7. The backport
should be referred to using the "ThreeTen" name.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt *.md

%changelog
* Wed Jun 10 2026 Evgeniy Serov <scala@altlinux.org> 1.7.3-alt1
- Updated to 1.7.3.

* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 1.7.2-alt1.1
- Cosmetic fixes.

* Wed Feb 25 2026 Evgeniy Serov <scala@altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus.
