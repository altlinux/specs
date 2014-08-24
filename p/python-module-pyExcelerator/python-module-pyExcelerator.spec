%define version 0.6.4.1
%define release alt1.svn20120213
%setup_python_module pyExcelerator

%def_without python3

Summary: Pure-python generating Excel 97+ files
Name: %packagename
Version: %version
Release: %release
Source0: %modulename-%version.tar.bz2
License: BSD
Group: Development/Python
Prefix: %prefix
BuildArch: noarch
Url: http://sourceforge.net/projects/pyexcelerator/

Patch1: %modulename-0.6.3a-stdout.patch
Patch2: %modulename-0.6.3a-p23.patch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%description
pyExcelerator is a library for generating Excel 97/2000/XP/2003 and
OpenOffice Calc compatible spreadsheets. pyExcelerator has full-blown support
for UNICODE in Excel and Calc spreadsheets, allows using variety of formatting
features, provides interface to printing options of Excel and OpenOffice Calc.
pyExcelerator contains also Excel BIFF8 dumper and MS compound documents
dumper. Main advantage is possibility of generating Excel spreadsheets without
COM  servers.  The only requirement -- Python 2.4b2 or higher. From version
0.5 pyExcelerator can import data from Excel spreadsheets.

%package -n python3-module-%modulename
Summary: Pure-python generating Excel 97+ files
Group: Development/Python3

%description -n python3-module-%modulename
pyExcelerator is a library for generating Excel 97/2000/XP/2003 and
OpenOffice Calc compatible spreadsheets. pyExcelerator has full-blown support
for UNICODE in Excel and Calc spreadsheets, allows using variety of formatting
features, provides interface to printing options of Excel and OpenOffice Calc.
pyExcelerator contains also Excel BIFF8 dumper and MS compound documents
dumper. Main advantage is possibility of generating Excel spreadsheets without
COM  servers.  The only requirement -- Python 2.4b2 or higher. From version
0.5 pyExcelerator can import data from Excel spreadsheets.

%prep
%setup -n %modulename-%version
#patch1 -p1
#patch2 -p1

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc *.txt examples

%if_with python3
%files -n python3-module-%modulename
%doc *.txt examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4.1-alt1.svn20120213
- Snapshot from svn

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
