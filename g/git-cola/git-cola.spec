%def_enable check

Name: git-cola
Version: 4.8.1
Release: alt1

Summary: A highly caffeinated git gui
License: GPL-2.0-or-later
Group: Development/Tools

Url: https://git-cola.github.io
Vcs: git://github.com/git-cola/git-cola.git
Source: %name-%version.tar
Patch: git-cola-4.5.0-alt-tox-v3.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_enabled check
BuildRequires(pre): python3-module-pytest python3-module-tox-pip-version python3-module-qtpy python3-module-PyQt5 python3-module-GitPython python3-module-polib
%endif
BuildRequires: python3-module-sphinx-devel python3-module-setuptools python3-module-wheel
# hasher tests:
Requires: python3-module-pyinotify python3-module-PyQt5 git-core

%description
A sweet, carbonated git gui known for its sugary flavour
and caffeine-inspired features.

%prep
%setup
%if "%(rpmquery --qf '%%{VERSION}' python3-module-tox)" < "4"
%patch -p1
%endif
%prepare_sphinx3 share/doc/%name
sed -i '/Git Cola version/s/%%(cola_version)s/%{version}/' \
    cola/widgets/about.py
# Not needed with virtualenv.
sed -i '/tox-venv/d' tox.ini
sed -i 's/ --flake8//' pytest.ini

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name
# because executable script is not executable
chmod +x %buildroot%python3_sitelibdir/cola/widgets/spellcheck.py
chmod +x %buildroot%python3_sitelibdir/cola/bin/ssh-askpass
chmod +x %buildroot%python3_sitelibdir/cola/bin/ssh-askpass-darwin

%if_enabled check
%check
%tox_check_pyproject
%endif

%files -f %name.lang
%doc COPYING COPYRIGHT README.md
%_bindir/*
%_desktopdir/*.desktop
%_docdir/git-cola
%_iconsdir/hicolor/scalable/apps/git-cola.svg
%_datadir/metainfo/git-*.appdata.xml
%python3_sitelibdir/*

%changelog
* Mon Jul 29 2024 Leontiy Volodin <lvol@altlinux.org> 4.8.1-alt1
- New version 4.8.1.

* Thu Jul 04 2024 Leontiy Volodin <lvol@altlinux.org> 4.8.0-alt1
- New version 4.8.0.

* Mon May 13 2024 Leontiy Volodin <lvol@altlinux.org> 4.7.1-alt1
- New version 4.7.1.

* Tue Mar 05 2024 Leontiy Volodin <lvol@altlinux.org> 4.6.1-alt1
- New version 4.6.1.

* Thu Jan 25 2024 Leontiy Volodin <lvol@altlinux.org> 4.5.0-alt1
- New version 4.5.0.
- Updated fix with tox < 4.

* Tue Nov 21 2023 Leontiy Volodin <lvol@altlinux.org> 4.4.1-alt1
- New version 4.4.1.

* Tue Nov 07 2023 Leontiy Volodin <lvol@altlinux.org> 4.4.0-alt1
- New version 4.4.0.
- Fixed check via tox < 4.

* Fri Sep 01 2023 Leontiy Volodin <lvol@altlinux.org> 4.3.2-alt1
- New version 4.3.2.

* Mon Aug 21 2023 Leontiy Volodin <lvol@altlinux.org> 4.3.1-alt1
- New version 4.3.1.

* Thu Aug 17 2023 Leontiy Volodin <lvol@altlinux.org> 4.3.0-alt1
- New version 4.3.0.

* Sun Apr 02 2023 Leontiy Volodin <lvol@altlinux.org> 4.2.1-alt1
- New version 4.2.1.

* Mon Mar 27 2023 Leontiy Volodin <lvol@altlinux.org> 4.2.0-alt1
- New version 4.2.0.

* Mon Dec 26 2022 Leontiy Volodin <lvol@altlinux.org> 4.1.0-alt1
- New version 4.1.0.

* Fri Nov 25 2022 Leontiy Volodin <lvol@altlinux.org> 4.0.4-alt1
- New version 4.0.4.
- Enabled tests.

* Mon Nov 14 2022 Leontiy Volodin <lvol@altlinux.org> 4.0.3-alt1
- New version 4.0.3.

* Mon Oct 03 2022 Leontiy Volodin <lvol@altlinux.org> 4.0.2-alt1
- New version 4.0.2.

* Tue Aug 02 2022 Leontiy Volodin <lvol@altlinux.org> 4.0.1-alt1
- New version 4.0.1.
- Ported to %%pyproject macros.

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
