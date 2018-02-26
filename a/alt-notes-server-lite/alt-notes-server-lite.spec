Name: alt-notes-server-lite
Version: 0.1
Release: alt1
Packager: Eugene Prokopiev <enp@altlinux.ru>

Summary: Distribution license and release notes
License: Distributable
Group: Documentation

BuildArch: noarch

Source0: %name-%version.tar

%description
Distribution license and release notes

%prep
%setup -q

%install
%makeinstall

%files
%_datadir/alt-notes/*

%changelog
* Tue Aug 12 2008 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- first build for Sisyphus

