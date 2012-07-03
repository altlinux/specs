# -*- coding: utf-8 -*-
Version: 0.1
Release: alt1rc2

%setup_python_module ropemode

Summary: ropemode, a helper for using rope refactoring library in IDEs.
Name: %packagename
Source: %modulename-%version-rc2.tar.gz
License: Python
Group: Development/Python
Prefix: %_prefix
Packager: Dmitry Derjavin <dd@altlinux.org>
Url: http://pypi.python.org/pypi/ropemode
BuildArch: noarch

%description
ropemode, a helper for using rope refactoring library in IDEs

This module is built for python %__python_version

%prep

%setup -q -n %modulename-%version-rc2

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

%changelog
* Mon Oct 31 2011 Dmitry Derjavin <dd@altlinux.org> 0.1-alt1rc2
- Initial build.

