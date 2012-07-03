Name: Pymacs
Version: 0.24
Release: alt1beta2.1

Summary: Two-way communication between Python and Emacs
Source: %name-%version.tar
License: GPL
Group: Development/Python
Requires: python
Requires: emacs
Packager: Andrey Khavryuchenko <akhavr@altlinux.ru>
Url: http://pymacs.progiciels-bpi.ca/
BuildArch: noarch

BuildRequires: python-devel python-module-docutils
BuildRequires: emacs

%description
Pymacs is a powerful tool which, once started from Emacs, allows both-way
communication between Emacs Lisp and Python. Pymacs aims Python as an
extension language for Emacs rather than the other way around, and this
asymmetry is reflected in some design choices. Within Emacs Lisp code,
one may load and use Python modules. Python functions may themselves use
Emacs services, and handle Emacs Lisp objects kept in Emacs Lisp space.

%prep
%setup

%build
env CFLAGS="%optflags" make all

%install
python setup.py install --root=%buildroot --record=INSTALLED_FILES
emacs -batch -eval '(byte-compile-file "pymacs.el")'
mkdir -p %buildroot%_emacslispdir/pymacs
mv pymacs.elc %buildroot%_emacslispdir/pymacs

mkdir -p %buildroot/%_sysconfdir/emacs/site-start.d/
cat <<EOF > %buildroot/%_sysconfdir/emacs/site-start.d/pymacs.el
(autoload 'pymacs-apply "pymacs")
(autoload 'pymacs-call "pymacs")
(autoload 'pymacs-eval "pymacs" nil t)
(autoload 'pymacs-exec "pymacs" nil t)
(autoload 'pymacs-load "pymacs" nil t)
EOF

python pppp -C ppppconfig.py pymacs.rst.in
rst2html.py --input-encoding=UTF-8 pymacs.rst pymacs.html

%files -f INSTALLED_FILES
%_sysconfdir/emacs/site-start.d/pymacs.el
%python_sitelibdir/%name
%_emacslispdir/pymacs/
%doc TODO README THANKS pymacs.html

%changelog
* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.24-alt1beta2.1
- Rebuild with Python-2.7

* Wed Oct 26 2011 Dmitry Derjavin <dd@altlinux.org> 0.24-alt1beta2
- 0.24-beta2;
- specfile cleanup.

* Wed Oct 26 2011 Dmitry Derjavin <dd@altlinux.org> 0.22-alt3
- Now using python_sitelibdir macro.

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 0.22-alt2.1
- Rebuilt with python-2.5.

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 0.22-alt2
- Fix 'Non-ASCII character' error.
- Don't try to pack missing *.pyo. 

* Wed Aug 01 2007 Slava Semushin <php-coder@altlinux.ru> 0.22-alt1.1.1.1
- NMU
- Trying to fix building under x86_64 again

* Mon Jul 30 2007 Slava Semushin <php-coder@altlinux.ru> 0.22-alt1.1.1
- NMU
- Fixed build under x86_64 (don't use %%_libdir macros)

* Sun Jul 01 2007 Slava Semushin <php-coder@altlinux.ru> 0.22-alt1.1
- NMU
- Fixed misprint in package %%description (#11834)
- Catalog /usr/lib/python2.4/site-packages/Pymacs now belongs to package
- Spec cleanup:
  + s|Source0|Source|
  + Added url to Source tag
  + Updated Url tag
  + Removed trailing spaces from %%description
  + s|%%setup -n Pymacs-%%version -q|%%setup|
  + s|$RPM_OPT_FLAGS|%%optflags|
  + s|$RPM_BUILD_ROOT|%%buildroot|
  + s|%%_datadir/emacs/site-lisp|%%_emacslispdir|

* Tue Dec 30 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.22-alt1
  Initial build
