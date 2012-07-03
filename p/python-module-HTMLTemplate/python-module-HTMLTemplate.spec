%define modulename HTMLTemplate
%define packagename python-module-%modulename
%define version 1.5.0
%define release alt1

%setup_python_module HTMLTemplate

Name: %packagename
Version: %version
Release: %release.1

Summary: HTMLTemplate python module
License: MIT
Group: Development/Python
URL: http://sourceforge.net/projects/py-templates/
Packager: Python Development Team <python@packages.altlinux.org>

# https://py-templates.svn.sourceforge.net/svnroot/py-templates/htmltemplate/trunk/
Source0: %modulename-%version.tar.gz

BuildArch: noarch

%description
HTMLTemplate converts HTML/XHTML templates into simple Python object models
that can be manipulated through callback functions in your scripts. Fast,
powerful and easy to use.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
mkdir -p %buildroot%python_sitelibdir
python setup.py install --root=%buildroot --optimize=2 \
	--record=INSTALLED_FILES

find %buildroot%python_sitelibdir/%name -type d | \
        sed -e "s,^%buildroot,%dir ,g" >> INSTALLED_FILES

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%files -f INSTALLED_FILES
%doc README doc sample

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Thu Dec 17 2009 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * macos-resource-fork-file-in-package for python-module-HTMLTemplate
  * postclean-05-filetriggers for spec file

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.4.2-alt1.1
- Rebuilt with python-2.5.

* Sat Jan 06 2007 L.A. Kostis <lakostis@altlinux.ru> 1.4.2-alt1
- initial build for ALTLinux.

