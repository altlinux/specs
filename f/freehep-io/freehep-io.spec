
Name:           freehep-io
Version:        2.2.2
Release:        alt3
Summary:        The FreeHEP IO package extends the Java IO package with a number of input and output streams

Group:          Development/Java
License:        Apache 2 and LGPL 2
URL:            http://freehep.github.io/freehep-io/
Source0:        %name-%version.tar

BuildRequires(pre): maven-local rpm-build-java
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  /proc
BuildRequires:  maven
BuildRequires:  maven-shared-artifact-resolver
BuildRequires:  maven-surefire-provider-junit

BuildArch:	noarch
Requires:       java >= 1.6.0
Requires:       jpackage-utils

%filter_from_requires /^java-headless/d

%description
The FreeHEP IO package extends the Java IO package with a number of
input and output streams.  The FreeHEP IO streams are in use by the
FreeHEP VectorGraphics package and the PostScript Viewer. Of course all
these classes are usable elsewhere.

%package javadoc
Summary:        Javadoc for %name
Group:          Documentation
Requires:       jpackage-utils
BuildArch:      noarch

Requires:       jpackage-utils
Requires:       %name = %version-%release

%description javadoc
Javadoc for %name.

%prep
%setup

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Jun 27 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt3
- Use new Java package build style

* Wed Aug 27 2014 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt2
- Rebuild with maven-local

* Wed Apr 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- Initial build for ALT Linux
