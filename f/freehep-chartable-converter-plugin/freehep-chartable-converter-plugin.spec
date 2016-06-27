
Name:           freehep-chartable-converter-plugin
Version:        2.2.1
Release:        alt3
Summary:        Converts 16 bit Unicode text files into lookup tables

Group:          Development/Java
License:        Apache 2.0 and LGPL 2.1
URL:            http://java.freehep.org/freehep-chartableconverter-plugin/
Source0:        %name-%version.tar

BuildRequires(pre): maven-local rpm-build-java
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  /proc
BuildRequires:  maven

BuildArch:	noarch
Requires:       java >= 1.6.0
Requires:       jpackage-utils

%filter_from_requires /^java-headless/d

%description
Converts 16 bit Unicode text files into lookup tables. These tables are
used by the VectorGraphics package to include and embed fonts in the
output formats.

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
* Mon Jun 27 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt3
- Use new Java package build style

* Wed Aug 27 2014 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt2
- Build with maven-local

* Wed Apr 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt1
- Initial build for ALT Linux
