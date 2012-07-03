Name: clearsilver
Version: 0.10.5
Release: alt1.1.1

Summary: Neotonic ClearSilver
License: Open Source - Neotonic ClearSilver License (Apache 1.1 based)
Group: Development/Other
Url: http://www.clearsilver.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: http://www.clearsilver.net/downloads/%name.tar

BuildPreReq: zlib-devel
BuildPreReq: python-devel >= %__python_version

%def_disable static
%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

# Automatically added by buildreq on Sun Oct 17 2004
BuildRequires: python-base python-modules-encodings zlib-devel

%description
ClearSilver is a fast, powerful, and language-neutral HTML template system.
In both static content sites and dynamic HTML applications, it provides a
separation between presentation code and application logic which makes
working with your project easier.

Because it's written as a C-library, and exported to scripting languages
like Python and Perl via modules, it is extremely fast compared to template
systems written in a script language.

%if_enabled static
%package -n lib%name-devel-static
Summary: Neotonic ClearSilver development files
Group: Development/Python

%description -n lib%name-devel-static
This package contains Neotonic ClearSilver development files.
%endif

%package -n python-module-%name
Summary: Neotonic ClearSilver Python Module
Group: Development/Python
#Requires: %name = %version-%release
Provides: python%__python_version(neo_cgi)
Provides: python%__python_version(neo_cs)
Provides: python%__python_version(neo_util)
Provides: %name-python
Obsoletes: %name-python

%description -n python-module-%name
The clearsilver-python package provides a python interface to the
clearsilver CGI kit and templating system.

%prep
%setup -q -n %name
sed -i 's/LIBRARIES = inserted + LIBRARIES/LIBRARIES = LIBRARIES + inserted/' \
	python/setup.py

%build
#__subst 's,python_versions=".*",python_versions="%__python_version",' configure.in
#__autoconf
%configure \
	--disable-wdb \
	--disable-apache \
	--disable-ruby \
	--disable-perl \
	--disable-java \
	--disable-csharp \
	--enable-gettext \
	--enable-python \
	--with-python=%__python \
	%{subst_enable static}

%add_optflags %optflags_shared
%make_build OPT='%optflags'
#__subst "s,/bin/env python,%_bindir/python%__python_version," scripts/document.py

%install
mkdir -p %buildroot{%python_sitelibdir,%_docdir/%name-%version}
%makeinstall PYTHON_SITE=%buildroot%python_sitelibdir install

%if_disabled static
rm -rf %buildroot{%_libdir/*.a,%_includedir/*,%_man3dir/*}
%endif

%files
%_bindir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%_includedir/*
%_man3dir/*
%endif

%files -n python-module-%name
%python_sitelibdir/neo_cgi.so

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.5-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.5-alt1.1
- Rebuilt with python 2.6

* Tue May 26 2009 Ilya Mashkin <oddity@altlinux.ru> 0.10.5-alt1
- 0.10.5
- rename %name-python to python-module-%name

* Wed Feb 20 2008 Grigory Batalov <bga@altlinux.ru> 0.10.4-alt3.1
- Rebuilt with python-2.5.

* Wed Feb 20 2008 Grigory Batalov <bga@altlinux.ru> 0.10.4-alt3
- Specify a python executable to avoid version search.

* Sat Jun 30 2007 Dmitry V. Levin <ldv@altlinux.org> 0.10.4-alt2
- Fixed neo_cgi.so linkage (wrar, #11798).
- Set %%_unpackaged_files_terminate_build to 1.
- Set %%_verify_elf_method to strict.
- Cleaned up specfile a bit.

* Sun Apr 22 2007 Ivan Fedorov <ns@altlinux.ru> 0.10.4-alt1
- 0.10.4

* Wed Jan 11 2006 Ivan Fedorov <ns@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Thu Apr 28 2005 Ivan Fedorov <ns@altlinux.ru> 0.9.14-alt1
- 0.9.14

* Sun Oct 17 2004 Ivan Fedorov <ns@altlinux.ru> 0.9.12-alt0.2
- Fixing privides for clearsilver-python

* Sun Oct 17 2004 Ivan Fedorov <ns@altlinux.ru> 0.9.12-alt0.1
- Initial build

