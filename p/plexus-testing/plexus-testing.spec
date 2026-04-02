Name:           plexus-testing
Version:        2.1.0
Release:        alt1.1

Summary:        Library to help testing plexus components
License:        Apache-2.0
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/plexus-testing/
VCS:            https://github.com/codehaus-plexus/plexus-testing

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.mockito:mockito-core)
# TODO: switch to mvn() prov, after fixing mockito bug
BuildRequires:  osgi(org.mockito.junit-jupiter)

BuildArch:      noarch

%description
The Plexus Testing contains the necessary classes to be able to test
Plexus components.

%prep
%setup

find . -name pom.xml -type f -exec sed -i '/<classifier>classes<\/classifier>/d' {} +

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.1.0-alt1.1
- Cosmetic fixes.

* Tue Feb 24 2026 Evgeniy Serov <scala@altlinux.org> 2.1.0-alt1
- Updated to 2.1.0.

* Fri Sep 05 2025 Anton Meleshnikov <alton@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus (thanks fedora for the spec).
