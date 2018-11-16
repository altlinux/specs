%define _unpackaged_files_terminate_build 1

Name:    simmetrics
Version: 3.2.3
Release: alt1
Summary: SimMetrics is a Similarity Metric Library
Group:   Development/Java
License: Apache-2.0
Url:     https://github.com/nickmancol/simmetrics

BuildArch: noarch

# https://github.com/nickmancol/simmetrics.git
Source: %name-%version.tar

BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: java-devel
BuildRequires: maven-local

%description
A Java library of similarity and distance metrics e.g.
Levenshtein distance and Cosine similarity.
All similarity metrics return normalized values
rather than unbounded similarity scores.
Distance metrics return non-negative unbounded scores.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
License: Apache-2.0
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup

%pom_remove_plugin -r :license-maven-plugin

%build
%mvn_build --skip-tests

%install
%mvn_install

%files -f .mfiles
%doc README.md AUTHORS CHANGES.md
%doc LICENCE

%files javadoc -f .mfiles-javadoc
%doc README.md AUTHORS CHANGES.md
%doc LICENCE

%changelog
* Fri Nov 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.3-alt1
- Initial build for ALT.
