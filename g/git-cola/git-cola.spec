Name: git-cola
Version: 3.5
Release: alt2

Summary: A highly caffeinated git gui
License: GPLv2+
Group: Development/Tools

Url: https://git-cola.github.io
# https://github.com/git-cola/git-cola.git
Source: %name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 08 2019 (-bi)
# optimized out: python-base python-modules python2-base python3 python3-base rpm-build-python3 sh4 tzdata
BuildRequires: rpm-macros-sphinx3 python3-module-sphinx python3-dev rpm-build-gir tk
BuildRequires: xmlto asciidoc mercurial rpm-macros-sphinx3
# hasher tests:
Requires: python3-module-pyinotify python3-module-PyQt5

%description
A sweet, carbonated git gui known for its sugary flavour
and caffeine-inspired features.

%prep
%setup

sed -i 's|/usr/bin/env python|/usr/bin/env python3|' \
	$(find ./ -name '*.py')

%prepare_sphinx3 share/doc/%name

%build
%python3_build

%install
%python3_install -O1 --skip-build --root %{buildroot} --prefix=%{_prefix}
#make DESTDIR=%buildroot prefix=%prefix install-doc
#make DESTDIR=%buildroot prefix=%prefix install-html
%find_lang %name

%files -f %name.lang
%doc COPYING COPYRIGHT README.md
%_bindir/*
%_desktopdir/*.desktop
%_datadir/git-cola
%_datadir/appdata/git-cola.appdata.xml
%_datadir/appdata/git-dag.appdata.xml
%_docdir/git-cola
#_man1dir/*
%python3_sitelibdir/*

%changelog
* Fri Nov 08 2019 Leontiy Volodin <lvol@altlinux.org> 3.5-alt2
- Switched to python3.

* Tue Sep 24 2019 Leontiy Volodin <lvol@altlinux.org> 3.5-alt1
- 3.5

* Tue Jul 09 2019 Leontiy Volodin <lvol@altlinux.org> 3.4-alt1
- 3.4
- changed url
- simplified futures

* Mon Apr 29 2019 Leontiy Volodin <lvol@altlinux.org> 3.3-alt1
- 3.3

* Tue Oct 20 2015 Michael Shigorin <mike@altlinux.org> 2.4-alt1
- 2.4

* Fri Jul 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1
- Version 2.0.4

* Tue May 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5-alt3
- Disabled docs (brocken)

* Tue Feb 14 2012 Michael Shigorin <mike@altlinux.org> 1.7.5-alt2
- added python-module-pyinotify dependency (which is recommended)

* Thu Feb 09 2012 Michael Shigorin <mike@altlinux.org> 1.7.5-alt1
- NMU: 1.7.5
- added i18n
- added git-dag
- micro spec cleanup

* Sat Mar 13 2010 Boris Savelev <boris@altlinux.org> 1.4.1.2-alt1
- new version

* Mon Jul 20 2009 Boris Savelev <boris@altlinux.org> 1.3.8-alt2.g0838b6e
- update from upstream

* Mon Jun 22 2009 Boris Savelev <boris@altlinux.org> 1.3.8-alt1.g9641c0b
- initial build from Fedora

* Mon Mar 23 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.6-1
- Update to 1.3.6

* Mon Mar 16 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5.42-1
- Update to 1.3.5.42

* Sat Feb 28 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5.28-1
- Added %post and %postun
- Use desktop-file-install

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 9 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-4
- Added missing Requires on PyQt4

* Thu Feb 5 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-3
- Added patch for shebang line removal

* Thu Feb 5 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-2
- Add missing BRs

* Sun Feb 1 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-1
- Update for 1.3.5

* Thu Jan 8 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.4.4-1
- Initial package
