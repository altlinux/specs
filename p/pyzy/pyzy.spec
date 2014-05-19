
Name:       pyzy
Version:    0.1.0
Release:    alt2
Summary:    The Chinese PinYin and Bopomofo conversion library
License:    LGPLv2+
Group:      System/Libraries
URL:        http://code.google.com/p/pyzy
Source0:    http://pyzy.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:    http://pyzy.googlecode.com/files/pyzy-database-1.0.0.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  libsqlite3-devel
BuildRequires:  libuuid-devel
BuildRequires:  opencc-devel
BuildRequires:  sqlite3
BuildRequires:  doxygen

# both android db and open phrase db are data files for pyzy, either one can be installed to provide pyzy-db.
Requires:   pyzy-db

%description
The Chinese Pinyin and Bopomofo conversion library.

%package    devel
Summary:    Development tools for pyzy
Group:      Development/C
Requires:   %{name} = %{version}-%{release}

%description devel
The pyzy-devel package contains the header files for pyzy.

%package    db-open-phrase
Summary:    The open phrase database for pyzy
Group:      System/Libraries
BuildArch:  noarch
Provides:   pyzy-db

%description db-open-phrase
The phrase database for pyzy from open-phrase project.

%package    db-android
Summary:    The android phrase database for pyzy
Group:      System/Libraries
BuildArch:  noarch
Provides:   pyzy-db

%description db-android
The phrase database for pyzy from android project.

%prep
%setup -q
cp -p %SOURCE1 data/db/open-phrase

%build
%configure --disable-static --enable-db-open-phrase
# make -C po update-gmo
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la

%files
%doc AUTHORS COPYING README
%_libdir/lib*.so.*
%_datadir/pyzy/phrases.txt
%_datadir/pyzy/db/create_index.sql
%dir %_datadir/pyzy
%dir %_datadir/pyzy/db

%files devel
%_libdir/lib*.so
%_libdir/pkgconfig/*
%_includedir/*

%files db-open-phrase
%_datadir/pyzy/db/open-phrase.db

%files db-android
%_datadir/pyzy/db/android.db

%changelog
* Mon May 19 2014 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt2
- Move from Autoimports to Sisyphus

* Tue Jan 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_4
- initial fc import

