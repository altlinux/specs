BuildRequires: /proc
BuildRequires: jpackage-compat
%global  git_commit d0ec879
%global  cluster jruby

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           bytelist
Version:        1.0.8
Release:        alt1_1jpp6
Summary:        A java library for lists of bytes

Group:          Development/Java
License:        CPL or GPLv2+ or LGPLv2+
URL:            http://github.com/%{cluster}/%{name}
Source0:        http://download.github.com/%{cluster}-%{name}-%{version}-0-g%{git_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  jcodings
BuildRequires:  jpackage-utils
BuildRequires:  junit

Requires:       jcodings
Requires:       jpackage-utils
Source44: import.info


%description
A small java library for manipulating lists of bytes.


%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;


%build
echo "See %{url} for more info about the %{name} project." > README.txt

export CLASSPATH=$(build-classpath junit jcodings)
%__mkdir_p lib
%ant


%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_javadir}

%__cp -p lib/%{name}-1.0.2.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir}/
  %__ln_s %{name}-%{version}.jar %{name}.jar
popd


%check
export CLASSPATH=$(build-classpath junit jcodings)
%ant test


%files
%{_javadir}/*
%doc README.txt

%changelog
* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_1jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2jpp5
- new version

