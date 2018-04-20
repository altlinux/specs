Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global cvs_ver 20100217

Name:		jai-imageio-core
Version:	1.2
Release:	alt1_0.22.20100217cvsjpp8
Summary:	Core Java Advanced Imaging Image I/O Tools API

License:	BSD
URL:		https://java.net/projects/jai-imageio-core
Source0:	jai-imageio-core-cvs%{cvs_ver}-CLEANED.tar.xz
Source1:	README-fedora-epel.txt

# jai-imageio-core contains code under a restrictive licence that we
# cannot ship. This script will download and generate a tarball from
# CVS. Unfortunately, a login is required to download from CVS and
# there are no source tarballs.
#
# Register at:
# https://www.dev.java.net/servlets/Join
#
# Then, run:
# ./generate-tarball.sh USERNAME DATE
Source2:	generate-tarball.sh

BuildRequires:	javapackages-local
BuildRequires:	ant
BuildRequires:	librecode recode


Patch0:		jai-imageio-core-remove-imageio-services.patch
Patch1:		jai-imageio-core-remove-codeclib-plugins.patch
Patch2:		jai-imageio-core-remove-jai-operations.patch
Patch3:		jai-imageio-core-remove-jpeg2000-plugin.patch
Patch4:		jai-imageio-core-no-sun-classes.patch

BuildArch:	noarch
Source44: import.info

%description
This package contains the core Java Advanced Imaging Image I/O Tools API,
minus JPEG 2000, JAI Image I/O operations, and the C-based codecLib.


%package javadoc
Group: Development/Java
Summary:	Javadocs for %{name}
Requires:	jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n jai-imageio-core-cvs%{cvs_ver}-CLEANED

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# remove unbuildable items
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# remove use of sun.*
# https://jai-imageio-core.dev.java.net/issues/show_bug.cgi?id=186
%patch4 -p0

# fix latin-1 documentation
recode latin1..utf-8 COPYRIGHT.txt

# install our documentation
cp -av %{SOURCE1} .


%build
# note: BUILD_TARGET is pretty much ignored, but we need it
# to know where the built files will be located
ant -DBUILD_TARGET=linux-i586 jar-opt docs-jcp


%install
%mvn_file : jai_imageio
%mvn_artifact net.java.dev.jai-imageio:jai-imageio-core:%{version} build/linux-i586/opt/lib/ext/jai_imageio.jar

%mvn_install -J %build/linux-i586/javadocs/docs-jcp

%files -f .mfiles
%doc LICENSE.txt COPYRIGHT.txt README-fedora-epel.txt

%files javadoc -f .mfiles
%doc LICENSE.txt COPYRIGHT.txt README-fedora-epel.txt


%changelog
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

