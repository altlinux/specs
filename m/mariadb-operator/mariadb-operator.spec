%global import_path github.com/mariadb-operator/mariadb-operator/v26
%define _unpackaged_files_terminate_build 1

Name:    mariadb-operator
Version: 26.6.0
Release: alt1

Summary: Run and operate MariaDB in a cloud native way
License: MIT
Group:   Other
Url:     https://github.com/mariadb-operator/mariadb-operator
Vcs:     https://github.com/mariadb-operator/mariadb-operator.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w -s"
export GOFLAGS="-trimpath"

%golang_prepare

%golang_build cmd/controller


%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

install -Dm755 $BUILDDIR/bin/controller %buildroot/usr/bin/%name
rm $BUILDDIR/bin/controller

%golang_install

# require internet access
#%check
#%make test-pkg

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Mon Jul 20 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 26.6.0-alt1
- Initial build for ALT.


