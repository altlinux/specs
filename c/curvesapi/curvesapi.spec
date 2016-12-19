Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global githash 1946c096a1321366771569b74297ddfaa12faffe
Name:          curvesapi
Version:       1.03
Release:       alt1_2jpp8
Summary:       Java implementation of various mathematical curves
# Fork of https://sourceforge.net/projects/curves/
License:       BSD
URL:           https://github.com/virtuald/curvesapi
Source0:       https://github.com/virtuald/curvesapi/archive/%{githash}/%{name}-%{githash}.tar.gz
# https://github.com/virtuald/curvesapi/issues/1
# https://github.com/virtuald/curvesapi/pull/2/
Patch0:        https://github.com/virtuald/curvesapi/commit/72a2627849a6e48fcca244388a5c1fca78a30300.patch

BuildRequires: maven-local

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
%patch0 -p1

# Remove JVM bundle code sun.awt.geom.Curve
rm -r src/com/graphbuilder/sun
sed -i "s|com.graphbuilder.sun.awt.geom|sun.awt.geom|" \
 src/com/graphbuilder/curve/ShapeMultiPath.java

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
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_2jpp8
- new version

