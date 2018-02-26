Name: sphinx
Version: 2.0.4
Release: alt1
Summary: Free open-source SQL full-text search engine

Group: Text tools
License: GPLv2+
Url: http:/sphinxsearch.com
Source0: http://sphinxsearch.com/downloads/%name-%version.tar.gz
Source1: %name.init
Patch0: sphinx-client-static.patch
Packager: Dmitriy Kulik <lnkvisitor@altlinux.org>

BuildRequires: libMySQL-devel postgresql-devel libexpat-devel gcc-c++

%description
Sphinx is a full-text search engine, distributed under GPL version 2.
Commercial licensing (eg. for embedded use) is also available upon request.

Generally, it's a standalone search engine, meant to provide fast,
size-efficient and relevant full-text search functions to other applications.
Sphinx was specially designed to integrate well with SQL databases and
scripting languages.

Currently built-in data source drivers support fetching data either via direct
connection to MySQL, or PostgreSQL, or from a pipe in a custom XML format.
Adding new drivers (eg. to natively support some other DBMSes) is designed to
be as easy as possible.

Search API is natively ported to PHP, Python, Perl, Ruby, Java, and also
available as a pluggable MySQL storage engine. API is very lightweight so
porting it to new language is known to take a few hours.

As for the name, Sphinx is an acronym which is officially decoded as SQL Phrase
Index. Yes, I know about CMU's Sphinx project.

%package -n libsphinxclient
Summary: Pure C searchd client API library
Group: System/Libraries

%description -n libsphinxclient
Pure C searchd client API library
Sphinx search engine, http://sphinxsearch.com

%package -n libsphinxclient-devel
Summary: Development libraries and header files for libsphinxclient
Group: System/Libraries
Requires: libsphinxclient = %version-%release

%description -n libsphinxclient-devel
Pure C searchd client API library
Sphinx search engine, http://sphinxsearch.com

%package -n libsphinxclient-devel-static
Summary: Development libraries and header files for libsphinxclient
Group: System/Libraries
Requires: libsphinxclient-devel = %version-%release
Conflicts: libsphinxclient-static

%description -n libsphinxclient-devel-static
Pure C searchd client API library
Sphinx search engine, http://sphinxsearch.com

%prep
%setup -q
#%patch0 -p1

# Fix wrong-file-end-of-line-encoding
sed -i 's/\r//' api/ruby/spec/sphinx/sphinx_test.sql
sed -i 's/\r//' api/java/mk.cmd
sed -i 's/\r//' api/ruby/spec/fixtures/keywords.php
sed -i 's/\r//' api/ruby/lib/sphinx/response.rb

%build
%configure --sysconfdir=/etc/sphinx --with-mysql --with-pgsql --with-libstemmer

%make_build

# Build libsphinxclient
cd api/libsphinxclient/
%configure
make

%install
make install DESTDIR=%buildroot INSTALL="%__install -p -c"

# Install sphinx initscript
install -p -D -m 0755 %SOURCE1 %buildroot%_initdir/searchd

# Create /var/log/sphinx
mkdir -p %buildroot%_var/log/sphinx

# Create /var/run/sphinx
mkdir -p %buildroot%_var/run/sphinx

# Create /var/lib/sphinx
mkdir -p %buildroot%_var/lib/sphinx

# Create sphinx.conf
cp %buildroot%_sysconfdir/sphinx/sphinx-min.conf.dist \
    %buildroot%_sysconfdir/sphinx/sphinx.conf

# Modify sphinx.conf
sed -i 's/\/var\/lib\/log\/searchd.log/\/var\/log\/sphinx\/searchd.log/g' \
%buildroot%_sysconfdir/sphinx/sphinx.conf

sed -i 's/\/var\/lib\/log\/query.log/\/var\/log\/sphinx\/query.log/g' \
%buildroot%_sysconfdir/sphinx/sphinx.conf

sed -i 's/\/var\/lib\/log\/searchd.pid/\/var\/run\/sphinx\/searchd.pid/g' \
%buildroot%_sysconfdir/sphinx/sphinx.conf

sed -i 's/\/var\/lib\/data\/test1/\/var\/lib\/sphinx\/test1/g' \
%buildroot%_sysconfdir/sphinx/sphinx.conf

# Create /etc/logrotate.d/sphinx
mkdir -p %buildroot%_sysconfdir/logrotate.d
cat > %buildroot%_sysconfdir/logrotate.d/sphinx << EOF
/var/log/sphinx/*.log {
       weekly
       rotate 10
       copytruncate
       delaycompress
       compress
       notifempty
       missingok
}
EOF

# Install libsphinxclient
cd api/libsphinxclient/
make install DESTDIR=%buildroot INSTALL="%__install -p -c"

%pre
%_sbindir/groupadd -r -f _sphinx &>/dev/null
%_sbindir/useradd -r -n -g _sphinx -d /var/empty -s /bin/false -c "Sphinx Searchd pseudo user" _sphinx >/dev/null 2>&1 ||:

%post
%post_service searchd

%preun
%preun_service searchd

%files
%doc COPYING doc/sphinx.txt sphinx-min.conf.dist sphinx.conf.dist example.sql
%dir %attr(775,root,_sphinx) %_sysconfdir/sphinx
%config(noreplace) %attr(644,root,_sphinx) %_sysconfdir/sphinx/sphinx.conf
%exclude %_sysconfdir/sphinx/*.conf.dist
%exclude %_sysconfdir/sphinx/example.sql
%_initdir/searchd
%config(noreplace) %_sysconfdir/logrotate.d/sphinx
%_bindir/*
%dir %attr(775,root,_sphinx) %_var/log/sphinx
%dir %attr(775,root,_sphinx) %_var/run/sphinx
%dir %attr(775,root,_sphinx) %_var/lib/sphinx
%_man1dir/*

%files -n libsphinxclient
%doc api/java api/ruby api/*.php api/*.py api/libsphinxclient/README
%_libdir/libsphinxclient-0*.so

%files -n libsphinxclient-devel
%_libdir/libsphinxclient.so
%_includedir/*

%files -n libsphinxclient-devel-static
%_libdir/libsphinxclient.a

%changelog
* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.0.4-alt1
- 2.0.4
- compiled with libstemmer

* Sat Mar 26 2011 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9.9-alt4
- Fix libsphixclient-devel-static package (closes: #24798)

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt3.1
- Rebuilt for soname set-versions

* Sat Aug 28 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9.9-alt3
- fix repocop warning to library-pkgnames-static

* Wed Aug 25 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9.9-alt2
- Merged with http://git.altlinux.org/people/thresh/packages/sphinx.git

* Wed Aug 25 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9.9-alt1
- New version 0.9.9

* Tue Oct 06 2009 Konstantin Pavlov <thresh@altlinux.org> 0.9.8.1-alt1
- First build for ALT Linux.

* Wed Aug 12 2009 Allisson Azevedo <allisson@gmail.com> 0.9.8.1-3
- Fixed macros consistency.
- Modified make install to keep timestamps.
- Added libsphinxclient package.

* Fri Aug  7 2009 Allisson Azevedo <allisson@gmail.com> 0.9.8.1-2
- Added sysv init.
- Added logrotate.d entry.

* Thu Jul 30 2009 Allisson Azevedo <allisson@gmail.com> 0.9.8.1-1
- Initial rpm release.
