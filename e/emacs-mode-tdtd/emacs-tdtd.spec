%define modename tdtd

Name: emacs-mode-%modename
Version: 0.71
Release: alt7

Summary: A GNU Emacs major mode for editing SGML and XML DTDs
Group: Editors
License: GPL
#OldUrl: http://www.mulberrytech.com/tdtd
Url: http://www.menteith.com/tdtd/
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: %modename-%version.tar.gz
Source2: tdtd-startup-script.el

%define WITH_CUSTOM_EL 0

%if %WITH_CUSTOM_EL
%define custom_eldir custom-%modename
Source1: %custom_eldir.tar.bz2
%endif

BuildArch: noarch

PreReq: emacs emacs-mode-psgml
# Automatically added by buildreq on Wed May 14 2008 (-bi)
BuildRequires: emacs-leim emacs-nox libX11-locales

#BuildRequires: XFree86 XFree86-libs Xaw3d emacs-common emacs-el emacs-leim libjpeg libtiff libungif xpm

%description
Emacs is an advanced and extensible editor. An Emacs major mode
customizes Emacs for editing particular types of text documents. %modename
is a major mode for SGML and XML DTDs.

The mode, which will extend PSGML mode, if available, contains functions
for writing and editing element, attribute, internal parameter entities
and external parameter entity declarations and comments to ease creating
and keeping a consistent style.

More advanced features include automatic XML detection, creation of
Emacs TAGS file, minibuffer completion of elements and parameter entity
names, and syntax highlighting.

All Emacs Lisp code is byte-copmpiled, install %name-el for sources.

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%define _emacs_startscriptsdir %_sysconfdir/emacs/site-start.d
%define modedir %_emacslispdir/%modename
%define __emacsbin %_bindir/emacs

%prep
%setup -q -n %modename-%version

%if %WITH_CUSTOM_EL
%__tar -jxf %SOURCE1 > %modename-%version
%endif

%build
%__cat <<EOF >_%modename-compile.el
    (setq load-path (cons "." load-path))
    (autoload 'mail-position-on-field "sendmail" nil)
EOF

%__emacsbin -batch \
	    -l ./_%modename-compile.el \
	    -f batch-byte-compile  [a-z]*.el

%install
%__mkdir_p %buildroot%modedir
%__install -m644 *.el *.elc %buildroot%modedir

%if %WITH_CUSTOM_EL
%__mkdir_p %buildroot%modedir/%custom_eldir
%__install -m644 %custom_eldir/*.el %buildroot%modedir/%custom_eldir
%endif

%if %WITH_CUSTOM_EL
# Add to %modename-init.el entries from %custom_eldir directory
echo ";;; Apply some customization (fonts, colors, keystrokes ...) for %modename mode" >>%SOURCE2
for f in %custom_eldir/*.el; do
echo -e "\t(load \"%modedir/$f\")" >>%SOURCE2
done
%endif

%__install -pD -m644 %SOURCE2 %buildroot%_emacs_startscriptsdir/%modename.el

%files
%dir %modedir
%modedir/*.elc

%if %WITH_CUSTOM_EL
%modedir/%custom_eldir/*.el
%endif

%config(noreplace) %_emacs_startscriptsdir/%modename.el
%doc TODO *.txt

%files el
%modedir/*.el

%changelog
* Wed May 14 2008 Igor Vlasenko <viy@altlinux.ru> 0.71-alt7
- updated buildreq

* Wed Jan 11 2006 Igor Vlasenko <viy@altlinux.ru> 0.71-alt6
- updated url; now maintained by Emacs Maintainers Team

* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 0.71-alt5
- Move startup script to external file, fix bug #2357

* Tue Jan 27 2004 Ott Alex <ott@altlinux.ru> 0.71-alt4
- Fixing startup scripts

* Mon Jan 26 2004 Ott Alex <ott@altlinux.ru> 0.71-alt3
- Fixing startup scripts

* Tue Dec 16 2003 Ott Alex <ott@altlinux.ru> 0.71-alt2
- fixing startup file

* Sun Mar 16 2003 Ott Alex <ott@altlinux.ru> 0.71-alt1
- fixing startup file

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.71-alt0.6
- rebuild

* Sat May 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.71-alt0.5
- First test release for Sisyphus.

* Wed Feb 21 2001 Yuri N. Sedunov <aris@altlinux.ru> 0.71-alt0.1
- initial release 0.71
