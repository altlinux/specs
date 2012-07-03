%define modulename PyOFC2

Name: python-module-%modulename
Version: 0.1.5dev
Release: alt1

Summary: Python library for Open Flash Chart 2
License: MIT
Group: Development/Python
Url: http://pradeepgowda.com/
Packager: Liudmila Butorina <lbutorina@altlinux.org>

BuildArch: noarch

Source0: %modulename-%version.tar.gz

BuildPreReq: %py_dependencies setuptools

%description
PyOFC2 - Python libraries for Open Flash Chart
==============================================

PyOFC2 generates data files required for `Open Flash Chart 2 <http://teethgrinder.co.uk/open-flash-chart-2/>`_.

Installation
------------

Using `Python Packaging Index <http://pypi.python.org>`_:

    $ easy_install PyOFC2
    
From the source:

    $ git://github.com/btbytes/pyofc2.git
    
Online `Demo <http://btbytes.github.com/pyofc2/>`_.


Using PyOFC2 with Web Frameworks
--------------------------------
`Django + PyOFC2 <http://github.com/btbytes/djofc2_demo>`_ example project.

     

NEWS
====

0.1.5
-----

*Release Date: 2010-09-21*

* Fixed setup bug. Thx http://github.com/marcinn


0.1.4
-----
*Release Date: 2010-09-21*

* converted README to `.rst`. Added `NEWS.rst` for project release information. 
* better pypi documentation.


0.1.3
-----
*Release Date: 2010-09-21*

* Added `bar_on_show` option. Thanks to `lukaszb <http://github.com/lukaszb>`_.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Mon Jan 30 2012 Liudmila Butorina <lbutorina@altlinux.org> 0.1.5dev-alt1
- Initial build

