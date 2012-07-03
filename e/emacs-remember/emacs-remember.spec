%define shortname remember

Name: emacs-remember
Version: 2.0
Release: alt1

Summary: "Remember" is a mode for remembering data
License: %gpl2plus
Group: Office
Url: http://gna.org/projects/remember-el/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

Packager: Evgenii Terechkov <evg@altlinux.org>
BuildArch: noarch
BuildPreReq: emacs-devel emacs-nox emacs-bbdb rpm-build-licenses

%description
"Remember" is a mode for remembering data, extending Emacs

%prep
%setup -n %name-%version
%patch0 -p1

%build
make EMACS="%__emacs" SITEFLAG="--no-site-file" all doc

%install
export PATH="/sbin:$PATH"
make install ELISPDIR=%buildroot%_emacslispdir/%shortname INFODIR=%buildroot%_infodir
mv %buildroot%_infodir/%shortname %buildroot%_infodir/%shortname-el.info
mv %buildroot%_infodir/%shortname-extra %buildroot%_infodir/%shortname-extra-el.info

mkdir -p %buildroot%_emacs_sitestart_dir
cat >%buildroot%_emacs_sitestart_dir/%shortname.el <<__EOF
; site-start script for Emacs, initializes Remember
; Evgenii Terechkov, January 2008, <evg@altlinux.org>

(setq load-path (cons "%_emacslispdir/%shortname" load-path))
(require 'remember)
__EOF

%files
%_emacs_sitestart_dir/%shortname.el
%_emacslispdir/%shortname/*.el*
%_infodir/%{shortname}*

%doc ChangeLog* %{shortname}*.html

%changelog
* Sun Jan 10 2010 Terechkov Evgenii <evg@altlinux.ru> 2.0-alt1
- 2.0

* Wed Nov 25 2009 Terechkov Evgenii <evg@altlinux.ru> 1.9-alt2
- Repocop patch applied

* Tue Feb 19 2008 Terechkov Evgenii <evg@altlinux.ru> 1.9-alt1
- Rebuild with new sisyphus_check

* Thu Jan 17 2008 Terechkov Evgenii <evg@altlinux.ru> 1.9-alt0
- Initial build for ALT Linux Sisyphus
