Name: sqlite3-regex_replace
Version: 0.1
Release: alt1

Summary: regular expression replace support for the SQLite
License: Public Domain
Group: Databases
URL: https://github.com/gwenn/sqlite-regex-replace-ext

Source: %name-%version.tar

Requires: libsqlite3 >= 3.3.8-alt2

# Automatically added by buildreq on Thu Nov 02 2006
BuildRequires: glib2-devel libsqlite3-devel sqlite3

%description
SQLite extensions that uses glib2/icu to provide a regex_replace() function.
* The glib code was adapted from the pcre match implementation by Alexey Tourbin

%prep
%setup -q

%build
cflags=`pkg-config --cflags sqlite3 glib-2.0`
libs=`pkg-config --libs sqlite3 glib-2.0`
gcc -shared -o glib_replace.so $cflags %optflags %optflags_shared -W glib_replace.c $libs -Wl,-z,defs

#check
sqlite3 >out <<EOF
.load ./glib_replace.so
SELECT regex_replace('sd','asdf','SD');
EOF
grep aSDf out

%install
install -pD -m755 glib_replace.so %buildroot%_libdir/sqlite3/glib_replace.so

%files
%doc README
%dir %_libdir/sqlite3
%_libdir/sqlite3/glib_replace.so

%changelog
* Fri Dec 13 2024 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
