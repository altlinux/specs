%define _unpackaged_files_terminate_build 1

Name:    gla11y
Version: 0.4
Release: alt1

Summary: check accessibility of glade widgets
License: ISC
Group:   Development/Python3
URL:     https://github.com/hypra/gla11y

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: help2man

BuildArch: noarch

Source: %name-%version.tar

%description
This tool checks accessibility of GtkBuilder .ui files
produced e.g. by glade.
It looks for various issues, and notably missing or bogus labelling
relations.

It can for instance be used in Continous Integration checks to make sure not to
introduce accessibility regressions.


%prep
%setup

%install
%makeinstall_std

%files
%doc *.md
%_bindir/gla11y
%_man1dir/gla11y.1.xz

%changelog
* Fri Dec 27 2024 Artem Semenov <savoptik@altlinux.org> 0.4-alt1
- Initial build for Sisyphus (ALT bug: 52323)
