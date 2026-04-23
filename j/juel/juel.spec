Name:           juel
Version:        2.2.7
Release:        alt1

Summary:        Java Unified Expression Language
License:        Apache-2.0
Group:          Development/Java
URL:            http://juel.sf.net/
VCS:            https://github.com/beckchr/juel

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:      noarch

%description
JUEL is an implementation of the Unified Expression Language (EL), specified as
part of the JSP 2.1 standard (JSR-245), which has been introduced in JEE5.
Additionally, JUEL 2.2 implements the JSP 2.2 maintenance release specification
for full JEE6 compliance.

%javadoc_package

%package        impl
Summary:        Java Unified Expression Language Implementation
Group:          Development/Java

%description    impl
%summary.

%package        spi
Summary:        Java Unified Expression Language Service Provider
Group:          Development/Java

%description    spi
%summary.

%prep
%setup

%mvn_package :%name-parent __noinstall

%build
%mvn_build -s -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-juel-api
%doc LICENSE.txt README.md

%files impl -f .mfiles-juel-impl
%files spi -f .mfiles-juel-spi

%changelog
* Wed Apr 22 2026 Evgeniy Serov <scala@altlinux.org> 2.2.7-alt1
- Initial build for Sisyphus.
