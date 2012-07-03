Name: rpm-build-python
Version: 0.36.0
Release: alt4

# redefine python_libdir for 0.29.alt2 is buggy 
%define python_libdir %_target_libdir/python%__python_version

Summary: RPM helper macros to rebuild python packages
License: GPL
Group: Development/Other

Source: %name-%version.tar
BuildArch: noarch
Packager: Python Development Team <python@packages.altlinux.org>

Requires: rpm >= 4.0.4-alt96.15
Requires: python-base >= 2.7.2-alt3
Requires: file >= 4.26-alt8

AutoReqProv: yes, nopython

# Automatically added by buildreq on Mon May 11 2009
BuildRequires: python-dev python-modules-encodings

%description
These helper macros provide possibility to rebuild
python modules by some Alt Linux Team Policy compatible way.

%package tools
Summary: diagnostic tools
Group: Development/Python
Requires: %name = %version-%release
AutoReqProv: yes, nopython

%description tools
Package consist small toolset to diaganostic common problem of requires in python modules.

%prep
%setup

%build
sed -i 's/@PYTHON_VERSION@/%__python_version/g' python
./test.sh

%install
install -pD -m644 python %buildroot%_rpmmacrosdir/python
install -pD -m644 python.env %buildroot%_rpmmacrosdir/python.env
install -pD -m644 python.buildreq %buildroot%_sysconfdir/buildreqs/files/ignore.d/%name
install -pD -m755 python.prov %buildroot%_rpmlibdir/python.prov
install -pD -m755 python.prov.py %buildroot%_rpmlibdir/python.prov.py
install -pD -m755 python.prov.files %buildroot%_rpmlibdir/python.prov.files
install -pD -m755 python.req %buildroot%_rpmlibdir/python.req
install -pD -m755 python.req.py %buildroot%_rpmlibdir/python.req.py
install -pD -m755 python.req.files %buildroot%_rpmlibdir/python.req.files
install -pD -m755 python.compileall.py %buildroot%_rpmlibdir/python.compileall.py
install -pd -m755 %buildroot%python_tooldir/rpm-build
#install -pD -m644 bdist_altrpm.py %buildroot%_libdir/python%__python_version/distutils/command/bdist_altrpm.py
install -pD -m755 tools/*py %buildroot%python_tooldir/rpm-build
install -pd -m755 %buildroot%python_tooldir/rpm-build/find
install -pD -m644 tools/find/*py %buildroot%python_tooldir/rpm-build/find
install -pd -m755 %buildroot%_bindir

ln -s `relative %buildroot%python_tooldir/rpm-build/imalyzer.py %buildroot%_bindir/` %buildroot%_bindir/imalyzer
ln -s `relative %buildroot%python_tooldir/rpm-build/requires.py %buildroot%_bindir/` %buildroot%_bindir/py_requires
ln -s `relative %buildroot%python_tooldir/rpm-build/provides.py %buildroot%_bindir/` %buildroot%_bindir/py_provides

unset RPM_PYTHON

%files
%_rpmmacrosdir/python
%_rpmmacrosdir/python.env
%_sysconfdir/buildreqs/files/ignore.d/%name
%_rpmlibdir/python.compileall.py
%_rpmlibdir/python.req
%_rpmlibdir/python.req.py
%_rpmlibdir/python.req.files
%_rpmlibdir/python.prov
%_rpmlibdir/python.prov.py
%_rpmlibdir/python.prov.files
#%_libdir/python%__python_version/distutils/command/bdist_altrpm.py
%doc python-module-SAMPLE.spec policy notes doc

%files tools
%_bindir/*
%python_tooldir/rpm-build

%changelog
* Wed Mar 21 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.36.0-alt4
- Take %%_python3_path into account

* Tue Dec 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.36.0-alt3
- Exclude /usr/lib*/python3.{2,3} from automatic compile

* Mon Dec 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.36.0-alt2
- Require python-base >= 2.7.2-alt3 (with subprocess module)

* Thu Dec 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.36.0-alt1
- Simplify automatic dependencies to python-base and python-modules
- Skip processing python3 scripts and %%_libdir/python3 stuff

* Wed Oct 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.35.0-alt1
- add python-2.7 support

* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.34.5-alt4
- Added macro %%python_build_install, an hybrid of %%python_build and
  %%python_install

* Sat Mar 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.34.5-alt3
- Moved directive --debug into macro %%python_build_debug (thnx ldv@)

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.34.5-alt2
- Added into macros %%python_build compiler flags, and now we may
  using %%add_optflags

* Tue Jun 08 2010 Dmitry V. Levin <ldv@altlinux.org> 0.34.5-alt1
- Fixed x86-64 support: changed %%_python_compile_include default
  value to contain both %%_target_libdir and %%_target_libdir_noarch.

* Tue Feb 16 2010 Dmitry V. Levin <ldv@altlinux.org> 0.34.4-alt8
- Fixed %%_python_set_noarch() and %%python_sitelibdir_noarch
  definitions to use %%_target_libdir_noarch instead of %%_libexecdir.
  Rationale: Some packages override %%_libexecdir to /usr/libexec,
  and %%python_sitelibdir_noarch shouldn't be affected by this.

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.34.4-alt7
- Added macros: %%_python_set_arch (backward of %%_python_set_noarch),
  and %%python_sitelibdir_noarch

* Tue Feb 02 2010 Dmitry V. Levin <ldv@altlinux.org> 0.34.4-alt6
- Reverted erroneous change made in previous release.

* Tue Feb 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.34.4-alt5
- Fixed %%py_dependencies

* Mon Jan 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.34.4-alt4
- Added macros %%_python_version as equivalent %%__python_version for
  use in spec files

* Sat Jan 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.34.4-alt3
- Added %%_python_set_noarch macro for set paths for noarch python
  subpackages in archdep packages

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.34.4-alt2
- Rebuilt with python 2.6

* Wed Jul 15 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.34.4-alt1
- Add support for python 2.6

* Sat Jul 04 2009 Fr. Br. George <george@altlinux.ru> 0.34.3-alt1
- Hierarchical search fixed (syntax tree format is evidently extended)

* Thu Jul 02 2009 Fr. Br. George <george@altlinux.ru> 0.34.2-alt1
- Relative Imports (PEP 328) ignored (closes #17154)

* Sat Jun 13 2009 Alexey Tourbin <at@altlinux.ru> 0.34.1-alt2
- rpm-build-python-tools: Disabled python dependencies,
  scheduled for removal.

* Sat Jun 13 2009 Alexey Tourbin <at@altlinux.ru> 0.34.1-alt1
- python.prov.py: Re-added limited support for multpile provides - e.g.
  PIL/Image.py provides both python2.5(PIL.Image) due to PIL/__init__.py
  and python2.5(Image) due to PIL.pth.
- python.prov.py: Do not provide module names with "-" dashes.

* Mon May 11 2009 Alexey Tourbin <at@altlinux.ru> 0.34-alt1
- python.prov.py: Major rewrite.

* Fri Feb 20 2009 Dmitry V. Levin <ldv@altlinux.org> 0.33.2-alt1
- %%python_build: Remove redundancy.

* Wed Feb 18 2009 Dmitry V. Levin <ldv@altlinux.org> 0.33.1-alt1
- Added %%python_build and %%python_install macros (closes: #13941).
- Relocated macro files to %_rpmmacrosdir/.

* Fri Feb 06 2009 Fr. Br. George <george@altlinux.ru> 0.33-alt2
- Fix #18210 (by roughly removing distutil file)
- Fix *64 byte compilation of noarch packages

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.33-alt1.1
- Rebuilt with python-2.5.

* Tue Nov 20 2007 Alexey Tourbin <at@altlinux.ru> 0.33-alt1
- python.req.py: implemented search for particular encoding modules, e.g.
  "# coding: cp1251" should yield dependency on "python2.4(encodings.cp1251)"
- python.req.py: relaxed fatal error condition for possibly non-pythonish
  files; files with *.py suffix or shebang line considered pythonish

* Sat Nov 17 2007 Alexey Tourbin <at@altlinux.ru> 0.32-alt1
- python.req.py: fixed parser.suite failures on empty lines
  with trailing whitespaces
- python.req.py: parser.suite failures are now fatal errors
- python.req.py: added support for "coding:" magic comments,
  which should yield dependency on "encodings"
- python.{req,prov}.files: more elaborate file selection

* Mon Sep 24 2007 Alexey Tourbin <at@altlinux.ru> 0.31-alt1
- adapted for new rpm-build
- python.req.py: attempted to implement stronger self-requires
  elimination, to deal with unmet dependencies which arise with
  non-standard directory layout

* Fri Mar 23 2007 Alexey Tourbin <at@altlinux.ru> 0.30-alt3
- Revert "added macros from /usr/lib/rpm/*/macros",
  due to rpm '%%undefine' unexpected behaviour

* Wed Mar 21 2007 Alexey Tourbin <at@altlinux.ru> 0.30-alt2
- python.req.py: restored .py suffix check until rpm-build
  can use python.req.files

* Wed Mar 21 2007 Alexey Tourbin <at@altlinux.ru> 0.30-alt1
- python.req.py:
  + fixed a bug in "import" clause analysis, due to which only
    the first dependency of multiple arguments was produced; i.e.
    Old result: 'import os, re' -> Requires: python2.4(os)
    New result: 'import os, re' -> Requires: python2.4(os), python2.4(re)
  + made it fail on import errors (also python.prov.py)
  + made it print stderr diagnostics when the dependency is being ignored
  + disabled .py suffix check, for the sake of plain python scripts
- added dependency on python-base, so that python.req.py and python.prov.py
  always work (also explained this change in policy/5-Python_FAQ.txt)
- added buildreq skiplist and placed LC_ALL=C as needed in order to avoid
  dumb dependency on encoding modules when e.g. evaluating %%__python_version
- added new files, for possible use with future rpm-build releases:
  + python.req (python.prov) - wrapper for python.req.py (resp. python.prov.py)
  + python.req.files (.prov.files) - will select python files for req/prov
  + /etc/rpm/macros.d/python.env - piece of rpm-build scriplets' preamble
  + also placed rpm-build python macros to /etc/rpm/macros.d/python

* Sat Jan 13 2007 Fr. Br. George <george@altlinux.ru> 0.29-alt5
- (avm@) Search for .pth files in lib64, too
- Minor policy fix
- move distutils extention to %_libdir instead of %_target_libdir

* Mon Dec 11 2006 Fr. Br. George <george@altlinux.ru> 0.29-alt4
- More verbose diagnostic in rpm-build-python-utils
- Minor policy bug fixed

* Sun Dec 03 2006 Fr. Br. George <george@altlinux.ru> 0.29-alt3
- x86_64 adapdation (so it builds equally on any architecture)
- _target_libdir is used
- absolute symlinks turned to relative

* Fri Sep 15 2006 Fr. Br. George <george@altlinux.ru> 0.29-alt2
- Override %%__python_version macro provided by rpm-build (#9974).
- Specfile cleanup.

* Sun Aug 13 2006 Ivan Fedorov <ns@altlinux.ru> 0.29-alt1
- Add support for python 2.5

* Sat Jun 10 2006 Ivan Fedorov <ns@altlinux.ru> 0.28-alt1
- convert text files to UTF-8
- Fix #8855

* Mon Jan 09 2006 Ivan Fedorov <ns@altlinux.ru> 0.27-alt1
- Fixing provides generator to work with ".pth" files

* Mon Jul 25 2005 Andrey Orlov <cray@altlinux.ru> 0.26-alt1
- Generation hierarchical requires fixed

* Wed May 11 2005 Andrey Orlov <cray@altlinux.ru> 0.24-alt2
- Tools renamed

* Tue May 10 2005 Andrey Orlov <cray@altlinux.ru> 0.23-alt2
- Diagnostic tools package added

* Tue Mar 22 2005 Andrey Orlov <cray@altlinux.ru> 0.21-alt2
- Some files moved from /python2.3 to /python2.4

* Wed Feb 02 2005 Andrey Orlov <cray@altlinux.ru> 0.21-alt1
- Draft of new policy version added

* Sat Jan 22 2005 Alexey Morozov <morozov@altlinux.org> 0.20-alt1
- numerous rpm macros enhancements (svn rev. 10)

* Thu Dec 09 2004 Andrey Orlov <cray@altlinux.ru> 0.19-alt1
- Some macros added: (py_requires, py_provides, etc)

* Fri Oct 29 2004 Andrey Orlov <cray@altlinux.ru> 0.18-alt1
- Preliminary fix for python2.4 compatibility has been added

* Wed Oct 27 2004 Andrey Orlov <cray@altlinux.ru> 0.17-alt1
- Documentation is fixed: special thanks for Ivan Fedorov
- Some stupid bugs that damaged tracebacks are fixed. I think all python 
  packages must be rebuilded.

* Tue Oct 05 2004 Andrey Orlov <cray@altlinux.ru> 0.16-alt6
- Splitted module support added
- Recursive module support added

* Sat Sep 11 2004 Andrey Orlov <cray@altlinux.ru> 0.15-alt1
- Policy files are renamed by MHZ request;
- Some macros added (see RpmMacros.txt);
- File "=" don't be created any more (bug);
- python-<modulename> don't be provided any more (bug #4819)

* Fri Sep 10 2004 Andrey Orlov <cray@altlinux.ru> 0.14-alt2
- Some changes from Alexey Morozov <morozov@altlinux.org> added,
  descriptions followed:

- Defined %%__python_package_prefix, typo fixes in macro functions
  documentation;
- Updated Python_MODULE.txt;

* Tue Jul 20 2004 Andrey Orlov <cray@altlinux.ru> 0.13-alt1
- Documentation changed
- Keyword "relaxed" can be used instead "slight"

* Wed Jun 30 2004 Andrey Orlov <cray@altlinux.ru> 0.12-alt3
- Article about "Require python2.3(__future__)" added into FAQ;
- Codec declaration excluded from find req/prov python scripts;

* Wed Jun 23 2004 Andrey Orlov <cray@altlinux.ru> 0.12-alt2
- Python build utilites will be silently exit if python are not fully installed;
- Python auto Prov use *pth files now;

* Thu May 20 2004 Andrey Orlov <cray@altlinux.ru> 0.11-alt1
- Fix some python2.2 incompatibilites

* Tue May 18 2004 Andrey Orlov <cray@altlinux.ru> 0.10-alt3
- Provides detection enchanced (detect old-style <name>module.so library);
- Some historical clauses exluded from bdist_altrpm;
- Some documentation changes;

* Mon May 17 2004 Andrey Orlov <cray@altlinux.ru> 0.9-alt1
- Ready for sysiphus

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 0.8-alt3
- Package rebuilded to use with new rpm

* Sun Apr 25 2004 Andrey Orlov <cray@altlinux.ru> 0.8-alt2
- Some domcmentations added;

* Wed Apr 21 2004 Andrey Orlov <cray@altlinux.ru> 0.8-alt1
- Fix another "BuildNoarch Problem": BuildRequires correctly inserted now;

* Tue Apr 13 2004 Andrey Orlov <cray@altlinux.ru> 0.7-alt1
- Add BuildPreReq: python_devel = X.Y into spec setup function;
- Fix "BuildNoarch Problem"
- Add some documentation

* Sun Mar 28 2004 Andrey Orlov <cray@altlinux.ru> 0.6-alt1
- Debugging operators removed

* Sat Mar 27 2004 Andrey Orlov <cray@altlinux.ru> 0.5-alt1
- Sources put into archive
- BuildPreReq added into setup_python_module

* Thu Mar 25 2004 Andrey Orlov <cray@altlinux.ru> 0.4-alt2
- Command bdist_altrpm for distutils added;
 
* Mon Mar 15 2004 Andrey Orlov <cray@altlinux.ru> 0.3-alt2
- New bytecompiler added
- Defaults treatment enhanced

* Sun Feb 29 2004 Andrey Orlov <cray@altlinux.ru> 0.2-alt2
- Python scripts for find provides and requires added;
- New RPM macros;
- Samples of find-* added;

* Mon Feb 23 2004 Andrey Orlov <cray@altlinux.ru> 0.1-alt1
- Initial release

