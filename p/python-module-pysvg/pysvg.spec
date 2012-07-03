Name: python-module-pysvg
Version: 0.2.1
Release: alt1.1
License: BSD
Group: Development/Python
Summary: Pure Python library to create/load and manipulate SVG documents
Source: pysvg-%version.zip
BuildArch: noarch
URL: http://codeboje.de/pysvg
%setup_python_module pysvg

# Automatically added by buildreq on Mon Jul 04 2011
# optimized out: python-base python-modules
BuildRequires: python-devel unzip

%description
pySVG is a pure Python library to create SVG documents. Essentially it
is a python wrapper around svg with the goal to allow people to "program
svg". pySVG can be used to produce svg as an outcome of algorithms you
implement (like koch curves, Lindenmayr systems etc.)

Working with pySVG is pretty straightforward. There is a small tutorial
in the docs folder but i would suggest refering to the testclasses in
the source.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir_noarch/%modulename
%python_sitelibdir_noarch/%modulename-*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Fr. Br. George <george@altlinux.ru> 0.2.1-alt1
- Autobuild version bump to 0.2.1

