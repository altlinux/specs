%define realname org

Name: emacs-%realname
Version: 6.34c
Release: alt1

Summary: Org-mode is a mode for keeping notes, ToDos, and project planning
License: %gpl2plus
Group: Office
Url: http://orgmode.org/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

Packager: Evgenii Terechkov <evg@altlinux.org>
BuildArch: noarch
BuildPreReq: emacs-devel emacs-nox rpm-build-licenses

# Automatically added by buildreq on Wed Nov 25 2009 (-bi)
BuildRequires: emacs-gnus emacs-leim tetex-dvips tetex-latex

%description
Org-mode is a mode for keeping notes, maintaining ToDo lists, and doing
project planning with a fast and effective plain-text system.

NOTE: emacs 22 and 23 already includes org-mode. This package is newer
version. Maybe, you even not need this fresh version.

%prep
%setup -n %name-%version
%patch0 -p1

%build
make EMACS="%__emacs --no-site-file" prefix=%buildroot%_prefix
make doc doc/org

%install
make install prefix=%buildroot%_prefix EMACS="%__emacs --no-site-file"
mv doc/%realname doc/%realname.info

mkdir -p %buildroot%_emacs_sitestart_dir
cat >%buildroot%_emacs_sitestart_dir/%realname.el <<__EOF
; site-start script for Emacs, initializes Org-mode
; Evgenii Terechkov, June 2009, <evg@altlinux.ru>

(require 'org-install)
(add-to-list 'auto-mode-alist '("\\.org$" . org-mode))
__EOF

%files
%_emacs_sitestart_dir/%realname.el
%_emacslispdir/*.el*

# org.info placed here to prevent file-level conflicts in %%_infodir (org.info already included in emacs22/23 distribution)
%doc README contrib doc/*.txt doc/*.pdf doc/*.info doc/*.html ChangeLog EXPERIMENTAL ORGWEBPAGE UTILITIES request-assign-future.txt

%changelog
* Sat Jan 30 2010 Terechkov Evgenii <evg@altlinux.ru> 6.34c-alt1
- 6.34c

* Sun Jan 10 2010 Terechkov Evgenii <evg@altlinux.ru> 6.33f-alt1
- 6.33f

* Wed Nov 25 2009 Terechkov Evgenii <evg@altlinux.ru> 6.28d-alt2
- Build with emacs23 fixed

* Sun Jul 19 2009 Terechkov Evgenii <evg@altlinux.ru> 6.28d-alt1
- 6.28d

* Sat Jun 27 2009 Terechkov Evgenii <evg@altlinux.ru> 6.28c-alt1
- 6.28c

* Thu May  1 2008 Terechkov Evgenii <evg@altlinux.ru> 6.02b-alt1
- 6.02b

* Tue Jan 15 2008 Terechkov Evgenii <evg@altlinux.ru> 5.18a-alt1
- 5.18a

* Sun Aug 19 2007 Terechkov Evgenii <evg@altlinux.ru> 5.04-alt1
- .org -> org-mode binding added

* Sun Aug 19 2007 Terechkov Evgenii <evg@altlinux.ru> 5.04-alt0
- Initial build for Sisyphus
