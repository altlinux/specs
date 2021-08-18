%def_without python
%def_without ruby

Name: libstfl0
Version: 0.24
Release: alt8

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
#Patch2: stfl-0.24-alt-ruby-linkage-fix.patch
Patch3: stfl-0.24-alt-warnings.patch

BuildRequires: libncursesw-devel perl-Encode swig
%{?_with_python: BuildRequires: python-devel}

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
Requires: perl
Requires: %name = %EVR
Summary: Perl binding to stfl

%description -n perl-%oname
Perl binding to stfl

%package -n python-module-%oname
Group: Terminals
Requires: python
Requires: %name = %EVR
Summary: Python binding to stfl
#%%setup_python_module %%oname

%description -n python-module-%oname
Python binding to stfl

%package -n ruby-%oname
Group: Terminals
Requires: swig ruby libstfl0
Summary: Ruby binding to stfl

%description -n ruby-%oname
Ruby binding to stfl

%prep
%setup -n %oname-%version
%autopatch -p2

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

%if_with python
%files -n python-module-%oname
%python_sitelibdir/lib-dynload/_stfl.so
%python_sitelibdir/stfl.py
%python_sitelibdir/stfl.pyc
%python_sitelibdir/stfl.pyo
%endif #python

%if_with ruby
%files -n ruby-%oname
%ruby_sitearchdir/stfl.so
%endif # ruby

%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.24-alt8
- NMU: drop unused swig require, make interdeps more strong

* Thu Apr 09 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.24-alt7
- Disabled Ruby module.

* Thu Apr 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.24-alt6.1
- ! build by adding proper build requires

* Mon Nov 18 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.24-alt6
- Disabled Python 2 module.

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.24-alt5.2
- rebuild with new perl 5.28.1

* Thu Jul 26 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.24-alt5.1
- Rebuilt for new Ruby autoreq.

* Mon Apr 16 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.24-alt5
- added explicit dependency on libstfl0 to perl-, python- and ruby- subpackages

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.24-alt4.2.3
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.24-alt4.2.2
- Rebuild with Ruby 2.5.0

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
