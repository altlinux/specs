Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global githash 9329195b310dd861e97b9655173b4aa564de05dc

Name:          jmatio
Version:       1.1
Release:       alt1_8jpp8
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
/usr/bin/perl -pi -e 's/\r$//g' LICENSE.txt README_old.txt

%build

%mvn_file :%{name} %{name}
%mvn_alias com.imaginglaboratory:%{name} net.sourceforge.%{name}:%{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md README_old.txt
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3jpp8
- new version

