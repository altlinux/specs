Name: cvsutils
Version: 0.2.5
Release: alt1

Summary: CVS Utilities
License: GPLv3+
Group: Development/Other
BuildArch: noarch

# http://www.red-bean.com/%name/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-0.2.5-alt-timestamp.patch

Requires: cvs

%description
CVS Utilities is a collection of tools to facilitate working with
Concurrent Versions System (CVS).

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%makeinstall_std
for f in %buildroot%_bindir/*; do
	ln -s %name.1 %buildroot%_man1dir/${f##*/}.1
done

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS NEWS README THANKS

%changelog
* Fri Aug 19 2011 Dmitry V. Levin <ldv@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Thu Feb 05 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.0-alt1
- Initial revision, based on spec included in the package.
