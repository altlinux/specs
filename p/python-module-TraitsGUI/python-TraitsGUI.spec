Name:           python-module-TraitsGUI
Version:        3.6.1
Release:        alt1.svn20110127.1
Summary:        Traits-capable windowing framework

Group:          Development/Python
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
License:        BSD and EPL and LGPLv2 and LGPLv3 and Public Domain
URL:            http://pypi.python.org/pypi/TraitsGUI
# https://svn.enthought.com/svn/enthought/TraitsGUI
Source:        TraitsGUI-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch: noarch
BuildRequires: python-devel python-module-setuptools
BuildPreReq: python-module-setupdocs
Requires: python-module-TraitsBackendQt

%description
The TraitsGUI project contains a toolkit-independent GUI abstraction layer
(known as Pyface), which is used to support the "visualization" features of
the Traits package.

%package docs
Summary: Documentation for traits-capable windowing framework
Group: Development/Documentation
BuildArch: noarch

%description docs
The TraitsGUI project contains a toolkit-independent GUI abstraction layer
(known as Pyface), which is used to support the "visualization" features of
the Traits package.

This package contains development documentation for TraitsGUI.

%prep
%setup -n TraitsGUI-%version
rm -rf TraitsGUI.egg-info
sed -i 's/\r//' image_*.txt examples/workbench/example_workbench_window.py \
 examples/workbench/images/image_LICENSE.txt examples/workbench/person.py \
 examples/workbench/example_workbench_window.py examples/dock/images/image_LICENSE.txt \
 examples/workbench/example_workbench.py examples/images/image_LICENSE.txt
iconv -f iso8859-1 -t utf-8 image_LICENSE_OOo.txt > image_LICENSE_OOo.txt.conv \
 && mv -f image_LICENSE_OOo.txt.conv image_LICENSE_OOo.txt
iconv -f iso8859-1 -t utf-8 image_LICENSE_Eclipse.txt > image_LICENSE_Eclipse.txt.conv \
 && mv -f image_LICENSE_Eclipse.txt.conv image_LICENSE_Eclipse.txt

chmod -x examples/workbench/black_view.py examples/workbench/blue_view.py \
 examples/workbench/red_view.py examples/workbench/yellow_view.py \
 examples/workbench/green_view.py

%build
%python_build

%install
%python_install

#sed -i 's|\.dev||' \
#	%buildroot%python_sitelibdir/TraitsGUI-%version-*.egg-info/requires.txt

%files
%doc *.txt docs/*.txt
%python_sitelibdir/*

%files docs
%doc examples docs/*.pdf docs/*.doc docs/*.ppt

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt1.svn20110127.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.svn20110127
- Version 3.6.1

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.svn20101101
- Version 3.5.1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20100716
- Version 3.4.1

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20100225
- Version 3.3.1
- Extracted docs into separate package

* Mon Jan 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.svn20090902.2
- Rebuilt with new NumPy

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.svn20090902.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.svn20090902
- Version 3.1.1

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1
- Initial build for Sisyphus (thnx Valery Pipin)

* Mon Jun 08 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.4-4
- Fixed BR: python-setupdocs

* Mon Jun 08 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.4-3
- fixed wrong-file-end-of-line-encoding & spurious-executable-perm
- for files in examples folder

* Sun May 24 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.4-2
- Included examples folder in %%doc
- Changed %%define to %%global and changes %%{__python} to python

* Sat May 02 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.4-1
- Updated to 3.0.4

* Sat May 02 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.3-2
- Removed egg-info folder already present, removed %%{version}
- from URL.

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.3-2
- Fixed BuildRequires

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.3-1
- Initial package
