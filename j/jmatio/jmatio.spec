Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global githash 9329195b310dd861e97b9655173b4aa564de05dc

Name:          jmatio
Version:       1.1
Release:       alt1_5jpp8
Summary:       Java Matlab IO library
License:       BSD
URL:           https://sourceforge.net/projects/jmatio/
Source0:       https://github.com/gradusnikov/jmatio/archive/%{githash}.zip
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local
BuildRequires: /usr/bin/perl
BuildArch:     noarch
Source44: import.info

%description
Matlab's MAT-file I/O API in Java.
Supports Matlab 5 MAT-file format
reading and writing.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}

# fix non ASCII chars
for s in src/main/java/com/jmatio/types/MLSparse.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

# fix eol
%{__perl} -pi -e 's/\r$//g' LICENSE.txt README_old.txt

%build

%mvn_file :%{name} %{name}
%mvn_alias com.imaginglaboratory:%{name} net.sourceforge.%{name}:%{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md README_old.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3jpp8
- new version

