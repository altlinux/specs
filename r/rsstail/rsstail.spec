Summary: RSS reader
Name: rsstail
Version: 1.6
Release: alt1.qa1
License: GPL2
Group: Networking/File transfer
Source0: http://www.vanheusden.com/rsstail/%name-%version.tgz
Url: http://www.vanheusden.com/rsstail/

BuildRequires: libcurl-devel libmrss-devel

%description
RSSTail is more or less an rss reader: it monitors an rss-feed and if
it detects a new entry it'll emit only that new entry.

%prep
%setup
%build
make

%install
mkdir -p %buildroot{%_bindir,%_man1dir}

%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1*
%doc readme.txt

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Sep  3 2010 Terechkov Evgenii <evg@altlinux.org> 1.6-alt1
- Initial build for ALT Linux Sisyphus
