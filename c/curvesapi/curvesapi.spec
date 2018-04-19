Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global githash 25f63a4a5a98a4bc82bb0e155cdf4d28e0c9e8a7
Name:          curvesapi
Version:       1.04
Release:       alt1_4jpp8
Summary:       Java implementation of various mathematical curves
# Fork of https://sourceforge.net/projects/curves/
License:       BSD
URL:           https://github.com/virtuald/curvesapi
Source0:       https://github.com/virtuald/curvesapi/archive/%{githash}/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)

BuildArch:     noarch
Source44: import.info

%description
Implementation of various mathematical curves that define themselves
over a set of control points. The API is written in Java. The curves
supported are: Bezier, B-Spline, Cardinal Spline, Catmull-Rom Spline,
Lagrange, Natural Cubic Spline, and NURBS.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}

# Convert from dos to unix line ending
for file in r*.txt demo/*.java
do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md readme.txt release-notes.txt scshot.png demo
%doc --no-dereference license.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference license.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_2jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_2jpp8
- new version

