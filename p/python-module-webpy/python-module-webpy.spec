Name: python-module-webpy
Version: 0.36
Release: alt1
Summary: A simple web framework for Python
Group: Development/Python

# The entire source code is Public Domain save for the following exceptions:
#   web/wsgiserver (CherryPy/BSD)
#     See LICENSE.wsgiserver.txt
#     See http://fedoraproject.org/wiki/Licensing:BSD#New_BSD_.28no_advertising.2C_3_clause.29
#   web/debugerror.py (Modified BSD)
#     This is from django
#     See http://code.djangoproject.com/browser/django/trunk/LICENSE
#   web/httpserver.py (Modified BSD)
#     This is from WSGIUtils/lib/wsgiutils/wsgiServer.py
#     See http://www.xfree86.org/3.3.6/COPYRIGHT2.html#5
License: Public Domain and BSD

Url: http://webpy.org/
Source0: http://webpy.org/static/web.py-%version.tar.gz

BuildRequires: python-devel
BuildArch: noarch

%description
web.py is a web framework for python that is as simple as it is
powerful. web.py is in the public domain; you can use it for whatever
purpose with absolutely no restrictions.

%prep
%setup -n web.py-%version

%build
%python_build

%install
%python_install

%files
#doc LICENSE.txt LICENSE.wsgiserver.txt ChangeLog.txt
%python_sitelibdir/web
%python_sitelibdir/web.py-%version-py%_python_version.egg-info

%changelog
* Wed Oct 26 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.36-alt1
- 0.36

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.34-alt1.1
- Rebuild with Python-2.7

* Wed Sep 22 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.34-alt1
- Initial build

* Tue Jul 07 2009 Ray Van Dolson <rayvd@fedoraproject.org> 0.32-3
- Strip shebang from non-scripts
- Update license information
- Enable unit tests

* Thu Jul 02 2009 Ray Van Dolson <rayvd@fedoraproject.org> 0.32-2
- Added python-devel BuildRequires
- Updated with multiple licensing annotations

* Wed Jul 01 2009 Ray Van Dolson <rayvd@fedoraproject.org> 0.32-1
- Rebase to 0.32

* Mon Jun 01 2009 Ray Van Dolson <rayvd@fedoraproject.org> 0.31-1
- Initial package

