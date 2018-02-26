BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# one of the sources is a zip file
BuildRequires: unzip
%define eclipse_base     %{_libdir}/eclipse
%define eclipse_dropin   %{_datadir}/eclipse/dropins

Name:      eclipse-phpeclipse
Version:   1.2.3
Release:   alt1_3jpp6
Summary:   PHP Eclipse plugin
Group:     Development/Java
License:   CPL
URL:       http://phpeclipse.net/

Source0:   http://downloads.sourceforge.net/project/phpeclipse/a%%29%%20Eclipse%%203.3.x/PHPEclipse-1.2.3/PHPEclipse-1.2.3.200910091456PRD-src.zip

# Fix broken PHP table of contents links in the Eclipse help
Patch0:    %{name}-broken-help-links.patch

# Don't package hidden eclipse project files
Patch1:    %{name}-fix-build-props.patch

# Integrate properly with Fedora's apache (probably does not want to go upstream)
Patch2:    %{name}-httpd-integration.patch

# Remove Windows specific preferences (probably does not want to go upstream)
Patch4:    %{name}-rm-win32-help.patch

# Fix a bug that passed the wrong file location to the external parser
Patch5:    %{name}-external-parser.patch

# Fix a bug that passed in the wrong URL to the browser
Patch6:    %{name}-external-preview.patch

# Fix an exception that was causing the phpmanual not to show when you first open the PHP perspective
Patch7:    %{name}-fix-phpmanual-view.patch

# Remove a reference that was causing a build failure on Eclipse 3.6+
Patch8:    %{name}-remove-internal-eclipse-ref.patch


BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    eclipse-pde >= 3.4
BuildRequires:    htmlparser
Requires:         jpackage-utils
Requires:         eclipse-platform >= 3.4
Requires:         htmlparser
Requires:         php5 >= 5
Requires:         php5-xdebug
Requires: apache2
Source44: import.info

%description
PHPEclipse is an open source PHP IDE based on the Eclipse platform. Features
supported include syntax highlighting, content assist, PHP manual integration,
templates and support for the XDebug and DBG debuggers.

%prep
%setup -q -c

# apply patches
%patch0 -p0 -b .orig
%patch1 -p0 -b .orig
%patch2 -p0 -b .orig
%patch4 -p0 -b .orig
%patch5 -p0 -b .orig
%patch6 -p0 -b .orig
%patch7 -p0 -b .orig
%patch8 -p0 -b .orig

#remove bundled jars
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# ditch bundled libs in favor of building against fedora packaged libs
pushd plugins
build-jar-repository -s -p net.sourceforge.phpeclipse.phpmanual.htmlparser htmlparser
popd

# fix jar versions
find -name MANIFEST.MF | xargs sed --in-place "s/0.0.0/%{version}/"
(?-xism:%__subst s,/usr/sbin/httpd,/usr/sbin/httpd2, net.sourceforge.phpeclipse.externaltools/prefs/default_linux.properties)

%build
# build the main feature
%{eclipse_base}/buildscripts/pdebuild -j "-Xmx1024m" -f net.sourceforge.phpeclipse.feature

# build the debug features
%{eclipse_base}/buildscripts/pdebuild -j "-Xmx1024m" -f net.sourceforge.phpeclipse.debug.feature
%{eclipse_base}/buildscripts/pdebuild -j "-Xmx1024m" -f net.sourceforge.phpeclipse.xdebug.feature

%install
install -d -m 755 %{buildroot}%{eclipse_dropin}
unzip -q -d %{buildroot}%{eclipse_dropin}/phpeclipse        build/rpmBuild/net.sourceforge.phpeclipse.feature.zip
unzip -q -d %{buildroot}%{eclipse_dropin}/phpeclipse-debug  build/rpmBuild/net.sourceforge.phpeclipse.debug.feature.zip
unzip -q -d %{buildroot}%{eclipse_dropin}/phpeclipse-xdebug build/rpmBuild/net.sourceforge.phpeclipse.xdebug.feature.zip

# need to recreate the symlinks to libraries that were setup in "prep"
# because for some reason the ant copy task doesn't preserve them
pushd %{buildroot}%{eclipse_dropin}/phpeclipse/eclipse/plugins/net.sourceforge.phpeclipse.phpmanual.htmlparser_*
rm *.jar
build-jar-repository -s -p . htmlparser
popd

%files
%doc features/net.sourceforge.phpeclipse.feature/cpl-v10.html
%{eclipse_dropin}/phpeclipse
%{eclipse_dropin}/phpeclipse-debug
%{eclipse_dropin}/phpeclipse-xdebug

%changelog
* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_3jpp6
- update to new release by jppimport

* Tue Mar 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_2jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_1jpp6
- new version

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_5jpp6
- build for new eclipse version

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2jpp6
- new release (eclipse >=3.4)

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_0.4.svn1573jpp6
- new version

* Wed Jul 30 2008 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_0.2.svn1573jpp6
- fixed dependency

* Mon Jul 28 2008 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_0.2.svn1573jpp6
- eclipse 3.3.2

* Tue Dec 11 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt2_17jpp5.0
- fixed dependencies

* Tue Dec 04 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_17jpp5.0
- converted from JPackage by jppimport script

