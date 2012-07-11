%define modename xslide
Name: emacs-%modename
Version: 0.2.2
Release: alt7

Summary: A GNU Emacs major mode for editing XSL stylesheets.
Group: Editors
License: GPL
Url: http://www.menteith.com/xslide
Packager: Emacs Maintainers Team <emacs@altlinux.org>
Source: %modename-%version.tar.gz
Source2: xslide-startup-script.el

%define WITH_CUSTOM_EL 0

%if %WITH_CUSTOM_EL
%define custom_eldir custom-%modename
Source1: %custom_eldir.tar.bz2
%endif

Obsoletes: emacs-mode-xslide
Provides: emacs-mode-xslide = %version

BuildArch: noarch
PreReq: emacs

# Automatically added by buildreq on Tue Sep 09 2008 (-bi)
BuildRequires: emacs-nox emacs-gnus

%description
Emacs is an advanced and extensible editor. An Emacs major mode
customizes Emacs for editing particular types of text documents. %modename
is a major mode for XSL stylesheets.

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

%prep
%setup -q -n %modename-%version

%if %WITH_CUSTOM_EL
%__tar -jxf %SOURCE1 > %modename-%version
%endif

%build
%make_build

%install
%__mkdir_p %buildroot%modedir
%__install -m644 *.el *.elc *.xsl %buildroot%modedir

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

%__install -pD -m644 %SOURCE2 %buildroot%_emacs_startscriptsdir/%{modename}.el

%files
%dir %modedir
%modedir/*.elc
%modedir/*.xsl

%if %WITH_CUSTOM_EL
%modedir/%custom_eldir/*.el
%endif

%config(noreplace) %_emacs_startscriptsdir/%modename.el
%doc *.TXT TODO NEWS ChangeLog

%files el
%modedir/*.el

%changelog
* Wed Jul 11 2012 Terechkov Evgenii <evg@altlinux.org> 0.2.2-alt7
- Fix build with emacs24

* Tue Sep 09 2008 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt6
- resurrected from orphaned

* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 0.2.2-alt5
- Move startup script to external storage, fix bug #2358

* Tue Jan 27 2004 Ott Alex <ott@altlinux.ru> 0.2.2-alt4
- Fixing startup scripts

* Mon Jan 26 2004 Ott Alex <ott@altlinux.ru> 0.2.2-alt3
- Fixing startup scripts

* Tue Dec 16 2003 Ott Alex <ott@altlinux.ru> 0.2.2-alt2
- fixing startup file

* Sat Dec 13 2003 Ott Alex <ott@altlinux.ru> 0.2.2-alt1
- New version

* Sat Jun 07 2003 Ott Alex <ott@altlinux.ru> 0.2.1-alt1
- New version

* Thu Mar 13 2003 Ott Alex <ott@altlinux.ru> 0.2-alt0.7
- Fixing startup file

* Fri Sep 06 2002 Ott Alex <ott@altlinux.ru> 0.2-alt0.6
- Fixing startup script

* Wed Mar 27 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2-alt0.5
- First test build for Sisyphus.
- We have not any required XSLT processor (XT or Saxon).
