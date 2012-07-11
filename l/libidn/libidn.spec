Name: libidn
Version: 1.25
Release: alt1

Summary: Internationalized Domain Name support library
Group: System/Libraries
License: LGPLv3+/GPLv2+ and GPLv3+ and GFDL
Url: http://www.gnu.org/software/%name/
# ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source: %name-%version.tar

%def_with emacs
%{?!_without_emacs:BuildRequires: emacs-devel emacs-nox}

%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%package devel
Group: Development/C
Summary: Development files for the %name library
Requires: %name = %version-%release

%description devel
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

This package includes headers and other development files necessary
for developing programs which use the GNU Libidn library.

%package devel-doc
Summary: Development documentation for the %name library
Group: Development/C
License: GFDL
Requires: %name-devel = %version-%release
BuildArch: noarch

%description devel-doc
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

This package contains %name development documentation.

%package -n emacs-%name
Summary: GNU Emacs %name support files
Group: Development/Other
License: GPLv3+
BuildArch: noarch

%description -n emacs-%name
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

This package includes %name support files for GNU Emacs.

%prep
%setup
iconv -f iso88591 -t utf8 -o doc/libidn.utf8 doc/libidn.info
mv doc/libidn.utf8 doc/libidn.info

%build
%configure \
	--disable-rpath \
	--disable-static \
	--disable-silent-rules \
	--with-packager="%packager" \
	--with-packager-version="%release" \
	--with-packager-bug-reports="http://bugs.altlinux.org" \
	#
# get rid of RPATH
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std
rm %buildroot%_infodir/*.png
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir/reference/html
install -pm644 doc/*.html doc/*.pdf %buildroot%docdir/
install -pm644 AUTHORS COPYING FAQ NEWS README THANKS %buildroot%docdir/
install -pm644 doc/reference/*.pdf %buildroot%docdir/reference/
install -pm644 doc/reference/html/* %buildroot%docdir/reference/html/

%find_lang %name
%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%make_build -k check

%files -f %name.lang
%_libdir/*.so.*
%_bindir/idn
%_man1dir/*
%dir %docdir
%docdir/[ACFNRT]*

%files devel
%_libdir/*.so
%_includedir/*.h
%_pkgconfigdir/*.pc
%_man3dir/*
%_infodir/*

%files devel-doc
%dir %docdir
%docdir/*.html
%docdir/*.pdf
%docdir/reference/

%if_with emacs
%files -n emacs-%name
%_emacslispdir/*
%endif #emacs

%changelog
* Wed Jul 11 2012 Dmitry V. Levin <ldv@altlinux.org> 1.25-alt1
- Updated to 1.25.

* Thu Jan 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.24-alt1
- Updated to 1.24.

* Sun Dec 11 2011 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt1
- Updated to 1.23.
- Rewritten specfile.
- Fixed RPATH issue.
- Enabled test suite.
- Created libidn-devel-doc and emacs-libidn subpackages.

* Thu May 05 2011 Sergey V Turchin <zerg@altlinux.org> 1.22-alt1
- new version

* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.21-alt1
- new version

* Tue Mar 15 2011 Alexey Tourbin <at@altlinux.ru> 1.19-alt2
- rebuilt for debuginfo

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 1.19-alt1
- new version

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 1.15-alt1
- new version

* Wed Apr 30 2008 Sergey V Turchin <zerg at altlinux dot org> 1.8-alt1
- new version

* Tue Jan 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4-alt1
- new version

* Thu Dec 20 2007 Sergey V Turchin <zerg at altlinux dot org> 1.3-alt1
- new version

* Wed Jul 18 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.14-alt1
- new version

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 0.6.10-alt1
- new version

* Fri Jun 02 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.3-alt1
- new version

* Fri Aug 12 2005 Sergey V Turchin <zerg at altlinux dot org> 0.5.18-alt1
- new version

* Thu Feb 10 2005 Sergey V Turchin <zerg at altlinux dot org> 0.5.13-alt1
- new version

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 0.5.12-alt1
- new version

* Mon Sep 27 2004 Sergey V Turchin <zerg at altlinux dot org> 0.5.5-alt1
- new version

* Tue May 25 2004 Sergey V Turchin <zerg at altlinux dot org> 0.4.6-alt1
- initial spec
