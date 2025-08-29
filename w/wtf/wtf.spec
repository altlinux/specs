%define _unpackaged_files_terminate_build 1
%global import_path github.com/wtfutil/wtf
%global pkg_name wtfutil

Name: wtf
Version: 0.46.0
Release: alt1
Summary: The personal information dashboard for your terminal.
License: MPL-2.0
Group: Terminals
Url: https://github.com/wtfutil/wtf
Vcs: https://wtfutil.com/

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang 
BuildRequires: golang
BuildRequires: glibc

%description
WTF (aka 'wtfutil') is the personal information dashboard for your
terminal, providing at-a-glance access to your very important but
infrequently-needed stats and data.

%prep
%setup -a 1
%autopatch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export GOSUMDB=off
export GO111MODULE=on
export CFLAGS="%optflags"
%make GOBIN=%prefix 

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
mkdir -p %buildroot%_bindir
%makeinstall_std GOBIN=%buildroot%_bindir
mkdir -p %buildroot%_docdir
cp -pr _sample_configs %buildroot%_docdir/

%files
%doc *.md
%_bindir/%name
%_docdir/_sample_configs

%changelog
* Fri Aug 29 2025 Pavel Shilov <zerospirit@altlinux.org> 0.46.0-alt1
- Initial build for Sisyphus.

