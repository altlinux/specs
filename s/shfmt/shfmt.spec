%define _unpackaged_files_terminate_build 1
%define buildpath $PWD/.build
%def_with check

Name: shfmt
Version: 3.5.1
Release: alt1

Summary: A shell parser, formatter, and interpreter
License: BSD-3-Clause
Group: Development/Tools

Url: https://github.com/mvdan/sh
Source0: %name-%version.tar
Source1: vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

BuildRequires: scdoc

%if_with check
BuildRequires: /proc
BuildRequires: /dev/pts
%endif

%description
%name formats shell programs. It can use tabs or any number of spaces to
indent.

You can feed it standard input, any number of files or any number of
directories to recurse into. When recursing, it will operate on .sh and .bash
files and ignore files starting with a period. It will also operate on files
with no extension and a shell shebang.

%prep
%setup -a1
%patch0 -p1

%build
export BUILDDIR="%buildpath"
export IMPORT_PATH="%name"

%golang_prepare

%golang_build cmd/*

# generating roff manual page
scdoc < cmd/%name/%name.1.scd > %name.1

%install
export BUILDDIR="%buildpath"
export IGNORE_SOURCES=1

%golang_install

install -Dm0644 -t %buildroot/%_man1dir %name.1

%check
cd %buildpath/src/%name/
go test -v ./...

%files
%doc LICENSE
%_bindir/%name
%_bindir/gosh
%_man1dir/%name.1.xz

%changelog
* Tue Aug 02 2022 Ivan Alekseev <qwetwe@altlinux.org> 3.5.1-alt1
- Initial build
