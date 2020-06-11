Name: arepoize
Version: 0.1
Release: alt1
Summary: A helper script to arepoize packages

License: GPL-2.0-or-later
Group: Development/Other
BuildArch: noarch

Source0: arepoize

%description
This package contains a helper script to arepoize packages.

%install
mkdir -p %buildroot%_bindir
install %SOURCE0 %buildroot%_bindir

%files
%_bindir/%name

%changelog
* Thu Jun 11 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Intial build.
