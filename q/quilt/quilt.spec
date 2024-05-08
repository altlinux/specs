%define _unpackaged_files_terminate_build 1

Name: quilt
Version: 0.68
Release: alt1

Summary: Scripts for working with series of patches
License: GPLv2+
Group: Text tools
Url: https://savannah.nongnu.org/projects/quilt/
BuildArch: noarch

Provides: bash-completion-quilt = %version-%release
Obsoletes: bash-completion-quilt
Requires: diffstat
# for test suite
%{?!_without_check:%{?!_disable_check:BuildRequires: ed procmail}}
# https://git.altlinux.org/gears/q/quilt.git
Source: %name-%version-%release.tar

%description
The scripts allow to manage a series of patches by keeping track of
the changes each patch makes.  Patches can be applied, un-applied,
refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts
found at http://userweb.kernel.org/~akpm/stuff/patch-scripts.tar.gz.

%prep
%setup -n %name-%version-%release

%build
%define docdir %_docdir/%name
export ac_cv_path_BASH=/bin/bash
%configure \
	--with-awk=gawk \
	--with-diffstat=diffstat \
	--with-sendmail=%_sbindir/sendmail \
	--docdir=%docdir
%make_build COMPAT_SYMLINKS=sendmail RELEASE=%release

%install
%makeinstall_std COMPAT_SYMLINKS=sendmail BUILD_ROOT=%buildroot
install -pm644 AUTHORS NEWS TODO doc/README.EMACS doc/*.pdf COPYING \
	%buildroot%docdir/
%find_lang %name

%check
%make_build -k check COMPAT_SYMLINKS=sendmail

%files -f %name.lang
%config(noreplace) %_sysconfdir/quilt.quiltrc
%config /etc/bash_completion.d/*
%_bindir/*
%_man1dir/*
%_datadir/%name/
%_datadir/emacs/site-lisp/*.el*
%docdir/

%changelog
* Wed May 08 2024 Vitaly Chikunov <vt@altlinux.org> 0.68-alt1
- Update to v0.68 (2024-03-27).

* Thu Sep 21 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.67-alt2
- Backported upstream change to avoid warnings with grep >= 3.8
  (thx Jean Delvare).

* Thu Mar 10 2022 Vitaly Chikunov <vt@altlinux.org> 0.67-alt1
- Updated to v0.67 (2022-02-15).

* Sat Aug 07 2021 Dmitry V. Levin <ldv@altlinux.org> 0.66-alt2
- Removed texlive from BR, packaged bundled docs instead.

* Thu Mar 28 2019 Dmitry V. Levin <ldv@altlinux.org> 0.66-alt1
- v0.65-27-g0f2a913 -> v0.66 (closes: #36476).

* Thu Nov 02 2017 Dmitry V. Levin <ldv@altlinux.org> 0.65.0.27.0f2a-alt1
- v0.65-3-g1cde193 -> v0.65-27-g0f2a913.

* Thu Mar 30 2017 Dmitry V. Levin <ldv@altlinux.org> 0.65.0.3.1cde1-alt1
- v0.60-54-g0bdc116 -> v0.65-3-g1cde193.

* Mon May 27 2013 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt4
- Updated to v0.60-54-g0bdc116.

* Tue May 21 2013 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt3
- Updated to v0.60-49-g95adfac.
- Fixed "find -perm" usage.

* Wed Apr 03 2013 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt2
- Updated to v0.60-47-g22e8ea8.

* Wed Feb 29 2012 Dmitry V. Levin <ldv@altlinux.org> 0.60-alt1
- Updated to v0.60.

* Sat Jan 21 2012 Dmitry V. Levin <ldv@altlinux.org> 0.50-alt1
- Updated to v0.50-17-gb2245d7.

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
