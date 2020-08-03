%def_without check

# https://github.com/kr/text
%global goipath github.com/kr/text

Name: golang-github-kr-text
Version: 0.2.0
Release: alt1
Summary: Miscellaneous functions for formatting text
License: MIT
Group: Development/Other
Url: https://github.com/kr/text
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: text-%version.tar.gz
Source1: glide.yaml
Source2: glide.lock

BuildRequires: rpm-build-golang
# BuildRequires: golang(github.com/kr/pty)
BuildRequires: golang-github-kr-pty-devel

%description
Miscellaneous functions for formatting text.

%package devel
Summary: Miscellaneous functions for formatting text
Group: Development/Other
BuildArch: noarch

%description devel
Miscellaneous functions for formatting text.

%prep
%setup -n text-%version
cp %SOURCE1 %SOURCE2 .
mv colwriter/Readme Readme-colwriter
mv mc/Readme Readme-mc

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in cmd/* ; do
%golang_build $cmd ||:
done
%golang_build mc ||:

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

#mv -f %%buildroot%%_bindir/mc %%buildroot%%_bindir/go-mc

%if_with check
%check
export GOPATH="%go_path"
%gotest
%endif

%files
%_bindir/*
%doc License Readme Readme-colwriter Readme-mc

%files devel
%go_path/src/%goipath

%changelog
* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 0.2.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

