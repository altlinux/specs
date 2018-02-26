%define realname bongo

Name: emacs-%realname
Version: 0
Release: alt0.20070221

Summary: Buffer-oriented media player for Emacs
License: GPL
Group: Sound
Url: http://www.brockman.se/software/bongo
Source: %realname.tbz
Source1: %realname-mplayer.el

Packager: %packager
BuildArch: noarch
BuildPreReq: emacs-devel emacs-nox

%description
Bongo is buffer-oriented media player for Emacs

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%prep
%setup -n %realname

%build

%install
%__mkdir_p %buildroot%_emacslispdir/%realname
%__cp -v *.png *.pbm *.el %buildroot%_emacslispdir/%realname
%__cp -v %SOURCE1 %buildroot%_emacslispdir/%realname
%byte_recompile_lispdir

%__mkdir_p %buildroot%_emacs_sitestart_dir
%__cat >%buildroot%_emacs_sitestart_dir/%realname.el <<__EOF
; site-start script for Emacs, initializes Bongo
; Evgenii Terechkov, Jun 2007, <evg@altlinux.ru>

(add-to-list 'load-path "%_emacslispdir/%realname")

(autoload 'bongo "bongo" "Start Bongo by switching to a Bongo buffer.")
(require 'bongo)

(defun bongo-show-osd ()
  "Display what Bongo is playing on the OSD."
  (interactive)
  (let* ((player (with-bongo-playlist-buffer
                  (or bongo-player
                      (error "No currently playing track"))))
         (elapsed-time (and player (bongo-player-elapsed-time player)))
         (total-time (and player (bongo-player-total-time player)))
         (description (bongo-format-infoset
                       (bongo-player-infoset player)))
         (string (if (not (and elapsed-time total-time))
                     description
                   (format "%%s [%%s/%%s]" description
                           (bongo-format-seconds elapsed-time)
                           (bongo-format-seconds total-time)))))
    (prog1 string
      (osd-show-string string)
      )
    )
  )

(require 'bongo-mplayer)
__EOF

%files
%config(noreplace) %_emacs_sitestart_dir/%realname.el
%dir %_emacslispdir/%realname
%_emacslispdir/%realname/*.elc
%_emacslispdir/%realname/*.png
%_emacslispdir/%realname/*.pbm

%doc README NEWS tree-from-tags.rb

%files el
%_emacslispdir/%realname/*.el

%changelog
* Sat Jun 30 2007 Terechkov Evgenii <evg@altlinux.ru> 0-alt0.20070221
- Initial build for Sisyphus
