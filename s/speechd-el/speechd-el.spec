%define _unpackaged_files_terminate_build 1
%define _speechdeldir %_emacslispdir/speechd-el
%define emacs_version %(%__emacs --version | head -1 | cut -d' ' --fields=3 | cut -d. --fields=1,2,3)

Name:    speechd-el
Version: 2.12
Release: alt2

Summary: Emacs speech and Braille output interface
License: GPL-3.0
Group:   Accessibility
Url:     https://github.com/brailcom/speechd-el

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-emacs

BuildRequires: emacs-speedbar
BuildRequires: texinfo
BuildRequires: info-install
BuildRequires: makeinfo
BuildRequires: info

Requires: %name-lisp = %EVR

%description
speechd-el is an Emacs client to speech synthesizers, Braille displays
and other alternative output interfaces.  It provides full speech and
Braille output environment for Emacs.

It is aimed primarily at visually impaired users who need non-visual
communication with Emacs, but it can be used by anybody who needs
sophisticated speech or other kind of alternative output from Emacs.
speechd-el can make Emacs a completely speech and BRLTTY enabled
application suitable for visually impaired users or, depending on its
configuration, it can only speak in certain situations or when asked,
to serve needs of any Emacs user.

This package contains the natively compiled Emacs lisp code.

%package lisp
Summary: Emacs speech and Braille output interface (bytecode)
Group:   Accessibility
BuildArch: noarch

%description lisp
speechd-el is an Emacs client to speech synthesizers, Braille displays
and other alternative output interfaces.  It provides full speech and
Braille output environment for Emacs.

This package contains the compiled Emacs lisp bytecode.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
%makeinstall_std datadir=%_datadir libdir=%_libdir \
		 emacslispdir=%_emacslispdir

mkdir -p %buildroot%_emacs_sitestart_dir
cat <<'EOF' >%buildroot%_emacs_sitestart_dir/speechd.el
(setq load-path (append load-path '("%_speechdeldir/")))
(autoload 'speechd-speak "speechd-speak"
  "Emacs speech and Braille output interface." t)
(speechd-speak)
EOF

%files lisp
%doc README COPYING AUTHORS ANNOUNCE NEWS
%_speechdeldir/*.elc
%_infodir/%name.info.xz
%_emacs_sitestart_dir/speechd.el

%files
%_libdir/emacs/%emacs_version/native-lisp/%emacs_version-*/*.eln

%changelog
* Tue Feb 11 2025 Artem Semenov <savoptik@altlinux.org> 2.12-alt2
- The package now contains natively compiled modules (thx Paul Wolneykien)

* Fri Dec 27 2024 Artem Semenov <savoptik@altlinux.org> 2.12-alt1
- Initial build for Sisyphus (ALT bug: 52267)
