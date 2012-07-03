%define version 1.0.5
%define release alt1
%setup_python_module cElementTree

Summary: A fast C implementation of the ElementTree API.
Name: %{packagename}
Version: %{version}
Release: %{release}.1.1.2.1
Source0: %{modulename}-%{version}-20051216.tar.gz
License: Python (MIT style)
Group: Development/Python
Prefix: %{_prefix}
URL: http://www.effbot.org/zone/celementtree.htm
Packager: Repocop Q. A. Robot <repocop@altlinux.org>
Requires: python-module-elementtree

# Automatically added by buildreq on Thu May 18 2006
BuildRequires: python-modules python-modules-compiler python-modules-encodings

BuildPreReq: python-devel

%description
A fast C implementation of the ElementTree API.

%prep
%setup -n %modulename-%version-20051216

%build
%python_build_debug

%install
%python_build_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.5-alt1.1.1.2.1
- Rebuild with Python-2.7

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.1.1.2
- Rebuilt for debuginfo

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.1.1.1
- Rebuilt with python 2.6

* Tue Nov 03 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1.1.1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-cElementTree

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.0.5-alt1.1
- Rebuilt with python-2.5.

* Thu May 18 2006 Andrey Khavryuchenko <akhavr@altlinux.ru> 1.0.5-alt1
  Initial build
