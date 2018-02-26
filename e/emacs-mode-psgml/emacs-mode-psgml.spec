%define modename psgml

Name: emacs-mode-%modename
Version: 1.2.5
Release: alt3

Summary: A GNU Emacs major mode for editing SGML/XML documents
Group: Editors
License: GPL
Url: http://www.lysator.liu.se/projects/about_%modename.html
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: ftp://ftp.lysator.liu.se/pub/sgml/%modename-%version.tar.gz

%define WITH_CUSTOM_EL 1

%if %WITH_CUSTOM_EL
%define custom_eldir custom-%modename
Source1: %custom_eldir.tar.bz2
%endif

BuildArch: noarch

PreReq: emacs sgml-common sgml-tools docbook-dtds openjade xml-utils

# Automatically added by buildreq on Thu Sep 25 2008 (-bi)
BuildRequires: emacs-leim emacs-nox libX11-locales

%description
Emacs is an advanced and extensible editor. An Emacs major mode
customizes Emacs for editing particular types of text documents. PSGML
is a major mode for SGML and XML documents.

PSGML contains a simple SGML parser and can work with any DTD. 
Functions provided includes menus and commands for inserting tags with
only the contextually valid tags, identification of structural errors,
editing of attribute values in a separate window with information about
types and defaults, and structure based editing.

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

# Emacs
%define _emacs_startscriptsdir %_sysconfdir/emacs/site-start.d
%define modedir %_emacslispdir/%modename

# SGML
%define sgml_catalogs_dir %_sysconfdir/sgml

%prep
%setup -q -n %modename-%version

%if %WITH_CUSTOM_EL
%__tar -jxf %SOURCE1 > %modename-%version
%endif

%build
%configure
%make_build lispdir=%_emacslispdir/%modename

%install
%makeinstall "lispdir=%buildroot%_emacslispdir/%modename"

%if %WITH_CUSTOM_EL
%__mkdir_p %buildroot%modedir/%custom_eldir
%__install -m644 %custom_eldir/*.el %buildroot%modedir/%custom_eldir
%endif

# Create %modename-init.el
%__cat <<__INIT__ >%modename-init.el
;;; %modename-init.el --- Startup code for PSGML mode
;;;
;;; Add this to your ~/.emacs or install this file into Emacs' site-start.d
    (setq load-path (append load-path '("%modedir")))

;; load sgml-mode 
    (autoload 'sgml-mode "psgml" "Major mode to edit SGML files." t)
    (autoload 'xml-mode "psgml" "Major mode to edit XML files." t)
    
;; load xml-mode 
    (setq auto-mode-alist (append '(("\\.xml\\'" . xml-mode)) auto-mode-alist))

;; set xmllint for validating xml instead nsgmls. 
    (setq sgml-xml-validate-command "xmllint --noout --valid %s %s")

;; load sgml catalog files (from docbook-dtds and sgml-tools packages)
    (if (not (getenv "SGML_CATALOG_FILES"))
    (defvar sgml-catalog-files '("CATALOG" "%sgml_catalogs_dir/catalog" "%_libdir/sgml-tools/dtd/catalog"))
    "*List of catalog entry files.")
    (put 'sgml-catalog-files 'sgml-type 'list)
    
__INIT__

%if %WITH_CUSTOM_EL
# Add to %modename-init.el entries from %custom_eldir directory
echo ";;; Apply some customization (fonts, colors, keystrokes ...) for PSGML mode" >>%modename-init.el 
for f in %custom_eldir/*.el; do
echo -e "\t(load \"%modedir/$f\")" >>%modename-init.el 
done
%endif

%__install -pD -m644 %{modename}-init.el %buildroot%_emacs_startscriptsdir/%{modename}.el

# install info files
%__mkdir_p %buildroot%_infodir
%__cp *.info %buildroot%_infodir

# Install sources *.el 
%__cp *.el %buildroot%modedir

%files
%dir %modedir
%modedir/*.elc
%modedir/*.map

%if %WITH_CUSTOM_EL
%dir %modedir/%custom_eldir
%modedir/%custom_eldir/*.el
%endif

%config(noreplace) %_emacs_startscriptsdir/%modename.el
%_infodir/*
%doc psgml.ps README.psgml

%files el
%modedir/*.el

%changelog
* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt3
- applied repocop patch: removed obsolete (un)install_info macros

* Fri Sep 26 2008 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt2
- refreshed buildreq

* Thu Mar 13 2003 Ott Alex <ott@altlinux.ru> 1.2.5-alt1
- Fixing startup file

* Sun May 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.5-alt0.5
- 1.2.5
- xmllint is a default parser for XML files (sgml-xml-validate-command).
  xml-utils added to requires list.

* Wed Mar 27 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.4-alt0.6
- First build for Sisyphus w/o xemacs-mode-%name package.
- initial customization.
