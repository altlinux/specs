Name: quilt
Version: 0.48
Release: alt1

Summary: Scripts for working with series of patches
License: GPLv2+
Group: Text tools
Url: http://savannah.nongnu.org/projects/quilt/
Provides: bash-completion-quilt = %version-%release
Obsoletes: bash-completion-quilt
Requires: diffstat
# for quilt-rus.pdf
BuildRequires: texlive-lang-cyrillic texlive-latex-extra
# for test suite
%{?!_without_check:%{?!_disable_check:BuildRequires: procmail}}
# git://git.altlinux.org/gears/q/quilt
Source: %name-%version-%release.tar

%description
The scripts allow to manage a series of patches by keeping track of
the changes each patch makes.  Patches can be applied, un-applied,
refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts
found at http://userweb.kernel.org/~akpm/stuff/patch-scripts.tar.gz.

%prep
%setup -n %name-%version-%release
sed -i s/libdir/libexecdir/g Makefile.in
rm doc/*.pdf

%build
%configure \
	--with-awk=gawk \
	--with-diffstat=diffstat \
	--with-sendmail=%_sbindir/sendmail
%make_build COMPAT_SYMLINKS=sendmail RELEASE=%release
%make_build -C doc
# rerun to get right cross-references
rm doc/*.pdf
%make_build -C doc

%install
%make_install install COMPAT_SYMLINKS=sendmail BUILD_ROOT=%buildroot
%define docdir %_docdir/%name-%version
install -pm644 AUTHORS TODO quilt.changes doc/README.EMACS doc/*.pdf \
	%buildroot%docdir/
%find_lang %name

%check
%make_build -k check COMPAT_SYMLINKS=sendmail

%files -f %name.lang
%config(noreplace) %_sysconfdir/quilt.quiltrc
%config /etc/bash_completion.d/*
%_bindir/*
%_man1dir/*
%_libexecdir/%name/
%_datadir/%name/
%_datadir/emacs/site-lisp/*.el*
%docdir/

%changelog
* Wed Jul 21 2010 Dmitry V. Levin <ldv@altlinux.org> 0.48-alt1
- Updated to v0.48-77-g5876294.
- Rewrote specfile.
- Merged bash-completion-quilt subpackage back into the main package.
- Added %%check section that runs test suite by default.
- Built and packaged quilt-rus.pdf article.

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt0.1
- new version 0.46 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.45-alt0.1
- new version 0.45 (with rpmrb script)

* Thu Feb 16 2006 Vitaly Lipatov <lav@altlinux.ru> 0.44-alt0.1
- new version (0.44)

* Fri Feb 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.43-alt0.1
- new version

* Sun Jan 22 2006 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)
