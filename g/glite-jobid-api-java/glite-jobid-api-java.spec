Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
%define fedora 33
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global groupId     org.glite
%global artifactId  jobid-api-java
%{!?_mavenpomdir: %global _mavenpomdir %{_datadir}/maven2/poms}

Name:           glite-jobid-api-java
Version:        1.3.9
Release:        alt2_15jpp11
Summary:        JAVA implementation of handling gLite jobid

License:        ASL 2.0
URL:            http://glite.cern.ch
Source:         http://scientific.zcu.cz/emi/emi.jobid.api-java/%{name}-%{version}.tar.gz
# https://github.com/CESNET/glite-lb/commit/00da23f52e6e680f3dee067f545e5f35b07a751c
Patch0:         glite-jobid-api-java-javadoc.patch

BuildArch:      noarch
BuildRequires:  ant
BuildRequires:  perl-devel
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  apache-commons-codec
BuildRequires:  maven-local
Requires:       apache-commons-codec
Source44: import.info

%description
JAVA implementation of library handling gLite jobid.


%package        javadoc
Group: Development/Java
Summary:        Java API documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description    javadoc
This package contains java API documentation for java implementation of gLite
jobid.


%prep
%setup -q
%patch0 -p2

# install in _javadir
%mvn_file org.glite:jobid-api-java %{name}

%build
perl ./configure --root=/ --prefix=%{_prefix} --libdir=%{_lib}
%make_build

%mvn_artifact JPP-%{name}.pom dist/%{name}.jar

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_javadir}/%{name}.jar
%mvn_install
mkdir -p %{buildroot}%{_javadocdir}
mv %{buildroot}%{_docdir}/%{name}-%{version}/api %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc ChangeLog LICENSE

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Sun Jun 05 2022 Igor Vlasenko <viy@altlinux.org> 1.3.9-alt2_15jpp11
- migrated to %%mvn_artifact

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.3.9-alt1_15jpp11
- new version

