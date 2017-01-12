Name: rpm-build-python3
Version: 0.1.11
Release: alt1

Summary: RPM helper macros to rebuild python3 packages
License: GPL
Group: Development/Other

Source: %name-%version.tar
BuildArch: noarch

Requires: file >= 4.26-alt11
Conflicts: rpm-build < 4.0.4-alt100.91
# Since the .so handling code in python3.req.py with the help of
# objdump is borrowed from rpm-build, we borrow the dependency, too:
Requires: binutils >= 1:2.20.51.0.7

# We want that the following directory gets detected as a dep of the built python3 pkgs;
# this happens automatically of the packages that owns it is installed.
Requires: %_rpmlibdir/python3-site-packages-files.req.list
# (The lib64 variant must be owned by the same package; thus it must be detected as well.)

Conflicts: python3 < 3.5

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
install -pD -m755 python3.req.constraint.py %buildroot%_rpmlibdir/python3.req.constraint.py
install -pD -m755 python3.req.files %buildroot%_rpmlibdir/python3.req.files
install -pD -m755 python3.compileall.py %buildroot%_rpmlibdir/python3.compileall.py
install -pD -m755 brp-bytecompile_python3 %buildroot%_rpmlibdir/brp.d/096-bytecompile_python3.brp
# It's like brp.d/128-hardlink_pyo_pyc.brp from rpm-build (but for python3-3.5):
install -pD -m755 brp-hardlink_opt_pyc %buildroot%_rpmlibdir/brp.d/128-hardlink_opt_pyc.brp
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
rpm_builddir="$PWD"
pushd %buildroot/%_rpmlibdir
# It calls ./python3.req, therefore we've changed the CWD:
"$rpm_builddir"/test.sh
popd

%files
%_rpmmacrosdir/python3
%_rpmmacrosdir/python3.env
%_sysconfdir/buildreqs/files/ignore.d/%name
%_rpmlibdir/brp.d/096-bytecompile_python3.brp
%_rpmlibdir/brp.d/128-hardlink_opt_pyc.brp
%_rpmlibdir/brp.d/000-fix_python3_site-packages_location.brp
%_rpmlibdir/python3.compileall.py
%_rpmlibdir/python3.req
%_rpmlibdir/python3.req.py
%_rpmlibdir/python3.req.constraint.py
%_rpmlibdir/python3.req.files
%_rpmlibdir/python3.prov
%_rpmlibdir/python3.prov.py
%_rpmlibdir/python3.prov.files

%changelog
* Wed Jan 11 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.1.11-alt1
- Now: %%python3_req_hier by default (more precise autoreqs like:
  m.sub.subsub instead of m; this often helps to install an otherwise
  missing subpackage or the correct one in case of name collisions).

  Suggest rules to rewrite/provide any special modules (like virtual six.*).

* Fri Jul 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.10-alt1
- %%py3_requires will honor the constraints of %%allow_python3_import_path.

* Fri Jul 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.9-alt1
- .prov.py: honor non-std %%python3_path also if it is inside the std path.

* Sat Jun 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.8-alt1
- %%python3{,_build}_install: force deterministic behavior (useful in
  case of conflicting stuff from simultaneous python2 and python3 builds).
- compileall.py: depth-first processing gives more correct results (compile
  __init__.py would happen before unlink __pycache__/__init__* (its result)).

* Tue May 10 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.7-alt1
- Additional import paths (where our deps are allowed to be
  located) must be given by the maintainer only willingly now with
  %%allow_python3_import_path.

* Sun May 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.6-alt3
- .{req,prov}.files fixed (in the rare case with %%_python3_compile_include).

* Tue May  3 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.6-alt2
- Revert an unintended change of defaults in 0.1.10.6-alt1 (planned
  for future).

* Fri Apr 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.6-alt1
- .{req,prov}.files: honor %%_python3_compile_exclude
  (when using %%_python3_compile_include)
- %%python3_req_nohier added, the reverse to %%python3_req_hier
  (in future, when there is enough provs thx to 0.1.10.2, we'd like to
  use the req_hier mode by default; packages can prepare beforehand)
- Print a bit more diagnostics for skipped autoreqs.

* Thu Apr 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.5-alt1
- .prov.py: generalize to generate longer provs, too.

* Wed Apr 27 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.4-alt1
- .req.py: handle simple __import__ exprs on the same level of code
  nesting as it is done for import statements, too (ALT#32026).
- .req.py: just in case: deps with (deep < 4) are also OK if
  RPM_PYTHON3_REQ_METHOD is slight (the default) or relaxed.

* Fri Apr 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.3-alt1
- Fix a bug of the prev.release: For the additional Provides with the
  full name (when there is also a short name), the optional non-std
  path was wrongly filled twice. (Example: python-module-Pillow.)

* Wed Apr 20 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10.2-alt1
- generate more Requires (many Python3 files used to be skipped
  because "python script text executable" were considered to be
  non-Python3; now, Python files under standard Python3 paths and
  %%_python3_path are considered).
- generate more Provides (ALT#31992) similarly
  (for Python files under standard Python3 paths).
- generate additional (specially-modified) Provides for modules under
  non-standard/non-builtin paths.
- generate more liberal Requires if %%_python3_path or
  %%_python3_compile_include has non-standard/non-builtin paths.

* Tue Mar 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10-alt1
- use only the major Python version number for pythonN(*) autoreqs.
  (This is mostly a cosmetic change in essence: the numbers in the
  pythonN(*) provs and reqs don't mean much. The guarantee that the
  module was run by exactly the same version of python used to be given
  by the dep on python3.3/site-packages/; we are changing this.)
  (The corresponding cosmetic removal of python3.3(*) provs is
  scheduled for later; and we'll let it go on its own, without
  forcing.)
- Now, as python 3.5 stores .pyc compiled with -O and -OO separately
  (as .opt-{1,2}.pyc), brp-bytecompile_python3 can safely make both.

* Tue Mar 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.9.4-alt1
- brp-hardlink_opt_pyc: handle .opt-?.pyc files (introduced in python3-3.5).

* Tue Mar 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.9.3-alt1
- implemented %%requires_python3-ABI, which ultimately asks
  verify_elf to LD_PRELOAD.

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.9.2-alt1
- macros: commented on %%__ vs %%_ (build vs target system properties)
  and cleaned up a bit accordingly.
- Path values fixed:
  + %%python3_includedir has a suffix in the case of Python3 (3.3&3.5, at least).
  + %%python3_tooldir synced with the real value that has been used
    in python3-3.3.
- %%_python3_path value should be adjusted when building python3 package;
  the default made suitable for modules only.
- macros: general-purpose %%ABI_suffix and special %%python3_ABI_dep added.
- simplified the implementation of %%py3_requires & %%py3_provides.

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

