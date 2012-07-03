BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}

%global nb_            netbeans
%global nb_org         %{nb_}.org
%global nb_ver         6.7.1

%global svnCA          svnClientAdapter
%global svnCA_ver      1.6.0

Name:           %{nb_}-svnclientadapter
Version:        %{nb_ver}
Release:        alt1_3jpp6
Summary:        Subversion Client Adapter

License:        ASL 2.0
Url:            http://subclipse.tigris.org/svnClientAdapter.html
Group:          Development/Java

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export --force --username guest -r4383 \
#     http://subclipse.tigris.org/svn/subclipse/trunk/svnClientAdapter/ \
#     svnClientAdapter-1.6.0
# tar -czvf svnClientAdapter-1.6.0.tar.gz svnClientAdapter-1.6.0
Source0:        %{svnCA}-%{svnCA_ver}.tar.gz
Patch0:         %{svnCA}-%{svnCA_ver}-build.patch

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  ant-junit
BuildRequires:  jpackage-utils
BuildRequires:  subversion-javahl

Requires:       jpackage-utils
Requires:       subversion
Source44: import.info

%description
SVNClientAdapter is a high-level Java API for Subversion.

%prep
%setup -q -n %{svnCA}-%{svnCA_ver}

# remove all binary libs
find . -name "*.jar" -exec %{__rm} -f {} \;

%patch0 -p1 -b .sav

%{__ln_s} -f %{_javadir}/svnkit-javahl.jar lib/svnjavahl.jar

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java 
ant -verbose svnClientAdapter.jar

%install
%{__rm} -fr %{buildroot}
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 build/lib/svnClientAdapter.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%doc license.txt readme.txt
%{_javadir}/*

%changelog
* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_3jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_2jpp6
- new version

* Thu Apr 30 2009 Igor Vlasenko <viy@altlinux.ru> 6.5-alt1_2jpp6
- new version

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 6.1-alt1_3jpp6
- converted from JPackage by jppimport script

