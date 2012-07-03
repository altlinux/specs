Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global git_commit e0fdedc
%global cluster olabini

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           jvyamlb
Version:        0.2.5
Release:        alt1_5jpp6
Summary:        YAML processor for JRuby

Group:          Development/Java
License:        MIT
URL:            http://github.com/%{cluster}/%{name}
Source0:        %{url}/tarball/%{version}/%{cluster}-%{name}-%{git_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  bytelist
BuildRequires:  jcodings
BuildRequires:  joda-time
BuildRequires:  jpackage-utils
BuildRequires:  junit

Requires:       bytelist
Requires:       jcodings
Requires:       joda-time
Requires:       jpackage-utils
Source44: import.info


%description
YAML processor extracted from JRuby.


%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

build-jar-repository -s -p lib joda-time bytelist jcodings


%build
%ant


%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_javadir}

%__cp -p lib/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir}/
  %__ln_s %{name}-%{version}.jar %{name}.jar
popd


%check
%ant test


%files
%defattr(644,root,root,755)
%{_javadir}/*
%doc LICENSE README CREDITS


%changelog
* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.2.5-alt1_5jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.2.5-alt1_4jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1.4-alt1_3jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.4-alt1_2jpp5
- converted from JPackage by jppimport script

