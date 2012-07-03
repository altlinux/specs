Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
%define svn_revision     5847

%define eclipse_name     eclipse
%define eclipse_base     %{_libdir}/%{eclipse_name}
%define install_loc      %{_datadir}/eclipse/dropins
%define local_dropins    %{install_loc}/svnkit/eclipse
%define local_plugins    %{local_dropins}/plugins
%define local_features   %{local_dropins}/features
%define core_plugin_name org.tmatesoft.svnkit_%{version}
%define core_plugin_dir  %{local_plugins}/%{core_plugin_name}
%define jna_plugin_name  com.sun.jna_3.0.9
%define jna_plugin_dir   %{local_plugins}/%{jna_plugin_name}

Name:           svnkit
Version:        1.3.0
Release:        alt1_1jpp6
Summary:        Pure Java Subversion client library

Group:          Development/Java
# License located at http://svnkit.com/license.html
License:        TMate License and ASL 1.1
URL:            http://www.svnkit.com/
# original source located at: http://www.svnkit.com/org.tmatesoft.svn_%{version}.src.zip
# repackaged removing binary dependencies using:
# zip $FILE -d \*.jar
Source0:        org.tmatesoft.svn_%{version}.src-CLEAN.zip
Patch0:         svnkit-1.2.2-dependencies.patch


BuildArch:      noarch

BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: eclipse-pde
Requires: eclipse-platform

BuildRequires: subversion-javahl >= 1.5
Requires: subversion-javahl >= 1.5
BuildRequires: jna >= 3.0
BuildRequires: trilead-ssh2 >= 213
Requires: jna >= 3.0
Requires: trilead-ssh2 >= 213
Obsoletes:              javasvn <= 1.1.0


%description
SVNKit is a pure Java Subversion client library. You would like to use SVNKit
when you need to access or modify Subversion repository from your Java
application, be it a standalone program, plugin or web application. Being a
pure Java program, SVNKit doesn't need any additional configuration or native
binaries to work on any OS that runs Java.

%package javadoc
Summary:        Javadoc for SVNKit
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for SVNKit - Java Subversion client library.

%package -n eclipse-svnkit
Summary:        Eclipse feature for SVNKit
Group:          Development/Java
Requires: svnkit = %{version}

%description -n eclipse-svnkit
Eclipse feature for SVNKit - Java Subversion client library.


%prep
%setup -q -n %{name}-src-%{version}.%{svn_revision}
%patch0 -p1

# delete the jars that are in the archive
JAR_files=""
for j in $(find -name \*.jar); do
if [ ! -L $j ] ; then
JAR_files="$JAR_files $j"
fi
done
if [ ! -z "$JAR_files" ] ; then
echo "These JAR files should be deleted and symlinked to system JAR files: $JAR_files"
exit 1
fi
find contrib -name \*.jar -exec rm {} \;

# delete src packages for dependencies
rm contrib/trilead/trileadsrc.zip

# relinking dependencies
ln -s /usr/share/java/svn-javahl.jar contrib/javahl
ln -sf %{_javadir}/jna.jar contrib/jna/jna.jar
ln -sf %{_javadir}/trilead-ssh2.jar contrib/trilead/trilead.jar

# fixing wrong-file-end-of-line-encoding warnings
sed -i 's/\r//' README.txt doc/javadoc/package-list
find doc/javadoc -name \*.html -exec sed -i 's/\r//' {} \;


%build
ECLIPSE_HOME=%{eclipse_base} ant

%install

# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 build/lib/%{name}-javahl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-javahl-%{version}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/javadoc/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

# eclipse
mkdir -p $RPM_BUILD_ROOT%{local_dropins}
cp -R build/eclipse/features $RPM_BUILD_ROOT%{local_dropins}

# extracting plugin jars
mkdir $RPM_BUILD_ROOT%{local_plugins}
unzip build/eclipse/site/plugins/%{jna_plugin_name}.jar -d $RPM_BUILD_ROOT%{jna_plugin_dir}
unzip build/eclipse/site/plugins/%{core_plugin_name}.jar -d $RPM_BUILD_ROOT%{core_plugin_dir}
 
# removing plugin internal jars and sources
rm -f $RPM_BUILD_ROOT%{jna_plugin_dir}/jna.jar
rm -f $RPM_BUILD_ROOT%{core_plugin_dir}/{svnkitsrc.zip,trilead.jar,svnkit.jar,svnkit-javahl.jar}

# main library links
pushd $RPM_BUILD_ROOT%{_javadir}/
ln -s %{name}-%{version}.jar %{name}.jar
ln -s %{name}-javahl-%{version}.jar %{name}-javahl.jar
popd

# We need to setup the symlink because the ant copy task doesn't preserve symlinks
# TODO file a bug about this
ln -s %{_javadir}/svn-javahl.jar $RPM_BUILD_ROOT%{core_plugin_dir}
ln -s %{_javadir}/trilead-ssh2.jar $RPM_BUILD_ROOT%{core_plugin_dir}/trilead.jar
ln -s %{_javadir}/svnkit.jar $RPM_BUILD_ROOT%{core_plugin_dir}
ln -s %{_javadir}/jna.jar $RPM_BUILD_ROOT%{jna_plugin_dir}


%files
%{_javadir}/*
%doc README.txt changelog.txt


%files -n eclipse-svnkit
%{install_loc}/svnkit


%files javadoc
%{_javadocdir}/%{name}-%{version}


%changelog
* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1jpp6
- new version

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_2jpp5.0
- converted from JPackage by jppimport script

