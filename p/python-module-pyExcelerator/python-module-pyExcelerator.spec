%define version 0.6.4.1
%define release alt1
%setup_python_module pyExcelerator

Summary: Pure-python generating Excel 97+ files
Name: %packagename
Version: %version
Release: %release.1
Source0: %modulename-%version.tar.bz2
License: BSD
Group: Development/Python
Prefix: %prefix
BuildArch: noarch
Url: http://sourceforge.net/projects/pyexcelerator/
Packager: Python Development Team <python@packages.altlinux.org>

Patch1: %modulename-0.6.3a-stdout.patch
Patch2: %modulename-0.6.3a-p23.patch

%description
pyExcelerator is a library for generating Excel 97/2000/XP/2003 and
OpenOffice Calc compatible spreadsheets. pyExcelerator has full-blown support
for UNICODE in Excel and Calc spreadsheets, allows using variety of formatting
features, provides interface to printing options of Excel and OpenOffice Calc.
pyExcelerator contains also Excel BIFF8 dumper and MS compound documents
dumper. Main advantage is possibility of generating Excel spreadsheets without
COM  servers.  The only requirement -- Python 2.4b2 or higher. From version
0.5 pyExcelerator can import data from Excel spreadsheets.

%prep
%setup  -q -n %modulename-%version
#patch1 -p1
#patch2 -p1

%build
%python_build

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.4.1-alt1.1
- Rebuild with Python-2.7

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4.1-alt1
- Version 0.6.4.1

* Wed Dec 16 2009 Igor Vlasenko <viy@altlinux.ru> 0.6.3a-alt1.1.1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-pyExcelerator
  * postclean-05-filetriggers for spec file

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3a-alt1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.6.3a-alt1.1
- Rebuilt with python-2.5.

* Wed Nov 01 2006 Alexey Morsov <swi@altlinux.ru> 0.6.3a-alt1
- NMU: new version
- NMU: Add patch for stdout output and for python23

* Tue Oct 04 2005 Ivan Fedorov <ns@altlinux.ru> 0.6.2a-alt1
- Initial build for ALT Linux.
