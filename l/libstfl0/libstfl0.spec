Name: libstfl0
Version: 0.24
Release: alt4.2.1

%define oname stfl

Summary: library which implements a curses-based widget set for text terminals

License: LGPLv3
Group: Terminals
Url: http://www.clifford.at/stfl/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
# repackaged http://www.clifford.at/stfl/stfl-%version.tar.gz
Source: %oname-%version.tar
Source1: %name.watch

Patch1: stfl-0.24-alt-as-needed.patch
Patch2: stfl-0.24-alt-ruby-linkage-fix.patch
Patch3: stfl-0.24-alt-warnings.patch

# Automatically added by buildreq on Fri Mar 03 2017
# optimized out: libncurses-devel libtinfo-devel perl perl-devel python-base python-modules ruby ruby-stdlibs swig-data
BuildRequires: libncursesw-devel libruby-devel perl-Encode python-devel swig

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

%package -n ruby-%oname
Group: Terminals
Requires: swig ruby
Summary: Ruby binding to stfl

%description -n ruby-%oname
Ruby binding to stfl

%prep
%setup -n %oname-%version
%patch1 -p2
%patch2 -p2
%patch3 -p2

%build
sed -i 's|$(prefix)/$(libdir)/ruby|%_ruby_lib_path/site_ruby|g' ruby/Makefile.snippet
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

%files -n ruby-%oname
%ruby_sitearchdir/stfl.so

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt4.2.1
- rebuild with new perl 5.26.1

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.24-alt4.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.24-alt4.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.24-alt4
- Rebuild with new %%ruby_sitearchdir location

* Fri Mar 03 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.24-alt3
- added support for watchfile.
- fixed compiler warnings.
- built with ruby module.
- added origin (alt) in patch filename.
- clearly marked that source is repackaged.

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2.1
- rebuild with new perl 5.24.1

* Sat Mar 12 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.24-alt2
- remove libstfl.a from -devel package.

* Tue Dec 08 2015 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.24-alt1
- Initial build.
