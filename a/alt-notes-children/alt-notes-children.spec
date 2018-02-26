Name: alt-notes-children
Version: 0.1
Release: alt1
Packager: Alexandra Panyukova <mex3@altlinux.ru>

Summary: Distribution license and release notes
License: Distributable
Group: Documentation

Provides: alt-license-children = %version
Obsoletes: alt-license-children

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
* Fri Jul 04 2008 Alexandra Panyukova <mex3@altlinux.ru> 0.1-alt1
- Initial build
