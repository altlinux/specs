Name: libstfl0
Version: 0.24
Release: alt2.1

%define oname stfl

Summary: library which implements a curses-based widget set for text terminals

License: LGPLv3
Group: Terminals
Url: http://www.clifford.at/stfl/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
Source: %oname-%version.tar.gz

Patch1: stfl-0.24-as-needed.patch

# Automatically added by buildreq on Mon Jan 18 2016
# optimized out: libncurses-devel libtinfo-devel perl-devel python-base python-modules swig-data
BuildRequires: libncursesw-devel python-devel swig

%description
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and Ruby.
The public STFL API is only 14 simple function calls big and there are
already generic SWIG bindings. Thus is very easy to port STFL to
additional scripting languages.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%package -n perl-%oname
Group: Terminals
Requires: perl swig
Summary: Perl binding to stfl

%description -n perl-%oname
Perl binding to stfl

%package -n python-module-%oname
Group: Terminals
Requires: python swig
Summary: Python binding to stfl
#%%setup_python_module %%oname

%description -n python-module-%oname
Python binding to stfl

# broken with ruby 2.0+
#%%package -n ruby-%%oname
#Group: Terminals
#Requires: swig ruby
#Summary: Ruby binding to stfl

#%%description -n ruby-%%oname
#Ruby binding to stfl

%prep
%setup -n %oname-%version
%patch1 -p2

%build
# SMP-incompatible build
export CFLAGS="%optflags"
make

%install
make DESTDIR=%buildroot prefix=%prefix libdir=%_lib install
rm %buildroot%_libdir/*.a

%files
%doc README
%_libdir/*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n perl-%oname
%_libdir/perl5/*

%files -n python-module-%oname
%python_sitelibdir/lib-dynload/_stfl.so
%python_sitelibdir/stfl.py
%python_sitelibdir/stfl.pyc
%python_sitelibdir/stfl.pyo

%changelog
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2.1
- rebuild with new perl 5.24.1

* Sat Mar 12 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.24-alt2
- remove libstfl.a from -devel package.

* Tue Dec 08 2015 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.24-alt1
- Initial build.
