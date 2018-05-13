%global import_path     github.com/spf13/cobra

%global commit ef82de70bb3f60c65fb8eebacbb2d122ef517385
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-spf13-cobra
Version: 0.0.2
Release: alt1.git%abbrev
Summary: Cobra is a library for creating powerful modern CLI applications
License: Apache v.2
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools
BuildRequires:	golang(github.com/spf13/pflag)
BuildRequires:	golang(github.com/cpuguy83/go-md2man)

%description
Cobra is a library providing a simple interface to create powerful modern CLI
interfaces similar to git & go tools.

Cobra is also an application that will generate your application scaffolding to rapidly
develop a Cobra-based application.

%package devel
Summary: Cobra is a library for creating powerful modern CLI applications
Group: Development/Other
Requires: golang
Requires:	golang(github.com/spf13/pflag)
Requires:	golang(github.com/cpuguy83/go-md2man)
Provides: golang(%import_path) = %version-%release

%description devel
Cobra is a library providing a simple interface to create powerful modern CLI
interfaces similar to git & go tools.

Cobra is also an application that will generate your application scaffolding to rapidly
develop a Cobra-based application.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

%golang_prepare

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

%files devel
%doc README.md LICENSE.txt
%go_path/src/*

%changelog
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 0.0.2-alt1.gitef82de70
- Initial package
- Skip build of binaries

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.21.git8e91712
- new version
