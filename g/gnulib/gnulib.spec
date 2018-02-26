Name: gnulib
Version: 0.0.7312.7995834
Release: alt1

Summary: GNU Portability Library
License: Freely distributable
Group: Development/C
BuildArch: noarch
Url: http://www.gnu.org/software/gnulib/
Source: %name-%version.tar
Patch: gnulib-alt-utimens.patch
AutoReqProv: no

%description
Gnulib is intended to be the canonical source for most of the important
"portability" and/or common files for GNU projects.  These are files
intended to be shared at the source level; Gnulib is not a typical
library meant to be installed and linked against.  Thus, unlike most
projects, Gnulib does not normally generate a source tarball
distribution; instead, developers grab modules directly from the
source repository.

%prep
%setup
%patch -p1

%build
make info

%install
mkdir -p %buildroot{%_bindir,%_infodir,%_datadir/%name}
cp -a * %buildroot%_datadir/%name/
for f in check-module gnulib-tool; do
	ln -s $(relative %_datadir/%name/$f %_bindir/) %buildroot%_bindir/
done
mv %buildroot%_datadir/%name/doc/*.info %buildroot%_infodir/

%files
%_bindir/*
%_infodir/*
%_datadir/%name/

%changelog
* Wed Apr 11 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7312.7995834-alt1
- Updated to gnulib snapshot v0.0-7312-g7995834.

* Wed Jan 11 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.6780.bfacc22-alt1
- Updated to gnulib snapshot v0.0-6780-gbfacc22.
- Applied patches originally made for coreutils.

* Thu Sep 15 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.6125.da1717b-alt1
- Updated to gnulib snapshot v0.0-6125-gda1717b.

* Tue Jun 28 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.5864.0f247f9-alt1
- Updated to gnulib snapshot v0.0-5864-g0f247f9.

* Wed Feb 02 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.4800.a036b76-alt1
- Gnulib snapshot v0.0-4800-ga036b76.
