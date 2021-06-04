Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
%define fedora 33
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global groupId     org.glite
%global artifactId  jobid-api-java
%{!?_mavenpomdir: %global _mavenpomdir %{_datadir}/maven2/poms}

Name:           glite-jobid-api-java
Version:        1.3.9
Release:        alt1_15jpp11
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
%if 0%{?rhel} >= 7 || 0%{?fedora}
BuildRequires:  apache-commons-codec
BuildRequires:  maven-local
%else
BuildRequires:  jakarta-commons-codec
BuildRequires:  jpackage-utils
%endif
%if 0%{?rhel} >= 7 || 0%{?fedora}
Requires:       apache-commons-codec
%else
Requires:       jakarta-commons-codec
%endif
%if 0%{?rhel} >= 7 || 0%{?fedora} >= 20
%else
Requires:       java
%endif
%if 0%{?rhel} <= 6 && ! 0%{?fedora}
Requires:       jpackage-utils
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
%endif
Source44: import.info

%description
JAVA implementation of library handling gLite jobid.


%package        javadoc
Group: Development/Java
Summary:        Java API documentation for %{name}
Requires:       %{name} = %{version}-%{release}
%if 0%{?rhel} <= 6 && ! 0%{?fedora}
Requires:       jpackage-utils
%endif
BuildArch: noarch

%description    javadoc
This package contains java API documentation for java implementation of gLite
jobid.


%prep
%setup -q
%patch0 -p2


%build
perl ./configure --root=/ --prefix=%{_prefix} --libdir=%{_lib}
%make_build


%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_javadocdir}
mv %{buildroot}%{_docdir}/%{name}-%{version}/api %{buildroot}%{_javadocdir}/%{name}
mkdir -p %{buildroot}%{_mavenpomdir}
install -m 0644 JPP-%{name}.pom %{buildroot}%{_mavenpomdir}
%if 0%{?add_maven_depmap:1}
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%else
%add_to_maven_depmap %{groupId} %{artifactId} %{version} JPP %{name}
touch .mfiles
%endif


%files -f .mfiles
%doc ChangeLog LICENSE
%if ! 0%{?add_maven_depmap:1}
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%endif

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.3.9-alt1_15jpp11
- new version

