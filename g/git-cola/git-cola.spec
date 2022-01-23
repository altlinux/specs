Name: git-cola
Version: 3.11.0
Release: alt2

Summary: A highly caffeinated git gui
License: GPL-2.0-or-later
Group: Development/Tools

Url: https://git-cola.github.io
# https://github.com/git-cola/git-cola.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx-devel
#BuildRequires: rpm-build-gir tcl
BuildRequires: asciidoc
# hasher tests:
Requires: python3-module-pyinotify python3-module-PyQt5 git-core

AutoReq: no
AutoProv: yes,nopython
# skip internal module reqs
%add_python3_req_skip cola cola.i18n cola.models cola.widgets

%description
A sweet, carbonated git gui known for its sugary flavour
and caffeine-inspired features.

%prep
%setup

# fix python shebangs
sed -i 's|/usr/bin/env python|%__python3|' $(find ./ -name '*.py')
sed -i 's|/usr/bin/env python|%__python3|' bin/git-cola bin/git-cola-sequence-editor bin/git-dag

%prepare_sphinx3 share/doc/%name

%build
%python3_build_debug

%install
%python3_install
%find_lang %name
# because executable script is not executable
chmod +x %buildroot%python3_sitelibdir/cola/widgets/spellcheck.py
chmod +x %buildroot%_datadir/git-cola/lib/cola/widgets/spellcheck.py

%files -f %name.lang
%doc COPYING COPYRIGHT README.md
%_bindir/*
%_desktopdir/*.desktop
%_datadir/git-cola
%_datadir/metainfo/git-cola.appdata.xml
%_datadir/metainfo/git-dag.appdata.xml
%_docdir/git-cola
#_man1dir/*
%python3_sitelibdir/*

%changelog
* Wed Jan 19 2022 Stanislav Levin <slev@altlinux.org> 3.11.0-alt2
- Fixed FTBFS (setuptools 60+).

* Wed Oct 20 2021 Leontiy Volodin <lvol@altlinux.org> 3.11.0-alt1
- New version 3.11.0.

* Tue Jul 20 2021 Leontiy Volodin <lvol@altlinux.org> 3.10.1-alt1
- New version 3.10.1.

* Thu Feb 25 2021 Leontiy Volodin <lvol@altlinux.org> 3.9-alt1
- New version 3.9.

* Mon Nov 16 2020 Leontiy Volodin <lvol@altlinux.org> 3.8-alt2
- Disabled AutoReq.

* Tue Sep 15 2020 Leontiy Volodin <lvol@altlinux.org> 3.8-alt1
- New version 3.8.

* Fri Feb 07 2020 Vitaly Lipatov <lav@altlinux.ru> 3.6-alt2
- NMU: build truly python3

* Mon Jan 13 2020 Leontiy Volodin <lvol@altlinux.org> 3.6-alt1
- New version 3.6
- Cleaned buildrequires.
- Built with python2 and python3.

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
