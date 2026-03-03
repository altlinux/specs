Name:           maven-scm-provider-svnjava
Version:        2.3.0
Release:        alt1

Summary:        Maven SCM SVN provider based on svnkit
License:        Apache-2.0
Group:          Development/Java
URL:            https://olamy.github.io/maven-scm-provider-svnjava/
VCS:            https://github.com/olamy/maven-scm-provider-svnjava
BuildArch:      noarch

Source0:        %name-%version.tar

BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-svn-commons)
BuildRequires:  mvn(org.tmatesoft.svnkit:svnkit)
BuildRequires:  mvn(commons-lang:commons-lang)

%description
The Apache Maven SCM Provider Impl is based on svnkit and so use Java process
to run svn subversion operations instead of forking a command line as the
default Apache Maven SCM svn implementation.

%javadoc_package

%prep
%setup

%build
# tests required internet connection
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt *.md

%changelog
* Tue Feb 24 2026 Evgeniy Serov <scala@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus.
