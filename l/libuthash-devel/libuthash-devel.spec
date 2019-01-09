Name: libuthash-devel
Version: 2.1.0
Release: alt1
Summary: A hash table for C structures
License: BSD
Group: Development/C
Url: http://troydhanson.github.io/uthash
Source0: %name-%version.tar
BuildArch: noarch

%description
Any C structure can be stored in a hash table using uthash. Just add a
UT_hash_handle to the structure and choose one or more fields in your
structure to act as the key. Then use these macros to store, retrieve or
delete items from the hash table.

%prep
%setup

%build
%install
install -d %buildroot%_includedir
cp -pa src/*.h %buildroot%_includedir/

%check
cd tests
make

%files
%_includedir/ut*.h

%doc LICENSE doc/*.txt

%changelog
* Wed Jan 09 2019 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Build new version.

* Thu May 24 2018 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- Build new version (Closes: #33241).

* Thu Jan 30 2014 Terechkov Evgenii <evg@altlinux.org> 1.9.8-alt1
- Initial build for ALT Linux Sisyphus
