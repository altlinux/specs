# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global svnrel 1169

Name:           jspecview
Version:        2
Release:        alt1_4.1169svnjpp7
Summary:        JAVA applets for the display of JCAMP-DX and AnIML/CML spectral files

Group:        	System/Base
License:        LGPLv2
URL:            http://jspecview.sourceforge.net/
# Upstream does not release stable source tarballs.
# Tarball created with
# svn checkout -r %{svnrel} http://svn.code.sf.net/p/jspecview/svn/dev2 jspecview
# rm -rf jspecview/.svn
# tar jcf jspecview-%{svnrel}svn.tar.bz2 jspecview
Source0:        jspecview-%{svnrel}svn.tar.bz2
# Include missing resources in jar
Patch0:	  	jspecview-resources.patch
# Use system libraries
Patch1:		jspecview-fedorabuild.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:	itext
BuildRequires:	mozilla-plugin-java-1.7.0-openjdk
# Upstream has hardcoded stuff for eclipse setup
BuildRequires:	eclipse

Requires:       jpackage-utils
Source44: import.info

%description
The JSpecView Project provides JAVA applets for the display of
JCAMP-DX and AnIML/CML spectral files.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n jspecview
%patch0 -p1 -b .resources
%patch1 -p1 -b .fedora

# Fix EOL encodings
for f in JSpecView/extras/{COPYRIGHT,LICENSE,README}.txt; do
 sed 's/\r//' $f > $f.new && \
 touch -r $f $f.new && \
 mv $f.new $f
done

# Remove pre-existing binaries
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Install netscape.jar
cp -a %{_datadir}/icedtea-web/plugin.jar JSpecView/libs/netscape.jar

%build
# Build library
cd JSpecViewLib
ant
cd ..

cd JSpecView
ant make-application-jar make-applet-jar
cd ..

%install
mkdir -p %{buildroot}%{_javadir}
install -D -p -m 644 -t %{buildroot}%{_javadir}/ JSpecView/build/jspecview.app.*.jar
install -D -p -m 644 -t %{buildroot}%{_javadir}/ JSpecView/build/jspecview.applet.*.jar

# Install symlinks
pushd %{buildroot}%{_javadir}
ln -s jspecview.app.*.jar jspecview.app.jar
ln -s jspecview.applet.*.jar jspecview.applet.jar
popd

# Javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp JSpecView/doc/ %{buildroot}%{_javadocdir}/%{name}

%files
%doc JSpecView/extras/README.txt JSpecView/extras/LICENSE.txt JSpecView/extras/COPYRIGHT.txt
%{_javadir}/jspecview.*.jar

%files javadoc
%{_javadocdir}/%{name}/

%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2-alt1_4.1169svnjpp7
- new version

