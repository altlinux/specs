
Name:           freehep-vectorgraphics
Version:        2.4
Release:        alt1
Summary:        Java library for export to a variety of vector and bitmap image formats

Group:          Development/Java
License:        Apache 2 and LGPL 2
URL:            http://freehep.github.io/freehep-vectorgraphics/
Source0:        %name-%version.tar

BuildRequires(pre): maven-local rpm-build-java
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  /proc
BuildRequires:  maven
BuildRequires:  maven-plugin-exec
BuildRequires:  maven-shared-artifact-resolver
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-surefire-provider-junit

BuildRequires:  freehep-io
BuildRequires:  freehep-chartable-converter-plugin

BuildArch:	noarch
Requires:       java >= 1.6.0
Requires:       jpackage-utils
Requires:	freehep-io
Requires:	freehep-chartable-converter-plugin

Provides:	freehep-graphicsio = %version-%release
Provides:	freehep-graphics2d = %version-%release

%filter_from_requires /^java-headless/d

%description
The Vector Graphics package of the FreeHEP Java Library enables any Java
program to export to a variety of vector graphics formats as well as
bitmap image formats. Among the vector formats are Encapsulated
PostScript (EPS), Portable Document Format (PDF), Enhanced Meta Format
(EMF), Scalable Vector Graphics (SVg), and Flash (SWF), while the image
formats include GIF, PNG, JPG and PPM.

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
# Remove obsoleted modules
rm -rf  freehep-graphics3d \
	freehep-graphicsio-cgm \
	freehep-graphicsio-latex

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Jun 27 2016 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1
- New version
- Use new Java package build style

* Wed Aug 27 2014 Andrey Cherepanov <cas@altlinux.org> 2.3-alt2
- Rebuild with maven-local

* Wed Apr 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- Initial build for ALT Linux
