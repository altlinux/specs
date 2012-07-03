Name: tepache
Version: 1.1
Release: alt2.1

Summary: Tepache is a code sketcher for python.

License: LGPL
Group: Development/Python
Url: http://primates.ximian.com/~sandino/python-glade/tepache/
Packager: Pavlov Konstantin <thresh@altlinux.ru>
Source: %name-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Aug 26 2005 (-bi)
BuildRequires: python-devel python-modules-compiler python-modules-encodings

%description
Tepache is a code sketcher for python that uses pygtk and glade.
t creates pure python modules with classes that are clean 
abstractions for the toplevel widgets of the glade files. 
That is why we say tepache is not a code generator, 
it is a code sketcher.

%prep
%setup -n %name-%version
rm -f glade-2.10.0-simplegladepython.2.patch

%build
%python_build

%install
%python_install

%files
%doc ChangeLog COPYING.LGPL README sample.glade

%_bindir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1.1-alt1.1
- Rebuilt with python-2.5.

* Fri Aug 26 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.1-alt1
- Initial build for Sisyphus.


