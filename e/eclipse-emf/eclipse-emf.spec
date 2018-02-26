# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
ExclusiveArch: x86_64
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%if 0%{?rhel} >= 6
%global debug_package %{nil}
%endif
%global eclipse_base     %{_libdir}/eclipse
%global eclipse_dropin   %{_datadir}/eclipse/dropins

Name:      eclipse-emf
Version:   2.7.1
Release:   alt1_1jpp6
Summary:   Eclipse Modeling Framework (EMF) Eclipse plugin
Group:     System/Libraries
License:   EPL
URL:       http://www.eclipse.org/modeling/emf/

# source tarball and the script used to generate it from upstream's source control
# script usage:
# $ sh get-emf.sh
Source0:   emf-%{version}.tar.gz
Source1:   get-emf.sh

# don't depend on ANT_HOME and JAVA_HOME environment vars, patch upstream
#Patch0:    %{name}-make-homeless.patch
# look inside correct directory for platform docs
Patch1:    %{name}-platform-docs-location.patch
# bundle examples in example-installer plugins from source in tarball instead of from cvs
Patch2:    %{name}-bundle-examples.patch
# Build docs correctly
Patch3:    %{name}-build-docs.patch
# Remove xsd2ecore components from SDK, they are not in the main feature
Patch4:    %{name}-no-xsd2ecore.patch


%if 0%{?rhel} >= 6
ExclusiveArch:    %{ix86} x86_64
%else
BuildArch:        noarch
%endif

# we require 1.6.0 because the javadocs fail to build otherwise
BuildRequires:    java-javadoc
BuildRequires:    jpackage-utils
BuildRequires:    eclipse-pde >= 1:3.6.1
BuildRequires:    dos2unix
Requires:         jpackage-utils
Requires:         eclipse-platform >= 1:3.7.0-5

# the standalone package was deprecated and removed in EMF 2.3 (see eclipse.org bug #191837)
Obsoletes:        %{name}-standalone < 2.4

# the SDO sub-project was terminated upstream and removed in EMF 2.5 (see eclipse.org bug #251402)
Obsoletes:        %{name}-sdo < 2.5
Obsoletes:        %{name}-sdo-sdk < 2.5
Source44: import.info

#TODO: ODA, GWT and RAP components are not packaged.
#TODO: Possibly spin XSD off into it's own package, upstream have moved it to it's project

%description
The Eclipse Modeling Framework (EMF) allows developers to build tools and
other applications based on a structured data model. From a model
specification described in XMI, EMF provides tools and runtime support to
produce a set of Java classes for the model, along with a set of adapter
classes that enable viewing and command-based editing of the model, and a
basic editor.

%package   sdk
Summary:   Eclipse EMF SDK
Group:     System/Libraries
Requires:  java-javadoc
Requires:  eclipse-pde >= 1:3.6.1
Requires:  %{name} = %{version}-%{release}

%description sdk
Documentation and source for the Eclipse Modeling Framework (EMF).

%package   xsd
Summary:   XML Schema Definition (XSD) Eclipse plugin
Group:     System/Libraries
Requires:  %{name} = %{version}-%{release}

%description xsd
The XML Schema Definition (XSD) plugin is a library that provides an API for
manipulating the components of an XML Schema as described by the W3C XML
Schema specifications, as well as an API for manipulating the DOM-accessible
representation of XML Schema as a series of XML documents.

%package   xsd-sdk
Summary:   Eclipse XSD SDK
Group:     System/Libraries
Requires:  java-javadoc
Requires:  eclipse-pde >= 1:3.6.1
Requires:  %{name}-xsd = %{version}-%{release}
Requires:  %{name}-sdk = %{version}-%{release}

%description xsd-sdk
Documentation and source for the Eclipse XML Schema Definition (XSD) plugin.

%package   examples
Summary:   Eclipse EMF/XSD examples
Group:     System/Libraries
Requires:  %{name} = %{version}-%{release}
Requires:  %{name}-xsd = %{version}-%{release}

%description examples
Installable versions of the example projects from the SDKs that demonstrate how
to use the Eclipse Modeling Framework (EMF) and XML Schema Definition (XSD)
plugins.

%prep
%setup -q -n emf-%{version}
%patch1 -p0 -b .orig
%patch2 -p1 -b .orig
%patch3 -p1 -b .orig
%patch4 -p1 -b .orig

rm org.eclipse.emf.doc/tutorials/jet2/jetc-task.jar
rm org.eclipse.emf.test.core/data/data.jar

# link to local java api javadocs
sed -i -e "s|http://java.sun.com/j2se/1.5/docs/api/|%{_javadocdir}/java|" -e "s|\${javaHome}/docs/api/|%{_javadocdir}/java|" \
  org.eclipse.emf.doc/build/javadoc.xml.template \
  org.eclipse.xsd.doc/build/javadoc.xml.template

# make sure upstream hasn't sneaked in any jars we don't know about
JARS=""
for j in `find -name "*.jar"`; do
  if [ ! -L $j ]; then
    JARS="$JARS $j"
  fi
done
if [ ! -z "$JARS" ]; then
   echo "These jars should be deleted and symlinked to system jars: $JARS"
   exit 1
fi

%build
# Note: We use forceContextQualifier because the docs plugins use custom build
#       scripts and don't work otherwise.
OPTIONS="-DjavacTarget=1.5 -DjavacSource=1.5 -DforceContextQualifier=v20110913-1526"

# Work around pdebuild entering/leaving symlink it is unaware of.
ln -s %{_builddir}/emf-%{version}/org.eclipse.emf.license-feature %{_builddir}/emf-%{version}/org.eclipse.emf.license
ln -s %{_builddir}/emf-%{version}/org.eclipse.xsd.license-feature %{_builddir}/emf-%{version}/org.eclipse.xsd.license

# We build the emf, xsd and examples features seperately, rather than just
# building the "all" feature, because it makes the files section easier to
# maintain (i.e. we don't have to know when upstream adds a new plugin)

# build emf features
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.emf -a "$OPTIONS"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.emf.sdk -a "$OPTIONS"

# build xsd features
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.xsd -a "$OPTIONS"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.xsd.edit -a "$OPTIONS"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.xsd.editor -a "$OPTIONS"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.xsd.mapping -a "$OPTIONS"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.xsd.mapping.editor -a "$OPTIONS"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.xsd.ecore.converter -a "$OPTIONS"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.xsd.sdk -a "$OPTIONS"

# build examples features
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.emf.examples -a "$OPTIONS"

%install
install -d -m 755 %{buildroot}%{eclipse_dropin}
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf-sdk      build/rpmBuild/org.eclipse.emf.sdk.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.edit.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.editor.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.mapping.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.mapping.editor.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.ecore.converter.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd-sdk      build/rpmBuild/org.eclipse.xsd.sdk.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf-examples build/rpmBuild/org.eclipse.emf.examples.zip

# the non-sdk builds are a subset of the sdk builds, so delete duplicate features & plugins from the sdks
(cd %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/features && ls %{buildroot}%{eclipse_dropin}/emf/eclipse/features | xargs rm -rf)
(cd %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins  && ls %{buildroot}%{eclipse_dropin}/emf/eclipse/plugins  | xargs rm -rf)
(cd %{buildroot}%{eclipse_dropin}/xsd-sdk/eclipse/features && ls %{buildroot}%{eclipse_dropin}/xsd/eclipse/features | xargs rm -rf)
(cd %{buildroot}%{eclipse_dropin}/xsd-sdk/eclipse/plugins  && ls %{buildroot}%{eclipse_dropin}/xsd/eclipse/plugins  | xargs rm -rf)

%files
%{eclipse_dropin}/emf
%doc org.eclipse.emf.license-feature/rootfiles/*

%files sdk
%{eclipse_dropin}/emf-sdk

%files xsd
%{eclipse_dropin}/xsd
%doc org.eclipse.xsd.license-feature/rootfiles/*

%files xsd-sdk
%{eclipse_dropin}/xsd-sdk

%files examples
%{eclipse_dropin}/emf-examples

%changelog
* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_1jpp6
- new version

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt1_1jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_2jpp6
- new version

* Tue Jan 26 2010 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_4jpp6
- new version

