Name: libstemmer
Version: 2.0.0
Release: alt1
Summary: C stemming algorithm library

Group: System/Libraries
License: BSD-2-Clause
Url: http://snowball.tartarus.org
Packager: Vladimir Didenko <cow@altlinux.org>

Source0: %{name}_c.tar

%description
Snowball stemming algorithms for use in Information Retrieval Snowball
provides access to efficient algorithms for calculating a "stemmed"
form of a word.  This is a form with most of the common morphological
endings removed; hopefully representing a common linguistic base form.
This is most useful in building search engines and information
retrieval software; for example, a search with stemming enabled should
be able to find a document containing "cycling" given the query
"cycles".

Snowball provides algorithms for several (mainly European) languages.
It also provides access to the classic Porter stemming algorithm for
English: although this has been superseded by an improved algorithm,
the original algorithm may be of interest to information retrieval
researchers wishing to reproduce results of earlier experiments.

%package -n %name-devel
Summary: libstemmer development libraries and includes
Group: Development/C
Requires: %name = %version-%release

%description -n %name-devel
Development files for C stemmer library

%prep
%setup -q -n %{name}_c

# Add rule to make libstemmer.so
sed -i -r "s|(^libstemmer.o:)|libstemmer.so: \$\(snowball_sources:.c=.o\)\n\
\t\$\(CC\) \$\(CFLAGS\) -shared \$\(LDFLAGS\) -Wl,-soname,libstemmer.so.0 \
-o \$\@.0.0.0 \$\^\n\1|" Makefile

%build
make libstemmer.so CFLAGS="%{optflags} -fPIC -Iinclude"

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -p -D -m 755 libstemmer.so.0.0.0 %{buildroot}%{_libdir}/
ln -s libstemmer.so.0.0.0 %{buildroot}%{_libdir}/libstemmer.so.0
ln -s libstemmer.so.0.0.0 %{buildroot}%{_libdir}/libstemmer.so
install -p -D -m 644 include/* %{buildroot}%{_includedir}/

%files -n %name
%doc README
%_libdir/%name.so.*

%files -n %name-devel
%_includedir/*
%_libdir/%{name}.so

%changelog
* Wed Aug 5 2020 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- New version

* Wed Nov 20 2019 Vladimir Didenko <cow@altlinux.org> 0-alt2.svn585
- Fix license name

* Tue Mar 24 2015 Vladimir Didenko <cow@altlinux.org> 0-alt1.svn585
- Initial build
