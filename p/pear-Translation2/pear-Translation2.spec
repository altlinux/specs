%define pear_name Translation2

Name: pear-Translation2
Version: 2.0.1
Release: alt1

Summary: Class for multilingual applications management

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
This class provides an easy way to retrieve all the strings for a
multilingual site from a data source (i.e. db).
The following containers are provided, more will follow:
- PEAR::DB
- PEAR::MDB
- PEAR::MDB2
- gettext
- XML
- PEAR::DB_DataObject (experimental)
It is designed to reduce the number of queries to the db, caching the
results when possible.
An Admin class is provided to easily manage translations (add/remove a
language, add/remove a string).
Currently, the following decorators are provided:
- CacheLiteFunction (for file-based caching)
- CacheMemory (for memory-based caching)
- DefaultText (to replace empty strings with their keys)
- ErrorText (to replace empty strings with a custom error text)
- Iconv (to switch from/to different encodings)
- Lang (resort to fallback languages for empty strings)
- SpecialChars (replace html entities with their hex codes)
- UTF-8 (to convert UTF-8 strings to ISO-8859-1)

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Translation2/
%pear_dir/Translation2.php
%pear_testdir/Translation2/
%_bindir/t2xmlchk.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

