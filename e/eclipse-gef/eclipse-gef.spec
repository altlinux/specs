BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global eclipse_base     %{_libdir}/eclipse
%global eclipse_dropin   %{_datadir}/eclipse/dropins
%global contextQualifier v20100913-2020

Name:      eclipse-gef
Version:   3.6.1
Release:   alt1_1jpp6
Summary:   Graphical Editing Framework (GEF) Eclipse plugin
Group:     Development/Java
License:   EPL
URL:       http://www.eclipse.org/gef/

# source tarball and the script used to generate it from upstream's source control
# script usage:
# $ sh get-gef.sh
Source0:   gef-%{version}.tar.gz
Source1:   get-gef.sh


BuildArch:        noarch

BuildRequires: java-javadoc
BuildRequires: jpackage-utils
BuildRequires: eclipse-pde >= 1:3.5.1
Requires: jpackage-utils
Requires: eclipse-platform >= 1:3.5.1
Source44: import.info

%description
The Graphical Editing Framework (GEF) allows developers to create a rich
graphical editor from an existing application model. GEF is completely
application neutral and provides the groundwork to build almost any
application, including but not limited to: activity diagrams, GUI builders,
class diagram editors, state machines, and even WYSIWYG text editors.

%package   sdk
Summary:   Eclipse GEF SDK
Group:     Development/Java
Requires: java-javadoc
Requires: eclipse-pde >= 1:3.5.1
Requires: %{name} = %{version}-%{release}

%description sdk
Documentation and source for the Eclipse Graphical Editing Framework (GEF).

%package   examples
Summary:   Eclipse GEF examples
Group:     Development/Java
Requires: %{name} = %{version}-%{release}

%description examples
Installable versions of the example projects from the SDK that demonstrates how
to use the Eclipse Graphical Editing Framework (GEF) plugin.

%prep
%setup -q -n gef-%{version}

#%patch0 -p0

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
# We build the gef and examples features seperately, rather than just
# building the "all" feature, because it makes the files section easier to
# maintain (i.e. we don't have to know when upstream adds a new plugin)

# Note: Use the tag in get-gef.sh as the context qualifier because it's
#       later than the tags of the individual plugins.

# build gef features
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.gef \
  -a "-DforceContextQualifier=%{contextQualifier}"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.zest \
  -a "-DforceContextQualifier=%{contextQualifier}"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.gef.sdk \
  -a "-DforceContextQualifier=%{contextQualifier} -DJAVADOC14_HOME=%{java_home}/bin"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.zest.sdk \
  -a "-DforceContextQualifier=%{contextQualifier} -DJAVADOC14_HOME=%{java_home}/bin"

# build examples features
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.gef.examples -a "-DforceContextQualifier=%{contextQualifier} -DJAVADOC14_HOME=%{java_home}/bin"

%install
install -d -m 755 %{buildroot}%{eclipse_dropin}
unzip -q -n -d %{buildroot}%{eclipse_dropin}/gef          build/rpmBuild/org.eclipse.gef.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/gef          build/rpmBuild/org.eclipse.zest.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/gef-sdk      build/rpmBuild/org.eclipse.gef.sdk.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/gef-sdk      build/rpmBuild/org.eclipse.zest.sdk.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/gef-examples build/rpmBuild/org.eclipse.gef.examples.zip

# the non-sdk builds are a subset of the sdk builds, so delete duplicate features & plugins from the sdks
(cd %{buildroot}%{eclipse_dropin}/gef-sdk/eclipse/features && ls %{buildroot}%{eclipse_dropin}/gef/eclipse/features | xargs rm -rf)
(cd %{buildroot}%{eclipse_dropin}/gef-sdk/eclipse/plugins  && ls %{buildroot}%{eclipse_dropin}/gef/eclipse/plugins  | xargs rm -rf)

%files
%{eclipse_dropin}/gef
%doc org.eclipse.gef-feature/rootfiles/*
%dir %_datadir/eclipse/dropins/gef/eclipse
%dir %_datadir/eclipse/dropins/gef/eclipse/features
%dir %_datadir/eclipse/dropins/gef/eclipse/plugins

%files sdk
%{eclipse_dropin}/gef-sdk
%doc org.eclipse.gef.sdk-feature/rootfiles/*

%files examples
%{eclipse_dropin}/gef-examples
%doc org.eclipse.gef.examples-feature/rootfiles/*

%changelog
* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 3.6.1-alt1_1jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 3.5.2-alt1_1jpp6
- new version

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1_2jpp6
- new version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 3.4.1-alt1_2jpp6
- new version

* Thu Jul 31 2008 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_2jpp6
- rebuild with eclipse 3.3.2

* Tue Dec 04 2007 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_1jpp5.0
- converted from JPackage by jppimport script

* Fri Oct 21 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.1.1-alt1
- 3.1.1
- Use the Ant XSLT task instead of xsltproc to build file lists

* Wed Aug 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.1-alt1
- Updated to 3.1
- Package the full distribution, with extra features as separate packages
- Corrected description and URL

* Wed Jun 08 2005 Pavel Vainerman <pv@altlinux.ru> 3.0-alt1
- first build
