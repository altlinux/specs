%define sname dvc

Name: emacs-%sname
Version: 0.0
Release: alt2.20090426

Summary: Distributed version control for Emacs
License: GPL2+
Group: Development/Other
Url: http://www.xsteve.at/prg/emacs_dvc/
Source: %name.tar

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch

BuildPreReq: emacs-devel emacs-nox emacs-common

%description
Distributed version control for Emacs

%prep
%setup -n %name

%build
%autoreconf
%configure
make

%install
make install prefix=%buildroot%_prefix info_dir=%buildroot%_infodir

mkdir -p %buildroot%_emacs_sitestart_dir
cat >> %buildroot%_emacs_sitestart_dir/%sname.el <<EOF
;; -*- mode: emacs-lisp -*-
; DVC initialization
; April 2009, evg@altlinux.org

(require '%sname-autoloads)
EOF

%files
%_emacs_sitestart_dir/%{sname}*
%_emacslispdir/%sname
%_infodir/%sname.info*

%changelog
* Wed Nov 25 2009 Terechkov Evgenii <evg@altlinux.ru> 0.0-alt2.20090426
- Repocop patch applied

* Sun Apr 26 2009 Terechkov Evgenii <evg@altlinux.ru> 0.0-alt1.20090426
- bzr-20090426

* Sun Jun  8 2008 Terechkov Evgenii <evg@altlinux.ru> 0.0-alt1.20080608
- bzr-20080608

* Mon Apr 14 2008 Terechkov Evgenii <evg@altlinux.ru> 0.0-alt1.20080414
- Initial build for ALT Linux Sisyphus
