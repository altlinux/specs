Name: metastore
Version: 1.1.1
Release: alt1

Summary: Store and restore metadata from a filesystem

License: GPL2
Group: Development/Other
Url: https://github.com/przemoc/metastore

# Source-url: https://github.com/przemoc/metastore/archive/v%version.tar.gz
Source: %name-%version.tar

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildRequires: libattr-devel libbsd-devel

%description
Metastore is a tool to store the metadata of files/directories/links in
a file tree to a separate file and to later compare and apply the stored
metadata to said file tree.

It was originally written as a supplement to git, which does not store
all metadata, making it unsuitable for e.g. storing /etc in a
repository.

%prep
%setup

%build
%make_build PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%files
%_bindir/%name
%_man1dir/%{name}.*
%_docdir/%name/

%changelog
* Mon Dec 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Thu Feb 11 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version (1.1.0) with rpmgs script

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Feb 19 2008 Terechkov Evgenii <evg@altlinux.ru> 0.0-alt1
- Rebuild with new sisyphus_check

* Wed Jan  2 2008 Terechkov Evgenii <evg@altlinux.ru> 0.0-alt0
- Initial build for ALT Linux Sisyphus
