%define _unpackaged_files_terminate_build 1

Name:    gumtree
Version: 2.1.1
Release: alt1
Summary: A neat code differencing tool
Group:   Development/Other
License: LGPLv3
Url:     https://github.com/GumTreeDiff/gumtree

BuildArch: noarch

# https://github.com/GumTreeDiff/gumtree.git
Source: %name-%version.tar

Source1: %{name}.sh

Patch1: %name-no-benchmark.patch
Patch2: %name-no-coveralls.patch
Patch3: %name-no-css.patch
Patch4: %name-no-java.patch
Patch5: %name-no-ruby.patch

BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: java-devel
BuildRequires: gradle-local
BuildRequires: mvn(org.reflections:reflections)
BuildRequires: mvn(org.antlr:antlr)
BuildRequires: mvn(org.antlr:antlr4)
BuildRequires: mvn(com.github.mpkorstanje:simmetrics-core) = 3.2.3
BuildRequires: mvn(net.sf.trove4j:trove4j) = 3.0.3
BuildRequires: mvn(org.jgrapht:jgrapht-core) = 1.0.1
BuildRequires: mvn(com.sparkjava:spark-core) = 2.6.0
BuildRequires: mvn(org.rendersnake:rendersnake) = 1.9

%description
GumTree is a complete framework to deal with source code as trees
and compute differences between them. It includes possibilities such as:
* converting a source file into a language-agnostic tree format
* export the produced trees in various formats
* compute the differences between the trees
* export these differences in various formats
* visualize these differences graphically

Compared to classical code differencing tools, it has two important particularities:
* it works on a tree structure rather than a text structure,
* it can detect moved or renamed elements in addition of deleted and inserted elements.

We already deal with a wide range of languages: Java, C, JavaScript and Ruby.
More languages are coming soon,
if you want to help contact http://www.labri.fr/perso/falleri.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

rm -rf gradle/wrapper/

%build
%gradle_build -f

%install
%mvn_install

install -d %buildroot%_bindir
install -m 755 %{SOURCE1} %buildroot%_bindir/%name

%files -f .mfiles
%doc README.md
%doc LICENSE
%_bindir/%name

%changelog
* Fri Nov 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt1
- Initial build for ALT.
