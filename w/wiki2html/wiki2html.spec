Name: wiki2html
Version: 0.1
Release: alt2

Summary: Convert wiki source to HTML

License: Public domain
Group: Text tools
Url: http://tools.wikimedia.de/~merphant/wiki2html/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://tools.wikimedia.de/~merphant/wiki2html/%name.tar.bz2

Patch1: %name-%version-alt-gcc6.patch

# Automatically added by buildreq on Sat Sep 10 2005
BuildRequires: flex

%description
wiki2html reads in a subset of the Wikipedia wikicode syntax
and converts it to HTML. If FILE is unspecified, input is from stdin
and output goes to stdout; this can be changed with the -o flag.

%prep
%setup -q -n %name
%patch1 -p2

%build
%make

%install
install -m0755 -D %name %buildroot%_bindir/%name

%files
%doc README
%_bindir/%name

%changelog
* Mon Jul 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt2
- Fix build with gcc-6

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Nov 30 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- fix Url (thanks to Nick Shaforostoff), fix Source Url

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt0.1
- first build for Sisyphus
