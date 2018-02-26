# -*- coding: latin-1; mode: rpm-spec -*-

Name: expect-lite
Version: 4.2.2
Release: alt1

Summary: Quick and easy command line automation tool
License: BSD-style
Group: Development/Tcl
Url: http://expect-lite.sourceforge.net
Source: %{name}_%{version}.tar.gz
BuildArch: noarch

Packager: Evgenii Terechkov <evg@altlinux.org>

%description
expect-lite is an quick and easy command line automation tool

%prep
%setup -n %name.proj
%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
install -p -m755 %name %buildroot%_bindir/
install -p -m644 man/%name.1.gz %buildroot%_man1dir

%files
%_bindir/%name
%_man1dir/%{name}.1.gz
%doc Examples Docs Tools README COPYING ChangeLog bashrc

%changelog
* Sat Mar  3 2012 Terechkov Evgenii <evg@altlinux.org> 4.2.2-alt1
- Initial build for ALT Linux Sisyphus
