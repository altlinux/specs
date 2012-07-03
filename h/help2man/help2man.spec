Name: help2man
Version: 1.40.9
Release: alt1

Summary: help2man creates simple man pages from the output of programs
License: GPLv3+
Group: Development/Other
Url: http://www.gnu.org/software/help2man/

%def_enable nls

# NLS support makes whole package arch-specific.
%{?!_enable_nls:BuildArch: noarch}

# ftp://ftp.gnu.org/gnu/help2man/%name-%version.tar.gz
Source: help2man-%version.tar
Patch: help2man-1.40.4-alt-runas.patch

Requires: coreutils

%if_enabled nls
%define lib_suffix %nil
%{expand:%%define lib_suffix %(test %_lib != lib64 && echo %%nil || echo '()(64bit)')}
Requires: preloadable_libintl.so%lib_suffix
BuildRequires: perl-Locale-gettext
%endif

%description
help2man is a tool for automatically generating simple manual
pages from program output.

This program is intended to provide an easy way for software authors
to include a manual page in their distribution without having to
maintain that document.

Given a program which produces reasonably standard --help and
--version outputs, help2man can re-arrange that output into
something which resembles a manual page.

%prep
%setup
%patch -p1
install -pm644 debian/README README.example
sed -i '1i .\\" -*- mode: troff; coding: utf8 -*-' help2man.*.1

%build
%{?_enable_nls:test -r %_libdir/preloadable_libintl.so}
%configure %{subst_enable nls}
%make_build

%install
%makeinstall_std
%find_lang --with-man help2man

%files -f help2man.lang
%if_enabled nls
%_libdir/%name
%endif
%_bindir/*
%_infodir/*.info*
%doc ChangeLog NEWS README* THANKS help2man.h2m

%changelog
* Fri Apr 27 2012 Dmitry V. Levin <ldv@altlinux.org> 1.40.9-alt1
- Updated to 1.40.9.

* Tue Feb 28 2012 Dmitry V. Levin <ldv@altlinux.org> 1.40.6-alt1
- Updated to 1.40.6.

* Fri Jan 13 2012 Dmitry V. Levin <ldv@altlinux.org> 1.40.5-alt1
- Updated to 1.40.5.

* Mon Oct 10 2011 Dmitry V. Levin <ldv@altlinux.org> 1.40.4-alt1
- Updated to 1.40.4.

* Thu Dec 30 2010 Dmitry V. Levin <ldv@altlinux.org> 1.38.4-alt1
- Updated to 1.38.4.

* Wed May 19 2010 Dmitry V. Levin <ldv@altlinux.org> 1.38.2-alt1
- Updated to 1.38.2.
- Reviewed and updated patches.

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1.36.4-alt3
- Removed obsolete %%install_info/%%uninstall_info calls.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.36.4-alt2
- Uncompressed tarball.

* Thu Mar 30 2006 Dmitry V. Levin <ldv@altlinux.org> 1.36.4-alt1
- Updated to 1.36.4.

* Wed Mar 02 2005 Dmitry V. Levin <ldv@altlinux.org> 1.35.1-alt1
- Updated to 1.35.1.
- Updated patches.
- Enabled nls support by default.

* Fri May 02 2003 Dmitry V. Levin <ldv@altlinux.org> 1.29-alt2
- Deal with info dir entries such that the menu looks pretty.
- Use runas(1) to run executable.
- Changed %%postun script to %%preun.
- Updated package dependencies.

* Mon Sep 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.29-alt1
- 1.29

* Fri May 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.27-alt1
- 1.27

* Tue Mar 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.26-alt1
- 1.26

* Sun Jan 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.25-alt1
- First build for Sisyphus.
