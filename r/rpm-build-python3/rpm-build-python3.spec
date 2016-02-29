Name: rpm-build-python3
Version: 0.1.9
Release: alt1

Summary: RPM helper macros to rebuild python3 packages
License: GPL
Group: Development/Other

Source: %name-%version.tar
BuildArch: noarch

Requires: file >= 4.26-alt11
Requires: rpm >= 4.0.4-alt100.45
# Since the .so handling code in python3.req.py with the help of
# objdump is borrowed from rpm-build, we borrow the dependency, too:
Requires: binutils >= 1:2.20.51.0.7

# We want that the following directory gets detected as a dep of the built python3 pkgs;
# this happens automatically of the packages that owns it is installed.
Requires: %_rpmlibdir/python3-site-packages-files.req.list
# (The lib64 variant must be owned by the same package; thus it must be detected as well.)

AutoReqProv: yes, nopython

BuildRequires: python3-dev

%description
These helper macros provide possibility to build python3 modules.

%prep
%setup

%install
install -pD -m644 python3 %buildroot%_rpmmacrosdir/python3
install -pD -m644 python3.env %buildroot%_rpmmacrosdir/python3.env
install -pD -m644 python3.buildreq %buildroot%_sysconfdir/buildreqs/files/ignore.d/%name
install -pD -m755 python3.prov %buildroot%_rpmlibdir/python3.prov
install -pD -m755 python3.prov.py %buildroot%_rpmlibdir/python3.prov.py
install -pD -m755 python3.prov.files %buildroot%_rpmlibdir/python3.prov.files
install -pD -m755 python3.req %buildroot%_rpmlibdir/python3.req
install -pD -m755 python3.req.py %buildroot%_rpmlibdir/python3.req.py
install -pD -m755 python3.req.files %buildroot%_rpmlibdir/python3.req.files
install -pD -m755 python3.compileall.py %buildroot%_rpmlibdir/python3.compileall.py
install -pD -m755 brp-bytecompile_python3 %buildroot%_rpmlibdir/brp.d/096-bytecompile_python3.brp
install -pD -m755 brp-fix_python3_site-packages_location %buildroot%_rpmlibdir/brp.d/000-fix_python3_site-packages_location.brp
#install -pd -m755 %buildroot%python_tooldir/rpm-build
#install -pD -m644 bdist_altrpm.py %buildroot%_libdir/python%__python_version/distutils/command/bdist_altrpm.py
#install -pD -m755 tools/*py %buildroot%python_tooldir/rpm-build
#install -pd -m755 %buildroot%python_tooldir/rpm-build/find
#install -pD -m644 tools/find/*py %buildroot%python_tooldir/rpm-build/find
#install -pd -m755 %buildroot%_bindir

#ln -s `relative %buildroot%python_tooldir/rpm-build/imalyzer.py %buildroot%_bindir/` %buildroot%_bindir/imalyzer
#ln -s `relative %buildroot%python_tooldir/rpm-build/requires.py %buildroot%_bindir/` %buildroot%_bindir/py_requires
#ln -s `relative %buildroot%python_tooldir/rpm-build/provides.py %buildroot%_bindir/` %buildroot%_bindir/py_provides

#unset RPM_PYTHON

%check
./test.sh

%files
%_rpmmacrosdir/python3
%_rpmmacrosdir/python3.env
%_sysconfdir/buildreqs/files/ignore.d/%name
%_rpmlibdir/brp.d/096-bytecompile_python3.brp
%_rpmlibdir/brp.d/000-fix_python3_site-packages_location.brp
%_rpmlibdir/python3.compileall.py
%_rpmlibdir/python3.req
%_rpmlibdir/python3.req.py
%_rpmlibdir/python3.req.files
%_rpmlibdir/python3.prov
%_rpmlibdir/python3.prov.py
%_rpmlibdir/python3.prov.files

%changelog
* Thu Mar 10 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.9-alt1
- if there is an .so (in /*/python3*/), generate a req like:
  python(abi)(64bit) = 3.3
- python3 RPM macros: adapt for the new common site-packages/
  and cleanup unused ones. (TODO: Check that the packages still build!)
- move the installed stuff to the new common site-packages/ by force
  (except "base" python packages).
- use only the major Python version number for pythonN(*) provides.
  (This is mostly a cosmetic change in essence: the numbers in the
  pythonN(*) provs and reqs don't mean much. The guarantee that the
  module was run by exactly the same version of python used to be given
  by the dep on python3.3/site-packages/; we are about to change this.)
  (The corresponding cosmetic change of reqs is scheduled for later;
  and we'll let it go on its own, without forcing.)
- python3.compileall.py: remove unused variable.

* Thu Mar 10 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt100
- provide python3.3(*) always (for the transition from python3.3).
  (NB: Revert this hack when the transition is done.)
  (This is useful, given that old modules can be "run" with
  python3-3.5.1-alt2, which has been hacked to be able to use modules
  from the old site-packages/.)

* Thu Mar 10 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt1
- python3.req: identify myself (in error messages) distinctively
  from python.req.

* Thu Apr 11 2013 Dmitry V. Levin <ldv@altlinux.org> 0.1.7-alt1
- python3.prov.py: added python >= 3.3.1 support.

* Sat Apr 06 2013 Dmitry V. Levin <ldv@altlinux.org> 0.1.6-alt1
- python3.{prov,req}.files:
  + skip files of type "python script text executable";
  + enhanced "python3 script text executable" type check;
  + added is_python3_path check from python3.{prov,req}.py,
    which is now applied only to files of uncertain type.
- python3.{prov,req}.py: removed is_python3 check (closes: #28762).

* Fri Feb 22 2013 Dmitry V. Levin <ldv@altlinux.org> 0.1.5-alt1
- macros.d/python3: use %%__python3 for python3-config location.
- python3.compileall.py: fixed file executability check (by iv@).

* Sat Feb 16 2013 Dmitry V. Levin <ldv@altlinux.org> 0.1.4-alt1
- python3.prov.py: changed to use sysconfig instead of hardcoded suffix.
- macros.d/python3: added %%_python3_extension_suffix macro.

* Fri Feb 15 2013 Dmitry V. Levin <ldv@altlinux.org> 0.1.3-alt1
- python3.{prov,req}.files: skip everything from /usr/lib*/python2*.
- python3.prov.files: skip all files that cannot be provided due to
  rpmbuild restrictions.

* Fri Feb 15 2013 Dmitry V. Levin <ldv@altlinux.org> 0.1.2-alt1
- macros.d/python3:
  + added %%__python3 macro;
  + added %%_python3_abiflags macro (by iv@; closes: #27788).

* Fri Feb 15 2013 Dmitry V. Levin <ldv@altlinux.org> 0.1.1-alt1
- python3.env: export RPM_PYTHON3 if %%__python3 is defined.
- python3.{prov,req}: parametrize python3 exec path.

* Tue Apr 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt5
- Add py3_provides,py3_requires macros (ALT #27153)

* Wed Mar 21 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt4
- Introduce %%_python3_path, %%add_python3_path macros

* Tue Jan 24 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt3
- Fix typo in %%python3_install
- Make brp-bytecompile_python3 usable

* Wed Dec 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2
- Fix %%__python3_version macro
- Fix provides/dependencies generators

* Tue Dec 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt1
- Initial

