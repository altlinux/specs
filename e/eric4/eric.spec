Summary: The eric is a Python IDE
Name: eric4
Version: 4.4.20
Release: alt1
Source0: %name-%version-%release.tar
#Packager: Gennady Kovalev <gik@altlinux.ru>
Packager: Mikhail Pokidko <pma@altlinux.org>

License: GPL
Group: Development/Python
URL: http://www.die-offenbachs.de/eric/

PreReq: python = %_python_version
BuildPreReq: python-devel
#BuildPreReq: libqscintilla2-qt4-python
BuildPreReq: python-module-qscintilla2-qt4
BuildPreReq: %py_package_dependencies sip
BuildPreReq: %py_package_dependencies PyQt4

#Requires: libqscintilla2-qt4-python
Requires: python-module-qscintilla2-qt4

%description
Eric4 is a full featured Python IDE that is written in PyQt using the QScintilla editor widget. For information on PyQt and QScintilla please see Riverbank Computing.


%prep
%setup


%build


%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%python_sitelibdir
mkdir -p %buildroot%_menudir
mkdir -p %buildroot%_datadir/pixmaps
# remove unsopprted Python3 files, examples, and it mod_python deps
rm -rf eric/Examples
rm -rf eric/DebugClients/Python3

python install.py -z -i %buildroot -b %_bindir -d %python_sitelibdir -c

install -m644 eric/icons/default/eric.png %buildroot/%_datadir/pixmaps/%name.png

cat <<EOF > %buildroot/%_menudir/eric4
?package(eric4): needs=X11 \
section="Applications/Development/Development environments" \
title="Eric" \
longtitle="" \
command="%_bindir/eric4" \
icon="eric4.png"
EOF
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Eric
Comment=A powerful python IDE
Icon=%{name}
Exec=%name
Terminal=false
Categories=Development;IDE;
EOF

export DESTDIR=%buildroot
python install-i18n.py

%files
%_bindir/*
%python_sitelibdir/*
%_desktopdir/%{name}.desktop
%_datadir/pixmaps/%name.png
%doc README LICENSE.GPL3 changelog README-i18n.txt THANKS 

%_datadir/qt4/qsci/api/python/*.api
%_datadir/qt4/qsci/api/ruby/*.api


%changelog
* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.20-alt1
- Version 4.4.20

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.4.16-alt1.1
- Rebuild with Python-2.7

* Thu Aug 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.16-alt1
- Version 4.4.16

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 4.4.0-alt1.qa1
- NMU: converted menu to desktop file

* Thu Jan 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1
- Built for Sisyphus version 4.4.0 (ALT #16640)

* Tue Jan 12 2010 Mikhail Pokidko <pma@altlinux.org> 4.4.0-alt1
- 4.4.0

* Fri Nov 13 2009 Mikhail Pokidko <pma@altlinux.org> 4.3.9-alt1
- 4.3.9 build

* Mon Jun 02 2008 Gennady Kovalev <gik@altlinux.ru> 4.2.0-alt1.20080525
-  Eric 4.2 snapshot 20080525

* Wed May 14 2008 Gennady Kovalev <gik@altlinux.ru> 4.2.0-alt1.20080503
-  Eric 4.2 snapshot 20080503

* Fri May 02 2008 Gennady Kovalev <gik@altlinux.ru> 4.2.0-alt1
- Eric 4.2.0

* Sun Mar 02 2008 Gennady Kovalev <gik@altlinux.ru> 4.1.0-alt1
- Eric 4.1.0

* Tue Feb 12 2008 Gennady Kovalev <gik@altlinux.ru> 4.0.4-alt5
- Rebuild for python 2.5

* Fri Jan 11 2008 Gennady Kovalev <gik@altlinux.ru> 4.0.4-alt4
- Remove sitecustomize.py (#13968)

* Wed Jan 02 2008 Gennady Kovalev <gik@altlinux.ru> 4.0.4-alt3
- Requires fixed

* Wed Jan 02 2008 Gennady Kovalev <gik@altlinux.ru> 4.0.4-alt2
- Spec file fixes
  + rename project to eric4
  + remove mod_python dependencies

* Wed Jan 02 2008 Gennady Kovalev <gik@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Mon Nov 05 2007 Alexey Morsov <swi@altlinux.ru> 3.9.5-alt1
- 3.9.5

* Sun May 28 2006 Ivan Fedorov <ns@altlinux.ru> 3.9.0-alt1
- 3.9.0

* Sun Apr 09 2006 Ivan Fedorov <ns@altlinux.ru> 3.8.2-alt1
- 3.8.2

* Sat Dec 31 2005 Ivan Fedorov <ns@altlinux.ru> 3.8.1-alt1
- 3.8.1

* Wed Nov 09 2005 Ivan Fedorov <ns@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Sat Jul 16 2005 Ivan Fedorov <ns@altlinux.ru> 3.7.1-alt1
- 3.7.1

* Wed Jun 08 2005 Ivan Fedorov <ns@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Sat Mar 12 2005 Ivan Fedorov <ns@altlinux.ru> 3.6.2-alt2
- rebuild with python 2.4

* Tue Feb 22 2005 Ivan Fedorov <ns@altlinux.ru> 3.6.2-alt1
- 3.6.2

* Tue Feb 01 2005 Ivan Fedorov <ns@altlinux.ru> 3.6.1-alt1
- 3.6.1

* Thu Jan 27 2005 Ivan Fedorov <ns@altlinux.ru> 3.6.0-alt0.M24.1
- Backport to Master 2.4

* Mon Jan 24 2005 Ivan Fedorov <ns@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Tue Jan 04 2005 Ivan Fedorov <ns@altlinux.ru> 3.5.1-alt1.M24.1
- Backport to Master 2.4

* Wed Dec 29 2004 Ivan Fedorov <ns@altlinux.ru> 3.5.1-alt2
- we doesn't hard require python-module-PyQt now

* Mon Dec 27 2004 Ivan Fedorov <ns@altlinux.ru> 3.6.0-alt0.snap20041223
- 3.6.0-snapshot-20041223

* Wed Dec 08 2004 Ivan Fedorov <ns@altlinux.ru> 3.5.1-alt1
- 3.5.1
- removed patch0 (applied to upsteam)
- we doesn't require python-strict now

* Mon Nov 22 2004 Ivan Fedorov <ns@altlinux.ru> 3.6.0-alt0.snap20041121
- Testing snapshot

* Fri Nov 19 2004 Ivan Fedorov <ns@altlinux.ru> 3.5.0-alt5
- fixing provides
- fixing requires
- rewrite spec

* Mon Nov 08 2004 Ivan Fedorov <ns@altlinux.ru> 3.5.0-alt4
- fixing scripts in %_bindir

* Sun Nov 07 2004 Ivan Fedorov <ns@altlinux.ru> 3.5.0-alt3
- Added patch for work russian translation.

* Sat Nov 06 2004 Ivan Fedorov <ns@altlinux.ru> 3.5.0-alt2
- Added i18n files.

* Fri Nov 05 2004 Ivan Fedorov <ns@altlinux.ru> 3.5.0-alt1
- New release

* Fri Nov 05 2004 Ivan Fedorov <ns@altlinux.ru> 3.3.1-alt2
- Fixing building

* Mon Dec 22 2003 Serge V. Sergeev <ssv@altlinux.ru> 3.3.1-alt1
- new release

* Thu Apr 10 2003 Serge Sergeev <ssv@altlinux.ru> 3.1-alt1
- new release

* Fri Dec 20 2002 Serge Sergeev <ssv@altlinux.ru> 3.0.0-alt2
- encoding patch added

* Tue Dec 17 2002 Serge Sergeev <ssv@altlinux.ru> 3.0.0-alt1
- new release

