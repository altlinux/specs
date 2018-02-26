Name: dynagen
Version: 0.11.0
Release: alt1.qa1.1.1

Summary: Cisco router emulator (dynamips) controller
License: GPL
Group: Emulators
URL: http://dyna-gen.sourceforge.net
Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

Source0: %name-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Mar 23 2008
BuildRequires: python-base

%description
A front end to the Dynamips router emulator.  Uses .ini style files
to build the router instances and control the hypervisor

%prep
%setup

%install
mkdir -p %buildroot/%_sysconfdir
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%python_sitelibdir
mkdir -p %buildroot/%_datadir/%name
mkdir -p %buildroot/%_docdir/%name-%version

#scripts
install -m 0644 dynagen.ini %buildroot/%_sysconfdir/%name.ini
install -m 0755 dynagen %buildroot/%_bindir/%name
install -m 0755 pemuwrapper.py %buildroot/%_bindir
install -m 0644 confConsole.py %buildroot/%python_sitelibdir/
install -m 0644 configobj.py %buildroot/%python_sitelibdir/
install -m 0644 console.py %buildroot/%python_sitelibdir/
install -m 0644 dynamips_lib.py %buildroot/%python_sitelibdir/
install -m 0644 pemu_lib.py %buildroot/%python_sitelibdir/
install -m 0644 pemubin.py %buildroot/%python_sitelibdir/
install -m 0644 validate.py %buildroot/%python_sitelibdir/
install -m 0644 configspec %buildroot/%_datadir/%name



#docs and examples
tar -cf - docs | tar -xf - -C %buildroot/%_docdir/%name-%version
tar -cf - sample_labs | tar -xf - -C %buildroot/%_docdir/%name-%version
install -m 0644 README.txt %buildroot/%_docdir/%name-%version

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%_sysconfdir/%name.ini
%_bindir/%name
%_bindir/pemuwrapper.py
%python_sitelibdir/confConsole.py
%python_sitelibdir/configobj.py
%python_sitelibdir/console.py
%python_sitelibdir/dynamips_lib.py
%python_sitelibdir/pemu_lib.py
%python_sitelibdir/pemubin.py
%python_sitelibdir/validate.py
%dir %_datadir/%name
%_datadir/%name/configspec
%dir %_docdir/%name-%version
%_docdir/%name-%version/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.0-alt1.qa1.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.qa1.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.11.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * macos-ds-store-file-in-package for dynagen
  * postclean-05-filetriggers for spec file

* Sat Apr 26 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Mon Mar 24 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.10.1-alt2
- fix package building on x86_64

* Sun Mar 23 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.10.1-alt1
- inital build for ALT Linux

