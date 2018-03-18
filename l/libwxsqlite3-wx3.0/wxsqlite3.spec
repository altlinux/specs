# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname wxsqlite3
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# https://github.com/utelle/wxsqlite3/commit/91de286b494f1a5239c9fc6fecbc21319a17e61b
%global commit0 91de286b494f1a5239c9fc6fecbc21319a17e61b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global wxversion %(wx-config-3.0 --release)
%global wxincdir %{_includedir}/wx-%{wxversion}

Name:           libwxsqlite3-wx3.0
Version:        3.4.1
Release:        alt1_0.5git%{shortcommit0}
Summary:        C++ wrapper around the SQLite 3.x database

Group:          System/Libraries
License:        wxWidgets
URL:            https://github.com/utelle/wxsqlite3
Source0:        https://github.com/utelle/wxsqlite3/archive/%{commit0}/%{oldname}-%{commit0}.tar.gz#/%{oldname}-%{shortcommit0}.tar.gz

# don't %%build the included wxSQLite+ application
BuildRequires:  libwxGTK3.0-devel
BuildRequires:  libsqlite3-devel
BuildRequires:  doxygen
BuildRequires:  dos2unix
Source44: import.info
Provides: wxsqlite3-wx3.0 = %{version}-%{release}


%description
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database and is
specifically designed for use in programs based on the wxWidgets library.
wxSQLite3 does not try to hide the underlying database, in contrary almost all
special features of the current SQLite3 version 3.6.22 are supported, like for
example the creation of user defined scalar or aggregate functions. Since
SQLite stores strings in UTF-8 encoding, the wxSQLite3 methods provide
automatic conversion between wxStrings and UTF-8 strings. This works best for
the Unicode builds of wxWidgets. In ANSI builds the current locale conversion
object (wxConvCurrent) is used for conversion to/from UTF-8. Special care has
to be taken if external administration tools are used to modify the database
contents, since not all of these tools operate in Unicode resp. UTF-8 mode.
wxSQLite3 includes an optional extension for SQLite supporting key based
database file encryption using 128 bit AES encryption. Starting with version
1.9.6 of wxSQLite3 the encryption extension is compatible with the SQLite
amalgamation source. Experimental support for 256 bit AES encryption has been
added in version 1.9.8.


%package        devel
Summary:        Development files for %{oldname}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Provides: wxsqlite3-wx3.0-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.

%package        doc
Summary:        Documentation files for %{oldname}
Group:          Documentation
BuildArch:      noarch
Provides: wxsqlite3-wx3.0-doc = %{version}-%{release}

%description    doc
The %{oldname}-doc package contains html documentation 
that use %{oldname}.


%prep
%setup -q -n %{oldname}-%{commit0}


# activate correct build folder
mv build30 build

# delete bundled sqlite3 files
find -name sqlite3 -type d | xargs rm -rfv

# set correct permission
chmod a+x configure

# use correct wx-config file
sed -i -e 's|WX_CONFIG_NAME=wx-config|WX_CONFIG_NAME=wx-config-3.0|g' configure

# fixex E: wrong-script-end-of-line-encoding
dos2unix readme.md 

# fixes W: spurious-executable-perm
find docs -type f -exec chmod a-x {} \;
chmod a-x include/wx/wxsqlite3.h src/wxsqlite3.cpp

# fixes E: script-without-shebang
chmod -x LICENCE.txt readme.md

%build
%configure
%make_build

# build docs
pushd docs
doxygen
popd

%install
%makeinstall_std INSTALL="install -p"

# move headers from /usr/include/wx to /usr/include/wx-?.?/wx
mkdir %{buildroot}%{wxincdir}
mv %{buildroot}%{_includedir}/wx %{buildroot}%{wxincdir}

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# install pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{oldname}.pc %{buildroot}%{_libdir}/pkgconfig/%{oldname}.pc


%files
%doc readme.md
%doc --no-dereference LICENCE.txt
%{_libdir}/*.so.*

%files devel
%{wxincdir}/wx/*
%{_libdir}/pkgconfig/%{oldname}.pc
%{_libdir}/*.so

%files doc
%doc docs/html


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 3.4.1-alt1_0.5git91de286
- new version

