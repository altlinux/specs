# -*- coding: utf-8 -*-
Version: 0.6
Release: alt1

%setup_python_module ropemacs

Summary: Emacs mode that uses rope library via pymacs.
Name: %packagename
Source: %modulename-%version.tar
License: Python
Group: Development/Python
Prefix: %_prefix
Url: http://rope.sourceforge.net/ropemacs.html
BuildArch: noarch

%description
Ropemacs is an emacs mode that uses rope_ library to provide features
like python refactorings and code-assists.  You should install rope_
library and pymacs_ before using ropemacs.

.. _rope: http://rope.sf.net/
.. _pymacs: http://pymacs.progiciels-bpi.ca/pymacs.html

This module is built for python %__python_version

%prep

%setup -q -n %modulename-%version

%build
mkdir -p buildroot

# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record

CFLAGS="%optflags" %__python setup.py \
	install --optimize=2 \
		--root=`pwd`/buildroot \
		--record=INSTALLED_FILES
%install

cp -pr buildroot %buildroot/

unset RPM_PYTHON

%files -f INSTALLED_FILES
%doc docs/ropemacs.txt docs/done.txt docs/todo.txt

%changelog
* Mon Oct 31 2011 Dmitry Derjavin <dd@altlinux.org> 0.6-alt1
- Initial build.

